from lib.api.getting.fetch_meals import fetch_meals
from lib.api.getting.authenticate import authenticate

from lib.api.posting.apply_changes import main as apply_changes

from lib.middleware.canteen3753.incoming import main as incoming3753
from lib.middleware.filter_unchanged import main as filter_unchanged

from lib.ui.login_user_input import main as user_input
from lib.ui.meal_select_ui import main as meal_select_ui


CANTEEN_NUMBER, USERNAME, PASSWORD = user_input()
SID = authenticate(CANTEEN_NUMBER, USERNAME, PASSWORD)
FETCHED_MEALS = fetch_meals(CANTEEN_NUMBER, USERNAME, SID)
UI_FORM = incoming3753(FETCHED_MEALS)
USER_MEAL_SELECTIONS = meal_select_ui(UI_FORM)
USER_CHANGES = filter_unchanged(USER_MEAL_SELECTIONS)
apply_changes(USER_CHANGES, CANTEEN_NUMBER, USERNAME, SID)
