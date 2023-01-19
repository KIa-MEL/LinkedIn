from TreeNode import TreeNode


class Tree :

    def __init__(self):
        self.root = None


    def addNode (self, parentData , data):

        if self.root is None:
           new_node = TreeNode(data)
           self.root = new_node

        parent = self.search(parentData , self.root)
        new_node = TreeNode (data)
        TreeNode(parent).children.append(new_node)
        new_node.parent = parent


    def search(self , data , currentNode):

        if data == currentNode.data :
            return currentNode

        node = None
        for child in currentNode.children :

            if node is not None:
                return node


            node=self.search(data , child)

        return node#=========================================should throws exception