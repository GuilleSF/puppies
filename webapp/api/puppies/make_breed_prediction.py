from encode_decode_image import IMAGE_WIDTH, IMAGE_HEIGHT
from prepare_image import prepare_image
from io import BytesIO
from PIL import Image
from tensorflow.python.keras.applications import ResNet50



def make_breed_prediction(image):
    image = Image.open(image.stream)
    image = prepare_image(image, (IMAGE_WIDTH, IMAGE_HEIGHT))
    model = ResNet50(weights='imagenet')
    preds = model.predict(image)

    return preds
