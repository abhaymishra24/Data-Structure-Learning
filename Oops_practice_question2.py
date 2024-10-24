
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

         