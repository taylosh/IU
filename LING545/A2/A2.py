#!/usr/bin/env python3
"""
LING545/CS659 A2: Text Classification -- Naive Bayes and Logistic Regression
@author: Shuju Shi

In this assignment, you will implement two text classification models for L2 writing assessment:
    1. Naive Bayes: For this, you will have to implement the algorithm from scratch.
    2. Logistic Regression: For this, you will be using the implementation from sklearn, which has already been imported for you.
"""

### Import libraries
import os
import numpy as np
import pandas as pd
from sklearn.metrics import accuracy_score, f1_score
from sklearn.linear_model import LogisticRegression

def data_prep_nb(input_file):
    """
    Extract the features and labels in the input_file and store them in the vectors X and y, respectively.
    :param input_file: path to the file containing the features and labels
    :return X: binary feature vector of shape N*4.
    :return y: label vector of shape N*1

    """
    ### This array holds the thresholds used to binarize the original features.
    ### If the feature value in each column is greater than or equal to the corresponding threshold, it is set to 1; otherwise, it is set to 0.

    thresholds = np.array([161, 104, 0.061, 5.8])

    ##Start your implementation here
    ...

    return X, y

def data_prep_lr(input_file):
    """
    Extract the features and labels in the input_file and store them in the vectors X and y, respectively.
    :param input_dir: directory to the file contain features and labels
    :return X: feature vector of shape N*4
    :return y: label vector of shape N*1
    """
    ##Start your implementation here
    ...

    return X, y


def naive_bayes(X_train, y_train, X_dev, y_dev, X_test, y_test):
    """
    :param X_train:
    :param y_train:
    :param X_dev:
    :param y_dev:
    :param X_test:
    :param y_test:
    :return accuracy:
    :return f1:
    """
    ### start your implementation here
    ...
    return accuracy, f1

def logistic_regression(X_train, y_train, X_dev, y_dev, X_test, y_test):
    """
    :param X_train:
    :param y_train:
    :param X_dev:
    :param y_dev:
    :param X_test:
    :param y_test:
    :return accuracy:
    :return f1:
    """
    ### start your implementation here

    ...
    return accuracy, f1

if __name__ == "__main__":

    ### path the feature and label files
    input_dir = "./"

    ### Get the features and labels for Naive Bayes
    X_train_nb, y_train_nb = data_prep_nb(os.path.join(input_dir, "train.csv"))
    X_dev_nb, y_dev_nb = data_prep_nb(os.path.join(input_dir, "dev.csv"))
    X_test_nb, y_test_nb = data_prep_nb(os.path.join(input_dir, "test.csv"))

    ### Peform text classification using Naive Bayes
    naive_bayes(X_train_nb, y_train_nb, X_dev_nb, y_dev_nb, X_test_nb, y_test_nb)

    ### Get the features and labels for Logistic Regression
    X_train_lr, y_train_lr = data_prep_lr(os.path.join(input_dir, "train.csv"))
    X_dev_lr, y_dev_lr = data_prep_lr(os.path.join(input_dir, "dev.csv"))
    X_test_lr, y_test_lr = data_prep_lr(os.path.join(input_dir, "test.csv"))

    ### Peform text classification using Logistic Regression
    logistic_regression(X_train_lr, y_train_lr, X_dev_lr, y_dev_lr, X_test_lr, y_test_lr)







