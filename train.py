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
print(train_dataset.class_names)
for images, labels in train_dataset:
    print(images.shape)
    print(labels.shape)
    break

NUM_CLASSES = len(train_dataset.class_names)

# Lage modellen
base_model = EfficientNetB0(
    weights="imagenet",
    include_top = False,
    input_shape = (224, 224, 3)
)

# Trene modellen
base_model.trainable = False 
inputs = keras.Input(shape=(224, 224, 3))
x = base_model(inputs)
x = keras.layers.GlobalAveragePooling2D()(x)
outputs = keras.layers.Dense(
    NUM_CLASSES,
    activation="softmax"
)(x)

model = keras.Model(inputs, outputs)

# Evaluere modellen

# Lagre modellen