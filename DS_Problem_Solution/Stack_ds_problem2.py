
# Here second problem solve of Stack Data Structure - 

# class Stack(list):

#     def is_empty(self):
#          return len(self)==0
    
#     def push(self,data):
#          self.append(data)

#     def pop(self):
#          if not self.is_empty():
#               return super().pop()
#          else:
#               raise IndexError("List is Empty")
         
#     def peek(self):
#          if not self.is_empty():
#               return self[-1]
#          else:
#               raise IndexError("List is Empty")
         
#     def size(self):
#          return len(self)
    
#     def insert(self, index, data):
#          return AttributeError ("No attribute int this insert function")
    
# s1= Stack()
# s1.push(1)
# s1.push(2)
# s1.push(3)
# print("topvalue = ", s1.peek())
# print(s1.pop())
# print("topvalue = ", s1.peek())

# second code try by my self again - 

class Stack(list):

    def is_empty(self):
        return self()==0
    def push(self,data):
        return self.append(data)
    def pop(self):
        return super().pop()
    def peek(self):
        return self[-1]
    def size(self):
        return len(self)
    def insert(self, index, data):
        raise AttributeError("No elements")
    
s1= Stack()
s1.push(2)
s1.push(4)
s1.push(6)
print("top elements=", s1.peek())
print(s1.size())
print(s1.pop())
print("top elements=", s1.peek())



