"""
Data classification project using Decision Tree and SVM (Support Vector Machine).

The goal of the project is to compare the effectiveness of two machine learning algorithms: Decision Tree and SVM in data classification.
The dataset used is the Pima Indians Diabetes Dataset, which contains information about diabetes diagnosis based on various features such as number of pregnancies, glucose level, etc.

Authors: Henryk Mudlaff and Benedykt Borowski
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn import svm
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

def load_dataset(url, column_names):
    """
    Load a dataset from a given URL

    Parameters:
    url (str): URL to the dataset
    column_names (list): List of column names for the dataset

    Returns:
    DataFrame: Loaded dataset as a pandas DataFrame
    """
    return pd.read_csv(url, names=column_names)

def split_features_target(df, target_column):
    """
    Split dataset into features and target column

    Parameters:
    df (DataFrame): Dataset as a pandas DataFrame
    target_column (str): Column name for target variable

    Returns:
    X (DataFrame): Features
    y (Series): Target column
    """
    X = df.drop(columns=[target_column])
    y = df[target_column]
    return X, y

def train_decision_tree(X_train, y_train):
    """
    Train a Decision Tree Classifier

    Parameters:
    X_train (DataFrame): Training features
    y_train (Series): Training target values

    Returns:
    DecisionTreeClassifier: Trained Decision Tree Classifier
    """
    classifier = DecisionTreeClassifier()
    classifier.fit(X_train, y_train)
    return classifier

def train_svm_classifier(X_train, y_train):
    """
    Train a Support Vector Machine (SVM) Classifier

    Parameters:
    X_train (DataFrame): Training features
    y_train (Series): Training target values

    Returns:
    SVC: Trained SVM Classifier
    """
    classifier = svm.SVC()
    classifier.fit(X_train, y_train)
    return classifier

def evaluate_classifier(classifier, X_test, y_test):
    """
    Evaluate the accuracy and other metrics of a classifier

    Parameters:
    classifier: Trained classifier
    X_test (DataFrame): Testing features
    y_test (Series): Testing target values

    Returns:
    None
    """
    y_pred = classifier.predict(X_test)
    print("Accuracy Score:", accuracy_score(y_test, y_pred))
    print("Classification Report:\n", classification_report(y_test, y_pred))
    print("Confusion Matrix:\n", confusion_matrix(y_test, y_pred))

def visualize_data(df):
    """
    Visualize the dataset using histograms for each feature

    Parameters:
    df (DataFrame): Dataset as a pandas DataFrame

    Returns:
    None
    """
    df.hist(bins=15, figsize=(15, 10))
    plt.tight_layout()
    plt.show()

def classify_sample(classifier, sample, feature_names):
    """
    Classify a given sample using the trained classifier

    Parameters:
    classifier: Trained classifier
    sample (list or np.array): Sample input data to classify
    feature_names (list): List of feature names for the sample

    Returns:
    int: Predicted class label
    """
    sample_df = pd.DataFrame([sample], columns=feature_names)
    return classifier.predict(sample_df)[0]

def main():
    """
    Main function to execute classification tasks using Decision Tree and SVM
    """
    # Load the first dataset (Pima Indians Diabetes Dataset)
    url_pima = "https://raw.githubusercontent.com/jbrownlee/Datasets/master/pima-indians-diabetes.data.csv"
    column_names_pima = ["Pregnancies", "Glucose", "BloodPressure", "SkinThickness", "Insulin", "BMI", "DiabetesPedigreeFunction", "Age", "Outcome"]
    df_pima = load_dataset(url_pima, column_names_pima)

    # Visualize the dataset
    visualize_data(df_pima)

    # Split dataset into features and target
    target_column = "Outcome"
    X, y = split_features_target(df_pima, target_column)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Train and evaluate Decision Tree Classifier
    print("\nDecision Tree Classifier (Pima Indians Dataset):")
    decision_tree_classifier = train_decision_tree(X_train, y_train)
    evaluate_classifier(decision_tree_classifier, X_test, y_test)

    # Train and evaluate SVM Classifier
    print("\nSVM Classifier (Pima Indians Dataset):")
    svm_classifier = train_svm_classifier(X_train, y_train)
    evaluate_classifier(svm_classifier, X_test, y_test)

    # Load the second dataset (Iris Flowers Dataset)
    url_iris = "https://raw.githubusercontent.com/jbrownlee/Datasets/master/iris.csv"
    column_names_iris = ["sepal_length", "sepal_width", "petal_length", "petal_width", "class"]
    df_iris = load_dataset(url_iris, column_names_iris)

    # Visualize the Iris dataset
    visualize_data(df_iris)

    # Split Iris dataset into features and target
    target_column_iris = "class"
    X_iris, y_iris = split_features_target(df_iris, target_column_iris)
    X_train_iris, X_test_iris, y_train_iris, y_test_iris = train_test_split(X_iris, y_iris, test_size=0.2, random_state=42)

    # Train and evaluate Decision Tree Classifier on Iris Dataset
    print("\nDecision Tree Classifier (Iris Dataset):")
    decision_tree_classifier_iris = train_decision_tree(X_train_iris, y_train_iris)
    evaluate_classifier(decision_tree_classifier_iris, X_test_iris, y_test_iris)

    # Train and evaluate SVM Classifier on Iris Dataset
    print("\nSVM Classifier (Iris Dataset):")
    svm_classifier_iris = train_svm_classifier(X_train_iris, y_train_iris)
    evaluate_classifier(svm_classifier_iris, X_test_iris, y_test_iris)

    # Classify a sample input using both classifiers
    sample = [6, 148, 72, 35, 0, 33.6, 0.627, 50]  # Sample data from Pima Indians dataset
    print("\nSample Classification using Decision Tree (Pima Indians Dataset):", classify_sample(decision_tree_classifier, sample, column_names_pima[:-1]))
    print("Sample Classification using SVM (Pima Indians Dataset):", classify_sample(svm_classifier, sample, column_names_pima[:-1]))

if __name__ == "__main__":
    main()
