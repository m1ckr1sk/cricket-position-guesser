from cricketpositionguesser.game import Game
from cricketpositionguesser.position_selector import PositionSelector
from cricketpositionguesser.positions import CricketPositions

@given(u'we have identified a position')
def identify_a_position_to_guess(context):
    cricket_positions = CricketPositions()
    cricket_position_selector = PositionSelector("mid on", cricket_positions)
    context.game = Game(cricket_position_selector)

@when(u'we make an incorrect guess')
def make_a_guess(context):
    context.result = context.game.make_guess("mid off")

@then(u'we should return the incorrect position')
def return_result(context):
    assert context.result.status == "incorrect", f"The guess should return incorrect but got {context.result.status}"

@then(u'its rating based on distance to correct position')
def return_rating(context):
    assert context.result.distance_rating == 8, f"The rating should be based on the distance to the correct position but got {context.result.distance_rating}"

@when(u'we make a correct guess')
def step_impl(context):
    context.result = context.game.make_guess("mid on")

@then(u'we should return the correct position')
def step_impl(context):
    assert context.result.status == "correct", "The guess should return correct"

@when(u'we make a guess with a position that is not identified')
def unknown_position(context):
    context.incorrect_position = "potato"
    context.result = context.game.make_guess(context.incorrect_position)

@then(u'we should return the message "Position not identified"')
def step_impl(context):
    assert context.result.status == f"Position '{context.incorrect_position}' not found.", "The guess should return 'Position not identified'"