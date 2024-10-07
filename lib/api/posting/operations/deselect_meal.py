import requests
import json


def main(HUMAN_READABLE_DATE, CREDENTIALS):
    print(f"Deselecting meal... {HUMAN_READABLE_DATE} ", end="")

    URL = 'https://app.strava.cz/api/objednejDenS5'
    DATE_ARRAY = HUMAN_READABLE_DATE.split(".")
    FORMATTED_DATE = f"{DATE_ARRAY[2]}-{DATE_ARRAY[1]}-{DATE_ARRAY[0]}"

    cookies = {
        'cislo': CREDENTIALS["CANTEEN_NUMBER"],
        'jmeno': CREDENTIALS["USERNAME"],
    }

    data = {
        "cislo": "3753",
        "sid": CREDENTIALS["SID"],
        "url": "https://wss5.strava.cz/WSStravne5_5/WSStravne5.svc",
        "datum": FORMATTED_DATE,
        "pocet": 0,
    }

    response = requests.post(URL, cookies=cookies, data=json.dumps(data))

    print("✅" if response.ok else "❌")
    return
