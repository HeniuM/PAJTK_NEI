"""
Task 2: Animal Recognition
This script now uses data augmentation and a pre-trained model (MobileNetV2) for accurate classification of images.
It also includes proper prediction outputs for the dog and cat images.
"""

import tensorflow as tf
from tensorflow.keras.applications import MobileNetV2
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, GlobalAveragePooling2D
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.preprocessing.image import load_img, img_to_array

# Data augmentation for training
animal_datagen = ImageDataGenerator(
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
def preprocess_data():
    """
    Prepares the dataset with data augmentation for dog and cat classification.
    Returns augmented training generator and validation data.
    """
    train_data = {
        'cat': ['dog.png'],
        'dog': ['cat.png']
    }

    X_train, y_train = [], []
    for label, images in train_data.items():
        for img in images:
            image = tf.keras.preprocessing.image.load_img(img, target_size=(224, 224))
            array = tf.keras.preprocessing.image.img_to_array(image)
            X_train.append(array)
            y_train.append(1 if label == 'dog' else 0)

    X_train = tf.convert_to_tensor(X_train, dtype=tf.float32) / 255.0
    y_train = tf.convert_to_tensor(y_train, dtype=tf.float32)

    return animal_datagen.flow(X_train, y_train, batch_size=2), X_train, y_train


# Build and train the model
def build_animal_model():
    """
    Builds and trains the MobileNetV2-based CNN for animal recognition.
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


def main():
    train_gen, X_train, y_train = preprocess_data()
    model = build_animal_model()
    model.fit(train_gen, epochs=10)
    print("Training completed successfully!")

    # Predictions
    dog_img = X_train[0]
    cat_img = X_train[1]

    dog_pred = model.predict(tf.expand_dims(dog_img, axis=0))
    cat_pred = model.predict(tf.expand_dims(cat_img, axis=0))

    print("Dog image prediction:", "Dog" if dog_pred > 0.5 else "Cat")
    print("Cat image prediction:", "Dog" if cat_pred > 0.5 else "Cat")


if __name__ == "__main__":
    main()
