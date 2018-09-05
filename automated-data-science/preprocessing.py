import pandas as pd
from pandas import ExcelWriter
from pandas import ExcelFile
import numpy as np

def guassian(mean,std):
    return (1/(std * np.sqrt(2 * np.pi)) * np.exp( - (x - mean)**2 / (2 * std**2)))

def missing_value_filling(file):
    a = file.split(".")
    if a[1] == "xlsx":
        df = pd.read_excel(file)
        columns = list(df.columns.values)
        for word in columns:
            Mode = df[word].mode()
            replaced = df[word].fillna(value=Mode)
            replaced.to_excel (file)
    
    elif a[1] == "csv":
        df = pd.read_csv(file)
        columns = list(df.columns.values)
        for word in columns:
            Mode = df[word].mode()
            replaced = df[word].fillna(value=Mode)
            replaced.to_csv (file)
    
        
