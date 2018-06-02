import requests


# LIST ACTIVE CONSENTS
# headers = {'Date': '2008-01-01',
#            'authorization': 'Bearer dummyToken',
#            'Request-ID': 'TPP-request-ID',
#            'Process-ID': 'TPP-process-ID',
#            }
# # payload = {'title': 'value1', 'name': 'value2'}
# payload = {  }
# params = {
#     'BIC': 'SANDLV22'
# }
#
# r = requests.get("https://psd2.api.swedbank.com/sandbox/v1/consents", data=payload, headers=headers, params=params)
#
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


## UPDATE PSU AUTHORIZATION

#update_psu_authorization': '
#https://psd2.api.swedbank.com/sandbox/v1/sign/consent/?bic=SANDLV22&id=6345asgas5343as1a38543ag153ag18531va5eg41a

headers = {'Date': '2008-01-01',
           'authorization': 'Bearer dummyToken',
           'Request-ID': 'TPP-request-ID',
           'Process-ID': 'TPP-process-ID',
           }
payload = {  }
params = {
    'BIC': 'SANDLV22',
    'id': '6345asgas5343as1a38543ag153ag18531va5eg41a',
}

r = requests.post("https://psd2.api.swedbank.com/sandbox/v1/sign/consent", data=payload, headers=headers, params=params)


###########################3

print('Request made: ' + r.url)
if r.status_code == 200:
    print('success. answer: ')
    print(r.text)
else:
    print('error. status code: ' + str(r.status_code))
    print(r.json())
