from Tree import Tree
from MyUser import UserClass
from MyEdge import EdgeClass
class Graph :

    #singleTon graph
    _instance = None
    edges = list()
    vertices = list()

    def __init__(self):
        # self.edges = list()
        # self.vertices = list()
        #
        # if Graph._instance is None :
        #     Graph._instance = self
        raise RuntimeError('Call instance() instead')


    @classmethod
    def getInstance(cls):
        if cls._instance is None:
            #Creating new instance
            cls._instance = cls.__new__(cls)
            # Put any initialization here.
        return cls._instance




    @staticmethod
    def findUserById(id):

        for user in Graph.getInstance().vertices :
            if user.id == id:
                return user


        return None

    @staticmethod
    def findByName(name):

        users = list()

        for user in Graph._instance.vertices :
            if isinstance(user , UserClass):
                if str(user.name).__contains__(name):
                    users.append(user)

        if len(users) == 0:
            return None

        return users

    @staticmethod
    def BFS (startingPoint = UserClass):
        known = list()
        BFS_tree = dict()
        level = list()

        known.append(startingPoint)
        level.append(startingPoint)

        five_rows = 1
        while len(level) != 0 :

            if five_rows == 7 :
                break

            next_level = list()
            for user in level:
                for linked in list(user.LinkedPeople.keys()):
                    if not known.__contains__(linked) :
                        known.append(linked)
                        if five_rows != 1:
                            BFS_tree[linked] = five_rows
                        next_level.append(linked)


            level = next_level
            five_rows += 1

        return BFS_tree
    @staticmethod
    def setGraph():
        users = UserClass.getUsers(UserClass._main_users_file_path)
        users += UserClass.getLocalUsers(UserClass._local_users_file_path)

        Graph.getInstance().vertices = users



    def make_edges(self):

        for user in self.vertices:

            for opposite_useres in user.connectionId:

                opposite_user = Graph.getInstance().findUserById(opposite_useres)

                try:
                    self.add_each_edge(user , opposite_user)
                except Exception : {}
    def getEdge(self , v = UserClass , u = UserClass):
        try:
            if v.LinkedPeople.keys().__contains__(u):
                return v.LinkedPeople[u]
        except Exception:
            return None

    def add_each_edge(self , user = UserClass , opposite_user = UserClass):

        if self.getEdge(user , opposite_user) is None:
            edge = EdgeClass(user, opposite_user)

            # adding connected people
            opposite_user.addLink(user , edge)
            user.addLink(opposite_user , edge)


            # adding the new edge
            self.edges.append(edge)

        else:
            raise Exception('you are already connected to this user')


    def follow(self , user):

        name = input('Enter the user id you want to connect to >> ')
        opposite_user = Graph.getInstance().findUserById(name)

        if opposite_user is None :
            raise Exception('there is no person with this id ')

        if isinstance(opposite_user , UserClass) :
            if not list(opposite_user.LinkedPeople.keys()).__contains__(user):

                edge = EdgeClass(user , opposite_user)

                #adding connected people
                opposite_user.LinkedPeople[user] = edge
                user.LinkedPeople[opposite_user] = edge

                #adding the new edge
                Graph.getInstance().edges.append(edge)
                print('added successfully !')

            else:
                print('you are already connected to this person')
