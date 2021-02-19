from flask import abort
from flask_restful import Resource, fields, marshal_with


nested_breed_fields = {
    'breed': fields.String(),
    'probability': fields.Float()
}
dog_fields = {
	'photo_id': fields.String(),
	'breed': fields.List(fields.Nested(nested_breed_fields)),
}

class PuppiesApi(Resource):
	@marshal_with(dog_fields)
	def post(self, dog_image=None):
		if dog_image:
			#transform-image
			#calculate prob
			breed_list = None
			if not breed_list:
				abort(404)
			return breed_list
		else:
			abort(400)

	def get(self):
		return{
				'info': 'This is an API for dogs breed categorization.',
				'help': 'Use in terminal: curl -X POST -F \"image=@/path_to_image_dog/image.jpg\" localhost/api/breed',
			}

