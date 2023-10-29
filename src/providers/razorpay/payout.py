class RazorpayPayout (RazorpayServiceBase):
    "Class to manage the payouts in razorpay X"

    def create_contact(self, payload):
        """
        Creates the contact
        """
        self.PAYLOAD = json.dumps(payload)
        self.URL = f"{BASE_URL}/contacts"

        response = self.excute_call(type='post')

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