
# Here second problem solve of Stack Data Structure - 

class Stack:

    def __init__(self):
         self.item=[]

    def is_empty(self):
         return len(self.is_empty())==0
    
    def push(self,data):
         self.item.append(data)

    def pop(self):
         if not self.is_empty():
              return self.item.pop()
         else:
              raise IndexError("List is Empty")
         
    def peek(self):
         if not self.is_empty():
              return self.item.peek()
         else:
              raise IndexError("List is Empty")
         
    def size(self):
         return len(self.item)
    