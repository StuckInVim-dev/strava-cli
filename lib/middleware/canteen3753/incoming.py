import datetime
meal_id = 0
DAYS_OF_THE_WEEK = ["Pondělí", "Úterý", "Středa", "Čtvrtek", "Pátek", "Sobota", "Neděle"]

def main(API_RESPONSE):

    def increment_id(step=1):
        global meal_id
        meal_id = meal_id + step
        return meal_id

    DAYS = API_RESPONSE.values()
    meal_form = {
        "title": "Vyber si obědy",
        "questions": [],
    }
    for day in list(DAYS):


        # Checks for holidays and locked in orders
        order_limitation = day[0]["omezeniObj"]["den"]



        date = day[0]["datum"]

        date_array = date.split(".")
        week_of_the_day_index = datetime.date(int(date_array[2]), int(date_array[1]), int(date_array[0])).weekday()

        if order_limitation == "VP":
            meal_form["questions"].append({
                "id": date,
                "question": f"{date} - {day[0]['nazev']}",
                "locked": True,
                "options": [],
            })
            continue

        for selectable in day:
            if selectable["pocet"] == 1:
                selected_meal = selectable["id"] - 1
                break
            elif selectable["pocet"] == 0 and selectable == day[-1]:
                selected_meal = None


        # print(f"Selected meal for {day[0]['datum']}: {selected_meal}")


        if selected_meal is not None:

            meal_form["questions"].append({
                "id": date,
                "question": f"{DAYS_OF_THE_WEEK[week_of_the_day_index]} {date}\n    Povévka: {day[0]['delsiPopis']}",
                "locked": bool(order_limitation),
                "default": selected_meal,
                "options": [{
                    "text": meal["nazev"],
                    "id": increment_id(),
                    "allergens": [int(item[0]) for item in meal["alergeny"]],
                } for meal in day[1:3]],

            })

        else:

  
            meal_form["questions"].append({
                "id": date,
                "question": f"{DAYS_OF_THE_WEEK[week_of_the_day_index]} {date}\n    Povévka: {day[0]['delsiPopis']}",
                "locked": bool(order_limitation),
                # "default": selected_meal, dont pass in since its none
                "options": [{
                    "text": meal["nazev"],
                    "id": increment_id(),
                    "allergens": [int(item[0]) for item in meal["alergeny"]],
                } for meal in day[1:3]],

            })
        

        day_excess = len(day) - 3
        if len(day) > 0:
            increment_id(day_excess)


    return (meal_form)