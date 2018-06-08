import requests
import datetime
import os

"""
Based on https://developer.swedbank.com/admin/app/api-explorer
"""


class PSD2SEBAPIBase:
    API_VERSION = 'v1'
    endpoint = 'https://test.api.ob.baltics.sebgroup.com/%s/' % API_VERSION

    request_date = ''
    BIC = ''  # Bank Identifier Code

    def __init__(self, api_type=''):
        self.endpoint += api_type
        now = datetime.datetime.now()
        self.request_date = now.strftime("%Y-%m-%d")

    def make_request(self, req='', type='get', add_headers=None, add_params=None):
        headers = {
            'Accept': 'application/json',
            'content-type': 'application/json',
            'request-id': '123',
            'request-initiator': 'PSU',
            'Authorization': 'Bearer eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiJERU1PTFYsaWJzVXNlcjIiLCJleHAiOjE1MzA2Mzk4MzF9.W5Q4cJjJVQ40wJQo8KM7-zT4ZtAFcXsMz7ioFXCfjtrPFJwbqzVDvAbWq2vsSRJbiJRmqo-wTkFJZ6VADVUJqg',
        }
        params = {
        }
        if add_headers is None:
            add_headers = {}
        if add_params is None:
            add_params = {}
        headers_fin = {**headers, **add_headers}
        params_fin = {**params, **add_params}
        private_key_file = os.path.join(os.path.dirname(__file__), 'client.key')
        cert_file = os.path.join(os.path.dirname(__file__), 'client.crt')
        if type == 'get':
            r = requests.get(self.endpoint + '/' + req, data={}, headers=headers_fin, params=params_fin, verify=False,
                             cert=(cert_file, private_key_file))
        elif type == 'post':
            r = requests.post(self.endpoint + '/' + req, data={}, headers=headers_fin, params=params_fin,
                              cert=(cert_file, private_key_file))
        else:
            raise AssertionError('Unknown request type (get, post allowed)')
        print('%s made request to to: %s' % (self.__class__.__name__, r.url))
        return r
