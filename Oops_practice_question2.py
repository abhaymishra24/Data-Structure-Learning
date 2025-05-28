
# Here solving basic to advance question on Oops concepts-

# Start from here

# Question 1 on payment transction voic notes 

class Payment:

    def __init__(self,ammount):
        self.ammount=ammount

    def pay_money(self):
        print(f"Rupees {self.ammount} is pay on phonepay")

    def greet(self):
        print("Thankyou!")

p=Payment(50)
p.pay_money()
p.greet()

# here very basic question-

class number:
    def a_number(self, l1, l2):

        self.l1=l1
        self.l2=l2

    def add(self):
        print(f"sum is {self.l1+self.l2}")

n=number()
n.a_number(6,7)
n.add()

# Here solve another oops concepts questions - 

class City:

    def __init__(self, area,toarea, Number):
        self.area=area
        self.toarea=toarea
        self.Number=Number

    def bus_time(self,n):
        print(f"this {self.Number} bus from {self.area} to {self.toarea} at {n} will go")
        print(f"Number = {self.Number}")

    
c = City("Ashok Nager", "Indira Nager", "224")
c.bus_time(f"{4}pm")   

# here we solve calculation on two number -

def sum(n,m):
    
    print(f"sum is :{n+m}")
    print(f"sub is :{n-m}")
    print(f"divide is :{n//m}")
    print(f"multi is :{n*m}")
    
sum(8,8)

 
 # here basice time problem , once time please watch this question and thik about it !
 
from datetime import datetime, timedelta

date1 = datetime(2023, 5, 1)
date2 = datetime(2023, 5, 15)
delta = date2 - date1
print(delta.days)

# Explaination of this code - 

# The code calculates the difference between two datetime objects using the timedelta class. 
# The result is stored in the 'delta' variable.
# The 'days' attribute of timedelta gives the number of days between the two dates.
# In this case, the difference between May 15 and May 1 is 14 days.


# wrtie to programme to check that the list is palindrome or not -(# this to build game on this code - )

# def is_palindrome(lst):
#     if lst == lst[::-1]:
#         print("It's a palindrome")
#     else:
#         print("It's not a palindrome")
#     print("Original list:", lst)
#     print("Reversed list:", lst[::-1])

# # Take input from user
# user_input = input("Enter list elements separated by spaces: ")
# lst = [int(x) for x in user_input.strip().split()]
# is_palindrome(lst)

# same code - 

lst = list(map(str, input("Enter list elements separated by spaces: ")))
lst2 = lst.copy()
lst2.reverse()

if lst == lst2:
    print("It's a palindrome")
else:
    print("It's not a palindrome")
    
print(lst)
print(lst2)