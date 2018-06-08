from api.seb.seb_api_authoriziation import PSD2SEBAuthorization


class PSD2Authorization:
    bank = ''
    bankobject = None

    def __init__(self, bank):
        if bank not in ['seb']:
            raise AssertionError("Bank %s not implemented" % bank)
        self.bank = bank
        if bank == 'seb':
            self.bankobject = PSD2SEBAuthorization()

    def get_redirect_url(self):
        return self.bankobject.get_redirect_url()


if __name__ == "__main__":
    AUTH = PSD2Authorization('seb')
    r = AUTH.get_redirect_url()
    print(r)
