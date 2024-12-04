import pandas as pd
import numpy as np


aqi_data=pd.read_csv('AQI_data.csv')

#Group the dataset by city 
grouped = aqi_data.groupby('City')

#Avg aqi for each city
avg_AQI=grouped['AQI'].mean()

#Max PM2.5 value for each city
max_PM2_5=grouped['PM2.5'].max()

#Min PM10 value for each city
min_PM10=grouped['PM10'].max()

#Display all three statistical information with each city

for city, aqi, pm2_5, pm10 in zip(avg_AQI.index, avg_AQI.values, max_PM2_5.values, min_PM10.values):
    print(f"City: {city}, Average AQI: {aqi}, Max PM2.5: {pm2_5}, Min PM10: {pm10}")