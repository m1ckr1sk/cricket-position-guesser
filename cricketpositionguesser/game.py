from cricketpositionguesser.guess_result import Result


class Game:

    def __init__(self, cricket_position_selector):
        self.cricket_position_selector = cricket_position_selector
        self.position_to_guess = (
            cricket_position_selector.get_position_to_guess()
        )
        self.guess = None
        self.distance_rating = None
        self.guess_log = []

    def make_guess(self, guess):
        self.guess = guess
        if self.cricket_position_selector.is_valid_position(guess):
            self.guessed_position = (
                self.cricket_position_selector.get_position(guess)
            )
            self.distance_rating = self.calculate_distance_rating()
            return self.get_result()
        else:
            return Result(guess, f"Position '{guess}' not found.", None)

    def calculate_distance_rating(self):
        # Get the position to guess and the guess
        return self.cricket_position_selector.rate_distance(
            self.position_to_guess, self.guessed_position
        )

    def get_result(self):

        if self.position_to_guess.name == self.guess:
            result = Result(self.guess, "correct", 0)
            self.guess_log.append(result)
            return result
        else:
            result = Result(self.guess, "incorrect", self.distance_rating)
            self.guess_log.append(result)
            return result

    def get_stats(self):
        return {
            "total_guesses": len(self.guess_log),
            "average_rating": self.calculate_average_distance_rating(),
        }

    def calculate_average_distance_rating(self):
        total_distance = sum(
            result.distance_rating
            for result in self.guess_log
            if result.distance_rating is not None
        )
        total_guesses = len(self.guess_log)
        if total_guesses > 0:
            return round(total_distance / total_guesses, 2)
        else:
            return 0
