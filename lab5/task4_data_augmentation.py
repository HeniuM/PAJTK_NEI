"""
Task 4: Enhanced Data Augmentation
This script demonstrates data augmentation by displaying and saving augmented images in real-time.
"""

import os
import tensorflow as tf
from tensorflow.keras.preprocessing.image import ImageDataGenerator, load_img, img_to_array
import matplotlib.pyplot as plt

# Directory to save augmented images
OUTPUT_DIR = "augmented_images"
if not os.path.exists(OUTPUT_DIR):
    os.makedirs(OUTPUT_DIR)


# Load and preprocess the image
def load_and_preprocess_image(image_path):
    """
    Load and preprocess the image for augmentation.

    Args:
        image_path (str): Path to the input image.

    Returns:
        numpy.ndarray: Preprocessed image.
    """
    img = load_img(image_path, target_size=(128, 128))
    img_array = img_to_array(img)
    img_array = img_array.reshape((1,) + img_array.shape)  # Add batch dimension
    return img_array


# Data augmentation generator
def create_datagen():
    """
    Create an ImageDataGenerator instance with augmentation configurations.

    Returns:
        ImageDataGenerator: Configured data augmentation generator.
    """
    return ImageDataGenerator(
        rotation_range=40,
        width_shift_range=0.2,
        height_shift_range=0.2,
        shear_range=0.2,
        zoom_range=0.2,
        horizontal_flip=True,
        fill_mode='nearest'
    )


# Generate and save/display augmented images
def generate_augmented_images(image_path, num_images=5):
    """
    Generate augmented images from the input image.

    Args:
        image_path (str): Path to the input image.
        num_images (int): Number of augmented images to generate.
    """
    img_array = load_and_preprocess_image(image_path)
    datagen = create_datagen()

    print("Generating augmented images...")
    i = 0
    for batch in datagen.flow(img_array, batch_size=1, save_to_dir=OUTPUT_DIR, save_prefix="aug", save_format="jpeg"):
        plt.figure()
        img = batch[0].astype('uint8')
        plt.imshow(img)
        plt.axis('off')
        plt.show()

        i += 1
        if i >= num_images:
            break


# Main function
def main():
    """
    Main function to demonstrate data augmentation.
    """
    image_path = "image.png"  # Update with your image file path
    generate_augmented_images(image_path, num_images=5)


if __name__ == "__main__":
    main()
