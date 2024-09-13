from datetime import datetime
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

def create_graph(graph_id: str, graph_name: str, graph_unit: str, unit_type: str = "int", color: str = "momiji") -> dict:
    """
    Creates a graph on Pixela.

    :param graph_id: The ID of the graph to be created.
    :param graph_name: The name of the graph.
    :param graph_unit: The unit of measurement for the graph.
    :param unit_type: The type of the graph (default is "int").
    :param color: The color of the graph (default is "momiji").
    :return: A dictionary containing the response from the API or None if an error occurs.
    :raises ValueError: If required environment variables are not set.
    :raises RequestException: If the request to create the graph fails.
    """

    key = os.getenv('create_user_account_token')
    username = os.getenv('create_user_account_username')
    end_point = f"https://pixe.la/v1/users/{username}/graphs"

    if not all([key, username]):
        raise ValueError("Missing required environmental variable")

    headers = {
        "X-USER-TOKEN": key
    }

    params = {
        "id": graph_id,
        "name": graph_name,
        "unit": graph_unit,
        "type": unit_type,
        "color": color
    }

    try:
        response = requests.post(url=end_point, json=params, headers=headers)
        response.raise_for_status()  # Raise an error for bad responses (4xx and 5xx)
    except requests.exceptions.RequestException as e:
        print(f"An error occurred while creating the graph: {e}")
        return None  # Return None or an appropriate error response

    return response.json()  # Return the response as a dictionary

def delete_graph(graph_id:str) -> dict:
    """
    This function delete a given graph from the user account.
    :param graph_id: graph id which user wants to delete
    :return: dict response code.
    """

    key = os.getenv('create_user_account_token')
    username = os.getenv('create_user_account_username')
    graphID= graph_id

    if not all([key, username, graphID]):
        raise "Required value missing"

    end_point = f"https://pixe.la//v1/users/{username}/graphs/{graphID}"

    headers = {
        "X-USER-TOKEN": key
    }

    try:
        response = requests.delete(url=end_point, headers=headers)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"Error occurred while deleting the graph: {e}")
        return {}

    return response.json()

def post_pixel(graph_id:str, quantity: str) -> dict:
    """
    This function update the pixel value of a given graphID
    :param graph_id: id of the graph where user wants to add pixel values.
    :param date: date should be a sing in yyyyMMdd format
    :param quantity: quantity value
    :return: HTTP status code of the task
    """

    graphID = graph_id
    key = os.getenv('create_user_account_token')
    username = os.getenv('create_user_account_username')

    if not all([graphID, key, username]):
        raise "Required values are missing.."

    end_point = f"https://pixe.la/v1/users/{username}/graphs/{graphID}"
    headers = {
        "X-USER-TOKEN":key
    }

    params = {
        "date": datetime.now().strftime('%Y%m%d'),
        "quantity":quantity
    }

    try:
        response = requests.post(url=end_point, headers=headers, json= params)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"Error occurred while posting pixels: {e}")
        return {}

    return response.json()

def update_graph(graph_id:str, variable_name: list, variable_new_value: list) -> dict:
    """
    This function updates the preexisting graphs.

    :param graph_id: id of the graph which user wants to update.
    :param variable_name: name of the variables which user wants to update this should be in a list
    :param variable_new_value: new values in a list
    :return: HTTP code of response.
    """

    key = os.getenv('create_user_account_token')
    username = os.getenv('create_user_account_username')
    end_point = f"https://pixe.la/v1/users/{username}/graphs/{graph_id}"
    variable_names = variable_name
    variable_values = variable_new_value

    if not all([key, username, end_point, variable_names, variable_values]):
        raise "required values are missing.."
    if len(variable_names) != len(variable_values):
        raise "variable names and variables values are not of same size"

    headers = {
        "X-USER-TOKEN": key
    }

    params = {}
    for num, names in enumerate(variable_names):
        params[names] = variable_values[num]

    try:
        response = requests.put(url=end_point, json=params, headers=headers)
        response.raise_for_status()

    except requests.exceptions.RequestException as e:
        print(f"Error occurred while updating the graph: {e}")
        return {}

    return response.json()



"/Users/gauravsingh/pythonProject/pythonlearning"
