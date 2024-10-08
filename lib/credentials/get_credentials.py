import os
from dotenv import load_dotenv

def main():

    credentials = {}
    DOTENV_VARS_AND_HUMAN_NAMES = {
        "STRAVA_CANTEEN_NUMBER": "canteen number",
        "STRAVA_USERNAME": "username",
        "STRAVA_PASSWORD": "password",
    }
    if os.path.exists('../../.env'):
        try:
            load_dotenv(".env")

            for dotenv_variable_name, dotenv_variable_human_name in DOTENV_VARS_AND_HUMAN_NAMES.items():
                dotenv_variable_value = os.environ.get(dotenv_variable_name)
                if dotenv_variable_value is None:
                    raise Exception(f"Missing {dotenv_variable_human_name} variable in dotenv, add {dotenv_variable_name} key")
                credentials[dotenv_variable_name] = dotenv_variable_value
            
        except Exception as e:
            print(f"Error loading dotenv file: {str(e)}")
            exit(1)
    else:
        for dotenv_variable_name, dotenv_variable_human_name in DOTENV_VARS_AND_HUMAN_NAMES.items():
            credentials[dotenv_variable_name] = input(f"Enter your {dotenv_variable_human_name}: ")
    
    return credentials
