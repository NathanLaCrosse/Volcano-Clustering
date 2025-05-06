import numpy as np
import pandas as pd
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import plotting as p

df = pd.read_csv("volcanoes.csv")
X = df[["Longitude", "Latitude"]].copy().to_numpy()

fig = plt.figure()
points = p.gen_sphere_projection(X)

# For each amount of clusters, display the inertia of the clustering
# By definition, inertia will always decrease, so we're looking for where that rate of change
# is slowing down, which is around n_clusters=9
inertia = np.zeros(20)
for i in range(1,21):
    kmeans = KMeans(n_clusters=i)
    kmeans.fit(points)

    inertia[i-1] = kmeans.inertia_

plt.plot(range(1,21), inertia)
plt.show()

ax = fig.add_subplot(projection='3d')

# 9 was chosen as it was chosen as the elbow in the elbow graph
kmeans = KMeans(n_clusters=9)
kmeans.fit(points)

# Plot the kmeans results
p.plot_clusters(points, kmeans, ax)
ax.set_aspect('equal')
plt.legend(prop={'size' : 5}, bbox_to_anchor=(0, 1))
plt.show()
