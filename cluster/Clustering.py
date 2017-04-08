import numpy as np
from sklearn import cluster

points = []  # stores features of the animals
labels = []  # stores the animal names

file = open('zoo.txt')
for line in file:
  # example line: aardvark,1,0,0,1,0,0,1,1,1,1,0,0,4,0,0,1
  data = line.strip().split(',')
  point = (int(data[1]), int(data[2]),int(data[3]),int(data[4]),int(data[5]),int(data[6]),int(data[7]),int(data[8]),int(data[9]),int(data[10]),int(data[11]), int(data[12]),int(data[13]),int(data[14]),int(data[15]),int(data[16]))
  name = data[0]

  points.append(point)
  labels.append(name)

# convert points list to a (number_of_points, 16) numpy array
points = np.asarray(points)
n_class = 4 # the number of culsters to be identified


# run K-Means five times with random initialization of centroids,
# and output best results
k_means = cluster.KMeans(init='random', n_clusters=n_class, max_iter=10, n_init=5)
k_means.fit(points)

for i in range(0,n_class):
    print ("class",i,": ",)
    for j in range(0,100):
        if k_means.labels_[j]==i:
            print (labels[j],end = " ")
    print ("\n")
