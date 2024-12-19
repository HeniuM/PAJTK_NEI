"""
Task 1: Data Classification (CSV-based)
Authors: Henryk Mudlaff, Benedykt Borowski
"""

import pandas as pd
import numpy as np
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix


def load_and_prepare_data(file_path):
    """
    Load a CSV file and prepare it for training a neural network.

    Args:
        file_path (str): Path to the CSV file.

    Returns:
        Tuple: Split dataset into training and testing features and targets.
    """
    df = pd.read_csv(file_path)
    features = df.iloc[:, :-1].values  # All columns except the last
    target = df.iloc[:, -1].values  # Last column
    target = np.where(target > 1, 1, 0)  # Binarize target
    return train_test_split(features, target, test_size=0.2, random_state=42)


def create_model(input_dim):
    """
    Create a neural network model for binary classification.

    Args:
        input_dim (int): Number of input features.

    Returns:
        keras.Model: Compiled neural network model.
    """
    model = Sequential([
        Dense(16, activation='relu', input_dim=input_dim),
        Dense(8, activation='relu'),
        Dense(1, activation='sigmoid')
    ])
    model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
    return model


def main():
    """
    Main function for Task 1: Train and evaluate the model using CSV data.
    """
    file_path = "seeds_dataset.csv"
    X_train, X_test, y_train, y_test = load_and_prepare_data(file_path)
    model = create_model(X_train.shape[1])
    model.fit(X_train, y_train, epochs=50, batch_size=8, verbose=0)
    predictions = (model.predict(X_test) > 0.5).astype("int32")
    print("Accuracy:", accuracy_score(y_test, predictions))
    print("Confusion Matrix:\n", confusion_matrix(y_test, predictions))


if __name__ == "__main__":
    main()
