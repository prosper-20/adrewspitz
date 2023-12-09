import requests
from decouple import config

url = "https://live.waypointapi.com/v1/email_messages"

def send_emails(url):
    api_key_username = config('API_USERNAME')
    api_key_password = config('API_PASSWORD')

    data = {
        "templateId": "wptemplate_sXxADVW2RbKGYZpx",
        "from": "Andrew Spitz <aspitz@caverecruits.com>",
        "to": "andrewspitz1@outlook.com",
        "variables": {
            "user": {
                "displayName": "Cave Recruits",
            },
            "product": {
                "title": "Beechers Mac & Cheese",
                "id": "02934203942"
            }
        }
    }

    headers = {
        "Content-Type": "application/json"
    }

    try:
        response = requests.post(url, json=data, headers=headers, auth=(api_key_username, api_key_password))
        response.raise_for_status()
        return response.json()
    except requests.exceptions.HTTPError as errh:
        print(f"HTTP Error: {errh}")
    except requests.exceptions.ConnectionError as errc:
        print(f"Error Connecting: {errc}")
    except requests.exceptions.Timeout as errt:
        print(f"Timeout Error: {errt}")
    except requests.exceptions.RequestException as err:
        print(f"Something went wrong: {err}")


print(send_emails(url))