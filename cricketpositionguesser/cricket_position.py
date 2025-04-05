from .polar_coordinate import PolarCoordinate

class CricketPosition:
    """
    A class representing a cricket fielding position using polar coordinates.
    """

    def __init__(self, name: str, coordinate: 'PolarCoordinate'):
        """
        Initialize a CricketPosition instance.

        :param name: The name of the cricket position.
        :param coordinate: The polar coordinates of the position.
        """
        self.name = name
        self.coordinate = coordinate

    def distance_to(self, other: 'CricketPosition') -> float:
        """
        Calculate the distance to another CricketPosition.

        :param other: The other CricketPosition to calculate the distance to.
        :return: The distance between the two positions.
        """
        return self.coordinate.distance_to(other.coordinate)