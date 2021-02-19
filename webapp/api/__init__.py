from flask_restful import Api
from .puppies.controllers import PuppiesApi

rest_api = Api()

def create_module(app, **kwargs):

    rest_api.add_resource(
        PuppiesApi,
        '/api/breed',
    )
    rest_api.init_app(app)