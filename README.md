# Volcano-Clustering
This repository explores applying clustering algorithms to a problem of clustering volcanoes.

Let's start with a what the dataset is. This dataset was obtained from the following kaggle link: https://www.kaggle.com/datasets/ramjasmaurya/volcanoes-on-earth-in-2021.
The two features of interest for this repository are the latitude and longitude coordinates of each volcano on earth (in 2021). The goal is simple: create clusters of these
volcanoes that make sense. 

Before diving into the details of the algorithms, we'll need to know a little bit of geography. Volcanoes form in two main ways: tectonic plate action and magma plumes. 
Volcanoes created by tectonic plates will be close two where two plates are either moving away or apart from one another. In other words, there will be volcanoes along the
borders of two tectonic plates. On the other hand, volcanoes that form via magma plumes can be created anywhere on the Earth's surface where the crust is sufficiently thin.

Now, let's visualize our data and see how it matches up with what geography predicts. We'll be projecting each of the latitude and longitude pairs onto the unit sphere like
so: 

![ExampleSphere](https://github.com/user-attachments/assets/4bb60fee-79f6-489b-a415-a7f586db601f)

With our volcanoes properly projected onto the sphere, now it's time to cluster some points!

# Clustering with DBSCAN
DBSCAN's premise is simple. Given a dataset of points in space, it will cluster points together in dense regions. All other points not in a dense region will then be 
classified as noise. DBSCAN is well suited for this problem as it can create clusters with unique shapes, supporting lines and curved surfaces. However, first we will
have to define what constitutes as "dense". 

Beginning with DBSCAN's first parameter, we need to determine how many points should be close to a point for it to be considered dense enough. What's typically done is to
set the number of points to be 2 * N, where N is the number of dimensions. Since N=3 for the sphere, we will stick with num_points=6 - though if you'd like to try something
different there is graphing support for that.

Onto DBSCAN's second paramter, we need to determine how close a point has to be to another point for the two to be close together. To do this, we create a graph that shows
how many points can be connected together for a given maximum distance. We are looking for the "elbow" in this graph, right before a jump where suddenly a majority of 
points will be classified as "dense". We want to have defined clusters but also don't want to cluster everything - we expect some noise, mainly due to magma plume 
volcanoes. Let's look at the graph:

![DistanceGraphDBSCAN](https://github.com/user-attachments/assets/35651529-2f3b-4af5-a672-8fea8c56a216)

Given this graph, I chose a maximum distance of epsilon=0.11 to determine density.

Now to the results - does this model produce a result that makes sense? Here are two screenshots from the resulting 3D plot:

The Ring of Fire:

![RingOfFire](https://github.com/user-attachments/assets/1b11a4c4-87c5-44e5-8245-5b63c8dd3ded)

The Horn of Africa:

![AfricaDBSCAN](https://github.com/user-attachments/assets/a28a35b7-be61-4ada-a704-3b95fbc9c4e2)


Overall, DBSCAN performs a good job in identifying volcano chains that have been produced by tectonic plates. I investigated modifying DBSCAN to cluster the entire region 
of the ring of fire into a single cluster, but there are a few significant gaps that would result in needing an epsilon far too large to create meaningful clusters. 

Another interesting property of DBSCAN's clusters is that a lot of magma plume volcanoes end up getting clustered as noise which naturally seperates them out from the other 
volcanoes produced by tectonic plates.

Now, let's see how DBSCAN compares to another popular clustering algorithm, KMeans.

# Clustering with KMeans
KMeans works quite differently than DBSCAN. With KMeans, you assume a certain amount of clusters exist and place each datapoint in a cluster based off of nearest centroid. 
These centroids are found through the use of Lloyd's algorithm, which minimizes a property of the clusters called "inertia". 

To get the best results, we first need to figure out how many clusters there should be. While a more geography-based argument could be used to determine the amount of
clusters, we'll instead be looking for another elbow in a graph. We'll run KMeans with different amounts of clusters and look at the amount of inertia they have. By 
definition inertia will descrease as we increase the amount of clusters, so we're looking for where the rate of change of inertia changes. Here are the results:

![Inertia Graph](https://github.com/user-attachments/assets/e6ed16d3-d377-4e80-93cd-b5d2208bee1b)

Based off of this graph, I chose n_clusters=6 as this was one of the points in the elbow region. Now we can observe how this model clusters the volcanoes:

![KmeansResult](https://github.com/user-attachments/assets/3c2aca70-6abb-47c5-a345-ee7e77f6ed58)

While the results are hard to convey in a single photo, (I recommend running the code yourself!) this model is assigning clusters much more arbitrarily than DBSCAN did. 
What made DBSCAN successful in identifying volcano chains was the fact that it was based around finding high volcano density. KMean's approach of clustering instead is just
creating general regions where a certain amount of volcanoes lie. This approach misses the complexity present in structures like the Ring of Fire, which DBSCAN approximated 
much better. Furthermore, KMeans is essentially fitting everything into circles with linear borders - whereas DBSCAN is flexible and can work with any shape, tectonic plate 
lines included.

All in all, in a quest to cluster volcanoes, DBSCAN produces a much more coherent result than KMeans that appeals directly to the tectonic plate lines that create a 
majority of volcanoes.
