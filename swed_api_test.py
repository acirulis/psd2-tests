# curl --include --header "Date:2008-01-01" --header "authorization:Bearer dummyToken" --header "Request-ID:TPP-request-ID"
# --header "Process-ID:TPP-process-ID" \
# --request GET 'https://psd2.api.swedbank.com/sandbox/v1/consents/?BIC=SANDSESS'

import requests


# list active consents
headers = {'Date': '2008-01-01',
           'authorization': 'Bearer dummyToken',
           'Request-ID': 'TPP-request-ID',
           'Process-ID': 'TPP-process-ID',
           }
# payload = {'title': 'value1', 'name': 'value2'}
payload = {  }
params = {
    'BIC': 'SANDLV22'
}

# list active consents
headers = {'Date': '2008-01-01',
           'authorization': 'Bearer dummyToken',
           'Request-ID': 'TPP-request-ID',
           'Process-ID': 'TPP-process-ID',
           }
# payload = {'title': 'value1', 'name': 'value2'}
payload = {  }
params = {
    'BIC': 'SANDLV22'
}

r = requests.get("https://psd2.api.swedbank.com/sandbox/v1/consents", data=payload, headers=headers, params=params)

# # CREATE NEW CONSENT
# headers = {'Date': '2008-01-01',
#            'authorization': 'Bearer dummyToken',
#            'Request-ID': 'TPP-request-ID',
#            'Process-ID': 'TPP-process-ID',
#            }
# payload = {  }
# params = {
#     'BIC': 'SANDLV22'
# }
#
# r = requests.post("https://psd2.api.swedbank.com/sandbox/v1/consents", data=payload, headers=headers, params=params)
#
#



###########################3

print('Request made: ' + r.url)
if r.status_code == 200:
    print('success. answer: ')
    print(r.json())
else:
    print('error. status code: ' + str(r.status_code))
    print(r.json())
