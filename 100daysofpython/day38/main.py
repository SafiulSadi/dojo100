import requests
from datetime import datetime
import json
GENDER = "male"
WEIGHT = 81
HEIGHT = 177
AGE = 32



query_text = "I ran hard 1km and cycling for 5min"

query_text = input("Tell me what exercises you did?\n")

nutritionix_app_id = "cf851d96"
nutritionix_api_key = "ae60882ddd6f75b8f73fb0a5d6f57588"


host_domain = "https://trackapi.nutritionix.com"
natural_exercise_endpoint = "/v2/natural/exercise"

headers = {
    "x-app-id": nutritionix_app_id,
    "x-app-key": nutritionix_api_key
}

q_params = {
    "query": query_text,
    "weight_kg": WEIGHT,
    "height_cm":HEIGHT,
    "age": AGE
}

response = requests.post(url=host_domain+natural_exercise_endpoint, headers=headers, json=q_params)
response.raise_for_status()
data = response.json()["exercises"]
exercise = ""
duration = ""
calories = ""
for i in data:
    print(i["name"])
    exercise = i["name"]
    print(i["duration_min"])
    duration = i["duration_min"]
    print(i['nf_calories'])
    calories = i['nf_calories']

date = datetime.now().strftime("%d/%m/%Y")
print(date)
time = datetime.now().time()
print(time)

sheety_url_post = "https://api.sheety.co/08c94756e97dad996f0868429416995c/workouts/workouts"

sheety_params = {
    "workout":{
    "date": str(date),
    "time": str(time),
    "exercise": exercise,
    "duration": duration,
    "calories": calories,
    }
}
# sheety_response = requests.post(url=sheety_url_post, json=sheety_params)
# sheety_response.raise_for_status()
# print(sheety_response.text)

headers = {
    "Authorization": "Bearer abcd"
}
sheety_get_response = requests.get(url="https://api.sheety.co/08c94756e97dad996f0868429416995c/workouts/workouts")
sheety_get_response.raise_for_status()
print(sheety_get_response.text)

sheety_post_response = requests.post(url="https://api.sheety.co/08c94756e97dad996f0868429416995c/workouts/workouts", json=sheety_params, headers=headers)
sheety_post_response.raise_for_status()
print(sheety_post_response.text)

user_pass = ()