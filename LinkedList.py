# Class LinkedList

class Node:
    def __init__(self, val):
        self.next=None
        self.data=val


class LL:
    def __init__(self):
        self.head=None
        self.tail=None

class myLL(LL):
    def __init__(self):
        super().__init__()

    def insertathead(self, val):
        newNode=Node(val)
        if not(self.head):
            self.head=newNode
            self.tail=newNode

        else:
            newNode.next=self.head
            self.head=newNode

    def insertattail(self, val):
        newNode=Node(val)
        if not(self.head):
            self.head=newNode

    def insertattail(self, val):
        newNode=Node(val)
        if not(self.head):
            self.head=newNode
            self.tail=newNode
        else:
            self.tail.next=newNode
            self.tail=newNode


    def deletefromhead(self):
        if not(self.head):
            print("Linked List is Empty")
            return 
        tempnode=self.head
        self.head=tempnode.next

    def deletefromtail(self):
        if not(self.head):
            print("Linked List is Empty")
            return

        if self.head==self.tail:
            self.head=None
            self.tail=None
            return

        tempnode=self.head
        while(tempnode.next!=self.tail):
            tempnode=tempnode.next
        tempnode.next=None
        self.tail=tempnode

    def display(self):
        if not(self.head):
            print("Linked List is Empty")
            return

        tempnode=self.head
        while(tempnode):
            print(tempnode.data," ")
            tempnode=tempnode.next




