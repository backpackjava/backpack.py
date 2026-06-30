class Rectangle:
    """Class representing a rectangle."""

    def __init__(self, width : int, height : int):
        """Init instance attributes."""
        self.width = width
        self.height = height

    def get_area(self) -> int:
        """Calculate the area."""
        return self.width * self.height

    def set_width(self, new_width : int) -> None:
        """Set the width attribute."""
        self.width = new_width

    def set_height(self, new_height : int) -> None:
        """Set the height attribute."""
        self.height = new_height

# Declare some Rectangles for testing.

assert type()

# Test the set_width() method

# Test the set_height() method

# Test the get_area() method now that we've made changes