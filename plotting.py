import numpy as np

"""Generate the projections of latitude and longitude pairs onto the unit sphere

Params:
    - lon_lat_pairs - longitude and latitude pairs

Returns:
    - points - the corresponding points on the sphere
"""
def gen_sphere_projection(lon_lat_pairs):
    # Convert to radians
    lon_lat_pairs = lon_lat_pairs * np.pi / 180
    lon_lat_pairs[:,0] += np.pi
    lon_lat_pairs[:,1] -= np.pi / 2

    points = np.zeros((lon_lat_pairs.shape[0], 3))

    # X - coordinate
    points[:, 0] = np.cos(lon_lat_pairs[:, 0]) * np.sin(lon_lat_pairs[:, 1])
    # Y - coordinate
    points[:, 1] = np.sin(lon_lat_pairs[:, 0]) * np.sin(lon_lat_pairs[:, 1])
    # Z - coordinate
    points[:, 2] = np.cos(lon_lat_pairs[:, 1])

    return points

"""Plot a globe on the provided axis object."""
def globe(ax):
    # Longitude 0 - 2pi
    longitudes = np.linspace(0, 2 * np.pi, 18)
    # Latitude 0 - pi
    latitudes = np.linspace(0, np.pi, 18)

    x = 0.9 * np.outer(np.cos(longitudes), np.sin(latitudes))
    y = 0.9 * np.outer(np.sin(longitudes), np.sin(latitudes))
    z = 0.9 * np.outer(np.ones(np.size(longitudes)), np.cos(latitudes))

    ax.plot_surface(x, y, z, color='w', linewidths=0.5)

"""Plot the clusters determined by a clustering algorithm as a scatterplot,
 with randomized color given to each cluster.
 
 Params:
    - points: The list of points the clstr object was fitted to, a (-1, 3) numpy array of 3-D points.
    - clstr: The clustering object
    - ax: An axis object to plot the scatterplot to

 Returns:
    - None
 """
def plot_clusters(points, clstr, ax):
    num_clusters = max(clstr.labels_) + 1

    for i in range(num_clusters):
        clstr_points = points[clstr.labels_ == i]

        ax.scatter(clstr_points[:, 0], clstr_points[:, 1], clstr_points[:, 2],
                   depthshade=True, edgecolors="black", linewidths=1,
                   label=f"Cluster {i + 1}, QTY: {clstr_points.shape[0]}", s=20,
                   color=np.random.rand(3))

"""Plots the noise of a DBSCAN object as a scatterplot to the provided axis object.

 Params:
    - points: The list of points dbscan was fitted to, a (-1, 3) numpy array of 3-D points.
    - dbscan: The DBSCAN object
    - ax: An axis object to plot the scatterplot to
"""
def plot_noise(points, dbscan, ax):
    clstr_points = points[dbscan.labels_ == -1]
    ax.scatter(clstr_points[:, 0], clstr_points[:, 1], clstr_points[:, 2],
               c='r', depthshade=True, edgecolors="black", linewidths=0.5,
               label=f"Noise, QTY: {clstr_points.shape[0]}", s=20)