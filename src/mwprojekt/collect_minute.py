import time
import argparse
import pandas

def script(resource_id, api_key, save, date):
    for minute in range(5):
        date_temp = date + "-" + str(minute) + ".json"
        df = pandas.read_json('https://api.um.warszawa.pl/api/action/busestrams_get/?resource_id=f2e5503e-927d-4ad3-9500-4ab9e55deb59&apikey=9c9a80e9-68d1-4f74-8d49-c241f3f5649f&type=2')
        df.to_json(date_temp)
        time.sleep(60)
    return "Done"

if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("-ri", "--resource_id", type=str, default='f2e5503e-927d-4ad3-9500-4ab9e55deb59', help="Resource ID")
    ap.add_argument("-ak", "--api_key", type=str, default='9c9a80e9-68d1-4f74-8d49-c241f3f5649f', help="Api Key")
    ap.add_argument("-sf", "--save", type=bool, default=True, help="save to file")
    ap.add_argument("-dt", "--date", type=str, default='03.02.2021', help="date to save")

    args = vars(ap.parse_args())
    ri =  args['resource_id']
    ak = args['api_key']
    sf = args['save']
    date = args['date']
    
    script(ri, ak, sf, date)
    