# Volcano-Clustering
This repository explores applying clustering algorithms to create a ring of fire cluster.

Let's start with a what the dataset is. This dataset was obtained from the following kaggle link: https://www.kaggle.com/datasets/ramjasmaurya/volcanoes-on-earth-in-2021.
The two features of interest for this repository are the latitude and longitude coordinates of each volcano on earth (in 2021). The goal is simple: create clusters of these
volcanoes that make sense. 

Before diving into the details of the algorithms, we'll need to know a little bit of geography. Volcanoes form in two main ways: tectonic plate tension and magma plumes. 
Volcanoes created by tectonic plates will be close two where two plates are either moving away or apart from one another. In other words, there will be volcanoes along the
borders of two tectonic plates. On the other hand, volcanoes that form via magma plumes can be created anywhere on the Earth's surface where the crust is sufficiently thin.

Now, let's visualize our data and see how it matches up with what geography predicts. We'll be projecting each of the latitude and longitude pairs onto the unit sphere like
so: 
