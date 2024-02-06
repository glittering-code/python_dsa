# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
#print("Hello world")
class Stack : 
    def __init__(self) :
        self.arr = []
    def push(self,data) :
        self.arr.append(data)
    def pop(self) :
        return self.arr.pop()
    def isEmpty(self):
        return len(self.arr) == 0

stk = Stack()
stk.push(10)
stk.push(20)
stk.push(30)
while(stk.isEmpty() == False) :
    print(stk.pop())
    
    
