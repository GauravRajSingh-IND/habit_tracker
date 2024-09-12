import requests
import dotenv
import os

from requests.exceptions import RequestException

# load dotenv.
dotenv.load_dotenv()


def create_user_account() -> int:
    """
    This function creates a user account on Pixela.

    :return: HTTP status code from the response.
    :raises ValueError: If required environment variables are not set.
    :raises RequestException: If the request to create the account fails.
    """

    # Retrieve environment variables and validate them
    token = os.getenv('create_user_account_token')
    username = os.getenv('create_user_account_username')
    endpoint = os.getenv('create_user_account_end_point')

    if not all([token, username, endpoint]):
        raise ValueError("Missing required environment variables.")

    # Parameters required to create a new user account
    params = {
        "token": token,
        "username": username,
        "agreeTermsOfService": "yes",
        "notMinor": "yes"
    }

    try:
        # Post the request to create a new account
        response = requests.post(url=endpoint, json=params)
        response.raise_for_status()  # Raise an error for bad responses (4xx and 5xx)
    except RequestException as e:
        print(f"An error occurred while creating the account: {e}")
        return None  # Return None or a specific error code

    return response.status_code

# create a new user
#create_user_account()

