import pandas as pd


int_1 = pd.read_json('/home/mw/Matematyka/projekt-python/data/test_0.json')
int_1 = pd.json_normalize(int_1['result'])
print(int_1)
int_2 = pd.read_json('/home/mw/Matematyka/projekt-python/data/test_1.json')
int_2 = pd.json_normalize(int_2['result'])

y = pd.merge(int_1, int_2, left_on='VehicleNumber', right_on='VehicleNumber', how='left').drop('VehicleNumber', axis=1)
