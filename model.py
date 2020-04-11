import pandas as pd
import numpy as np
import math

from sklearn.model_selection import train_test_split 
from sklearn.linear_model import LinearRegression
from sklearn import metrics

def read_glacier_dataset():
    return pd.read_csv('data/glacier.csv')

def read_sea_ice_dataset():
    return pd.read_csv('data/seaice_extent_temp.csv')

def read_seaice_dataset_year():
    return pd.read_csv('data/year_data.csv')

def predict_seaice_extent_from_temp(inputValue):
    sc = read_sea_ice_dataset()
    sc['mean_extent'] = (sc['extent_north']+sc['extent_south'])*0.5
    X = sc['temp'].values.reshape(-1,1)
    y = sc['mean_extent'].values.reshape(-1,1)
    regressor = LinearRegression()
    regressor.fit(X, y)
    return regressor.predict([[inputValue]])[0][0]

def predict_seaice_extent_from_date(inputValue):
    sc = read_seaice_dataset_year()
    X = sc['year'].values.reshape(-1,1)
    y = sc['mean_extent'].values.reshape(-1,1)
    regressor = LinearRegression()
    regressor.fit(X, y)
    return regressor.predict([[inputValue]])[0][0]

def predict_panic_temp(inputValue):
    result = []
    for i in range(math.floor(inputValue)-25, math.floor(inputValue)+25):
        result.append(predict_seaice_extent_from_date(i))
    return result

def predict_panic_year(inputValue):
    result = []
    for i in range(math.floor(inputValue)-5, math.floor(inputValue)+5):
        result.append(predict_seaice_extent_from_date(i))
    return result