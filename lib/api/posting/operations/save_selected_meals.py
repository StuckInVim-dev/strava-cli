import requests
import json


def main(CREDENTIALS):

    print("Saving selected meals... ", end="")

    cookies = {
        'cislo': CREDENTIALS["CANTEEN_NUMBER"],
        'jmeno': CREDENTIALS["USERNAME"],
    }

    data = {
        "cislo": CREDENTIALS["CANTEEN_NUMBER"],
        "sid": CREDENTIALS["SID"],
        "url": "https://wss5.strava.cz/WSStravne5_5/WSStravne5.svc",
        "xml": None,
    }

    response = requests.post(
        'https://app.strava.cz/api/saveOrders', cookies=cookies, data=json.dumps(data))

    print("✅" if response.ok else "❌")

    return
