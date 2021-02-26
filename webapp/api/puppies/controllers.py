
from flask import abort
from flask_restful import Resource, fields, marshal_with, request
from .parsers import image_post_parser
from rq import Queue
from rq.job import Job
from worker import conn

from .make_breed_prediction import make_breed_prediction


q = Queue(connection=conn)


class PuppiesApi(Resource):
    def post(self, dog_image=None):
        args = image_post_parser.parse_args(strict=True)
        dog_image = args['dog_image'].stream
        if dog_image:
            job = q.enqueue_call(func=make_breed_prediction,
                                 args=(dog_image,), result_ttl=500)
            while not job.is_finished:
                status = job.get_status()
                if status in ["failed"]:
                    abort(503)
            breed_list = job.result
            if not breed_list:
                abort(404)
            return {'dog_breed': breed_list}
        else:
            abort(400)

    def get(self):
        return{
            'info': 'This is an API for dogs breed prediction.',
            'help': 'Use in terminal: curl -X POST -F \"image=@/path_to_image_dog/image.jpg\" localhost/api/breed',
        }
