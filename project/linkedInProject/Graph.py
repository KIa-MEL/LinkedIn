from Tree import Tree
from MyUser import UserClass
from MyEdge import EdgeClass
class Graph :

    #singleTon graph
    unlinkedOutGraph = None


    def __init__(self):
        self.edges = list()
        self.vertices = list()

        if Graph.unlinkedOutGraph is None :
            Graph.unlinkedOutGraph = self

    @staticmethod
    def findUserId(username):

        for user in Graph(Graph.unlinkedOutGraph).vertices :
            if user.username == username:
                return user


        return None

    @staticmethod
    def findByName(name):

        users = list()

        for user in Graph(Graph.unlinkedOutGraph).vertices :
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

                    if list(known).__contains__(user)  :
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

        for user in Graph(Graph.unlinkedOutGraph).vertices:

            user = UserClass(user)

            for opposite_useres in UserClass(user).connectionId:

                opposite_user = Graph(Graph.unlinkedOutGraph).findUserId(opposite_useres)
                opposite_user = UserClass(opposite_user)

                try:
                    Graph.add_each_edge(user , opposite_user)
                except Exception : print('')


    @staticmethod
    def add_each_edge(user , opposite_user):

        if list(opposite_user.LinkedPeople.keys()).__contains__(user):
            edge = EdgeClass(user, opposite_user)

            # adding connected people
            opposite_user.LinkedPeople[user] = edge
            user.LinkedPeople[opposite_user] = edge

            # adding the new edge
            Graph(Graph.unlinkedOutGraph).edges.append(edge)

        else:
            raise Exception('you are already connected to this user')

