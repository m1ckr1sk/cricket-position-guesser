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
    
    def rate_distance(self, distance):
        # normalise the distance to a rating between 0 and 10 based on the maximum distance
        max_distance = self.positions.maximum_distance
        rating = max(0, 10 - (distance / max_distance) * 10)
        return round(rating)

