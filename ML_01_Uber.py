# -*- coding: utf-8 -*-
"""ML Ass1.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1lYRCMsttIUL-VO1u8OT3N_J3wF3h26DU
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split

df=pd.read_csv("uber.csv")
df

df.shape

df.size

df.isna().sum()

df.duplicated().sum()

df['dropoff_longitude']=df['dropoff_longitude'].fillna(df['dropoff_longitude'].mean())
df['dropoff_latitude']=df['dropoff_latitude'].fillna(df['dropoff_latitude'].mean())
df.isna().sum()

df.drop(['Unnamed: 0', 'key'], axis=1, inplace=True)
df

df['datetime'] = pd.to_datetime(df['pickup_datetime'], utc=True)
df['weekday'] = df['datetime'].dt.weekday
df['month'] = df['datetime'].dt.month
df['year'] = df['datetime'].dt.year
df['hour'] = df['datetime'].dt.hour
df['minute'] = df['datetime'].dt.minute
df.head()

import numpy as np

def filter_latitude(val):
    if val < -90 or val > 90:
        return np.nan
    else:
        return val

def filter_longitude(val):
    if val < -180 or val > 180:
        return np.nan
    else:
        return val

df['pickup_longitude'] = df['pickup_longitude'].apply(filter_longitude)
df['pickup_latitude'] = df['pickup_latitude'].apply(filter_latitude)
df['dropoff_longitude'] = df['dropoff_longitude'].apply(filter_longitude)
df['dropoff_latitude'] = df['dropoff_latitude'].apply(filter_latitude)

df.isna().sum()

df.dropna(inplace=True)

df[df['fare_amount'].values <= 0]

df.drop(df[df['fare_amount'].values <= 0].index,inplace= True)

df[df['fare_amount'].values <= 0]

df.shape

!pip install geopy

from geopy.distance import great_circle

def distance_km(x):
    pickup = (x['pickup_latitude'], x['pickup_longitude'])
    dropoff = (x['dropoff_latitude'], x['dropoff_longitude'])
    dist = great_circle(pickup, dropoff).km
    return dist

df['distance_km'] = df.apply(lambda x: distance_km(x), axis=1)
df.drop(['pickup_longitude', 'pickup_latitude', 'dropoff_longitude',
          'dropoff_latitude', 'pickup_datetime'], axis=1, inplace=True) # Assuming you want to drop these columns as well

df[df['distance_km'].values <= 0]

df.drop(df[df['distance_km'].values <= 0].index,inplace= True)
 df.shape

df.drop('datetime',axis=1,inplace=True)
df

df[df['passenger_count'].values <= 0]

df.drop(df[df['passenger_count'].values <= 0].index,inplace= True)
df[df['passenger_count'].values <= 0]

def f_outlier(df):
 q1=df.quantile(0.25)
 q3=df.quantile(0.75)
 IQR=q3-q1
 outliers = df[((df<(q1-1.5*IQR))| (df>(q3+1.5*IQR)))]
 return outliers
out = f_outlier(df['fare_amount'])
outpc = f_outlier(df['passenger_count'])
print('number of outliers: ',len(out)+len(outpc))

df.drop(df[df['distance_km'] == 0].index, inplace = True)
 df.drop(df[df['distance_km'] > 60].index, inplace = True)
 df.drop(df[df['fare_amount'] > 100].index, inplace = True)
 df.drop(df[df['fare_amount'] < 0].index, inplace = True)
 df.drop(df[df['passenger_count'] > 6].index, inplace = True)

from sklearn.linear_model import LinearRegression
 from sklearn.model_selection import train_test_split
 from sklearn.preprocessing import StandardScaler
 x = df[['year','distance_km','passenger_count']]
 y = df['fare_amount']
 scaler = StandardScaler()
 x = scaler.fit_transform(x)

 x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.2,random_state=42)
 model=LinearRegression()
 model.fit(x_train,y_train)

y_pred = model.predict(x_test)
y_pred

from sklearn.metrics import mean_squared_error,mean_absolute_error,r2_score
 import numpy as np
 print(f"mean sq error: {mean_squared_error(y_test,y_pred)}")
 print(f"root mean sq error: {np.sqrt(mean_squared_error(y_test,y_pred))}")
 print(f"mean absolute: {mean_absolute_error(y_test,y_pred)}")
 print(f"R2: {r2_score(y_test,y_pred)}")

from sklearn.ensemble import RandomForestRegressor
model = RandomForestRegressor()
model.fit(x_train,y_train)
y_pred = model.predict(x_test)
print(f"mean sq error: {mean_squared_error(y_test,y_pred)}")
print(f"root mean sq error: {np.sqrt(mean_squared_error(y_test,y_pred))}")
print(f"mean absolute: {mean_absolute_error(y_test,y_pred)}")
print(f"R2: {r2_score(y_test,y_pred)}")