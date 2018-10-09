# This is free and unencumbered software released into the public domain.

class Game:
    """A game."""

    def __init__(self, uuid=None):
        super().__init__(uuid=uuid)

    def __repr__(self):
        """Returns a human-readable string representation of this object."""
        return "game{{uuid={}}}".format(self.uuid)

    def __str__(self):
        """Returns a human-readable string representation of this object."""
        return self.__repr__()
