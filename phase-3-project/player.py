# player.py

# Define the Player class for the player in the game.
class Player:
    def __init__(self, name):
        self._name = name
        self._alive = True

    @property
    def name(self):
        # Get the player's name.
        return self._name

    @name.setter
    def name(self, value):
        # Set the player's name.
        self._name = value

    @property
    def alive(self):
        # Check if the player is alive or not.
        return self._alive

    @alive.setter
    def alive(self, value):
        # Set the player's alive status (True or False).
        if isinstance(value, bool):
            self._alive = value
        else:
            raise ValueError("Alive status must be a boolean.")

    def reset(self):
        # Resets the player's state for a new game.
        self.alive = True