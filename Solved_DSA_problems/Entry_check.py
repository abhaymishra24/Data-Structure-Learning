
# # this is codechef contest question - 

# def entry_check(age):
  
#         if age >= 10:    
#             print("yes")
#         else:    
#             print("no")
        
# x = int(input("Enter your age: "))
# entry_check(x) 

# def identity(nation):
    
#     if nation == 'Indian':
#         print("Yes, entry")
        
#     else:
#         print("No")
        
# n = input("Enter your Nation: ")
# identity(n)


# check once - 

class Entrycheck:
    
    def country(name):
        name = input("Enter your Origin Nation:")
        if name == 'Australia':
            print("Yes, acccepted")
            print("Welcome to India")
        else:
            print("No, Not accepted")
            print("Sorry, Try with other country")
            
    def age_check(age):
        age = int(input("Enter you current age: "))
        if age >= 21:
            print("Accepted")
        else:
            print("Not accepted")
            
    def work_check(work):
        work = input("Enter your current work postion:")
        if work == "Software Engineer":
            print("Yes")
        else:
            print("No")
            
check = Entrycheck()
check.country()
check.age_check()
check.work_check()
