class Node:
    def __init__(self,datavalue,leftpointer,rightpointer):
        self.__DataValue = datavalue #string
        self.__LeftPointer = leftpointer #integer
        self.__RightPointer = rightpointer #integer
    def leftpointer_getter(self):
        return self.__LeftPointer
    def rightpointer_getter(self):
        return self.__RightPointer
    def data_getter(self):
        return self.__DataValue
    def leftpointer_setter(self,value):
        self.__LeftPointer = value
    def rightpointer_setter(self,value):
        self.__RightPointer = value
    def __repr__(self):
        return self.__DataValue

arrayname = []
for i in range(0,12):
    arrayname.append(Node('Name',-1,-1))
NextNode = -1
def CreateTree(NodeData):
    global NextNode
    NextNode = 0
    arrayname[NextNode] = Node(NodeData,-1,-1)
    NextNode += 1
def AttachLeft(NodeData,ParentNode):
    global NextNode
    arrayname[NextNode] = Node(NodeData,-1,-1)
    arrayname[ParentNode].leftpointer_setter(NextNode)
    NextNode += 1
def AttachRight(NodeData, ParentNode):
    global NextNode
    arrayname[NextNode] = Node(NodeData, -1, -1)
    arrayname[ParentNode].rightpointer_setter(NextNode)
    NextNode += 1
def printTreeLeft():
    pointer = 0
    while pointer != -1:
        print(arrayname[pointer].data_getter())
        pointer = arrayname[pointer].leftpointer_getter()

CreateTree("Red")
AttachLeft("Blue", 0)
AttachRight("Green", 0)
AttachRight("Black", 2)
AttachLeft("Brown", 2)
AttachLeft("Peach", 3)
AttachLeft("Yellow", 1)
AttachRight("Purple", 1)
AttachLeft("White", 6)
AttachLeft("Pink", 7)
AttachLeft("Grey", 9)
AttachRight("Orange", 9)
printTreeLeft()
