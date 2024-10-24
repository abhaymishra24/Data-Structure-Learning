
# Here I solve basic queations using python oops-

# Start from Here 1 to 6-

# Number 1-

class Number:

    def plus(self,a,b):
        print(f"sum number is: {a+b}")
         
    def subt(self,c,d):
        print(f"subtraction of value is:{c-d}")
         
num = Number()
print(num.plus(4, 7))
print(num.subt(4, 4))


# Number 2-

class Phone:

    def __init__(self,call, music, movie):

        self.call= call
        self.music= music
        self.movie= movie

    def c_call(self):
        print(f"this calling is comming from spam:{self.call}")
        print("dont accept it: thankyou")

    def p_music(self):
        print(f"If we are play music by this:{self.music}")
        print("So it will play")

    def p_movie(self):
        print(f"if we play a movie by this:{self.movie}")
        print("so it will show us movies")
         

mb=Phone("Caller", "Spotify","Netflix")

mb.c_call()
mb.p_music()
mb.p_movie()


# Number 3-

class Person:

    def __init__(self, run, slp, eat):
         self.run=run 
         self.slp=slp
         self.eat=eat

    def p_run(self,a,b):
        print(f"Ramesh can run by {a+b} km per/h and run at {self.run}")

    def p_slp(self,a,b):
        print(f"Ramesh can sleep around {a+b} h/perday and sleep on {self.slp}")

    def p_eat(self):
        print(f"Ramesh can eat {self.eat}")

pn = Person("Road","Bed", "Chawal,daal,roti and salad at a one time")

pn.p_run(1,1)
pn.p_slp(4,4)
pn.p_eat()

# Number 4-

class Numberprint:

    def __init__(self):
         self.number=[ 
             [1],
             [2, 3],
             [4, 5, 6]
         ]

    def print_number(self):
        for row in self.number:
            print(" ".join(map(str, row)))

pnt= Numberprint()
pnt.print_number()


# Number 5-

class TwoSum:
    def __init__(self, nums):
        self.nums = nums

    def find_indices(self, target):
        # Create a dictionary to store the numbers and their indices
        num_to_index = {}
        
        for index, num in enumerate(self.nums):
            complement = target - num
            
            # Check if the complement exists in the dictionary
            if complement in num_to_index:
                return [num_to_index[complement], index]
            
            # Store the number and its index in the dictionary
            num_to_index[num] = index
        
        return None  # Return None if no solution is found

# Example usage
nums = [3, 2, 4]
target = 6

# Create an instance of TwoSum
two_sum_instance = TwoSum(nums)

# Find and print the indices
result = two_sum_instance.find_indices(target)

# Output: [1, 2]
print(result)  

# Here is also number six 6 -

# Number 6-


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



# Here I solve some basic question on oops concepts 

# Here End 1 to 6 questions and thier solutions.

# To be continue