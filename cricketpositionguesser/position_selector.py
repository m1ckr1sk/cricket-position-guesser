class PositionSelector:

    def __init__(self, position_name, positions):
        self.position = positions.get_position(position_name)
        self.positions = positions

    def get_position_to_guess(self):
        return self.position

    def is_valid_position(self, position_name):
        return self.positions.is_valid_position(position_name)

    def get_position(self, position_name):
        return self.positions.get_position(position_name)

    def rate_distance(self, position1, position2):
        if self.is_valid_position(position1.name) and self.is_valid_position(
            position2.name
        ):

            distance = position1.distance_to(position2)

            # normalise the distance to a rating between 0 and 10 based on the
            # maximum distance
            max_distance = self.positions.maximum_distance
            rating = min(10, (distance / max_distance) * 10)
            return round(rating)
        else:
            raise ValueError(
                f"Invalid positions: " f"{position1.name}, {position2.name}"
            )
