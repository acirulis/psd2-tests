from flask import Blueprint, render_template

frontpage = Blueprint('frontpage', __name__)


@frontpage.route('/')
def index():
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
         'login_url': '#',
         },
        {'logo': 'nordea.png',
         'title': 'NORDEA',
         'api': 'v2.2',
         'api_url': 'https://developer.nordeaopenbanking.com/',
         'login_url': '#',
         },

    ]
    return render_template('index.html', banks=banks)
