# This is free and unencumbered software released into the public domain.

class Client:
    """The client connection."""

    def __init__(self):
        pass

    def __repr__(self):
        """Returns a human-readable string representation of this object."""
        return "client{{}}" # TODO

    def __str__(self):
        """Returns a human-readable string representation of this object."""
        return self.__repr__()
