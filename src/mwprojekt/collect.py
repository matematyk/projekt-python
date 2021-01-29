import pandas
import requests

def get_courses(resource_id, api_key):
    req = requests.get(
        f"https://api.um.warszawa.pl/api/action/busestrams_get/?resource_id={resource_id}&apikey={api_key}&type=2"
    )
    data = req.json()

    return data


def collect_from_api(resource_id, api_key, save, date):
    data = get_courses(resource_id, api_key)
    df = pandas.DataFrame(pandas.json_normalize(data['result']))

    if save==True:
        df.to_json('{0}.json'.format(date))

    return df

