# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
#print("Hello world")
class node :
    def __init__(self, data):
        self.data = data #self.data = data part
        self.next = None #self.next = address part
        
class linkedList :
    def __init__(self) :
        self.head = None
        
    def insert_begin(self,data) : #O(1)
        new_node = node(data) #1
        if self.head == None : #1
            self.head = new_node #1
        else :
            new_node.next = self.head # connection with old head #1
            self.head = new_node #1
          
    def traverse(self) :
        n = self.head
        while n != None :
            print(n.data,"\t")
            n = n.next
        #if self.head != None :
        #    print(self.head.data)
            
l = linkedList()
l.insert_begin(3)
l.insert_begin(4)
l.insert_begin(5)
l.traverse()
            
            
