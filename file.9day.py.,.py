# 1.) Write a Python script to generate and print a dictionary that 
# contains a number (between 1 and n) in the form (x, x*x).
# Sample Dictionary ( n = 5) :
# Expected Output : {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

# 2.)Find the uncommon words from 2 strings

# # s1 = "Hello how are you"
# s2 = "Hello how is"

#s1= "Hello how are you"
#s2="Hello how is"

#s1=s1.split(" ")
#s2=s2.split(" ")

#for val in s1:
#    if val not in s2:
#        print(val)
#for val in s2:
#    if val not in s1:
#        print(val)

# 3.)Wrire a code print the 8th fibanochi number
# 0, 1, 1, 2, 3, 5, 8

# n1 = 0
# n2 = 1
# ans = 0+1 =1

# n1 = 1
# n2 = 1
# ans = 1+1 =2

# n1 = 1
# n2 = 2
# ans = 1+2 =3

# n1 = 2
# n2 = 3
# ans = 2+3 =5

# num = 8
# n1 = 0
# n2 = 1

# for val in range(5):
#    ans = n1+n2
#     print(ans)
#     n1 = n2
#     n2 = ans
# print(ans)

# ! constructors
# ? eg:2

#unparametarised constructor
#class profile:
#    def _init_ (self):
#        print("hello world")
#obj =profile()
#obj._init_()

#Problem Statement -: A taxi can take multiple passengers to the railway station at the same time.On the way back to the starting point,the taxi driver may pick up additional passengers for his next trip to the airport.A map of passenger location has been created,represented as a square matrix.

#The Matrix is filled with cells,and each cell will have an initial value as follows:

#A value greater than or equal to zero represents a path.
#value equal to 1 represents a passenger.
#A value equal to -

# ? eg: 3
# * parametarised constructor
# class profile:
#       def_init_(self, id, name, age):
#            print(id, name, age)

# obj = profile(1, "sid", 29)

# ? eg:4
#class c1:
   # name = "sid"
   #place = "cbe"

#    def m1(self):
#        # name = "sid"
#       #place = "cbe"
#        print(self.name, self.place)

#object = c1()
#object.m1()

# ? eg:6
#class class1:
    # email = "babaafzal@gmail.com"           # static variable
#    def_init_(self):
#        self.name = "sid"
#        self.email = "babaafzal@gmail.com"
        # return name, email # error --> cannot use return with constructor

# ! Eg:2
#class c1:
#    def _init_(self):
#       print("Iam constructor from parent class")

#class child1(c1):
#    pass

#obj = child1()

# ! eg:3
#class parent:
#    name = "afzal"
          
# class child(parent):
#    name = "hero"

#    def display(self):
#        print(self.name)

 # d = child()
 # d.display()

# ! multilevel inheritance
# ? eg:1

# class voice:
#          def sound(self):
#              print("all the animals have there own voice")

#class dog(voice):
#    def dog_voice(self):
#        print("bark")

#class cat(dog):
#    def cat_voice(self):
#        print("meow")

#class parrot(cat):
#    def parrot_voice(self):
#        print("speak")

#all = parrot()
#all.dog_voice()
#all.cat_voicve()
#all.sound()
#all.parrot_voice()



 # ? Eg:2
#class honda city: I
#def honda_city_engine_specs (self, cc, Hp, torque, fuel_type, num_of_piston):
#print (cc, Hp, torque, fuel_type, num_of_piston)

#def honda_city_body_specs (self, color, weight, height, length, vehicle_type):
#print(color, weight, height, length, vehicle_type)

#class amaze (honda_city):
#def amaze_engine_specs (self, cc, Hp, torque, fuel_type, num_of_piston):
#print (cc, Hp, torque, fuel_type, num_of_piston)

#def amaze_body_specs (self, color, weight, height, length, vehicle_type):
#print(color, weight, height, length, vehicle_type)

#class Honda(civic):
#    pass

#honda = Honda()
#honda.honda_city_engine_specs(1500, 230, 2979, "petrol", 4)
#honda.civic_body_specs("white", 2000, 5.5, "Hatchback")

# Multiple Inheritance
 #? It has multiple parent and 1 child
#class while_pertol:
#    def function_w(self):
#        print("used to Airplans")

#class Organic_petrol:
#    def function_o(self):
#        print("used for Bike, cars")
        
#class premium_petrol:
#  def function_p(self):
#        print("spots cars, bikes")
        
#class petrol(while_pertol, Organic_petrol, premium_petrol):
#  def defanition(self):
#         print("Petrols types")
        
#p=petrol()
#p.defanition()
#p.function_o()

# ! Eg:2
# MRO --> Method resolution Order
#class addition:
#    def add(self, a, b):
#        print(a+b)
        
#    def mul(self, a, b):
#        print(a%b)
        
#class subract:
#    def sub(self, a, b):
#        print(a-b)
#class multiply:
#    def mul(self, a, b):
#        print(a*b)
#class division(addition, subract, multiply):
#    def div(self, a, b):
#        print(a/b)
        
#calc = division() 
# calc.add(3, 4)
#calc.mul(4, 2)

# heirarichal Inheritance
# ! Heirarical inheritance
#class catagory:
#    def weight(self,weight):
#        print("weight")
#    def display(self,color,taste):
#        print(color,taste)
#class Tomato(catagory):
#    def tomato_specs(self):
#        color="black"
#        taste= "neutral taste"
#        self.display(color,taste)
#class carrot(catagory):
#    def carrot_specs (self):
#        color="green"
#        taste= "sweet"
#        self.display(color,taste)
        
        
# c=Carrot()
# c.carrot_specs()
# c.weight("30gms")

# t=Tomato()
# t.tomato_spec()
# t.weight("20gms")

# hybrid Inheritance
 # The combination of above 4 inheritance is called Hybrid inheritance
# class c1:
#     def m1(self):
#         print("Class1")
# class c2(c1):
#     def m2(self):
#         print("class2")
# class c3(c2):
#     def m3(self):
#         print("Class 3")
        
#     def m4(self):
#         print("i am m3 from c4")
# class c5(c4):
#     def m5(self):
#         print("Class 5")
# class c6(c5, c3):
#     def m6(self):
#         print("Class 4")

# obj = c6()
# obj.m3()

# ! --------------> Polymorphism
# poly - many, morph --> form
# A function which has the ability to perform more than 1 functionality
# then  it is considered to be as polymorphism

# * Polymorphism in builtin functions
# len() --> which is used to find the length of list, tuple, dict etc...
# index()
# max()
# min()
# count()
# pop()
# and more...

# * Ploymorphism in operators
# +
# print(8+8)
# print("k"+"1")
# print([1,2,3]+[5,6])

# *
# print(6*7)
# l1 = {12,3,4,5,6}
# print(*l1)
# def f1(*args)
# l1 = [1,2,3,4]
# print(11*10)

