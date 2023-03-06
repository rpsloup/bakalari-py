"""Module allowing for the usage of HTTP Requests"""
import requests

def fetch_api_token(auth_data):
    """Fetches the access token from the API by entered data"""
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
        print(data['access_token'])

class BakaClient:
    """Custom wrapper class for accessing the Bakaláři API"""

    def __init__(self):
        self.auth = None

    def login(self, auth_data):
        """Handles login by fetching the access token"""
        self.auth = auth_data
        fetch_api_token(auth_data)

    def fetch(self, endpoint):
        """Handles fetching data from the Bakaláři API"""
