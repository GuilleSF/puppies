from .decode_predictions import decode_predictions
from .encode_decode_images import IMAGE_WIDTH, IMAGE_HEIGHT
from .prepare_images import prepare_image
from io import BytesIO
from PIL import Image
from tensorflow.python.keras.applications.resnet import ResNet50


def make_breed_prediction(image):
    image = Image.open(image)
    image = prepare_image(image, (IMAGE_WIDTH, IMAGE_HEIGHT))
    model = ResNet50(weights='imagenet')
    preds = model.predict(image)
    decode_pred = decode_predictions(preds=preds, top=3)

    return decode_pred
