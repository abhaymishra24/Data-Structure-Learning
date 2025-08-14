
print("Hello world, this new file.")


def number():
    k = int(input())
    m = int(input())
    
    print(k*m)
    
number()
print("This number is the multiplication.")


def collect():
    
    a = int(input("Enter a your number:"))
    print(f"Your number is: {a}. This is your number's answer: {a*a}.")
    
    
collect()

print("THis is the final number.")
    

def final_number():
    
    num = int(input("Enter your final number: "))
    print(f"Your final number is: {num}. This is your number for final answer and the number is {(num*num)- num}.")
    
final_number()
    
def number():
    
    n,k = map(int, input("ENter your number: ").split())
    
    if n*5 == k:
        print(f"Yes, this is your find out number{k}.")
        
    else:
        print("No this is not correct number .")
        
    print(f"Your prineted number is {k} and {n}.")
        
    
number()


# write normal program here - 

