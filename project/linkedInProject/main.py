import math

from AI_settings import ClusteringMatrix
from Graph import Graph
from MyEdge import EdgeClass
from MyUser import UserClass
from Recommender import ClusteringRecommender
import numpy as np


def showMenu():
    print('1.LogIn\n2.SignUp\n3.Show all users\n4.Search')
    inp = input('>> ')
    return inp
def login(username , password):
    try:
        user = UserClass.findInFile(username , password , UserClass._local_users_file_path)
        if user != None:
            #go to login
            return user
        else:
            return None
    except Exception:
        return None

def loginByEmail(email):
    try:
        user = UserClass.searchByEmail(email , '****' , UserClass._main_users_file_path)
        if user != None:
            #go to login
            return user
        else:
            return None
    except Exception:
        return None






def signup(username, password, name, dateOfBirth, universityLocation, field, workplace , email, specialties):
    u = UserClass()
    u.setData1(username, password, name, dateOfBirth, universityLocation, field, workplace , email, specialties , [])
    u.saveFile(UserClass._local_users_file_path)

def loginMenu(user = UserClass):

     order = int (1)
     while order != 0:
        print('Name : ' + user.name)
        print('specialties : ' , end='')
        for sp in user.specialties:
            print(sp , end=', ')
        print('\nRecommended users 1 \nconnect to another person 2\nback 0 ')

        order = input('>> ')

        if int(order) == 0 :
            return
        elif int(order) == 1:
            userInGraph = Graph.findUserById(user.id)
            BFSTraverse = Graph.BFS(userInGraph)
            matrix = ClusteringMatrix(len(BFSTraverse))
            matrix.setScore(userInGraph, BFSTraverse)

            recommender = ClusteringRecommender(matrix , BFSTraverse)
            recommender.setKMeans()
            recommender.showPlt()


            tmp = list()
            tmp.append([2, sum(range(len(user.specialties) , 1 , -1))  , 1 ,1 , 1])
            recommendedList = recommender.recommend(tmp)

            i = int(1)
            for item in recommendedList:
                if isinstance(item , UserClass) :
                    print(str(i) + '. ######################################################################')
                    item.toString()
                    i += 1

        elif int(order) == 2:
            Graph.getInstance().follow(user)











#################################
Graph.setGraph()
G = Graph.getInstance()
G.make_edges()



print('Welcome to Unlinked Out')
inp = showMenu()

while True:
    if inp == '1':
        username = input('Enter Username >> ')
        password = input('Enter Password >> ')
        user = login(username , password)
        user2 = loginByEmail(username)
        if user is not None:
            loginMenu(user)
        elif user2 is not None:
            loginMenu(user2)

    elif inp == '2':
        name = input('Name >> ')
        email = input('email >> ')
        dateOfBirth = input('Date of birth >> ')
        universityLocation = input('University location >> ')
        field = input('Field >> ')
        workplace = input('Work place >> ')
        specialties = list(input('Specialties >> ').split())
        username = input('username >> ')
        password = input('password >> ')
        signup(username, password, name, dateOfBirth, universityLocation, field, workplace , email, specialties)
    elif inp == '3':
        g = Graph.getInstance()
        i = int(1)
        for user in g.vertices:
            if isinstance(user, UserClass):
                print(str(i) + '. ######################################################################')
                user.toString()
                i += 1
    elif inp == '4':
        name = input('Enter the name >> ')
        users = Graph.findByName(name)
        if users is None:
            print('The user ' + name + ' not found')
        else:
            i = 1
            for user in users:
                if isinstance(user, UserClass):
                    print(str(i) + '. ######################################################################')
                    user.toString()
                    i += 1
    #elif inp == '5':



    print('\n*******************************************')

    inp = showMenu()