from pathlib import Path
from PIL import Image
import unittest
from webapp.api.puppies.make_breed_prediction import make_breed_prediction, IMAGE_WIDTH, IMAGE_HEIGHT
from webapp.api.puppies.prepare_images import prepare_image
import numpy


class TestMLFunction(unittest.TestCase):
    def setUp(self):
        here = Path(__file__)
        english_setter_img_path = here.parent.parent / \
            'utils/00e9ed3fab1d2032603d1a90e557976f.jpg'
        pug_img_path = here.parent.parent / \
            'utils/4ca18a5617593265513954b17b30f37a.jpg'
        self.english_setter = open(english_setter_img_path, 'rb')
        self.english_setter_image = Image.open(self.english_setter)
        self.pug_image = open(pug_img_path, 'rb')

    def test_prepare_image(self):
        """Test process_image function"""
        process_image = prepare_image(
            self.english_setter_image, (IMAGE_WIDTH, IMAGE_HEIGHT))
        self.english_setter.close()
        self.english_setter_image.close()
        assert isinstance(process_image, numpy.ndarray)
        assert process_image.dtype == 'float32'
        assert process_image.shape == (1, IMAGE_WIDTH, IMAGE_HEIGHT, 3)

    def test_make_breed_prediction(self):
        """Test the POST localhost/api/breed return the correct status"""
        prediction = make_breed_prediction(self.pug_image)
        self.pug_image.close()
        breed, prob = prediction[0]
        assert breed == 'pug'



if __name__ == '__main__':
    unittest.main()
