import requests
import dotenv
import os

# load dotenv.
dotenv.load_dotenv()


def create_user_account():

    params = {
        "token": os.getenv('create_user_account_token'),
        "username": os.getenv('create_user_account_username'),
        "agreeTermsOfService": "yes",
        "notMinor": "yes"
    }

    response = requests.post(url= os.getenv('create_user_account_end_point'), json=params)
    print(response.status_code)

# create a new user
# create_user_account()

