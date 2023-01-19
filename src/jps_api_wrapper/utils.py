from datetime import datetime
from typing import Union


def identification_type(identifications: dict):
    """
    Assesses the type of identification given a dictionary of keys set as the
    identification type and the values set as either a corresponding value or
    None.

    :param dict identifications:

    """
    identification = []
    for key in identifications:
        if identifications[key] or identifications[key] == 0:
            identification.append(key)

    if len(identification) == 0:
        raise NoIdentification(
            "Need to supply at least one identification type for the endpoint."
        )
    if len(identification) > 1:
        raise MultipleIdentifications(
            "You supplied more than one form of identification, "
            "please only choose one."
        )
    return identification[0]


def valid_subsets(subsets: Union[list, bool], subset_options: list) -> bool:
    """
    Given a list of subsets and a seperate list of valid subset options returns
    whether or not there are subsets along with checking to see if the passed
    subsets are valid options for the endpoint.

    :param subsets: Passed subset values to an endpoint request
    :param subset_options: The valid subset options for an endpoint

    :raises InvalidSubset:
        The subsets passed had a subset that is not a valid optionf for the
        endpoint.
    """
    if subsets:
        for subset in subsets:
            if subset not in subset_options:
                raise InvalidSubset(
                    "The subsets passed had a subset that is not a valid "
                    "option for this endpoint. The valid subsets are:\n"
                    f"{subset_options}"
                )
        return True
    else:
        return False


def param_or_data(params: Union[dict, bool], data: Union[str, bool]) -> str:
    """
    Given a dict of params and a data variable check to see if one and only
    one of them are not None type. This is used for endpoints that can be
    resolved with either url parameters or data.

    :param params: List of parameters
    :param data: Data for an API endpoint

    :raises NoParametersOrData:
        This module requires either a selection of the available parameters or
        data to be passed.
    :raises ParametersAndData:
        This module requires either a selection of the available parameters or
        data to be passed.
    """
    if not data and not any(params.values()):
        raise NoParametersOrData(
            "This module requires either a selection of the available "
            "parameters or data to be passed."
        )
    if data and any(params.values()):
        raise ParametersAndData(
            "This module requires only the use of a selection of the "
            "available parameters or data to be passed, but not both."
        )
    if any(params.values()):
        return "params"
    if data:
        return "data"


def enforce_params(params: dict):
    """
    Makes sure that required paramters are not None types.

    :param params: Dict of required parameters

    :raises MissingParameters:
        Reports the missing parameters
    """
    if None in params.values():
        missing_params = [param for param in params if not params[param]]

        raise MissingParameters(
            f"The following required parameters were not passed: {missing_params}"
        )


def valid_param_options(params: Union[str, list], param_options: list):
    """
    Makes sure that the values supplied to a module are within valid criteria.

    :param params: Supplied parameter values
    :param param_options: List of valid parameter options

    :raises InvalidParameterOptions:
        The values that were passed to this parameter do not match the valid
        options.
    """
    if type(params) == str:
        params = [params]
    for param in params:
        if param not in param_options:
            raise InvalidParameterOptions(
                "The values that were passed to this parameter do not match "
                "the following valid options:\n"
                f"{param_options}"
            )


def validate_date(date: str):
    """
    Makes sure that any date str passed is in the yyyy-mm-dd format.

    :param date: Date str

    :raises ValueError: Incorrect date format
    """
    try:
        datetime.strptime(date, "%Y-%m-%d")
    except ValueError:
        raise ValueError("Incorrect date format, should be YYYY-MM-DD")


def check_conflicting_params(params: dict):
    """
    Ensures that only one of the parameters given has a non NoneType value

    :param params: Dictionary of params
    """
    i = iter(params.values())
    if any(i) and any(i):
        raise ConflictingParameters(
            f"Only one of the following parameters are allowed:\n" f"{params.keys()}"
        )


def remove_empty_params(params: dict) -> dict:
    """
    Removes all key, value pairs where the value is None

    :param params: Dictionary of params
    """
    params = {k: v for k, v in params.items() if v is not None}

    return params


def enforce_type(value, types: tuple) -> bool:
    """
    Makes sure that a value is the specified type, used when a different type
    of data may cause issues

    :param value: Value to check type of
    :param types: Tuple of types
    """
    if isinstance(value, types):
        return True
    else:
        types = (i.__name__ for i in types)
        raise TypeError(f"{value} must be of type(s): {', '.join(types)}")


class NoIdentification(Exception):
    """
    Used if an endpoint is used without at least one form of identification
    passed in the parameters that it needs.
    """


class MultipleIdentifications(Exception):
    """
    Used when multiple types of identification is passed in the parameters of
    an endpoint module.
    """


class InvalidSubset(Exception):
    """
    The subsets passed had a subset that is not a valid option for this
    endpoint.
    """


class NoParametersOrData(Exception):
    """
    This module requires either a selection of the available parameters or data
    to be passed.
    """


class ParametersAndData(Exception):
    """
    This module requires only the use of a selection of the available
    parameters or data to be passed, but not both.
    """


class MissingParameters(Exception):
    """
    This module requires a specific set of parameters that were not passed.
    """


class InvalidParameterOptions(Exception):
    """
    The values that were passed to this parameter do not match the valid
    options.
    """


class ConflictingParameters(Exception):
    """
    Only one of the following parameters can be used:
    {parameters}
    """
