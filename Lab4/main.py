"""
Data classification project using Decision Tree and SVM (Support Vector Machine).

The goal of the project is to compare the effectiveness of two machine learning algorithms: Decision Tree and SVM in data classification.
The dataset used is the Pima Indians Diabetes Dataset, which contains information about diabetes diagnosis based on various features such as number of pregnancies, glucose level, etc.

Authors: Henryk Mudlaff and Benedykt Borowski
"""

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn import svm
from sklearn.metrics import accuracy_score


def load_dataset():
    """
    Load the Pima Indians Diabetes Dataset

    Returns:
    DataFrame: Loaded dataset as a pandas DataFrame
    """
    url = "https://raw.githubusercontent.com/jbrownlee/Datasets/master/pima-indians-diabetes.data.csv"
    column_names = ["Pregnancies", "Glucose", "BloodPressure", "SkinThickness", "Insulin", "BMI",
                    "DiabetesPedigreeFunction", "Age", "Outcome"]
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
    Evaluate the accuracy of a classifier

    Parameters:
    classifier: Trained classifier
    X_test (DataFrame): Testing features
    y_test (Series): Testing target values

    Returns:
    float: Accuracy score of the classifier
    """
    y_pred = classifier.predict(X_test)
    return accuracy_score(y_test, y_pred)


def main():
    """
    Main function to execute classification tasks using Decision Tree and SVM
    """
    df = load_dataset()
    target_column = "Outcome"
    X, y = split_features_target(df, target_column)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    decision_tree_classifier = train_decision_tree(X_train, y_train)
    decision_tree_accuracy = evaluate_classifier(decision_tree_classifier, X_test, y_test)
    print(f"Decision Tree Classifier Accuracy: {decision_tree_accuracy}")

    svm_classifier = train_svm_classifier(X_train, y_train)
    svm_accuracy = evaluate_classifier(svm_classifier, X_test, y_test)
    print(f"SVM Classifier Accuracy: {svm_accuracy}")


if __name__ == "__main__":
    main()
