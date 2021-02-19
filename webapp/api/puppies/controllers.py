from flask import abort
from flask_restful import Resource, fields, marshal_with

dog_fields = {
	'photo_id': fields.Stringr(),
	'breed': fields.Nested(),
}

class PuppiesApi(Resources):
	@marshal_with(post_fields)
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

