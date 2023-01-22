import numpy as np
from matplotlib import pyplot as plt
from MyUser import UserClass
from sklearn.cluster import KMeans


class ClusteringMatrix:
    matrix = np.array
    kmeans = KMeans
    # [level , specialtiesScore , fieldScore , uniScore , workScore ]

    def __init__(self , row):
        a_shape = (row, 5)
        self.matrix = np.zeros(a_shape)


    def setScore(self , startingPoint = UserClass , bfsTree = dict):

        specialtiesScore = int(0)
        fieldScore = int(0)
        uniScore = int(0)
        workScore = int(0)

        i = int(0)
        for user in list(bfsTree.keys()) :
            specialtiesWeight = len(startingPoint.specialties)
            if isinstance(user , UserClass):

                if bfsTree[user] == 1:
                    continue


                # specialties :
                try:
                    for ss in startingPoint.specialties: # startingPoint specialties
                        for us in user.specialties:
                            if ss == us: # if had common specialties
                                specialtiesScore += specialtiesWeight # to set priority
                                specialtiesWeight -= 1
                except Exception:
                    specialtiesScore = 0
                # field :
                try:
                    if user.field == startingPoint.field :
                        fieldScore += 1
                except Exception:
                    fieldScore = 0
                # uni :
                try:
                    if user.universityLocation == startingPoint.universityLocation:
                        uniScore += 1
                except Exception:
                    uniScore = 0
                # work :
                try:
                    if user.workplace == startingPoint.workplace:
                        workScore += 1
                except Exception:
                    workScore = 0


            self.matrix[i] = [bfsTree[user] , specialtiesScore , fieldScore , uniScore , workScore ]
            i+=1
        self.setKMeans()




    def setKMeans(self):
        x = np.array(self.matrix)
        self.kmeans = KMeans(n_clusters=6, random_state=0, n_init="auto").fit(x)
    def showPlt(self):
        plt.scatter(self.matrix[:,1] + self.matrix[:,2] + self.matrix[:,0] , self.matrix[:,3] + self.matrix[:,4] + self.matrix[:,4] , c = self.kmeans.labels_)
        plt.show()