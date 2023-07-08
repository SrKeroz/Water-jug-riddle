class State:
    """
    The State class represents the state of the jugs.

    Attributes:
        x (int): Gallons in the x_gallon jug.
        y (int): Gallons in the y_gallon jug.

    Methods:
        __eq__(self, other): Compares if two states are equal.
        __hash__(self): Returns the hash value of a state.
        __str__(self): Returns a string representation of a state.

    """
    def __init__(self, x, y):
        self.x = x  # Gallons in the x_gallon jug
        self.y = y  # Gallons in the y_gallon jug

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __hash__(self):
        return hash((self.x, self.y))

    def __str__(self):
        return f"(X: {self.x}, Y: {self.y})"