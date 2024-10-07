from lib.api.posting.operations.deselect_meal import main as deselect_meal  # type: ignore
from lib.api.posting.operations.select_meal import main as select_meal  # type: ignore
from lib.api.posting.operations.save_selected_meals import main as save_selected_meals  # type: ignore


def main(USER_CHANGES, CANTEEN_NUMBER, USERNAME, SID):
    CREDENTIALS = {
        "CANTEEN_NUMBER": CANTEEN_NUMBER,
        "USERNAME": USERNAME,
        "SID": SID,
    }

    for date, changed_meal in USER_CHANGES.items():
        if changed_meal is None:
            deselect_meal(date, CREDENTIALS)
            continue
        select_meal(changed_meal, CREDENTIALS)
    if len(USER_CHANGES) == 0:
        print("NOTE: No changes made, not saving selected meals")
        return

    save_selected_meals(CREDENTIALS)
