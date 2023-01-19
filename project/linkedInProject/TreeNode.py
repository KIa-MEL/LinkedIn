

class TreeNode:

    def __init__(self , parent , data):
        self.parent = parent
        self.data = data
        self.children = list()


    def __int__(self , data):
        self.parent = None
        self.data = data
        self.children = list()