class node:
    def __init__(self,data,nextNode):
        self.__data = data
        self.__nextNode = nextNode
    def data_getter(self):
        return self.__data
    def nextNode_getter(self):
        return self.__nextNode

linkedList = []
def getData():
    try:
        with open ("TreasureChestData.txt") as f:
            count = 0
            for line in f:
                if count%2 == 0:
                    data = line.strip()
                else:
                    nextNode = line.strip()
                    linkedList.append(node(data,nextNode))
                count += 1
    except OSError:
        print("File not found")

getData()

linkedList = [node(1,1),node(5,4),node(6,7),node(7,-1),node(2,2),node(0,6),node(0,8),node(56,3),node(0,9),node(0,-1)]
startPointer = 0
emptyList = 5
def outputNodes(a,p):
    while p != -1:
        print(a[p].data_getter())
        p = a[p].nextNode_getter()
outputNodes(linkedList,startPointer)
def addNode(a,startpointer,emptylist): #sp=0 el=5
    if emptylist > 0 and emptylist < 10:
        data = int(input("Enter the data to be entered: "))
        nextNode = -1
        a[emptylist] = node(data,nextNode) #Index=5, Data=data, nextNode = -1
        while startpointer != -1: #startPointer = 0
            previous_index = startpointer #previous_index = 3
            startpointer = a[startpointer].nextNode_getter() #startpointer = -1
        nextdata = a[previous_index].data_getter() #nextdata = 7
        a[previous_index] = node(nextdata,emptylist)
        return True
    else:
        return False
addNode(linkedList,startPointer,emptyList)
outputNodes(linkedList, startPointer)
