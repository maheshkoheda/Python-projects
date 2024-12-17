#strings
str= "mahesh"

print (str[0])
print (str[0:4])
print (len(str))
y=str.capitalize()
print (y)
#Lists
list= ["mahesh", "John","Smith", 85]
print (list[1])
print (list[1:4])
list.append(6)
list.remove("John")
print (list)
#Tuples
tup = (87, 64, 33, 95, 76) #tup[0], tup[1]..
#tup[0] = 43 #NOT allowed in python since immutable
tup1 = ( )
tup2 = ( 1, )
tup3 = ( 1, 2, 3 )
print (tup[1])
#dictionaries
dict = {
    "name" : "Mahesh",
    "age": 34,
    "marks" : [1,2,3]
    
}
print (dict.keys())
print (dict.values())
print (dict["name"])
dict.update({"Score" : 89})
print (dict)

#while condition :
#some work
#Break : used to terminate the loop when encountered.take search example& stop the search when found

#Continue : terminates execution in the current iteration & continues execution of the loop with the next iteration
list1 = [1,2,6]
for el in list1:
    print (el)
    
#range(start?,stop,step?)
for e in range(100,105,2) :
    print (e)
    
#functions syntax 
#def func_name(param1, param2..): 
#    work
#    return val
#func_name(arg1, arg2..)

def sum(a,b):
    s =a+b
    return s

print(sum(2,3))

##
def fact(n):
    if(n ==1 or n ==0 ):
        return 1
    return fact(n-1) * n

print(fact(38))

#OOPS with objects and classes for reducing redundancy and increase reusability
#class is a blueprint of objects

class Student:
    name = "karan"
    
#create objects or instance
s1 = Student()
print (s1)
print (s1.name)

#All classes have a function called _init_() which is always executed when object is initiated.
#self parameter is reference to current instanc of class and used to access variable that belong to class
class Student:
    def __init__(self, fullname):
        self.name = fullname
        print ("adding new student in database..")
        
    
s1 = Student("karan")
print (s1.name)

s2 = Student("mahesh")
print (s2.name)
###
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
        print ("adding new student in database..")
        
    
s1 = Student("karan", 89)
print (s1.name, s1.marks)

s2 = Student("mahesh", 92)
print (s2.name, s2.marks)
##
class Student:
    college_name = "MVSR"
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
        print ("adding new student in database..")
        
    
s1 = Student("karan", 89)
print (s1.name, s1.marks)

s2 = Student("mahesh", 92)
print (s2.name, s2.marks)

print (s2.college_name)
#If defined in both class and object then object precedence is high than class, so object name is printed

#Methods are functions that belong to objects. we can use @property on methods to use them as properties.
#Example creating a method to averga the marks
class Student:
    college_name = "MVSR"
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
        print ("adding new student in database..")
    
    def get_average(self):
        sum =0
        for val in self.marks:
            sum +=val
        print("hi", self.name, "your average score is : ", sum/3)  
    
s1 = Student("karan", [89,90,87])
print (s1.name, s1.marks)
s1.get_average()

s2 = Student("mahesh", 92)
print (s2.name, s2.marks)

print (s2.college_name)

#static methods dont use self parameter and they work at class level
#Decorators changes the behaviour of normal function using @staticmethod
#Abstraction- showing essential features and hiding implementation details
#Encapsulation - wrapping data and objects into single unit.

#Below is abstraction
class Car:
    def __init__(self):
        self.acc = False
        self.brk = False
        self.clutch = False
        
    def start(self):
        self.clutch = True
        self.acc = True
        print("car started..")
        
car1 = Car()
car1.start()

#
class Account:
    def __init__(self, balance, AccountNo):
        self.balance = balance
        self.AccountNo = AccountNo
        print ("adding new account in database..")
    
    def debit(self, amount):
        self.balance -= amount
        print("Hello", self.AccountNo, "your account is debited with : ", amount)  
        print("Hello", self.AccountNo, "your new total balance : ", self.getbalance()) 
        
    def credit(self, amount):
        self.balance += amount
        print("Hello", self.AccountNo, "your account is credited with : ", amount)  
        print("Hello", self.AccountNo, "your new total balance : ", self.getbalance()) 
        
    def getbalance(self):
        return self.balance  
    
s1 = Account(10, "176xx2")

s1.debit(5)
s1.credit(15)
s1.getbalance()

s2 = Account(10000, "78YxxZ2")
s2.debit(543)
s2.credit(134)
s2.getbalance()

#To make attributes private just use __ this will not make them accessible outside class to protect sensitive info like passwords
#Inheritance-One class derives the properties & methods of another class(parent/base)
class Car:
    @staticmethod
    def start():
        print("car started..")
    @staticmethod
    def stop():
        print("car stopped..")
    
class Toyotacar(Car):
    def __init__(self, brand):
        self.brand = brand
        
class Fortuner(Toyotacar):
    def __init__(self, type):
        self.type = type
        
car1 = Fortuner("diesel")
car1.start()
##
#since @staticmethod cant access or modify class state  and general for utility we use @classmethod.

#Polymorphism- when same operator is allowed to have different meaning per context.
print(1+2) #3
print ("Apna"+"college") #concat
