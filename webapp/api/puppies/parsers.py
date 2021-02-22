from flask_restful import reqparse
import werkzeug

image_post_parser = reqparse.RequestParser()
image_post_parser.add_argument(
    'dog_image',
    type=werkzeug.datastructures.FileStorage,
    location='files'
)
