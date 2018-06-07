from flask import Flask

application = Flask(__name__)
application.jinja_env.autoescape = False

from controllers.frontpage import frontpage
from controllers.login import login
from controllers.tests import tests

application.register_blueprint(frontpage, url_prefix='/')
application.register_blueprint(login, url_prefix='/login')
application.register_blueprint(tests, url_prefix='/tests')

if __name__ == "__main__":
    application.run(host='178.62.77.129', port=8080, debug=True, threaded=True)
