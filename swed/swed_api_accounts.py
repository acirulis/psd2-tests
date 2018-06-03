from swed_api_base import PSD2SwedbankAPIBase

class PSD2SwedbankAccounts(PSD2SwedbankAPIBase):
    def __init__(self):
        super().__init__('accounts')

    def listAccounts(self):
        params = {'with-balance': True}
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


###########################3


if __name__ == '__main__':
    # # GET Account transactions
    # # LT377300010010269362 #bez transakcijam ; atveras
    # # LT377300010010270888 # missing consent
    # # LT747300010010270636 # bez transakcijam
    # # LT377300010010270623 # ir transakcijas
    # # LT377300010010270568 # missing consent

    AISP = PSD2SwedbankAccounts()

    # r = AISP.listAccounts()
    # r = AISP.accountTransactions('LT377300010010270623')
    r = AISP.accountDetails('LT377300010010270623')

    if r.status_code == 200:
        print('success. answer: ')
        print(r.text)
    else:
        print('error. status code: ' + str(r.status_code))
        print(r.json())
