import pandas as pd 
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from mwprojekt.velocity_analytics import compute_velocity

int_1 = pd.read_json('/home/mw/Matematyka/projekt-python/data/test_0.json')
int_1 = pd.json_normalize(int_1['result'])
int_2 = pd.read_json('/home/mw/Matematyka/projekt-python/data/test_1.json')
int_2 = pd.json_normalize(int_2['result'])

df = compute_velocity(int_1, int_2)
df = df.dropna()


  
df = pd.DataFrame(df,columns=['Lat_x','Lon_y'])

kmeans = KMeans(n_clusters=6).fit(df)
centroids = kmeans.cluster_centers_
print(centroids)
plt.scatter(df['Lat_x'], df['Lon_y'], c= kmeans.labels_.astype(float), s=50, alpha=0.5)
plt.scatter(centroids[:, 0], centroids[:, 1], c='red', s=50)
plt.show()