
# Here stack question sloved

class Stack:
    def __init__(self):
         self.item=[]
        
    def is_empty(self):
         return len(self.item)==0
    
    def push(self, data):
         self.item.append(data)

    def pop(self):
         if not self.is_empty():
              return self.item.pop()
         else:
              raise IndexError("Stack is empty")

    def peek(self):
         if not self.is_empty():
              return self.item[-1]
         else:
              raise IndexError("Stack is Empty")

    def size(self):
         return len(self.item) 

s1= Stack()
s1.push(4)
s1.push(5)
s1.push(6)
print("Size of elemnt:", s1.size())
print("top element:", s1.peek())
print("Removed item:", s1.pop())
print("top element:", s1.peek())
print("Size of elemnt:", s1.size())
print()

# Second time same code try by  myself of stack-

class Stack:
    
    def __init__(self):
         self.item=[]

    def is_empty(self):
         return len(self.item)==0
    
    def push(self,data):
         self.item.append(data)
         
    def  pop(self):
         if not self.is_empty():
              return self.item.pop()
         else:
              raise IndexError("list is empty")
         
    def peek(self):
         if not self.is_empty():
              return self.item[-1]
         else:
              raise IndexError("lsit is empty")
         
    def size(self):
         return len(self.item)

s = Stack()
s.push(10)
s.push(20)
s.push(30)
print(s.size())
print(s.peek())
print(s.pop())
print(s.peek())
print(s.is_empty())   