import os

from flask_script import Manager

from boogle import create_app


try:
    app_env = os.environ['BOOGLE_APP_ENVIRONMENT']
except KeyError:
    app_env = 'dev'

app = create_app(app_env)
manager = Manager(app)


if __name__ == '__main__':
    """Activate manager.

    Register app instance with manager.

    Config from object takes 1 of 3 values:
        * 'dev'
        * 'test'
        * 'production'
    """

    manager.run()
