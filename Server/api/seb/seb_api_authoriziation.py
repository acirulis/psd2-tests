from api.seb.seb_api_base import PSD2SEBAPIBase


class PSD2SEBAuthorization(PSD2SEBAPIBase):
    def __init__(self):
        super().__init__('oauth')

    def get_redirect_url(self):
        params = {
            'bic': 'UNLALV2X'
        }
        response = self.make_request(req="authorization/links", add_params=params)
        if response.status_code == 200:
            data = response.json()
            return data[0]['url']
        return response


if __name__ == "__main__":
    AUTH = PSD2SEBAuthorization()
    r = AUTH.get_redirect_url()
    if type(r) is str:
        print('URL: %s' % r)
    else:
        print("Status code: " + str(r.status_code))
        print("Response: " + r.text)
