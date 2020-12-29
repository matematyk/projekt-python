import pandas as pd
from velocity import velocity_on_geoid

int_1 = pd.read_json('/home/mw/Matematyka/projekt-python/data/test_0.json')
int_1 = pd.json_normalize(int_1['result'])
int_2 = pd.read_json('/home/mw/Matematyka/projekt-python/data/test_1.json')
int_2 = pd.json_normalize(int_2['result'])

df = pd.merge(int_1, int_2, left_on='VehicleNumber', right_on='VehicleNumber', how='left').drop('VehicleNumber', axis=1)
for index, row in df.iterrows():
    kph = velocity_on_geoid(row['Lat_x'], row['Lon_x'], row['Lat_y'], row['Lon_y'], row['Time_x'], row['Time_y'])
    if  kph > 50:
        print(kph)
