class Node:
    def __init__(self,val):
        self.val = val;
        self.left = None
        self.right = None

def insertData(myRoot,node):
    if myRoot==None:
        myRoot = node
    else:
        if node.val < myRoot.val:
            myRoot.left = insertData(myRoot.left,node)
        elif node.val > myRoot.val:
            myRoot.right = insertData(myRoot.right,node)
    return myRoot
def search(myRoot,target):
    if myRoot==None:
        print("Tree is empty")
    else:
        if target < myRoot.val:
            print("left")
            search(myRoot.left,target)
        elif target > myRoot.val:
            print("right")
            search(myRoot.right,target)
        else:
            print("Item found")

def deleteData(myRoot,target):
    if myRoot == None:
        print("Empty tree")
    else:
        if target < myRoot.val:
            print("left")
            search(myRoot.left,target)
        elif target > myRoot.val:
            print("right")
            search(myRoot.right,target)
        else:
            pass
            


        

def traversalIn(myRoot):
    if myRoot == None:
        pass
    else:
        traversalIn(myRoot.left)
        print(myRoot.val,end = " ")
        traversalIn(myRoot.right)

def traversalPost(myRoot):
    if myRoot == None:
        pass
    else:
        traversalPost(myRoot.left)
        traversalPost(myRoot.right)
        print(myRoot.val,end = " ")

def traversalPre(myRoot):
    if myRoot == None:
        pass
    else:
        print(myRoot.val,end = " ")
        traversalPre(myRoot.left)
        traversalPre(myRoot.right)
        
    

myRoot = None

node1 = Node(10)
myRoot = insertData(myRoot,node1);
node2 = Node(7)
myRoot = insertData(myRoot,node2);
node3 = Node(9)
myRoot = insertData(myRoot,node3);
node4 = Node(8)
myRoot = insertData(myRoot,node4);
node4 = Node(15)
myRoot = insertData(myRoot,node4);
node4 = Node(14)
myRoot = insertData(myRoot,node4);
node4 = Node(13)
myRoot = insertData(myRoot,node4);
traversalPre(myRoot)
print()
traversalIn(myRoot)
print()
traversalPost(myRoot)
