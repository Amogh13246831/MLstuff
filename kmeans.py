import random

class DataItem:

    def __init__(self, val):

        self.value = val
        self.cluster = -1

    def __repr__(self):

        # return 'Value: ' + str(self.value)  + ', Cluster: ' + str(self.cluster)
        return str(self.value)


dataList = [DataItem(random.randint(1, 50)) for i in range(10)]

clusters = 3 # int(input("Enter the number of clusters: "))

means = [dataList[random.randint(0, len(dataList)-1)].value for i in range(clusters)]


def getcluster():

    for i in range(len(dataList)):
        dist = [abs(dataList[i].value - means[j]) for j in range(len(means))]
        dataList[i].cluster = dist.index(min(dist))


def getmeans():

    for i in range(len(means)):
        vals = [j.value for j in dataList if j.cluster == i]
        if len(vals) > 0:
            means[i] = sum(vals) / len(vals)
        else:
            diff = [abs(j.value - means[i]) for j in dataList]
            means[i] = dataList[diff.index(min(diff))].value


def kmeans():

    while True:
        prevmeans = [i for i in means]
        getcluster()
        getmeans()
        completed = [prevmeans[i] == means[i] for i in range(len(means))]
        if all(completed):
            return [[item for item in dataList if item.cluster == i] for i in range(len(means))]


print("\nData is: ", dataList)
print("Number of clusters: ", clusters)
print("Cluster means: ", means, "\n")
print("\nClusters after k-means: ", kmeans())
print("Cluster means: ", means)

