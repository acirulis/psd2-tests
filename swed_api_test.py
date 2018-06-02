# curl --include --header "Date:2008-01-01" --header "authorization:Bearer dummyToken" --header "Request-ID:TPP-request-ID"
# --header "Process-ID:TPP-process-ID" \
# --request GET 'https://psd2.api.swedbank.com/sandbox/v1/consents/?BIC=SANDSESS'

import requests

headers = {'Date': '2008-01-01',
           'authorization': 'Bearer dummyToken',
           'Request-ID': 'TPP-request-ID',
           'Process-ID': 'TPP-process-ID',


           }
# payload = {'title': 'value1', 'name': 'value2'}
payload = { }

r = requests.post("https://psd2.api.swedbank.com/sandbox/v1/consents/?BIC=SANDSESS", data=payload, headers=headers)

print(r)

