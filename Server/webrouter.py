from flask import Flask
from controllers import *
import sys
import os
from logger import Logger

# CREATE MAIN APPLICATION #
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


# application.register_blueprint(login.login, url_prefix='/login')

@application.template_filter('autoversion')
def autoversion_filter(filename):
    # determining fullpath might be project specific
    full_path = os.path.join('.', filename[1:])
    try:
        timestamp = str(os.path.getmtime(full_path))
    except OSError:
        return filename
    new_filename = "{0}?v={1}".format(filename, timestamp)
    return new_filename


if __name__ == "__main__":
    application.run(host='178.62.77.129', port=8080, debug=True, threaded=True)
