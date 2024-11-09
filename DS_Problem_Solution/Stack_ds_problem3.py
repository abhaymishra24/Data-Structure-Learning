
# Here third problem of Stack question -

# class Node:

#     def __init__(self, item=None, next=None):
#         self.item=item
#         self.next=next

# class Stack:

#     def __init__(self):
#         self.start=None
#         self.item_count=0

#     def is_empty(self):
#         return self.start==None
    
#     def push(self,data):
#         n = Node(data, self.start)
#         self.start=n
#         self.item_count+=1 
    
#     def pop(self):
#         if not self.is_empty():
#             data= self.start.item
#             self.start=self.start.next
#             self.item_count-=1
#             return data
#         else:
#             raise IndexError("Stack is empty")
        
#     def peek(self):
#         if not self.is_empty():
#             return self.start.item
#         else:
#             raise self.is_empty()
        
#     def size(self):
#         return self.item_count     

# s2=Stack()
# s2.push(5)
# s2.push(6)
# s2.push(7)
# print("total elemnts=", s2.size())
# print("top value=", s2.peek())
# print("remove top value=", s2.pop())
# print("total elements again=", s2.size())
# print("top value again=", s2.peek())


# third code try by my self again -

class Node:

    def __init__(self, item=None, next=None):
        self.item=item
        self.next=next

class Stack:

    def __init__(self):
         self.start=None
         self.item_count=0

    def is_empty(self):
        return self.start==None
    
    def push(self, data):
        n= Node(data, self.start)
        self.start=n
        self.item_count+=1

    def pop(self):
        if not self.is_empty():
            data=self.start.item
            self.start=self.start.next
            self.item_count-=1
        else:
            raise IndexError("Stack is none")
        
    def peek(self):
        if not self.is_empty():
            return self.start.item
        else:
            raise self.is_empty()
        
    def size(self):
        return self.item_count
    
s2=Stack()
s2.push(8)
s2.push(9)
s2.push(0)
print("len of elements is = ", s2.size())
print("top elements of stack = ", s2.peek())
print("delete a value from stack = ", s2.pop())
print("top value again is = ",s2.peek())
print("size of elements is = ", s2.size())
            
        
