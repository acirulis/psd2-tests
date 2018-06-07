from flask import Blueprint, Response

tests = Blueprint('tests', __name__)


@tests.route('/')
def index():
    import json
    raw = {'key': 'value', 'key2: ': ['el', 'em', 'ent']}
    data = json.dumps(raw)
    return Response(data, mimetype='text/json')


@tests.route('/raw')
def raw():
    return Response('raw data', mimetype='text/html')


