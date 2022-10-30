def identification_type(identifications: dict):
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
