from mwprojekt.velocity_analytics import compute_velocity
import pandas as pd

def traffic_computation(date):
    traffics = []
    for i in range(0,4):
        datajson1 = '../../data/'+date+"-{0}.json".format(i)
        datajson2 = '../../data/'+date+"-{0}.json".format(i+1)
        int_1 = pd.read_json(datajson1)
        int_1 = pd.json_normalize(int_1['result'])
        int_2 = pd.read_json(datajson2)
        int_2 = pd.json_normalize(int_2['result'])
        df = compute_velocity(int_1, int_2)
        df = df.dropna()
        df = pd.DataFrame(df,columns=['Lat_y', 'Lon_y', 'kph'])
        traffics.append(df)

    return traffics

print([x.head() for x in traffic_computation('03.02.2021')])