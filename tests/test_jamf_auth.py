import base64
import requests
import responses
from responses import matchers
from jamf_auth import AuthResponseWasNotValid, JamfAuth, JamfAuthException
from datetime import datetime, timezone, timedelta
import pytest
import time_machine

useful_datetime = datetime(
    year=2021, month=6, day=1, hour=12, minute=0, tzinfo=timezone.utc
)
example_jss = "http://jss.example.com"

keep_alive_401 = responses.Response(
    method="POST",
    url=f"{example_jss}/api/v1/auth/keep-alive",
    json={"httpStatus": 401, "errors": []},
    status=401,
)
get_token_401 = responses.Response(
    method="POST",
    url=f"{example_jss}/api/v1/auth/token",
    json={"httpStatus": 401, "errors": []},
    status=401,
)


def get_invalidate_token():
    return responses.Response(
        method="POST",
        url=f"{example_jss}/api/v1/auth/invalidate-token",
        match=[
            matchers.header_matcher({"Authorization": "Bearer get_token_200_token"})
        ],
    )


def now_utc():
    return datetime.now(timezone.utc)


def iso_8601_z_without_fraction_of(dt):
    return dt.strftime("%Y-%m-%dT%H:%M:%SZ")


def iso_8601_z_of(dt):
    return dt.strftime("%Y-%m-%dT%H:%M:%S.%fZ")


def get_token_200(
    token_text="get_token_200_token",
    token_lifetime=timedelta(minutes=100),
    time_conversion=iso_8601_z_of,
):
    expires = now_utc() + token_lifetime
    authorization = f"Basic {base64.urlsafe_b64encode(b'username:password').decode()}"
    return responses.Response(
        method="POST",
        url=f"{example_jss}/api/v1/auth/token",
        json={"token": token_text, "expires": time_conversion(expires)},
        match=[matchers.header_matcher({"Authorization": authorization})],
    )


def keep_alive_200(
    token_text="keep_alive_200_token",
    token_lifetime=timedelta(minutes=100),
    expected_token="get_token_200_token",
):
    expires = now_utc() + token_lifetime
    return responses.Response(
        method="POST",
        url=f"{example_jss}/api/v1/auth/keep-alive",
        json={"token": token_text, "expires": iso_8601_z_of(expires)},
        match=[matchers.header_matcher({"Authorization": f"Bearer {expected_token}"})],
    )


def default_auth():
    return JamfAuth(example_jss, "username", "password")


@responses.activate
def test_initial_403():
    responses.add(get_token_401)
    responses.add(keep_alive_401)

    with pytest.raises(JamfAuthException):
        default_auth()


@responses.activate
def test_refresh_first_token():
    """
    Ensures that the auth object grabs a token right when it starts.
    Not having the keep-alive responder ensures we throw an error here if
    keep-alive is attempted before we even have a token.
    """
    with time_machine.travel(useful_datetime, tick=False):
        responses.add(get_token_200())

        j = default_auth()
        assert j._token == "get_token_200_token"


@responses.activate
def test_refresh_not_needed():
    """
    Ensures that the auth object uses its existing token when there is no need
    to refresh it.
    """
    with time_machine.travel(useful_datetime, tick=False):
        responses.add(get_token_200())
        auth = default_auth()
        responses.add(get_token_200("this_should_not_be_the_token"))
        req = requests.Request()
        auth(req)
        assert req.headers["Authorization"] == "Bearer get_token_200_token"


@responses.activate
def test_refresh_needed():
    """
    Ensures that the auth object refreshes its existing token when it needs to.
    """
    with time_machine.travel(useful_datetime, tick=False):
        first_keepalive = keep_alive_200(token_text="second_token")
        responses.add(get_token_200())
        auth = default_auth()
        responses.add(first_keepalive)

    with time_machine.travel(useful_datetime + timedelta(minutes=81), tick=False):
        req = requests.Request()
        auth(req)
        assert req.headers["Authorization"] == "Bearer second_token"
        responses.remove(first_keepalive)

        # Make sure it doesn't refresh again, 80% of the lifetime has not
        # passed
        auth(req)
        assert req.headers["Authorization"] == "Bearer second_token"

    with time_machine.travel(useful_datetime + timedelta(minutes=162), tick=False):
        responses.add(
            keep_alive_200(token_text="fourth_token", expected_token="second_token")
        )
        req = requests.Request()
        auth(req)
        assert req.headers["Authorization"] == "Bearer fourth_token"


