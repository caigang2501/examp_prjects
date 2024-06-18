"""
This is a boilerplate pipeline
generated using Kedro 0.18.8
"""
import logging
from typing import Any, Dict, Tuple

import numpy as np
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import mean_squared_error
from joblib import dump, load

from sklearn.naive_bayes import MultinomialNB

from sklearn.svm import SVC
from sklearn.feature_extraction.text import TfidfVectorizer,TfidfTransformer,CountVectorizer
from sklearn.pipeline import Pipeline

def text_split_aws_data(
    data: pd.DataFrame, parameters: Dict[str, Any]
) -> Tuple[pd.DataFrame, pd.DataFrame, pd.Series, pd.Series]:
    """Splits data into features and target training and test sets.

    Args:
        data: Data containing features and target.
        parameters: Parameters defined in parameters.yml.
    Returns:
        Split data.
    """

    data_train = data.sample(
        frac=parameters["train_fraction"], random_state=parameters["random_state"]
    )
    data_test = data.drop(data_train.index)
    X_train = data_train[parameters["text_column"]]
    X_test = data_test[parameters["text_column"]]
    y_train = data_train[parameters["text_target_column"]]
    y_test = data_test[parameters["text_target_column"]]

    return X_train, X_test, y_train, y_test


def text_split_twitter_data(
    data: pd.DataFrame, parameters: Dict[str, Any]
) -> Tuple[pd.DataFrame, pd.DataFrame, pd.Series, pd.Series]:

    data_train = data.sample(
        frac=parameters["train_fraction"], random_state=parameters["random_state"]
    )
    data_test = data.drop(data_train.index)
    X_train = data_train[parameters["text_twitter"]]
    X_test = data_test[parameters["text_twitter"]]
    y_train = data_train[parameters["rating_twitter"]]
    y_test = data_test[parameters["rating_twitter"]]

    return X_train, X_test, y_train, y_test


def new_and_train_model(X_train: pd.DataFrame, y_train: pd.Series):

    LR_pipeline = Pipeline([
        ('tfidf', TfidfVectorizer()), 
        ('clf', LogisticRegression())
    ])

    svm_pipeline = Pipeline([
        ("tfidf", TfidfVectorizer(stop_words="english")),
        ("clf", SVC(kernel="linear"))
    ])

    NB_pipeline = Pipeline([
        ("vectorizer", CountVectorizer(stop_words="english")),
        ('tfidf', TfidfTransformer()),
        ("clf", MultinomialNB())
    ])

    # svm_pipeline.fit(X_train,y_train)
    # dump(svm_pipeline,'SVM_twiter_model.pkl')

    # NB_pipeline.fit(X_train,y_train)
    # dump(LR_pipeline,'NB_twiter_model.pkl')

    LR_pipeline.fit(X_train,y_train)
    # dump(LR_pipeline,'LR_twiter_model.pkl')

    return LR_pipeline

def emotion_predict(model:Pipeline, X_test: pd.DataFrame,y_test: pd.Series):
    y_pred = model.predict(X_test)
    mse = mean_squared_error(y_test, y_pred)
    print('NB Mean Squared Error:', mse)

    accuracy = (y_pred == y_test).sum() / len(y_test)
    print('accuracy:', accuracy)
    logger = logging.getLogger(__name__)
    logger.info("Model has accuracy of %.3f on test data.", accuracy)

    return mse  


