import numpy as np

from MyUser import UserClass


class ClusteringMatrix:
    matrix = np.array
    def __init__(self , row):
        a_shape = (row, 5)
        matrix = np.zeros(a_shape)

    def setScore(self , startingPoint = UserClass , bfsTree = dict):

        specialtiesScore = int(0)
        fieldScore = int(0)
        uniScore = int(0)
        workScore = int(0)

        for user in list(bfsTree.keys()) :
            specialtiesWeight = len(startingPoint.specialties)
            if isinstance(user , UserClass):
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
