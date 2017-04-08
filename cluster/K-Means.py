from sklearn import cluster
file = open("zoo.txt")
points = []
labels = []
for line in file:
    data = line.strip().split(',')
    point = (int(data[1]), int(data[2]), int(data[3]), int(data[4]), int(data[5]), int(data[6]), int(data[7]), int(data[8]), int(
        data[9]), int(data[10]), int(data[11]), int(data[12]), int(data[13]), int(data[14]), int(data[15]), int(data[16]))
    label = data[0]
    points.append(point)
    labels.append(label)
    
    k_inertia = 99999
for n_class in range(2,11):
    k_means = cluster.KMeans(init='random', n_clusters=n_class, max_iter=10, n_init=10).fit(points)
    # print("when k is", n_class, "the correspoing SSE is", k_means.inertia_,
    #       "the improvement of new cluster is ", k_inertia-k_means.inertia_)
    k_inertia = k_means.inertia_

    for i in range(n_class):
        print("cluseter"+str(i)+":")
        # print("hair","feathers","eggs","milk","airborne","aquatic","predator","toothed","backbone","breathes","venomous","fins","legs","tail","domestic","catsize")
        for node in range(len(points)):
            if k_means.labels_[node] == i:
                for j in range(16):
                    print(points[node][j],end=' ')
                print("\t")
        print("\n")




