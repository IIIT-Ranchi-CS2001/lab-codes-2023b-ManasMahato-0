import pandas as pd
import numpy as np


aqi_data=pd.read_csv('AQI_data.csv')

#Display first 8 rows
print("First 8 Rows:\n",aqi_data.head(8))

#Display last 5 rows
print("Last 5 Rows:\n",aqi_data.tail(5))

#Datatype and number of non null values in each column
print("Datatype and Non-Null Values:\n", aqi_data.info())

#mean AQI , max PM 2.5 and min PM 10 values for each city using numpy
aqi_data['AQI'] = pd.to_numeric(aqi_data['AQI'])
aqi_data['PM2.5'] = pd.to_numeric(aqi_data['PM2.5'])
aqi_data['PM10'] = pd.to_numeric(aqi_data['PM10'])

mean_aqi = np.mean(aqi_data['AQI'])
max_pm25 = np.max(aqi_data['PM2.5'])
min_pm10 = np.min(aqi_data['PM10'])

print("Mean AQI: ", mean_aqi)
print("Max PM 2.5: ", max_pm25)
print("Min PM 10: ", min_pm10)