@responses.activate
def test_refresh_token_falls_back_to_basic():
    """
    Ensures that the auth object will refresh using HTTP Basic if it fails to
    refresh using the token, and that the refreshed token's properties are
    reflected in the auth object.
    """
    responses.add(keep_alive_401)
    with time_machine.travel(useful_datetime, tick=False):
        responses.add(get_token_200())

        auth = default_auth()
        req1 = requests.Request()
        auth(req1)
        assert req1.headers["Authorization"] == "Bearer get_token_200_token"

    with time_machine.travel(useful_datetime + timedelta(minutes=81), tick=False):
        responses.add(get_token_200("next_token"))
        req2 = requests.Request()
        auth(req2)
        assert req2.headers["Authorization"] == "Bearer next_token"


@responses.activate
def test_auth_token_invalid_json():
    """
    Ensures the auth object raises AuthResponseWasNotValid when it receives
    non-JSON content from /auth/token upon creation
    """
    responses.add(
        responses.Response(
            method="POST",
            url=f"{example_jss}/api/v1/auth/token",
            body="this is not json",
        )
    )
    with pytest.raises(AuthResponseWasNotValid):
        default_auth()


@responses.activate
def test_auth_token_wrong_json():
    """
    Ensures the auth object raises AuthResponseWasNotValid when it receives
    unexpected JSON from /auth/token
    """
    responses.add(
        responses.Response(
            method="POST",
            url=f"{example_jss}/api/v1/auth/token",
            body='{"this_is_not_auth_token": true}',
        )
    )
    with pytest.raises(AuthResponseWasNotValid):
        default_auth()


@responses.activate
def test_auth_keep_alive_invalid_json():
    """
    Ensures the auth object raises AuthResponseWasNotValid when it receives
    non-JSON content from /auth/keep-alive
    """
    responses.add(
        responses.Response(
            method="POST",
            url=f"{example_jss}/api/v1/auth/keep-alive",
            body="nope, not json",
        )
    )
    with time_machine.travel(useful_datetime, tick=False):
        responses.add(get_token_200())
        auth = default_auth()

    with time_machine.travel(useful_datetime + timedelta(81), tick=False):
        req = requests.Request()
        with pytest.raises(AuthResponseWasNotValid):
            auth(req)


@responses.activate
def test_auth_keep_alive_wrong_json():
    """
    Ensures the auth object raises AuthResponseWasNotValid when it receives
    unexpected JSON from /auth/keep-alive
    """
    responses.add(
        responses.Response(
            method="POST",
            url=f"{example_jss}/api/v1/auth/keep-alive",
            body='{"this_is_not_auth_keepalive": true}',
        )
    )
    with time_machine.travel(useful_datetime, tick=False):
        responses.add(get_token_200())
        auth = default_auth()

    with time_machine.travel(useful_datetime + timedelta(81), tick=False):
        req = requests.Request()
        with pytest.raises(AuthResponseWasNotValid):
            auth(req)


@responses.activate
def test_invalidate():
    """
    Ensures that the token is invalidated by calls to invalidate()
    """
    invalidate = get_invalidate_token()
    responses.add(invalidate)

    with time_machine.travel(useful_datetime):
        create = get_token_200()
        responses.add(create)
        auth = default_auth()
        assert auth.invalidate()

    assert create.call_count == 1
    assert invalidate.call_count == 1


@responses.activate
def test_session_manager():
    """
    Ensures that the token is created when the session is opened and forgotten
    when the session is closed
    """
    invalidate = get_invalidate_token()
    responses.add(invalidate)

    with time_machine.travel(useful_datetime):
        create = get_token_200()
        responses.add(create)

        with default_auth() as auth:
            r = requests.PreparedRequest()
            r.prepare(method="GET", url=f"{example_jss}/api/v1/auth", auth=auth)
            assert r.headers["Authorization"] == "Bearer get_token_200_token"

    assert create.call_count == 1
    assert invalidate.call_count == 1


@responses.activate
def test_session_manager_with_session_too():
    invalidate = get_invalidate_token()
    responses.add(invalidate)

    with time_machine.travel(useful_datetime):
        create = get_token_200()
        responses.add(create)

        with requests.Session() as session, default_auth() as auth:
            session.auth = auth
            r = session.prepare_request(
                requests.Request(method="GET", url=f"{example_jss}/api/v1/auth")
            )
            assert r.headers["Authorization"] == "Bearer get_token_200_token"

    assert create.call_count == 1
    assert invalidate.call_count == 1


@responses.activate
def test_seconds_without_fractions():
    """
    Sometimes the Jamf API returns time values with fractional seconds omitted.
    This seems to occur when an event is being described that occurred between
    0 and 5 thousandths of a second after a second. We need to accept and work
    with this oddity.
    """
    with time_machine.travel(useful_datetime):
        create = get_token_200(time_conversion=iso_8601_z_without_fraction_of)
        responses.add(create)

        j = default_auth()
        assert j._token == "get_token_200_token"
