import requests
import json

meal_id = 0


def fetch_meals(CANTEEN_NUMBER, USERNAME, SID):
    print("Fetching meals... ", end="")

    URL = "https://app.strava.cz/api/objednavky"

    data = {
        "cislo": CANTEEN_NUMBER,
        "sid": SID,
        "s5url": "https://wss5.strava.cz/WSStravne5_5/WSStravne5.svc",

    }

    cookies = {
        "cislo": CANTEEN_NUMBER,
        "jmeno": USERNAME,
    }

    response = requests.post(URL, cookies=cookies, data=json.dumps(data))

    print("✅" if response.ok else "❌")
    return json.loads(response.text)


if __name__ == "__main__":
    print("Running importable module as main")
    CANTEEN_NUMBER = input("CANTEEN_NUMBER ")
    USERNAME = input("USERNAME ")
    SID = input("SID ")
    print(fetch_meals(CANTEEN_NUMBER, USERNAME, SID))
