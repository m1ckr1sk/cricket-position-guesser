from cricketpositionguesser.game import Game
from cricketpositionguesser.position_selector import PositionSelector

@given(u'we have idnentified a position')
def identify_a_position_to_guess(context):
    cricket_position_selector = PositionSelector("mid-on")
    context.game = Game(cricket_position_selector)

@when(u'we make an incorrect guess')
def make_a_guess(context):
    context.result = context.game.make_guess("mid-off")

@then(u'we should return the incorrect position')
def return_result(context):
    assert context.result.status == "incorrect", "The guess should return incorrect"

@then(u'its rating based on distance to correct position')
def return_rating(context):
    assert context.result.distance_rating == 5, "The rating should be based on the distance to the correct position"