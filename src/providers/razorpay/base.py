"""
Razorpay Service Base configurations to be used with other services
"""
import base64
import json
import requests

from types import ModuleType

from .constants import HTTP_STATUS_CODE, ERROR_CODE, URL
from . import resources

from .errors import (BadRequestError, GatewayError,ServerError)

def capitalize_camel_case(string):
    return "".join(map(str.capitalize, string.split('_')))

# Create a dict of resource classes
RESOURCE_CLASSES = {}
for name, module in resources.__dict__.items():
    if isinstance(module, ModuleType) and \
            capitalize_camel_case(name) in module.__dict__:
        RESOURCE_CLASSES[name] = module.__dict__[capitalize_camel_case(name)]

class RazorpayService:
    """
    Class to connect with the Razorpay services
    """

    DEFAULTS = {
        'base_url': URL.BASE_URL
    }

    def __init__(self, session=None, auth=None, **options):
        """
        Initialize a Service object with session,
        """
        self.session = session or requests.Session()
        self.auth = auth

        self.base_url = self._set_base_url(**options)

        # intializes each resource
        # injecting this client object into the constructor
        for name, Klass in RESOURCE_CLASSES.items():
            setattr(self, name, Klass(self))

    def _set_base_url(self, **options):
        base_url = self.DEFAULTS['base_url']

        if 'base_url' in options:
            base_url = options['base_url']
            del(options['base_url'])

        return base_url

    def excute_call(self, url, type='get', payload={}):
        if type == 'get':
            response = requests.get(url, headers=self.HEADER)
        elif type == 'post':
            response = requests.post(url, data=payload, headers=self.HEADER)
        
        return response


class RazorpayPayout (RazorpayServiceBase):
    "Class to manage the payouts in razorpay X"


    URL_CONTACTS = f"{BASE_URL}/contacts"


    def create_contact(self, payload):
        """
        Creates the contact
        """
        self.PAYLOAD = json.dumps(payload)

        response = self.excute_call(self.URL_CONTACTS, type='post')

        return response.json()

    def create_fund_account(self, payload):
        """
        Creates the contact fund account
        """
        self.PAYLOAD = json.dumps(payload)
        self.URL = f"{BASE_URL}/fund_accounts"

        response = self.excute_call(type='post')

        return response.json()

    def create_payout(self, payload):
        """
        Creates the payout for the corresponding fund account
        """
        self.PAYLOAD = json.dumps(payload)
        self.URL = f"{BASE_URL}/payouts"

        response = self.excute_call(type='post')

        return response.json()
    
    def get_contacts(self, id=None):
        """Get all contact, if id is provided then only get the id details"""
        self.URL = f"{BASE_URL}/contacts"

        if id:
            self.URL = self.URL + f"/{id}"

        response = self.excute_call(type='get')

        return response.json()
