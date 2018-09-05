# -*- coding: utf-8 -*-
"""
Created on Fri Jun  8 22:23:46 2018

@author: prithvi
"""

import autosklearn.classification
import sklearn.model_selection
import sklearn.datasets
import sklearn.metrics
def model(df,todo):
    X, y = sklearn.datasets.load_digits(return_X_y=True)
    X_train, X_test, y_train, y_test = \
            sklearn.model_selection.train_test_split(X, y, random_state=1)
    if todo = 'classification':
        automl = autosklearn.classification.AutoSklearnClassifier()
        automl.fit(X_train, y_train)
        y_hat = automl.predict(X_test)
    elif todo = 'regression':
        automl = autosklearn.regression.AutoSklearnClassifier()
        automl.fit(X_train, y_train)
        y_hat = automl.predict(X_test)
    elif todo = 'clustering':
        automl = autosklearn.clustering.AutoSklearnClassifier()
        automl.fit(X_train, y_train)
        y_hat = automl.predict(X_test)
    print("Accuracy score", sklearn.metrics.accuracy_score(y_test, y_hat))
    return sklearn.metrics.accuracy_score(y_test, y_hat)
 