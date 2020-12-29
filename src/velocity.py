from distance import distance_on_geoid
from datetime import datetime


def velocity_on_geoid(lat1, lon1, lat2, lon2, date1, date2):

    

    elapsed_time = 0

    try:
        start_time = datetime.strptime(date1, '%Y-%m-%d %H:%M:%S')
        end_time = datetime.strptime(date2, '%Y-%m-%d %H:%M:%S')
        diff = end_time - start_time
        elapsed_time = diff.seconds
    except:
        return 0

    dist = distance_on_geoid(lat1, lon1, lat2, lon2)
    try:
        speed_mps = dist / elapsed_time
    except ZeroDivisionError:
        speed_mps = 0

    
    speed_kph = (speed_mps * 3600.0) / 1000.0
    
    return speed_kph