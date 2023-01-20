from User import User


class Edge:
    start = User()
    end = User()
    element = int()
    def __init__(self , s , e):
        self.start = s
        self.end = e
    def setElement(self , e):
        self.element = e
