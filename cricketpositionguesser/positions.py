from .polar_coordinate import PolarCoordinate
from .cricket_position import CricketPosition


class CricketPositions: 

    def __init__(self):
        self.positions = [
                CricketPosition("deep cover", PolarCoordinate(0.99, 265)),
                CricketPosition("cover", PolarCoordinate(0.45, 265)),
                CricketPosition("deep midwicket", PolarCoordinate(0.99, 95)),
                CricketPosition("midwicket", PolarCoordinate(0.45, 95)),
                CricketPosition("silly mid on", PolarCoordinate(0.10, 105)),
                CricketPosition("silly mid off", PolarCoordinate(0.10, 255)),
                CricketPosition("cow corner", PolarCoordinate(0.99, 120)),
                CricketPosition("long on", PolarCoordinate(0.99, 160)),
                CricketPosition("mid on", PolarCoordinate(0.45, 160)),
                CricketPosition("long off", PolarCoordinate(0.99, 200)),
                CricketPosition("mid off", PolarCoordinate(0.45, 200)),
                CricketPosition("deep extra cover", PolarCoordinate(0.99, 240)),
                CricketPosition("extra cover", PolarCoordinate(0.45, 240)),
                CricketPosition("deep point", PolarCoordinate(0.99, 290)),
                CricketPosition("point", PolarCoordinate(0.45, 290)),
                CricketPosition("deep backward point", PolarCoordinate(0.99, 315)),
                CricketPosition("backward point", PolarCoordinate(0.45, 315)),
                CricketPosition("third man", PolarCoordinate(0.99, 340)),
                CricketPosition("short third man", PolarCoordinate(0.45, 340)),
                CricketPosition("fly slip", PolarCoordinate(0.45, 350)),
                CricketPosition("straight hit", PolarCoordinate(0.99, 180.0)),
                CricketPosition("deep square leg", PolarCoordinate(0.99, 80.0)),
                CricketPosition("square leg",PolarCoordinate(0.45, 80.0)),
                CricketPosition("long leg", PolarCoordinate(0.99, 50.0)),
                CricketPosition("backward square leg", PolarCoordinate(0.45, 50.0)),
                CricketPosition("deep fine leg", PolarCoordinate(0.99, 35.0)),
                CricketPosition("short fine leg", PolarCoordinate(0.45, 35.0)),
                CricketPosition("long stop", PolarCoordinate(0.99, 0.0)),
                CricketPosition("first slip", PolarCoordinate(0.20, 355)),
                CricketPosition("second slip", PolarCoordinate(0.20, 353)),
                CricketPosition("third slip", PolarCoordinate(0.20, 351)),
                CricketPosition("fourth slip", PolarCoordinate(0.20, 349)),
                CricketPosition("fifth slip", PolarCoordinate(0.20, 347)),
                CricketPosition("gully", PolarCoordinate(0.20, 342)),
                CricketPosition("leg gully", PolarCoordinate(0.20, 18)),
                CricketPosition("short leg", PolarCoordinate(0.10, 18)),
                CricketPosition("silly point", PolarCoordinate(0.10, 342)),
                CricketPosition("leg slip", PolarCoordinate(0.20, 9)),
                CricketPosition("wicket keeper", PolarCoordinate(0.15, 0.0))
                ]
        self.maximum_distance = self.calculate_maximum_distance()
        
    def is_valid_position(self, position_name: str) -> bool:
        """
        Check if the given position name is valid.

        :param position_name: The name of the cricket position.
        :return: True if the position name is valid, False otherwise.
        """
        return any(position.name == position_name for position in self.positions)   
    
    def get_position(self, position_name: str) -> CricketPosition:
        """
        Get a CricketPosition by its name.

        :param position_name: The name of the cricket position.
        :return: A CricketPosition instance.
        """
        for position in self.positions:
            if position.name == position_name:
                return position
        raise ValueError(f"Position '{position_name}' not found.")
    
    def calculate_maximum_distance(self) -> float:
        """
        Calculate the maximum distance between any two positions.

        :return: The maximum distance between any two positions.
        """
        max_distance = 0.0
        for i in range(len(self.positions)):
            for j in range(i + 1, len(self.positions)):
                distance = self.positions[i].distance_to(self.positions[j])
                if distance > max_distance:
                    max_distance = distance
        return max_distance