
# return a*b and f"this is double numbe{self.d}"

# Here first problem - 

class Node:
    def __init__(self, item,next=None):
        self.item = item
        self.next = next

class Cal_number:

    def __init__(self, d, s):
        self.d = d
        self.s = s

    def a_number(self,a,b):
        print(f"{a+b} this is combine number {self.d}")
    
    def s_number(self,a,b):
        print(f"{a-b} this is not combine number {self.s}")
    
    def p_number(self,a,b):
        print(f"{a*b} this is double numbe {self.d}")
    
    def d_number(self,a,b):
        print(f"{a/b} this is half of number {self.s}")
    

n = Cal_number("Given value", "Taken value")
n.a_number(4,5)
n.s_number(16,4)
n.p_number(5,6)
n.d_number(10,5)
