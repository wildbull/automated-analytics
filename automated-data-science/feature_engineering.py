# -*- coding: utf-8 -*-
"""
Created on Fri Aug 10 10:19:33 2018

@author: prithvi
"""
import pandas as pd
import numpy as np
import 

# featuretools for automated feature engineering
import featuretools as ft

# ignore warnings from pandas
import warnings
warnings.filterwarnings('ignore')

def feature_engineering(data):
    features = list(data.columns.values)
    es = ft.EntitySet(features[0])
    primitives = ft.list_primitives()
    pd.options.display.max_colwidth = 100
    primitives[primitives['type'] == 'aggregation'].head(10)
    primitives[primitives['type'] == 'transform'].head(10)
    sLength = len(data[features[0]])
    data['new_feature'] = list(np.random.randn(sLength), index=data.index)
    features, feature_names = ft.dfs(entityset=es, target_entity='new_features', max_depth = 2)
    features.iloc[:, 4:].head()
    
    return data