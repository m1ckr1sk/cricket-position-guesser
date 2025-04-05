from cricketpositionguesser.guess_result import Result

class Game:

    def __init__(self, cricket_position_selector):
        self.position_to_guess = cricket_position_selector.get_position()
        self.guess = None
        self.distance_rating = None

    def make_guess(self, guess):
        self.guess = guess
        self.distance_rating = self.calculate_distance_rating()
        return self.get_result()
    
    def calculate_distance_rating(self):
        # Placeholder for distance calculation logic
        # For now, we will just return a fixed value for demonstration purposes
        return 5
    
    def get_result(self):
        if self.position_to_guess == self.guess:
            return Result(self.guess, "correct", 0)
        else:
            return Result(self.guess, "incorrect", self.distance_rating)