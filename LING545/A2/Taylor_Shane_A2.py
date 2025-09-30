#!/usr/bin/env python3
"""
LING545/CS659 A2: Text Classification -- Naive Bayes and Logistic Regression
@author: taylosh

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
    Extract the features and labels in the input_file and store them in the vectors x and y, respectively.
    :param input_file: path to the file containing the features and labels
    :return x: binary feature vector of shape N*4
    :return y: label vector of shape N*1
    """
    
    # Thresholds for binaries
    thresholds = np.array([161, 104, 0.061, 5.8])
    
    # Read file
    data = pd.read_csv(input_file, sep='\t')
    
    # Extract features
    features = data[['Number_Word_Tokens', 'Number_Word_Types', 'Spelling_Error_Ratio', 'Average_Word_Length']]
    
    # Binarize features by thresholds
    x = (features.values >= thresholds).astype(int)  # Convert to binary 0 or 1
    
    # Extract labels 
    y = data['Proficiency'].values
    
    return x, y


def data_prep_lr(input_file):
    """
    Extract the features and labels in the input_file and store them in the vectors X and y, respectively.
    :param input_file: path to the file containing the features and labels
    :return X: feature vector of shape N*4
    :return y: label vector of shape N*1
    """
    
    # Read the data (tab-separated)
    data = pd.read_csv(input_file, sep='\t')
    
    # Extract relevant features (no binarization)
    x = data[['Number_Word_Tokens', 'Number_Word_Types', 'Spelling_Error_Ratio', 'Average_Word_Length']].values
    
    # Extract labels (Proficiency column)
    y = data['Proficiency'].values
    
    return x, y


def naive_bayes(x_train, y_train, x_dev, y_dev, x_test, y_test):
    """
    Train a Naive Bayes classifier and evaluate its performance.
    :param x_train: training feature matrix (binary)
    :param y_train: training labels
    :param x_dev: development feature matrix (binary)
    :param y_dev: development labels
    :param x_test: test feature matrix (binary)
    :param y_test: test labels
    :return accuracy: accuracy on the test set
    :return f1: F1 score on the test set
    """
    
    # 2 classes for binary: prof. = 0 or 1
    classes = np.unique(y_train)
    
    # Features
    num_features = x_train.shape[1]
    
    # Priors P(class)
    priors = np.array([np.mean(y_train == c) for c in classes])
    
    # Conditional probs P(feature | class)
    cond_probs = np.zeros((len(classes), num_features))
    
    for c in classes:
        # Get all training samples where y == c (is that right?)
        x_c = x_train[y_train == c]
        
        # P(feature=1 | class=c) with Laplace
        cond_probs[c] = (np.sum(x_c, axis=0) + 1) / (x_c.shape[0] + 2)
    
    # Compute log-prob for given set of features
    def compute_log_prob(x, priors, cond_probs):
        log_probs = []
        for i in range(x.shape[0]):
            # log P(class | features) for each
            log_prob_class_0 = np.log(priors[0]) + np.sum(np.log(cond_probs[0]) * x[i] + np.log(1 - cond_probs[0]) * (1 - x[i]))
            log_prob_class_1 = np.log(priors[1]) + np.sum(np.log(cond_probs[1]) * x[i] + np.log(1 - cond_probs[1]) * (1 - x[i]))
            
            # Store both probs
            log_probs.append([log_prob_class_0, log_prob_class_1])
        
        return np.array(log_probs)
    
    
    # Prediction
    def predict(x, priors, cond_probs):
        log_probs = compute_log_prob(x, priors, cond_probs)
        # Pick class with highest log-prob
        return np.argmax(log_probs, axis=1)
    
    # Predictions on dev & test set
    y_pred_dev = predict(x_dev, priors, cond_probs) #in case I want evaluate the model with dev set
    y_pred_test = predict(x_test, priors, cond_probs)
    
    # Accuracy and F1 on test
    accuracy = accuracy_score(y_test, y_pred_test)
    f1 = f1_score(y_test, y_pred_test)
    
    print(f"Naive Bayes - Test Accuracy: {accuracy}, Test F1 Score: {f1}")
    
    return accuracy, f1


