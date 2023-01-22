from matplotlib import pyplot as plt
from sklearn.cluster import KMeans
import numpy as np

from AI_settings import ClusteringMatrix


class ClusteringRecommender:

    kmeans = KMeans
    matrix = np.array
    bfs_tree = dict

    def __init__(self, matrix = ClusteringMatrix , bfs_tree = dict):
        self.matrix = matrix.matrix
        self.bfs_tree = bfs_tree
        self.setKMeans()



    def setKMeans(self):
        x = np.array(self.matrix)
        self.kmeans = KMeans(n_clusters=6, random_state=0, n_init="auto").fit(x)
    def showPlt(self ):
        plt.scatter(self.matrix[:,1] + self.matrix[:,2] + self.matrix[:,0] , self.matrix[:,3] + self.matrix[:,4] + self.matrix[:,4] , c = self.kmeans.labels_)
        plt.show()


    def recommend(self , predictionPoint = np.array):
        print(self.kmeans.labels_)
        cluster_number = self.kmeans.predict(predictionPoint)

        all_clusters = self.kmeans.labels_


        recommendeing_users = list()

        counter = int (0)
        user_keys = list(self.bfs_tree.keys())
        for user_cluster in list(all_clusters):

            if len(recommendeing_users) == 20:
                return recommendeing_users

            if user_cluster == cluster_number[0] :
                recommendeing_users.append(user_keys[counter])


            counter+=1

        return recommendeing_users

