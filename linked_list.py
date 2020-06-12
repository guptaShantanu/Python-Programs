class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class LinkedList:
    def __init__(self):
        self.first=None
        self.head=None

    def insert(self,a):
        if self.first!=None:
            temp=self.head
            temp.next=Node(a)
            self.head=temp.next
        else:
            self.first=Node(a)
            self.head=self.first

    def search(self,item):
        temp=self.first
        while temp!=None:
            if temp.data==item:
                print("Item found")
                break
            temp=temp.next
        else:
            print("Item not found")

    def display(self):
        temp=self.first
        while temp!=None:
            print(temp.data,end="-> ")
            temp=temp.next

if __name__=="__main__":
    llist=LinkedList()
    llist.insert(7)
    llist.insert(10)
    llist.insert(7)
    llist.insert(10)
    llist.insert(5)
    llist.insert(7)
    llist.insert(10)
    llist.insert(7)
    llist.insert(10)

    llist.display()
    llist.search(5)
                
        
