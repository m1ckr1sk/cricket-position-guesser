from behave import then


@then("we should return the stats")
def return_stats(context):
    stats = context.game.get_stats()
    for i, row in enumerate(context.table):
        if "total_guesses" == row["stat"]:
            assert (
                str(stats["total_guesses"]) == row["value"]
            ), f"Expected total guesses {row['value']} but got {stats['total_guesses']}"
        if "average_rating" == row["stat"]:
            assert (
                str(stats["average_rating"]) == row["value"]
            ), f"Expected average rating {row['value']} but got {stats['average_rating']}"
