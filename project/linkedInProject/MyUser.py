import json
import os.path
from collections import namedtuple
import demjson3

from types import SimpleNamespace as Namespace


class UserClass :
    _main_users_file_path = '../Files/users1.json'
    _local_users_file_path = '../Files/users.json'
    id = str
    username = str
    password = str
    name = str
    dateOfBirth = str
    universityLocation = str
    field = str
    workplace = str
    specialties = str
    connectionId = list
    email = str
    LinkedPeople = dict()


    # def __init__(self , username, password, name, dateOfBirth, universityLocation, field, workplace, specialties):
    #     self.username = username
    #     self.password = password
    #     self.name = name
    #     self.dateOfBirth = dateOfBirth
    #     self.universityLocation = universityLocation
    #     self.field = field
    #     self.workplace = workplace
    #     self.specialties = specialties

    def setData1(self , username, password, name, dateOfBirth, universityLocation, field, workplace , email, specialties):
        self.username = username
        self.password = password
        self.name = name
        self.dateOfBirth = dateOfBirth
        self.universityLocation = universityLocation
        self.field = field
        self.workplace = workplace
        self.email = email
        self.specialties = specialties
    def setData(self , name, dateOfBirth, universityLocation, field, workplace , email, specialties , connectionId):
        self.name = name
        self.dateOfBirth = dateOfBirth
        self.universityLocation = universityLocation
        self.field = field
        self.workplace = workplace
        self.email = email
        self.specialties = specialties
        self.connectionId = connectionId

    def getUsers(path): # static function
        f = open(path)
        data = json.load(f)
        users = list()

        for item in data:
            u = UserClass()
            u.setData(item['name'] , item['dateOfBirth'] , item['universityLocation'] , item['field'] , item['workplace'] , item['email'] , item['specialties'] , item['connectionId'])
            users.append(u)
        return users
    def toUser(item):
        u = UserClass()
        u.setData(item['name'], item['dateOfBirth'], item['universityLocation'], item['field'], item['workplace'],item['email'], item['specialties'], item['connectionId'])
        return u
    def saveFile(self , path):

        if os.stat(path).st_size == 0: #to avoid reading empty file
            tmp = open(path , 'w')
            tmp.write('[]')
            tmp.close()

        f = open(path)
        data = json.load(f)
        f.close()
        f = open(path , 'w')
        data.append(self.__dict__)
        #print(json.dumps(self.__dict__))
        f.write(json.dumps(data))
        print(self.__dict__)
        f.close()

    def findInFile(username , password , path):
        f = open(path)
        data = json.load(f)
        f.close()
        for item in data:
            if item['username'] == username and item['password'] == password:
                u = UserClass()
                u.setData1(item['username'], item['password'],item['name'], item['dateOfBirth'], item['universityLocation'], item['field'],item['workplace'] , item['email'], item['specialties'])
                return u
        return None

    def searchByName(name , path):
        f = open(path)
        data = json.load(f)
        f.close()
        for item in data:
            if item['name'] == name:
                return UserClass.toUser(item)
        return None
    def isInFile(name , path):
        f = open(path)
        data = json.load(f)
        f.close()
        for item in data:
            if item['name'] == name:
                return True
        return False

    def LinkUser(self , u):
        import MyEdge
        e = MyEdge.EdgeClas(self, u)
        self.LinkedPeople[u] = e
        UserClass(u).LinkedPeople[self] = e

    def toString(self):
        print('Name : ' + self.name)
        print('Birthday : ' + self.dateOfBirth)
        print('University Location : ' + self.universityLocation)
        print('Field : ' + self.field)
        print('Work place : ' + self.workplace)
        print('Email : ' + self.email)
        print('Specialties : ' , end= '')
        print(self.specialties)
