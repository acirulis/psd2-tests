import http.client

conn = http.client.HTTPSConnection("test.api.ob.baltics.sebgroup.com")

headers = {
    'accept': "application/json",
    'content-type': "application/json",
    'request-id': "123",
    'request-initiator': "TPU"
    }

conn.request("GET", "/v1/accounts", headers=headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))