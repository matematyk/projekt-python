import pandas as pd
from mwprojekt.velocity import velocity_on_geoid

def compute_velocity(dataframe1, dataframe2):
    df = pd.merge(dataframe1, dataframe2, left_on='VehicleNumber', right_on='VehicleNumber', how='left').drop('VehicleNumber', axis=1)

    df['kph'] = df.apply(lambda x: velocity_on_geoid(x['Lat_x'], x['Lon_x'], x['Lat_y'], x['Lon_y'], x['Time_x'], x['Time_y']), axis=1)

    return df
 


