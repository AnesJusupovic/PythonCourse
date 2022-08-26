import requests

APP_ID = "b9328b85"
API_KEY = "5c18d489d525df7edd3492b8f88e17cc"
GENDER = "M"
WEIGHT_KG = "78"
HEIGHT_CM = "183"
AGE = "18"

if __name__ == "__main__":
    print("test")
    endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
    headers = {
        'x-app-id': APP_ID,
        'x-app-key': API_KEY,
    }

    text = input("Tell me which exercises you did: ")
    parameters = {
        "query": text,
        "gender": GENDER,
        "weight_kg": WEIGHT_KG,
        "height_cm": HEIGHT_CM,
        "age": AGE
    }
    response = requests.post(url=endpoint, json=parameters, headers=headers)
    result = response.json()
    print(result)