import pandas

df = pandas.read_json('../data/mock.json')

print(df['result'])