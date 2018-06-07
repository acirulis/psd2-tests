from flask import Blueprint, render_template

frontpage = Blueprint('frontpage', __name__)


@frontpage.route('/')
def index():
    data = {'key': 'value'}
    return render_template('index.html', key=data)
