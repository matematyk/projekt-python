import pandas as pd
from velocity import velocity_on_geoid

int_1 = pd.read_json('/home/mw/Matematyka/projekt-python/data/test_0.json')
int_1 = pd.json_normalize(int_1['result'])
int_2 = pd.read_json('/home/mw/Matematyka/projekt-python/data/test_1.json')
int_2 = pd.json_normalize(int_2['result'])

def compute_velocity(dataframe1, dataframe2):
    df = pd.merge(dataframe1, dataframe2, left_on='VehicleNumber', right_on='VehicleNumber', how='left').drop('VehicleNumber', axis=1)

    df['kph'] = df.apply(lambda x: velocity_on_geoid(x['Lat_x'], x['Lon_x'], x['Lat_y'], x['Lon_y'], x['Time_x'], x['Time_y']), axis=1)

    return df
 

def find_50_kph(dataframe):
    for index, row in dataframe.iterrows():
        if  row > 50:
            print(row)
