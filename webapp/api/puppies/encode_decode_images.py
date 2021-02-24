IMAGE_WIDTH = 224
IMAGE_HEIGHT = 224
IMAGE_CHANS = 2
IMAGE_DTYPE = 'FLOAT32'

import numpy as np
import base64
import sys


def base64_encode_image(a):
    return base64.b64encode(a).decode("utf-8")


def base64_decode_image(a, dtype, shape):
    a = bytes(a, encoding="utf-8")

    a = np.frombuffer(base64.decodestring(a), dtype=dtype)
    a = a.reshape(shape)

    return a
