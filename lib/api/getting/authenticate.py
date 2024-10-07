import requests
import json


def authenticate(CANTEEN_NUMBER, USERNAME, PASSWORD):
    print("Authenticating... ", end="")

    data = {
        "cislo": CANTEEN_NUMBER,
        "jmeno": USERNAME,
        "heslo": PASSWORD
    }

    URL = 'https://app.strava.cz/api/login'

    response = requests.post(URL, data=json.dumps(data))

    SID = json.loads(response.text)['sid']

    print("✅" if response.ok else "❌")

    return SID


if __name__ == "__main__":
    print("Running importable module as main")
    print(authenticate(
        input("CANTEEN_NUMBER "),
        input("USERNAME "),
        input("PASSWORD ")
    ))
