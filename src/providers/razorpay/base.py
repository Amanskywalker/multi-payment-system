"""
Razorpay Service Base configurations to be used with other services
"""
import base64
import json
import requests

BASE_URL = f"https://api.razorpay.com/v1"

class RazorpayServiceBase:
    """
    Abstract class to connet with the Razorpay services
    """

    API_KEY = None
    API_SECRET = None

    URL = None
    HEADER = {
        'Content-Type' : "application/json",
        'Authorization' : f"Basic {base64.b64encode(f'{API_KEY}:{API_SECRET}'.encode('ascii')).decode('ascii')}"
    }
    PAYLOAD = {}

    def __init__(self, api_key, api_secret):
        """
        override the authentication
        """
        # generate the keys
        auth_token = base64.b64encode(f"{api_key}:{api_secret}".encode("ascii")).decode("ascii")

        # attached the keys to the header
        self.HEADER['Authorization'] = f"Basic {auth_token}"


    def excute_call(self, type='get'):
        if type == 'get':
            response = requests.get(self.URL, headers=self.HEADER)
        elif type == 'post':
            response = requests.post(self.URL, data=self.PAYLOAD, headers=self.HEADER)
        
        return response