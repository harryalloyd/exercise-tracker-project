import requests
from datetime import datetime
from dotenv import load_dotenv
import os

# Load environment variables from .env
load_dotenv()


GENDER = "male"
AGE = 20
WEIGHT_KG = 79
HEIGHT_CM = 187

APP_ID = os.getenv("APP_ID")
API_KEY = os.getenv("API_KEY")
AUTHENTICATION = os.getenv("AUTHENTICATION")

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
sheety_endpoint = "https://api.sheety.co/2905ab585ad4a2d240ed018ee019826f/workoutTracking/workouts"


exercise_text = input("Tell me which exercises you did: ")

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}

parameters = {
    "query": exercise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

today_date = datetime.now().strftime("%m/%d/%Y")
now_time = datetime.now().strftime("%X")

response = requests.post(url=exercise_endpoint, json=parameters, headers=headers)
result = response.json()
#print(result)

basic_auth_headers = {
    "Authorization": "Basic SGFycnlMbG95ZDpDcm9zc0ZpcmU0Mz8="
}

for exercise in result["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

    sheet_response = requests.post(
        url=sheety_endpoint,
        json=sheet_inputs,
        headers=basic_auth_headers
    )

    print(sheet_response.text)
