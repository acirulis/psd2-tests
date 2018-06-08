from flask import Blueprint, render_template
from api.PSD2Authorization import PSD2Authorization
frontpage = Blueprint('frontpage', __name__)


@frontpage.route('/')
def index():
    seb = PSD2Authorization('seb')
    # redirect_url = seb.get_redirect_url()
    banks = [
        {'logo': 'swedbank.png',
         'title': 'Swedbank',
         'api': 'Beta v1.0',
         'api_url': 'https://www.swedbank.com/openbanking/',
         'login_url': '#',
         },
        {'logo': 'seb.svg',
         'title': 'SEB',
         'api': 'v1.0',
         'api_url': 'https://developer.baltics.sebgroup.com/landing',
         # 'login_url': seb.get_redirect_url(),
         'login_url': 'https://developer.baltics.sebgroup.com/ib-emulator/UNLALV2X?response_type=code&redirectUrl=https:%2F%2Fpsd2.whitedigital.eu&clientId=andis.cirulis@gmail.com&scopes=accounts%20payments%20users.consents&state=1234',
         },
        {'logo': 'nordea.png',
         'title': 'NORDEA',
         'api': 'v2.2',
         'api_url': 'https://developer.nordeaopenbanking.com/',
         'login_url': '#',
         },

    ]
    return render_template('index.html', banks=banks)
