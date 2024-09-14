from datetime import datetime
import requests
import os.path
import json

from future.backports.datetime import datetime


class Pixela:

    def __init__(self):

        self.user_name = None
        self.authentication_token = None
        self.end_point = "https://pixe.la"

        self.error_message = None
        self.response_message = None


    def create_user(self, username:str, authentication_token:str, term_condition: str="yes", not_minor:str="yes"):
        """
        This function takes two parameters and create a new user account in pixela
        :param authentication_token: This token is the password of the user. user needs this during every login.
        :param username: username in str.
        :param term_condition: default set to yes, if user don't accept the condition no account is created.
        :param not_minor: default to yes, if user is a minor account not created.
        :return: success:response or not success:error message
        """

        self.authentication_token = authentication_token
        self.user_name = username

        if not all([self.authentication_token, self.user_name]):
            raise "required parameters are misssing"

        end_point = f"{self.end_point}/v1/users"

        params = {
            'token':self.authentication_token,
            'username':self.user_name,
            'agreeTermsOfService':term_condition,
            'notMinor':not_minor
        }

        try:
            response = requests.post(url= end_point, json=params)
            response.raise_for_status()
            self.response_message = response.json()
            self.error_message = None

        except requests.exceptions.RequestException as e:
            self.error_message = f"Error while create the new user: {e}"
            self.response_message = None

        finally:

            date = str(datetime.now().strftime("%y%m%d"))
            if self.response_message is not None:
                response = str(self.response_message)
                self.store_new_user_data(username=self.user_name, params= params, date=date, response_message= response)

    def store_new_user_data(self, username:str, params:dict, date:str, response_message:str):

        # check if the txt file exist or not
        file_path = 'hidden_docs/user_data.json'
        isfile = os.path.isfile(file_path)

        if not isfile:
            # Create a new file and write an empty JSON object
            with open(file_path, "w") as file:
                json.dump({}, file)  # Initialize with an empty JSON object
                print("Created a new file.")

            # Open the existing file and read its contents
            with open(file_path, "r") as file:
                data = json.load(file)  # Load the JSON data
                print("Loaded data:", data)

        else:
            # Open the existing file and read its contents
            with open(file_path, "r") as file:
                data = json.load(file)  # Load the JSON data
                print("Loaded data:", data)

        # dictionary of the user data.
        user_dict = {
            "username": username,
            "params":params,
            "date":date,
            "response":response_message
        }

        # update the dictionary.
        data[username] = user_dict

        # Write the updated data back to the JSON file
        with open(file_path, "w") as file:
            json.dump(data, file, indent=4)



pixela = Pixela()



