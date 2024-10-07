import requests
import json


def main(MEAL_NUMBER, CREDENTIALS):
    print(f"Selcting meal... {MEAL_NUMBER} ", end="")

    URL = 'https://app.strava.cz/api/pridejJidloS5'

    cookies = {
        'cislo': CREDENTIALS["CANTEEN_NUMBER"],
        'jmeno': CREDENTIALS["USERNAME"],
    }

    data = {
        "cislo": CREDENTIALS["CANTEEN_NUMBER"],
        "sid": CREDENTIALS["SID"],
        "url": "https://wss5.strava.cz/WSStravne5_5/WSStravne5.svc",
        "veta": str(MEAL_NUMBER),
        "pocet": 1
    }

    response = requests.post(URL, cookies=cookies, data=json.dumps(data))

    print("✅" if response.ok else "❌")

    return
