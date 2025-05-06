import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import plotting as p

from sklearn.cluster import DBSCAN

df = pd.read_csv("volcanoes.csv")
X = df[["Longitude", "Latitude"]].copy().to_numpy()

fig = plt.figure()
points = p.gen_sphere_projection(X)

# Use DBSCAN to find clusters
# For epsilon - eyeballed it in DistanceGraph.py -> using n=4

# Good results with 0.12
# Getting the "full" ring of fire seems infeasible - distances between
# connected components too far apart, leads to clustering beyond ring of fire line
clstr = DBSCAN(p=6, eps=0.11)
clstr.fit(points)

# rReset plot and add a globe to it
fig.clear()
ax = fig.add_subplot(projection='3d')

# Plot each individual cluster (ignoring noise)
p.plot_clusters(points, clstr, ax)

# Plot the noise separately
p.plot_noise(points, clstr, ax)

ax.set_aspect('equal')
plt.legend(prop={'size' : 5}, bbox_to_anchor=(0, 1))
plt.show()


