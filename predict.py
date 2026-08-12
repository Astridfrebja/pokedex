import tensorflow as tf
from tensorflow import keras

MODEL_PATH = "models/pokemon_model.keras"
CLASS_NAMES_PATH = "models/class_names.txt"
IMAGE_SIZE = (224, 224)

model = keras.models.load_model(MODEL_PATH)

with open(CLASS_NAMES_PATH) as file:
    class_names = file.read().splitlines()


def predict(image_path):

    image = keras.utils.load_img(
        image_path,
        target_size=IMAGE_SIZE
    )

    image_array = keras.utils.img_to_array(image)
    image_array = tf.expand_dims(image_array, axis=0)

    predictions = model.predict(image_array, verbose=0)

    top_3 = tf.argsort(
        predictions[0],
        direction="DESCENDING"
    )[:3]

    results = []

    for index in top_3:

        pokemon = class_names[index]
        confidence = float(predictions[0][index] * 100)

        results.append(
            (pokemon, confidence)
        )

    return results