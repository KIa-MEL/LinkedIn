from Tree import Tree
from MyUser import UserClass

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

        BFS_tree = dict()
        level = list()

        list(known).append(startingPoint)
        level.append(startingPoint)

        five_rows = 5
        while len(level) != 0 :

            if five_rows == 0 :
                break

            next_level = list()
            for user in level:

                for linked in dict(user.LinkedPeople).keys():

                    if list(known).index(user) == -1 :
                        list(known).append(user)
                        BFS_tree[linked] = five_rows
                        next_level.append(linked)


            level = next_level
            five_rows -= 1

        return BFS_tree

    def setGraph(self):
        users = UserClass.getUsers(UserClass._main_users_file_path)
        # users.append(UserClass.getLocalUsers(UserClass._local_users_file_path))
        # for user in users:
        #     print(user.name)
        self.vertices = users


    @staticmethod
    def make_edges():

        for user in Graph(Graph.unlinkedInGraph).vertices:
            break
