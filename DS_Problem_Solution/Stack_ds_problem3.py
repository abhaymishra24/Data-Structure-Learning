
# Here third problem of Stack question -

class Stack:

    def __init__(self,item):
        self.item=item()

    def is_empty(self):
        return len(self.item)==0
    
    def push(self,data):
        return self.item.append(data)
    
    def pop(self):
        if not self.is_empty():
            return self.item.pop()
        else:
            raise IndexError("Stack is empty")
        
    def peek(self):
        if not self.is_empty():
            return self.item[-1]
        else:
            raise IndexError("Stack is empty")
        
    def size(self):
        return len(self.item())
    

         