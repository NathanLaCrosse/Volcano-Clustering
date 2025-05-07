import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import plotting as f

from sklearn.neighbors import NearestNeighbors

df = pd.read_csv("volcanoes.csv")
X = df[["Longitude", "Latitude"]].copy().to_numpy()

points = f.gen_sphere_projection(X)

n = None
while n is None or n < 1:
    print("Enter amount of neighbors to consider (must be positive, nonzero): ")

    try:
        n = int(input())
    except ValueError:
        print("Please enter in a valid number.")

# Fit nearest neighbors to find distances to neighbors
nearest = NearestNeighbors(n_neighbors=n).fit(points)
distances, _ = nearest.kneighbors(points, return_distance=True)

# Sort the distances for graphing
distances = np.sort(distances[:, -1])

# Plot the distance graph
plt.plot(distances)
plt.savefig("Images/DistanceGraphDBSCAN.png")
plt.show()