def logistic_regression(X_train, y_train, X_dev, y_dev, X_test, y_test):
    """
    Train a Logistic Regression classifier and evaluate its performance on both development and test sets.
    :param X_train: training feature matrix
    :param y_train: training labels
    :param X_dev: development feature matrix
    :param y_dev: development labels
    :param X_test: test feature matrix
    :param y_test: test labels
    :return accuracy: accuracy on the test set
    :return f1: F1 score on the test set
    """
    # Initialize lr model
    model = LogisticRegression(max_iter=1000)

    # Fit model on training data
    model.fit(X_train, y_train)

    # Predictions on dev set
    y_pred_dev = model.predict(X_dev)

    # Accuracy and F1 on dev set
    dev_accuracy = accuracy_score(y_dev, y_pred_dev)
    dev_f1 = f1_score(y_dev, y_pred_dev)

    # Print dev set performance
    print(f"Logistic Regression - Dev Accuracy: {dev_accuracy}, Dev F1 Score: {dev_f1}")

    # Predict on test 
    y_pred_test = model.predict(X_test)

    # Accuracy and F1 on  test set
    test_accuracy = accuracy_score(y_test, y_pred_test)
    test_f1 = f1_score(y_test, y_pred_test)

    # Print test set performance
    print(f"Logistic Regression - Test Accuracy: {test_accuracy}, Test F1 Score: {test_f1}")

    return test_accuracy, test_f1


if __name__ == "__main__":

    ### path the feature and label files
    input_dir = "./"

    ### Get the features and labels for Naive Bayes
    x_train_nb, y_train_nb = data_prep_nb(os.path.join(input_dir, "train.csv"))
    x_dev_nb, y_dev_nb = data_prep_nb(os.path.join(input_dir, "dev.csv"))
    x_test_nb, y_test_nb = data_prep_nb(os.path.join(input_dir, "test.csv"))

    ### Experiment with feature subsets for Naive Bayes

    # Using all features
    print("Using all features:")
    naive_bayes(x_train_nb, y_train_nb, x_dev_nb, y_dev_nb, x_test_nb, y_test_nb)

    # Using only the first feature
    print("Using only Number_Word_Tokens:")
    naive_bayes(x_train_nb[:, [0]], y_train_nb, x_dev_nb[:, [0]], y_dev_nb, x_test_nb[:, [0]], y_test_nb)

    # Using only the second feature
    print("Using only Number_Word_Types:")
    naive_bayes(x_train_nb[:, [1]], y_train_nb, x_dev_nb[:, [1]], y_dev_nb, x_test_nb[:, [1]], y_test_nb)

    # Using three features (first three)
    print("Using first three features:")
    naive_bayes(x_train_nb[:, :3], y_train_nb, x_dev_nb[:, :3], y_dev_nb, x_test_nb[:, :3], y_test_nb)

    ### Get the features and labels for Logistic Regression
    x_train_lr, y_train_lr = data_prep_lr(os.path.join(input_dir, "train.csv"))
    x_dev_lr, y_dev_lr = data_prep_lr(os.path.join(input_dir, "dev.csv"))
    x_test_lr, y_test_lr = data_prep_lr(os.path.join(input_dir, "test.csv"))

    ### Experiment with feature subsets for Logistic Regression

    # Using all features
    print("Using all features for Logistic Regression:")
    logistic_regression(x_train_lr, y_train_lr, x_dev_lr, y_dev_lr, x_test_lr, y_test_lr)

    # Using only the first feature
    print("Using only Number_Word_Tokens for Logistic Regression:")
    logistic_regression(x_train_lr[:, [0]], y_train_lr, x_dev_lr[:, [0]], y_dev_lr, x_test_lr[:, [0]], y_test_lr)

    # Using only the second feature
    print("Using only Number_Word_Types for Logistic Regression:")
    logistic_regression(x_train_lr[:, [1]], y_train_lr, x_dev_lr[:, [1]], y_dev_lr, x_test_lr[:, [1]], y_test_lr)

    # Using three features (first three)
    print("Using first three features for Logistic Regression:")
    logistic_regression(x_train_lr[:, :3], y_train_lr, x_dev_lr[:, :3], y_dev_lr, x_test_lr[:, :3], y_test_lr)
