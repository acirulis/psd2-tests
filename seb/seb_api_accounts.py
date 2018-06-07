from seb_api_base import PSD2SEBAPIBase


class PSD2SEBAccounts(PSD2SEBAPIBase):
    def __init__(self):
        super().__init__('accounts')

    def list_accounts(self):
        params = {

        }
        response = self.make_request(add_headers=params)
        return response

    def account_details(self, accId):
        """
        Get account details /accounts/<accountId>
        :param accId:
        :return: Response
        """
        params = {
            'with-balance': True,
        }
        req = '%s/' % accId
        response = self.make_request(req=req, add_params=params)
        return response

    def account_transactions(self, acc_id):
        """
        List account Transactions /accounts/<accountId>/transactions
        :param accId:
        :return:
        """
        params = {
            'with-balance': True,
            'date_from': '2017-01-01T00:00:00',
            'date_to': '2018-06-01T12:00:00'
        }
        req = '%s/transactions' % acc_id
        response = self.make_request(req=req, add_params=params)
        return response


if __name__ == "__main__":
    AISP = PSD2SEBAccounts()
    r = AISP.list_accounts()

    print("Status code: " + str(r.status_code))
    print("Response: " + r.text)
