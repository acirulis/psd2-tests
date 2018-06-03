import requests
import datetime


"""
Based on https://developer.swedbank.com/admin/app/api-explorer
"""
class PSD2SwedbankAPIBase:
    API_VERSION = 'v1'
    endpoint = 'https://psd2.api.swedbank.com/sandbox/%s/' % API_VERSION

    request_date = ''
    BIC = 'SANDLV22' # 	Bank Identifier Code Allowed values = [SANDSESS, SANDEE2X, SANDLV22, SANDLT22, SWEDSESS, HABAEE2X, HABALT22, HABALV22]


    def __init__(self, api_type = ''):
        self.endpoint += api_type
        now = datetime.datetime.now()
        self.request_date = now.strftime("%Y-%m-%d")



    def make_request(self, req = '', type = 'get', addheaders = {}, addparams = {}):
        headers = {'Date': self.request_date,
                   'authorization': 'Bearer dummyToken',
                   'Request-ID': 'TPP-request-ID',
                   'Process-ID': 'TPP-process-ID',
        }
        params = {
            'BIC': self.BIC,
        }
        headers_fin = {**headers, **addheaders}
        params_fin  = {**params, **addparams}
        if type == 'get':
            r = requests.get(self.endpoint + '/'+ req, data={}, headers=headers_fin, params=params_fin)
        elif type == 'post':
            r = requests.post(self.endpoint + '/'+ req, data={}, headers=headers_fin, params=params_fin)
        else:
            raise AssertionError('Unknown request type (get, post allowed)')
        print('%s made request to to: %s' % (self.__class__.__name__, r.url))
        return r

