
from flask import abort
from flask_restful import Resource, fields, marshal_with, request
from .parsers import image_post_parser
from rq import Queue
from rq.job import Job
from worker import conn

from .make_breed_prediction import make_breed_prediction


q = Queue(connection=conn)

nested_breed_fields = {
    'breed': fields.String(),
    'probability': fields.Float()
}

dog_fields = {
    'photo_id': fields.String(),
    'breed': fields.List(fields.Nested(nested_breed_fields)),
}


def classificate_image():
    print("Classifying image")
    return "Classifying image"


def transform_image(dog_image):
    print("Transforming image")
    return classificate_image()


class PuppiesApi(Resource):
    @marshal_with(dog_fields)
    def post(self, dog_image=None):
        args = image_post_parser.parse_args(strict=True)
        dog_image = args['dog_image']
        if dog_image:
            response = make_breed_prediction(dog_image)
            return(response, type(response)), 200
            # job = q.enqueue_call(
                # func=transform_image, args=(dog_image,), result_ttl=5000)
            # transform-image
            # calculate prob
            breed_list = None
            if not breed_list:
                abort(404)
            return breed_list
        else:
            abort(400)

    def get(self):
        return{
            'info': 'This is an API for dogs breed prediction.',
            'help': 'Use in terminal: curl -X POST -F \"image=@/path_to_image_dog/image.jpg\" localhost/api/breed',
        }
