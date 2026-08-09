# Imports
import tensorflow as tf
from tensorflow import keras

model = keras.models.load_model("models/pokemon_model.keras")

with open("models/class_names.txt", "r") as file:
    class_names = file.read().splitlines()

IMAGE_PATH = "images/pikachu.png"

image = keras.utils.load_img(
    IMAGE_PATH,
    target_size=(224, 224)
)

image_array = keras.utils.img_to_array(image)

image_array = tf.expand_dims(image_array, axis=0)

predictions = model.predict(image_array)

predicted_index = tf.argmax(predictions[0]).numpy()

predicted_pokemon = class_names[predicted_index]

confidence = predictions[0][predicted_index] * 100

print(f"Predikert Pokémon: {predicted_pokemon}")
print(f"Sannsynlighet: {confidence:.2f}%")