from swed_api_base import PSD2SwedbankAPIBase

class PSD2SwedbankConsents(PSD2SwedbankAPIBase):
    def __init__(self):
        super().__init__('consents')

    def listConsents(self):
        """
        List current customer consents
        :return:
        """
        Response = self.make_request()
        return Response


    def createConsent(self):
        """
        Create new consent
        :return: Response
        """
        Response = self.make_request(type="post")
        return Response




## UPDATE PSU AUTHORIZATION

#update_psu_authorization': '
#https://psd2.api.swedbank.com/sandbox/v1/sign/consent/?bic=SANDLV22&id=6345asgas5343as1a38543ag153ag18531va5eg41a

# headers = {'Date': '2008-01-01',
#            'authorization': 'Bearer dummyToken',
#            'Request-ID': 'TPP-request-ID',
#            'Process-ID': 'TPP-process-ID',
#            }
# payload = {  }
# params = {
#     'BIC': 'SANDLV22',
#     'id': '6345asgas5343as1a38543ag153ag18531va5eg41a',
# }
#
# r = requests.post("https://psd2.api.swedbank.com/sandbox/v1/sign/consent", data=payload, headers=headers, params=params)
#

###########################3

if __name__ == "__main__": # test class

    CONS = PSD2SwedbankConsents()
    # r = CONS.listConsents()
    r = CONS.createConsent()

    if r.status_code == 200:
        print('success. answer: ')
        print(r.text)
    else:
        print('error. status code: ' + str(r.status_code))
        print(r.json())
