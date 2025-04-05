from cricketpositionguesser.guess_result import Result

class Game:

    def __init__(self, cricket_position_selector):
        self.cricket_position_selector = cricket_position_selector
        self.position_to_guess = cricket_position_selector.get_position_to_guess()
        self.guess = None
        self.distance_rating = None

    def make_guess(self, guess):
        self.guess = guess
        if self.cricket_position_selector.is_valid_position(guess):
            self.guessed_position = self.cricket_position_selector.get_position(guess)
            self.distance_rating = self.calculate_distance_rating()
            return self.get_result()
        else:
            return Result(guess, f"Position '{guess}' not found.", None)
    
    def calculate_distance_rating(self):
        # Get the position to guess and the guess     
        distance_of_guess = self.position_to_guess.distance_to(self.guessed_position)   
        return self.cricket_position_selector.rate_distance(distance_of_guess)
    
    def get_result(self):
        if self.position_to_guess.name == self.guess:
            return Result(self.guess, "correct", 0)
        else:
            return Result(self.guess, "incorrect", self.distance_rating)