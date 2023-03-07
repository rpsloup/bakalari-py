"""Module allowing for the usage of HTTP Requests"""
import requests

def fetch_api_token(auth_data):
    """Fetches the access token from the API by entered data"""
    try:
        headers = { 'Content-Type' : 'application/x-www-form-urlencoded' }
        response = requests.post(
            f'{auth_data["endpoint"]}/api/login',
            headers=headers,
            data=f'client_id=ANDR&grant_type=password&\
                username={auth_data["username"]}&password={auth_data["password"]}',
            timeout=10
        )
        if response.status_code == 200:
            data = response.json()
            return data
        return None
    except requests.exceptions.RequestException as error:
        print(error)
        return None

def fetch_from_api(token_data, auth_data, endpoint):
    """Fetches data from the API via the passed access token"""
    try:
        headers = {
            'Content-Type' : 'application/x-www-form-urlencoded',
            'Authorization': f'{token_data["token_type"]} {token_data["access_token"]}',
        }
        response = requests.get(
            f'{auth_data["endpoint"]}/api/3{endpoint}',
            headers=headers,
            timeout=10
        )
        if response.status_code == 200:
            data = response.json()
            return data
        return None
    except requests.exceptions.RequestException as error:
        print(error)
        return None

class BakaClient:
    """Custom wrapper class for accessing the Bakaláři API"""

    def __init__(self):
        self.auth_data = None
        self.token_data = None

    def login(self, auth_data):
        """Handles login by fetching the access token"""
        token_data = fetch_api_token(auth_data)
        self.auth_data = auth_data
        self.token_data = token_data

    def fetch(self, endpoint):
        """Handles fetching data from the Bakaláři API"""
        data = fetch_from_api(self.token_data, self.auth_data, endpoint)
        return data

    def get_subjects(self):
        """Fetches the subjects from the API"""
        data = fetch_from_api(self.token_data, self.auth_data, '/subjects')
        return data['Subjects']

    def get_timetable(self):
        """Fetches the timetable from the API"""
        data = fetch_from_api(self.token_data, self.auth_data, '/timetable/actual')
        return data
