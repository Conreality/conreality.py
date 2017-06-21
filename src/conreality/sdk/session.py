# This is free and unencumbered software released into the public domain.

class Session:
    """The client session."""

    def __init__(self):
        pass

    def __repr__(self):
        """Returns a human-readable string representation of this object."""
        return "session{{}}"

    def __str__(self):
        """Returns a human-readable string representation of this object."""
        return self.__repr__()
