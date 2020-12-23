from distance import distance_on_geoid



def velocity_on_geoid(lat1, lon1, lat2, lon2, date1, date2):

    from datetime import datetime

    elapsed_time = 0

    start_time = datetime.strptime(date1, '%Y-%m-%d %H:%M:%S')
    end_time = datetime.strptime(date2, '%Y-%m-%d %H:%M:%S')

    diff = end_time - start_time
    elapsed_time = diff.seconds
    dist = distance_on_geoid(lat1, lon1, lat2, lon2)
    print(dist)
    speed_mps = dist / elapsed_time
    speed_kph = (speed_mps * 3600.0) / 1000.0
    return speed_kph

