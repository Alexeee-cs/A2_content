class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
    def insert(self,data):
        if data < self.data:
            if self.left:
                self.left.insert(data)
            else:
                self.left = Node(data)
                return
        else:
            if self.right:
                self.right.insert(data)
            else:
                self.right = Node(data)
                return
    def search(self,data):
        if data == self.data:
            return str(data) + " is found in the Tree"
        elif data < self.data:
            if self.left:
                return self.left.search(data)
            else:
                return str(data) + " is not found in the Tree"
        else:
            if self.right:
                return self.right.search(data)
            else:
                return str(data) + " is not found in the Tree"
    def PrintTree(self): #inorder traversal
        if self.left is not None:
            self.left.PrintTree()
        print(self.data)
        if self.right is not None:
            self.right.PrintTree()

Tree = Node(36)
Tree.insert(17)
Tree.insert(5)
Tree.insert(21)
Tree.insert(70)
Tree.insert(50)
Tree.insert(102)
Tree.insert(91)
print(Tree.search(21))
print(Tree.search(66))
Tree.PrintTree()
