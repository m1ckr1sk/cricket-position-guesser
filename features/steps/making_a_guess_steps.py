from cricketpositionguesser.game import Game
from cricketpositionguesser.position_selector import PositionSelector
from cricketpositionguesser.positions import CricketPositions
from behave import given, when, then


@given("we have identified a position")
def identify_a_position_to_guess(context):
    cricket_positions = CricketPositions()
    cricket_position_selector = PositionSelector("mid on", cricket_positions)
    context.game = Game(cricket_position_selector)


@given('we have identified a position of "{position_name}"')
def step_impl(context, position_name):
    cricket_positions = CricketPositions()
    cricket_position_selector = PositionSelector(position_name, cricket_positions)
    context.game = Game(cricket_position_selector)


@when("we make an incorrect guess")
def make_a_guess(context):
    context.result = context.game.make_guess("mid off")


@then("we should return the incorrect position")
def return_result(context):
    assert (
        context.result.status == "incorrect"
    ), f"The guess should return incorrect but got {context.result.status}"


@then("its rating based on distance to correct position")
def return_rating(context):
    assert (
        context.result.distance_rating == 2
    ), f"The rating should be based on the distance to the correct position but got {context.result.distance_rating}"


@when("we make a correct guess")
def make_correct_guess(context):
    context.result = context.game.make_guess("mid on")


@then("we should return the correct position")
def return_correct_position(context):
    assert context.result.status == "correct", "The guess should return correct"


@when("we make a guess with a position that is not identified")
def unknown_position(context):
    context.incorrect_position = "potato"
    context.result = context.game.make_guess(context.incorrect_position)


@then('we should return the message "Position not identified"')
def return_message(context):
    assert (
        context.result.status == f"Position '{context.incorrect_position}' not found."
    ), "The guess should return 'Position not identified'"
