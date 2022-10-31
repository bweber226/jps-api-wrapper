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
        if identifications[key]:
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
                    "option for this endpoint."
                )
        return True
    else:
        return False


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
