
# Number 1-

class Number:

    def plus(self,a,b):
        print(f"sum number is: {a+b}")
         
    def subt(self,c,d):
        print(f"subtraction of value is:{c-d}")
         
num = Number()
print(num.plus(4, 7))
print(num.subt(4, 4))


# Number 2

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