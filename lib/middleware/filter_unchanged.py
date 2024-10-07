def main(USER_MEAL_SELECTIONS):
    changed_meals = {}
    for day in USER_MEAL_SELECTIONS:
        if day["default_answer_id"] == day["answer_id"]:
            continue
        changed_meals[day["question_id"]] = day["answer_id"]
    return changed_meals
