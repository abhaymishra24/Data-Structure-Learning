
# Here second problem solve of Stack Data Structure - 

class Stack(list):

    def is_empty(self):
         return len(self)==0
    
    def push(self,data):
         self.append(data)

    def pop(self):
         if not self.is_empty():
              return super().pop()
         else:
              raise IndexError("List is Empty")
         
    def peek(self):
         if not self.is_empty():
              return self[-1]
         else:
              raise IndexError("List is Empty")
         
    def size(self):
         return len(self)
    
    def insert(self, index, data):
         return AttributeError ("No attribute int this insert function")
    
s1= Stack()
s1.push(1)
s1.push(2)
s1.push(3)
print("topvalue = ", s1.peek())
print(s1.pop())
print("topvalue = ", s1.peek())

# second code try by my self again - 

class Stack(list):                         # define the class stack with that parent class 

    def is_empty(self):                    # define empty function for check the list is empty or not
        return self()==0
    
    def push(self,data):                   # define push function for put the value in the list
        return self.append(data)
    
    def pop(self):                         # define pop function for delete the top value or last value of list
        return super().pop()
    
    def peek(self):                      # define peek function for return top value from list
        return self[-1]
    
    def size(self):                      # define size function for check the elements size of list
        return len(self)
    
    def insert(self, index, data):       # define insert for not implement the insert method by itself or user
        raise AttributeError("No elements")
    
s1= Stack()                               # here s1 assign with stack object
s1.push(2)                                # here we put first value in the list by using push function
s1.push(4)                                # here second value
s1.push(6)                                # here third value
print("top elements=", s1.peek())         # here we can see top value of list by using peek function
print(s1.size())                          # here we can see the size of list by using size function
print(s1.pop())                           # here we can delete the top value by using pop function 
print("top elements=", s1.peek())         # here we again see the top value by peek function
