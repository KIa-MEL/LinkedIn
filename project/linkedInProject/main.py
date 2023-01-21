from MyEdge import MyEdge2
from MyUser import MyUser2

user = MyUser2()
def showMenu():
    print('1.LogIn\n2.SignUp\n3.Show All users\n4.Search')
    inp = input('>> ')
    return inp
def login(username , password):
    try:
        if MyUser2.findInFile(username , password , MyUser2._local_users_file_path) != None:
            #go to login
            print()
        else:
            print('User not found!')
    except Exception:
        print("Something went wrong!")
def signup(username, password, name, dateOfBirth, universityLocation, field, workplace , email, specialties):
    u = MyUser2()
    u.setData1(username, password, name, dateOfBirth, universityLocation, field, workplace , email, specialties)
    u.saveFile(MyUser2._local_users_file_path)

print('Welcome to Unlinked Out')
inp = showMenu()

while True:
    if inp == '1':
        username = input('Enter Username >> ')
        password = input('Enter Password >> ')
        login(username , password)
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
        users = MyUser2.getUsers( MyUser2._main_users_file_path)
        i = int(1)
        for user in users:
            print(str(i) + '.' + user.name)
            i += 1
    elif inp == '4':
        name = input('Enter the name >> ')
        user = MyUser2.searchByName(name , MyUser2._main_users_file_path)
        if user == None :
            print('The user ' + name + ' not found')
        else:
            user.toString()

    print('\n###############################################\n')

    inp = showMenu()
