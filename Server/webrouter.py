from flask import Flask
from controllers import *
import sys

application = Flask(__name__, static_folder='assets')
application.jinja_env.autoescape = False

# simple autoloader for controller routes
modules = sys.modules.keys()
for module in modules:
    parts = module.split('.')
    if len(parts) == 2 and parts[0] == 'controllers':
        mod = parts[1]
        url = '' if mod == 'frontpage' else mod  # exception for index page - does not have extra url
        application.register_blueprint(getattr(sys.modules['controllers.' + mod], mod), url_prefix='/' + url)

# application.register_blueprint(frontpage.frontpage, url_prefix='/')
# application.register_blueprint(login.login, url_prefix='/login')

if __name__ == "__main__":
    application.run(host='178.62.77.129', port=8080, debug=True, threaded=True)
