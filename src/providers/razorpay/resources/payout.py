from .base import Resource
from ..constants.url import URL


class Payout(Resource):
    def __init__(self, client=None):
        super(Payout, self).__init__(client)
        self.base_url = URL.PAYOUT_URL

    def all(self, data={}, **kwargs):
        """"
        Fetch all Payout entities

        Returns:
            Dictionary of Payout
        """
        return super(Payout, self).all(data, **kwargs)

    def create(self, data={}, **kwargs):
        """"
        Create a Payout

        Args:
            data : Dictionary having keys using which payout have to be created
                'account_number' :  The account from which you want to make the payout
                'fund_account_id' : The unique identifier linked to a fund account
                'amount' : The payout amount, in paise
                'currency' : The payout currency
                'mode' : The mode to be used to create the payout. Available modes: NEFT, RTGS, IMPS, card.
                'purpose' :  The purpose of the payout that is being created. Example : refund, cashback, payout, salary, utility bill, vendor bill

        Returns:
            payout Dict which was created
        """
        url = self.base_url
        return self.post_url(url, data, **kwargs)