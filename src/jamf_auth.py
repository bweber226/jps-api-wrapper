from datetime import datetime, timedelta, timezone

import requests
from requests.auth import AuthBase
from requests.exceptions import JSONDecodeError


class JamfAuthException(Exception):
    """Raised when JamfAuth fails to refresh its authentication"""


class AuthResponseWasNotValid(JamfAuthException):
    """
    Raised when the given Jamf server returned a successful status code but the
    data returned was not what we expected.
    """


class JamfAuth(AuthBase):
    """Automatically-refreshing, token-based auth for the Jamf API.

    :param base_url: The root URL of your Jamf Pro Server instance. Include the
        leading https:// and port number. A trailing slash is not necessary.
        For example, "https://jss.example.com:8443".

    :param username: The username of an account on the specified Jamf Pro
        Server.

    :param password: The password corresponding to the given username.
    """

    def __init__(self, base_url: str, username, password):

        self._base_url = base_url
        self._auth = (username, password)
        self._reset_token_to_none()
        self.refresh_auth_if_needed()

    def _reset_token_to_none(self):
        self._token = None
        self._token_expiry = datetime.min.replace(tzinfo=timezone.utc)
        self._total_token_lifetime = timedelta.min

    def __enter__(self):
        self.refresh_auth_if_needed()
        return self

    def __exit__(self, exception_type, exception_value, traceback):
        self.invalidate()

    def get_bearer(self):
        return f"Bearer {self._token}"

    def refresh_auth_if_needed(self) -> bool:
        remaining_token_lifetime = self._token_expiry - datetime.now(timezone.utc)
        remaining_token_lifetime_percent = (
            remaining_token_lifetime / self._total_token_lifetime
        )

        # We only want to refresh if we're within 20% of the token's lifetime
        if remaining_token_lifetime_percent > 0.20:
            return False

        r = None
        # We could skip keep-alive if we knew that our token was expired, but
        # even if the current time comes after the expiry time of the token it
        # could still be valid (for example, because of clock differences
        # between us and the jamf server). Since keep-alive is cheap and we'll
        # use basic if it fails anyway, we'll eat the cost of a failed
        # keep-alive.
        with requests.Session() as session:
            if self._token is not None:
                r = session.post(
                    f"{self._base_url}/api/v1/auth/keep-alive",
                    headers={
                        "Accept": "application/json",
                        "Authorization": self.get_bearer(),
                    },
                )
            if r is None or r.status_code != 200:
                r = session.post(
                    f"{self._base_url}/api/v1/auth/token",
                    headers={"Accept": "application/json"},
                    auth=self._auth,
                )
                if r.status_code != 200:
                    raise JamfAuthException(
                        f"Unable to refresh authentication to {self._base_url}. Return"
                        f" code {r.status_code}. Response body: {r.text}"
                    )

        try:
            token_json = r.json()
        except JSONDecodeError as e:
            raise AuthResponseWasNotValid(
                f"Failed to decode token JSON from the Jamf API. It sent: '{r.text}'"
            ) from e
        try:
            token = token_json["token"]
            token_expiry = token_json["expires"]
        except KeyError as e:
            raise AuthResponseWasNotValid(
                "The JSON from the Jamf API did not have the expected values. It sent:"
                f" '{r.text}'"
            ) from e
        self._token = token
        try:
            self._token_expiry = datetime.strptime(
                token_expiry, "%Y-%m-%dT%H:%M:%S.%fZ"
            ).replace(tzinfo=timezone.utc)
        except ValueError:
            # If we request a token exactly on the second, milliseconds are
            # omitted
            self._token_expiry = datetime.strptime(
                token_expiry, "%Y-%m-%dT%H:%M:%SZ"
            ).replace(tzinfo=timezone.utc)
        self._total_token_lifetime = self._token_expiry - datetime.now(timezone.utc)
        return True

    def invalidate(self) -> bool:
        """
        Invalidate the currently-held token and forget it. JamfAuth still has
        the username and password that were passed into it, so a new token will
        be created if another request uses the instance as an authorizer.

        Returns True if the token was invalidated successfully (Jamf returned
        200 or 204). Returns False in any other case. The token may still be
        valid if False is returned, but it may also be invalid.
        """
        if self._token is None:
            # If it was never valid, it is still not valid
            return True
        r = requests.post(
            f"{self._base_url}/api/v1/auth/invalidate-token",
            headers={"Accept": "application/json", "Authorization": self.get_bearer()},
        )
        self._reset_token_to_none()
        if r.status_code in [200, 204]:
            return True
        return False

    def __call__(self, r: requests.Request):
        self.refresh_auth_if_needed()
        r.headers["Authorization"] = self.get_bearer()
        return r
