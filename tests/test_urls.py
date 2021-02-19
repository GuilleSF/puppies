import unittest
from webapp import create_app
from webapp.api import rest_api

class TestURLs(unittest.TestCase):
	def setUp(self):
		rest_api.resources = []
		app = create_app('config.TestConfig')
		self.client = app.test_client()

	def test_get_api_breed(self):
		"""Test the GET localhost/api/breed return the correct status"""
		result = self.client.get('/api/breed')
		print(result)
		print(result.data)
		assert result.status_code == 200

	def test_post_api_breed(self):
		"""Test the POST localhost/api/breed return the correct status"""
		result = self.client.post('/api/breed')
		print(result)
		print(result.data)
		assert result.status_code == 200
		



if __name__ == '__main__':
	unittest.main()