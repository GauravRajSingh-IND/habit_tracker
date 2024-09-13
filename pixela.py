import requests


class Pixela:

    def __init__(self):

        self.user_name = None
        self.authentication_token = None
        self.end_point = "https://pixe.la"

        self.error_message = None
        self.response_message = None


    def create_user(self, authentication_token:str, username:str, term_condition: str="yes", not_minor:str="no"):
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





