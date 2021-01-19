import pandas
import configparser 


config = configparser.ConfigParser()
config.read('config.ini')
df = pandas.read_json('https://api.um.warszawa.pl/api/action/busestrams_get/?resource_id=f2e5503e-927d-4ad3-9500-4ab9e55deb59&apikey=9c9a80e9-68d1-4f74-8d49-c241f3f5649f&type=2')

df.to_json('19.02.2021-3.json')