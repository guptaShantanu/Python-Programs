class Node:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

        
    def insert(self,node,rt):
        if rt == None:
            rt = node
        else:
            if node.val < rt.val:
                rt.left = self.insert(node,rt.left)  
            elif node.val > rt.val:
                rt.right = self.insert(node,rt.right)
        return rt
                    

    def remove(self,val):
        print(self.root.val)

    def search(self,val,root):
        if root == None:
            print("Item not found")
        else:
            if val < root.val:
                self.search(val,root.left)
            elif val > root.val:
                self.search(val,root.right)
            else:
                print("Item found")

       

myBst = BST()
    
node1 = Node(10)
node2 = Node(20)
node3 = Node(30)
node4 = Node(15)
node5 = Node(5)
node6 = Node(1)

myBst.root  = myBst.insert(node1,myBst.root)
myBst.root  = myBst.insert(node2,myBst.root)
myBst.root  = myBst.insert(node3,myBst.root)
myBst.root  = myBst.insert(node4,myBst.root)
myBst.root  = myBst.insert(node5,myBst.root)
myBst.root  = myBst.insert(node6,myBst.root)

myBst.search(10,myBst.root)
myBst.search(15,myBst.root)
myBst.search(99,myBst.root)
myBst.search(1,myBst.root)

myBst.remove(34)
    
