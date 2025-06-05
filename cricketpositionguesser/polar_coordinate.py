import math
from .cartesian_coordinate import CartesianCoordinate


class PolarCoordinate:

    def __init__(self, distance: float, angle: float):
        """
        Initialize a PolarCoordinate instance.

        :param radius: The radial distance from the origin.
        :param angle: The angle in degrees.
        """
        self.distance = distance
        self.angle = angle

    def to_cartesian(self):
        """
        Convert polar coordinates to Cartesian coordinates.

        :return: A CartesianCoordinate representing the Cartesian
        coordinates (x, y).
        """
        x = self.distance * math.cos(math.radians(self.angle))
        y = self.distance * math.sin(math.radians(self.angle))
        return CartesianCoordinate(x, y)

    def distance_to(self, other: "PolarCoordinate") -> float:
        """
        Calculate the distance to another PolarCoordinate.

        :param other: The other PolarCoordinate to calculate the distance to.
        :return: The distance between the two polar coordinates.
        """
        cartesian_self = self.to_cartesian()
        cartesian_other = other.to_cartesian()
        return math.sqrt(
            (cartesian_self.x - cartesian_other.x) ** 2
            + (cartesian_self.y - cartesian_other.y) ** 2
        )
