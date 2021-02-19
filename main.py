import os
from webapp import create_app

env = os.environ['APP_SETTINGS']
app = create_app(env)

if __name__ == '__main__':
    app.run()
