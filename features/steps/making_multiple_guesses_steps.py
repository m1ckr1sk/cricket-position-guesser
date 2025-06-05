from behave import when, then


@when("we make the following guesses")
def multiple_guesses(context):
    context.results = []
    for row in context.table:
        guess = row["guess"]
        result = context.game.make_guess(guess)
        context.results.append(result)


@then("we should return the results")
def multiple_results(context):
    for i, row in enumerate(context.table):
        distance_rating = context.results[i].distance_rating
        status = context.results[i].status
        assert distance_rating == int(
            row["rating"]
        ), f"Expected distance rating {row['rating']} but got {distance_rating}"
        assert (
            status == row["status"]
        ), f"Expected status {row['status']} but got {status}"
