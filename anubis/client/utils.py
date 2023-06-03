import PIL.Image
import io
import numpy as np
import cv2
import tensorflow as tf
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Dense, Flatten, Reshape
from tensorflow.keras.layers import Dense, Dropout
import pymongo
import uuid
from io import BytesIO
from app1.views import rms
from django.conf import settings
from django.core.mail import send_mail



client_access = pymongo.MongoClient('mongodb+srv://root:UR6dgfcLBXkMlkUW@hackton.u1vq7f7.mongodb.net/')

db = client_access['aventus']

collection = db['metadata']


def create_image(image_byte):
    img_list = []
    for img in image_byte:
        pillow_image = PIL.Image.open(io.BytesIO(img.read()))
        np_array = np.array(pillow_image)
        np_array = np.resize(np_array, new_shape=(224, 224))
        img_list.append(np_array)
    return img_list


def preprocess_image(img_file):
    np_img_pil = PIL.Image.open(io.BytesIO(img_file.read()))
    np_img = np.array(np_img_pil, dtype=np.float64())
    img = cv2.resize(np_img, (224, 224))
    img = img / 255.

    return img


def model_tranning(tensorflow_dataset):
    model = tf.keras.models.Sequential([
        Reshape((224, 224, 1), input_shape=(224, 224)),
        Conv2D(32, (3, 3), activation='relu'),
        MaxPooling2D((2, 2)),
        Conv2D(64, (3, 3), activation='relu'),
        MaxPooling2D((2, 2)),
        Conv2D(128, (3, 3), activation='relu'),
        MaxPooling2D((2, 2)),
        Flatten(),
        Dense(64, activation='relu'),
        Dropout(0.5),
        Dense(4, activation='softmax')
    ])
    model.compile(optimizer='adam',
                  loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
                  metrics=['accuracy'])
    history = model.fit(tensorflow_dataset.batch(32), epochs=10)
    acc = history.history['accuracy']
    loss = history.history['loss']
    print(acc[len(acc) - 1])
    
    weights_list = [arr.tolist() for arr in model.get_weights()]
    username,email_id = rms()
    unique_id = str(uuid.uuid4())
    collection.insert_one({"id":unique_id,'weights':model.get_weights()[0].tolist(),'name':username,'email':email_id,"accuracy":acc[len(acc) - 1],'loss':loss[len(acc) - 1]})
    message = f"Model Accuracy: {acc[9]*100} \n, ID: {unique_id},\nModel Loss:{loss[9]}"
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [email_id]
    subject = "Paramter"
    send_mail( subject, message, email_from, recipient_list )



def predection(img):
    img = np.expand_dims(img,axis=0)
    model = tf.keras.models.load_model('client/alzheimer_model.h5')
    pre = model.predict(img)
    return pre