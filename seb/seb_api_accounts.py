from seb_api_base import PSD2SEBAPIBase

class PSD2SEBAccounts(PSD2SEBAPIBase):
    def __init__(self):
        super().__init__('accounts')

    def listAccounts(self):
        params = {

        }
        Response = self.make_request(addparams=params)
        return Response


    def accountDetails(self, accId):
        """
        Get account details /accounts/<accountId>
        :param accId:
        :return: Response
        """
        params = {
            'with-balance': True,
        }
        req = '%s/' % accId
        r = self.make_request(req=req,addparams=params)
        return r


    def accountTransactions(self, accId):
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
        req = '%s/transactions' % accId
        r = self.make_request(req=req,addparams=params)
        return r

if __name__ == "__main__":
    AISP = PSD2SEBAccounts()
    r = AISP.listAccounts()

    print("Status code: " + str(r.status_code))
    print("Response: " + r.text)