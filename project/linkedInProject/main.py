from MyEdge import MyEdge
from MyUser import MyUser

user = MyUser()

def showMenu():
    print('1.LogIn\n2.SignUp\n3.Show All users\n4.Search')
    inp = input('>> ')
    return inp
def login(username , password):
    if MyUser.findInFile(username , password , MyUser._local_users_file_path) != None:
        #go to login
        print()
    else:
        print('User not found!')
        showMenu()

def signup(username, password, name, dateOfBirth, universityLocation, field, workplace, specialties):
    u = MyUser()
    u.setData1(username, password, name, dateOfBirth, universityLocation, field, workplace, specialties)
    u.saveFile(MyUser._local_users_file_path)


print('Welcome to Unlinked Out')

inp = showMenu()

if inp == '1':
    username = input('Enter Username >> ')
    password = input('Enter Password >> ')
    login(username , password)
elif inp == '2':
    name = input('Name >> ')
    dateOfBirth = input('Date of birth >> ')
    universityLocation = input('University location >> ')
    field = input('Field >> ')
    workplace = input('Work place >> ')
    specialties = list(input('Specialties >> ').split())
    username = input('username >> ')
    password = input('password >> ')
    signup(username, password, name, dateOfBirth, universityLocation, field, workplace, specialties)