import os
from api import create_app

env = os.environ.['APP_SETTING']
app = create_app(env)

if __name__ == '__main__':
    app.run()
