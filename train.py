# Imports
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.applications import EfficientNetB0


# Konstanter
TRAIN_DIR = "dataset/train"
TEST_DIR = "dataset/test"

IMAGE_SIZE = (224, 224)
BATCH_SIZE = 32

# Laste inn datasettet
train_dataset = keras.utils.image_dataset_from_directory(
    TRAIN_DIR,
    image_size = IMAGE_SIZE,
    batch_size = BATCH_SIZE
    )

test_dataset = keras.utils.image_dataset_from_directory(
    TEST_DIR,
    image_size = IMAGE_SIZE,
    batch_size = BATCH_SIZE
    )

# Utforske datasettet

NUM_CLASSES = len(train_dataset.class_names)

print(f"Antall klasser: {NUM_CLASSES}")
print(f"Første 10 klasser: {train_dataset.class_names[:10]}")
for images, labels in train_dataset:
    print(images.shape)
    print(labels.shape)
    break

# Lage modellen
base_model = EfficientNetB0(
    weights="imagenet",
    include_top = False,
    input_shape = (224, 224, 3)
)

base_model.trainable = False 

# Trene modellen
inputs = keras.Input(shape=(224, 224, 3))
x = base_model(inputs, training=False)
x = keras.layers.GlobalAveragePooling2D()(x)
outputs = keras.layers.Dense(
    NUM_CLASSES,
    activation="softmax"
)(x)

model = keras.Model(inputs, outputs)

model.compile(
    optimizer="adam",
    loss = "sparse_categorical_crossentropy",
    metrics = ["accuracy"]
)

history = model.fit(
    train_dataset,
    validation_data=test_dataset,
    epochs=3
)

# Evaluere modellen
test_loss, test_accuracy = model.evaluate(test_dataset)

print(f"Test loss: {test_loss:.4f}")
print(f"Test accuracy: {test_accuracy:.4f}")

# Lagre modellen
model.save("models/pokemon_model.keras")
with open("models/class_names.txt", "w") as file:
    for class_name in train_dataset.class_names:
        file.write(class_name + "\n")