import MyUser

class EdgeClas:
    start = MyUser.UserClass()
    end = MyUser.UserClass()
    element = int()
    def __init__(self , s , e):
        self.start = s
        self.end = e
    def setElement(self , e):
        self.element = e

