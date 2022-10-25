"""
Razorpay Service Base configurations to be used with other services
"""
# Django libraries
from django.conf import settings

# razorpay Library
import razorpay

# import the logging library
import logging

# Get an instance of a logger
logger = logging.getLogger(__name__)


class RazorpayService:
    """
    Abstract class to connet with the Razorpay services
    """

    API_KEY = settings.SERVICES["razorpay"]["KEY_ID"]
    API_SECRET = settings.SERVICES["razorpay"]["SECRET"]

    CLIENT = razorpay.Client(auth=(API_KEY, API_SECRET))

    def __init__(self, api_key, api_secret):
        """
        override the authentication
        """
        self.CLIENT = razorpay.Client(auth=(api_key, api_secret))
