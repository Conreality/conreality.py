# This is free and unencumbered software released into the public domain.

class Theater:
    """A theater of operations."""

    def __init__(self, uuid=None):
        self.uuid = uuid

    def __repr__(self):
        """Returns a human-readable string representation of this object."""
        return "theater{{uuid={}}}".format(self.uuid)

    def __str__(self):
        """Returns a human-readable string representation of this object."""
        return self.__repr__()
