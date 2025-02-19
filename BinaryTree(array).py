Tree = []
null = -1
first_node_index = null
freepointer = 0
def Initialisation():
    global null
    for i in range(6):
        Tree.append([i+1,0.0,-1])
    Tree.append([null,0.0,-1])
Initialisation()

def insert(value):
    global null
    global first_node_index
    global freepointer
    if freepointer == null:
        print("The Tree is full")
    else:
        position_index = freepointer
        freepointer = Tree[freepointer][0]
        Tree[position_index][0] = null
        Tree[position_index][1] = value
        if first_node_index == -1:
            first_node_index = position_index #the tree is no longer empty
        else:
            temp_pointer = first_node_index
            while temp_pointer != null: #loop until it reaches the bottom of the sub-trees
                previous_node_pointer = temp_pointer
                if Tree[temp_pointer][1] > value: #turn left
                    TurnLeft = True
                    temp_pointer = Tree[temp_pointer][0]
                else:
                    TurnLeft = False
                    temp_pointer = Tree[temp_pointer][2]
            if TurnLeft == True:
                Tree[previous_node_pointer][0] = position_index
            else:
                Tree[previous_node_pointer][2] = position_index
def search(value):
    temp_pointer = 0
    while temp_pointer != -1 and Tree[temp_pointer][1] != value:
        if Tree[temp_pointer][1] > value:
            temp_pointer = Tree[temp_pointer][0]
        else:
            temp_pointer = Tree[temp_pointer][2]
    if temp_pointer == -1:
        return "Item is not found"
    return "Found at position " + str(temp_pointer)
def print_tree(root):
    global null
    if root != null:
        print_tree(Tree[root][0])
        print(Tree[root][1])
        print_tree(Tree[root][2])

insert(5)
insert(3)
insert(7)
insert(4)
insert(1)
insert(6)
insert(11)
print_tree(0)
print(search(5))
print(search(13))
print(search(4))
