"""
Task 3: Clothing Recognition
Uses the same structure as Task 2 with augmentation and pre-trained MobileNetV2 for recognizing jackets and trousers.
Includes proper prediction outputs for jacket and trousers images.
"""

import tensorflow as tf
from tensorflow.keras.applications import MobileNetV2
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, GlobalAveragePooling2D
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.preprocessing.image import load_img, img_to_array

# Data augmentation for training
clothing_datagen = ImageDataGenerator(
    rescale=1. / 255,
    rotation_range=20,
    width_shift_range=0.2,
    height_shift_range=0.2,
    shear_range=0.2,
    zoom_range=0.2,
    horizontal_flip=True,
    fill_mode='nearest'
)


# Load and preprocess images
def preprocess_clothing_data():
    """
    Prepares the dataset with data augmentation for jacket and trousers classification.
    Returns augmented training generator and validation data.
    """
    train_data = {
        'trousers': ['jacket.png'],
        'jacket': ['trausers.png']
    }

    X_train, y_train = [], []
    for label, images in train_data.items():
        for img in images:
            image = tf.keras.preprocessing.image.load_img(img, target_size=(224, 224))
            array = tf.keras.preprocessing.image.img_to_array(image)
            X_train.append(array)
            y_train.append(1 if label == 'jacket' else 0)

    X_train = tf.convert_to_tensor(X_train, dtype=tf.float32) / 255.0
    y_train = tf.convert_to_tensor(y_train, dtype=tf.float32)

    return clothing_datagen.flow(X_train, y_train, batch_size=2), X_train, y_train


# Build and train the model
def build_clothing_model():
    """
    Builds and trains the MobileNetV2-based CNN for clothing recognition.
    """
    base_model = MobileNetV2(weights='imagenet', include_top=False, input_shape=(224, 224, 3))
    base_model.trainable = False

    model = Sequential([
        base_model,
        GlobalAveragePooling2D(),
        Dense(128, activation='relu'),
        Dense(1, activation='sigmoid')
    ])

    model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
    return model


def main_clothing():
    train_gen, X_train, y_train = preprocess_clothing_data()
    model = build_clothing_model()
    model.fit(train_gen, epochs=10)
    print("Training completed successfully!")

    # Predictions
    jacket_img = X_train[0]
    trousers_img = X_train[1]

    jacket_pred = model.predict(tf.expand_dims(jacket_img, axis=0))
    trousers_pred = model.predict(tf.expand_dims(trousers_img, axis=0))

    print("Jacket image prediction:", "Jacket" if jacket_pred > 0.5 else "Trousers")
    print("Trousers image prediction:", "Jacket" if trousers_pred > 0.5 else "Trousers")


if __name__ == "__main__":
    main_clothing()
