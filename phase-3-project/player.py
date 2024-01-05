class Player:
    def __init__(self, name):
        self._name = name
        self._alive = True

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def alive(self):
        return self._alive

    @alive.setter
    def alive(self, value):
        if isinstance(value, bool):
            self._alive = value
        else:
            raise ValueError("Alive status must be a boolean.")

    def reset(self):
        """ Resets the player's state for a new game. """
        self.alive = True