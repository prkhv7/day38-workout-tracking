import requests
import datetime as dt

# Variables with person data
GENDER = "male"
WEIGHT_KG = 85
HEIGHT_CM = 179
AGE = 30

# Nutritionix app id and api key
APP_ID = "d288eadd"
API_KEY = "be868efca68f65dde9336fd4193107f6"

# Sheety token
SHEETY_TOKEN = "Bearer 45gDRJ%V9v4lvldr"

# Nutritionix and sheety endpoints
exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
add_row_endpoint = "https://api.sheety.co/9af3d586517055b3383f1fdffacb8f95/workoutTracking/workouts"

# Input
exercise_text = input("Tell me which exercises you did: ")

# Nutritionix headers and params for request
nutritionix_headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}
request_params = {
    "query": exercise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE,
}

# Nutritionix response
response_exercise = requests.post(url=exercise_endpoint, headers=nutritionix_headers, json=request_params)
result = response_exercise.json()['exercises']

# Now date and time
today_date = dt.datetime.now().strftime("%d/%m/%Y")
now_time = dt.datetime.now().strftime("%X")

# Adding exercises to table
for item in result:
    sheety_headers = {
        "Authorization": SHEETY_TOKEN,
    }
    new_row = {
        "workout": {
            "date": today_date,
            "time": now_time,
            "exercise": item['name'].title(),
            "duration": round(item['duration_min']),
            "calories": round(item['nf_calories']),
        }
    }

    post_row = requests.post(url=add_row_endpoint, headers=sheety_headers, json=new_row)
    print(post_row.text)


# Request for deleting row
# sheety_headers = {"Authorization": SHEETY_TOKEN}
# requests.delete(url=f"{add_row_endpoint}/3", headers=sheety_headers)
