#Types of Inheritence

#Single Level Inheritance

'''class Animal:
    def __init__(self,name):
        self.name=name
    
    def eat(self):
        print(self.name,"is eating")

class Dog(Animal):
    def __init__(self,name,color,breed):
        super().__init__(name)
        self.breed=breed
        self.color=color
    def bark(self):
        print(self.name,"is barking")
obj=Dog("Alex","Brown","Pitbull")
print(obj.name)
print(obj.breed)
print(obj.color)
obj.bark()
obj.eat()'''

#Multiple Inheritence

'''class Animal:
    def __init__(self,name):
        self.name=name
    def n(self):
        print(self.name,"is an animal")

class leg:
    def __init__(self,legs):
        self.legs=legs
    def l(self):
        print("It has ",self.legs," legs")

class Dog(Animal,leg):
    def __init__(self,name,legs,sound):
        Animal.__init__(self,name)
        leg.__init__(self,legs)
        self.sound=sound
    def s(self):
        print(self.name,self.sound)

obj=Dog("Alex","4","Barks")

print(obj.name)
print(obj.legs)
print(obj.sound)

obj.n()
obj.l()
obj.s()
'''
#Multilevel Inheritence
'''
class Animal:
    def __init__(self,name):
        self.name=name
    def n(self):
        print(self.name,"is an animal")

class leg(Animal):
    def __init__(self,name,legs):
        super().__init__(name)
        self.legs=legs
    def l(self):
        print("It has ",self.legs," legs")

class Dog(leg):
    def __init__(self,name,legs,sound):
        super().__init__(name,legs)
        self.sound=sound
    def s(self):
        print(self.name,self.sound)

obg=Dog("Maxi","4","Barks")
print(obg.name)
print(obg.legs)
print(obg.sound)

obg.n()
obg.l()
obg.s()
'''

#Hierarchical Inheritence
'''
class Animal:
    def __init__(self,name):
        self.name=name
    
    def run(self):
        print(self.name,"runs")

class dog(Animal):
    def __init__(self,name,breed):
        super().__init__(name)
        self.breed=breed
    
    def color(self,c):
        self.c=c
        print(self.name,"is",self.breed,"looks in ",self.c,"color")

class cat(Animal):
    def __init__(self,name,color):
        super().__init__(name)
        self.color=color
    
    def food(self,f):
        self.f=f
        print(self.name,"is in",self.color,"Likes",self.f)
        
obj=dog("Jimmy","Golden retriever")
print(obj.name)
print(obj.breed)

obj.color("Golden")

obj1=cat("Roxy","Black")
print(obj1.name)
print(obj1.color)

obj1.food("fish")'''

#polymorphism

#Method Overriding

'''class vehicle():
    def ride(self,name):
        self.name=name
        print(self.name,"ride on road")

class Car(vehicle):
    def ride(self,name):
        print(name," rides on road")

class Bike(vehicle):
    def ride(self,name):
        print(name,"rides on road")
        
obj=Car()
obj.ride("BMW")

obj=Bike()
obj.ride("Unicorn")'''

#Encapsulation

#it hides the implementation details of an object from outside the world

'''class BankAccount:
    def __init__(self,acno,bal):
        self.__acno=acno
        self.__bal=bal
    
    def get_bal(self):
        return self.__bal
    
    def deposit(self,amount):
        self.amount=amount
        self.__bal+=amount
        return self.__bal
    
    def withdraw(self,wa):
        self.wa=wa
        self.__bal-=wa
        return self.__bal
Atm=BankAccount(12345,2000)

print(Atm.deposit(200))
print(Atm.withdraw(500))
print(Atm.get_bal())'''

#Abstraction

#here we hide the implementation details and shows the neccesary information to the world
#we hide the details by using double underscore (__)

'''class coffeeMachine:
    def make_coffee(self):
        self.__heat_water()
        self.__mix_coffee()
        return "Coffee is ready"
    
    def __heat_water(self):
        self.__water_temp=100
        return "water is heated"
        
    def __mix_coffee(self):
        self.__cof_sol=20
        return "Cofee mixed"
    
cm=coffeeMachine()
print(cm.make_coffee())'''



