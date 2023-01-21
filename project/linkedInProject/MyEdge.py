import MyUser

class MyEdge2:
    start = MyUser.MyUser2()
    end = MyUser.MyUser2()
    element = int()
    def __init__(self , s , e):
        self.start = s
        self.end = e
    def setElement(self , e):
        self.element = e

