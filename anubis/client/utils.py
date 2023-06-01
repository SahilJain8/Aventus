import tensorflow.python.data
from PIL import Image
import io
import numpy as np
import tensorflow as tf


def data_set(class1):
    img_arr = []
    for file_1 in class1:
        np_img_pil = Image.open(io.BytesIO(file_1.read()))
        np_img = np.array(np_img_pil)
        img_arr.append(np_img)
    dataset = tensorflow.data.Dataset.from_tensor_slices(img_arr)
    return dataset
