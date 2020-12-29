import pandas
import configparser 


config = configparser.ConfigParser()
config.read('config.ini')
df = pandas.read_json(config['DEFAULT']['api_src'])

df.to_json('test_10.json')