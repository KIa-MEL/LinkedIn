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
    LinkedPeople = dict

    def __init__(self):
        self.LinkedPeople = dict()
    def setData1(self , username, password, name, dateOfBirth, universityLocation, field, workplace , email, specialties , connectionId):
        self.username = username
        self.password = password
        self.name = name
        self.dateOfBirth = dateOfBirth
        self.universityLocation = universityLocation
        self.field = field
        self.workplace = workplace
        self.email = email
        self.specialties = specialties
        self.connectionId = connectionId
    def setData(self,id , name, dateOfBirth, universityLocation, field, workplace , email, specialties , connectionId):
        self.id = id
        self.name = name
        self.dateOfBirth = dateOfBirth
        self.universityLocation = universityLocation
        self.field = field
        self.workplace = workplace
        self.email = email
        self.specialties = specialties
        self.connectionId = connectionId

    @staticmethod
    def getUsers(path): # static function
        f = open(path)
        data = json.load(f)
        users = list()

        for item in data:
            u = UserClass()
            u.setData(item['id'], item['name'] , item['dateOfBirth'] , item['universityLocation'] , item['field'] , item['workplace'] , item['email'] , item['specialties'] , item['connectionId'])
            users.append(u)
        return users

    def getLocalUsers(path): # static function
        f = open(path)
        data = json.load(f)
        users = list()

        for item in data:
            u = UserClass()
            u.setData1(item['username'],item['password'] ,item['name'] , item['dateOfBirth'] , item['universityLocation'] , item['field'] , item['workplace'] , item['email'] , item['specialties'] , item['connectionId'])
            users.append(u)
        return users


    @staticmethod
    def toUser(item):
        u = UserClass()
        u.setData(item['id'],item['name'], item['dateOfBirth'], item['universityLocation'], item['field'], item['workplace'],item['email'], item['specialties'], item['connectionId'])
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
    @staticmethod
    def findInFile(username , password , path):
        f = open(path)
        data = json.load(f)
        f.close()
        for item in data:
            if item['username'] == username and item['password'] == password:
                u = UserClass()
                u.setData1(item['username'], item['password'],item['name'], item['dateOfBirth'], item['universityLocation'], item['field'],item['workplace'] , item['email'], item['specialties'] , item['connectionId'])
                return u
        return None




    @staticmethod
    def searchByEmail(email , password , path):
        f = open(path)
        data = json.load(f)
        f.close()
        for item in data:
            if item['email'] == email and password == '****':
                u = UserClass()
                u.setData(item['id'], item['name'], item['dateOfBirth'], item['universityLocation'], item['field'],
                          item['workplace'], item['email'], item['specialties'], item['connectionId'])
                return u
        return None



    @staticmethod
    def searchByName(name , path):
        f = open(path)
        data = json.load(f)
        f.close()
        for item in data:
            if item['name'] == name:
                return UserClass.toUser(item)
        return None

    @staticmethod
    def isInFile(name , path):
        f = open(path)
        data = json.load(f)
        f.close()
        for item in data:
            if item['name'] == name:
                return True
        return False

    def addLink(self , u , e):
        self.LinkedPeople[u] = e

    def toString(self):
        print('Name : ' + self.name)
        print('Birthday : ' + self.dateOfBirth)
        print('University Location : ' + self.universityLocation)
        print('Field : ' + self.field)
        print('Work place : ' + self.workplace)
        print('Email : ' + self.email)
        print('Specialties : ' , end= '')
        print(self.specialties)
