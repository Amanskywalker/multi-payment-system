"""
Razorpay Service Base configurations to be used with other services
"""
import base64

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

        self.HEADER['Authorization'] = f"Basic {auth_token}"


        
