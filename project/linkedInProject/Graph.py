from Tree import Tree
from User import User


class Graph :

    #singleTon graph
    unlinkedInGraph = None


    def __init__(self):
        self.edges = list()
        self.vertices = list()

        if Graph.unlinkedInGraph is None :
            Graph.unlinkedInGraph = self

    @staticmethod
    def findUserId(username):

        for user in Graph(Graph.unlinkedInGraph).vertices :
            if user.username == username:
                return user


        return None

    @staticmethod
    def findByName(name):

        users = list()

        for user in Graph(Graph.unlinkedInGraph).vertices :
            if user.name == name :
                users.append(user)

        if len(users) == 0:
            return None

        return users

    @staticmethod
    def BFS (startingPoint , known):

        BFS_tree = Tree()
        level = list()

        list(known).append(startingPoint)
        level.append(startingPoint)

        while len(level) != 0 :

            next_level = list()
            for user in next_level:








