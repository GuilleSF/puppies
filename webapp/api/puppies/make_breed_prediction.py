from .encode_decode_images import IMAGE_WIDTH, IMAGE_HEIGHT, base64_encode_image
from .prepare_images import prepare_image
from io import BytesIO
from PIL import Image
from tensorflow.python.keras.applications.resnet import ResNet50


def make_breed_prediction(image):
    image = Image.open(image.stream)
    image = prepare_image(image, (IMAGE_WIDTH, IMAGE_HEIGHT))
    model = ResNet50(weights='imagenet')
    preds = model.predict(image)

    return preds
