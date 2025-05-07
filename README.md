# Volcano-Clustering
This repository explores applying clustering algorithms to create a ring of fire cluster.

Let's start with a what the dataset is. This dataset was obtained from the following kaggle link: https://www.kaggle.com/datasets/ramjasmaurya/volcanoes-on-earth-in-2021.
The two features of interest for this repository are the latitude and longitude coordinates of each volcano on earth (in 2021). The goal is simple: create clusters of these
volcanoes that make sense. 

Before diving into the details of the algorithms, we'll need to know a little bit of geography. Volcanoes form in two main ways: tectonic plate action and magma plumes. 
Volcanoes created by tectonic plates will be close two where two plates are either moving away or apart from one another. In other words, there will be volcanoes along the
borders of two tectonic plates. On the other hand, volcanoes that form via magma plumes can be created anywhere on the Earth's surface where the crust is sufficiently thin.

Now, let's visualize our data and see how it matches up with what geography predicts. We'll be projecting each of the latitude and longitude pairs onto the unit sphere like
so: 

![ExampleSphere](https://github.com/user-attachments/assets/f5ef1658-caec-4d37-bd20-c98f28b2cbf7)

With our volcanoes properly projected onto the sphere, now it's time to cluster some points!

# Clustering with DBSCAN
DBSCAN's premise is simple. Given a dataset of points in space, it will cluster points together in dense regions. All other points not in a dense region will then be 
classified as noise. DBSCAN is well suited for this problem as it can create clusters with unique shapes, supporting lines and curved surfaces. However, first we will
have to define what constitutes as "dense". 

Beginning with DBSCAN's first parameter, we need to determine how many points should be close to a point for it to be considered dense enough. What's typically done is to
set the number of points to be 2 * N, where N is the number of dimensions. Since N=3 for the sphere, we will stick with num_points=6 - though if you'd like to try something
different there is graphing support for that.

Onto DBSCAN's second paramter, we need to determine how close a point has to be to another point for the two to be close together. To do this, we create a graph that shows
how many points can be connected together for a given maximum distance.
