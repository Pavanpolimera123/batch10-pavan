'''
# ! Eg:3
def profile(name,age,place):
    txt ="My name is{}.Iam{}years old. Iam from{}."
    print(txt.format(name,age,place))
profile("pavan", "21", "mydukur")

# ! Eg:4
# ? Function with return statement

# 1.) A variable declared inside the function can be accessed outside the function
#using return
#2.) return does not prrint anything
#3.) we cannot write any code below return statement


def f1(a,b):
    c = a*b
    return c
# print(f1(6,8))
obj = f1(6,8)
obj1 = f1(4,6) 


def gracemark(object):
    print(object+4)
gracemark(obj)    
gracemark(obj1)

# 123
def palindrome(n):
    string = str(n)
    rev = str(n)[::-1]
    if string==rev:
        print(n, "palindrome")
    else:
         print("not palindrome")
a = int(input("Enter the value: "))
palindrome(a)

# ? based on the declaration of parameter and args
# ? functions are divided in to catageries
#Positional args
#keyword args
#default args
#variable length args
# keyword variable length args
# Positional args   

# * positional args
# Eg:1
def profile(name, phone, mark):
    txt = "my name is {}. My phone number is {}.I got {} marks."
    print(txt.format(phone, name, mark))
profile(9876543210, "pavan", 97) # unexpected output

# * key args
# ! Eg;1
# ? overcome the disadvantage of position args, we use keyword args

# todo ----> Exception of keyword args function
def profile(name, phone, mark):
    txt = "My name is {}. My phone number is {}. I got {} marks."
    print(txt.format(name,phone, mark))

# profile(name="pavan", "8978140742", mark=98) # error -> positional args folloe keywordargs
# pofile(789456123, name"pavan", mark=98) # error --> name has multiple values
profile("pavan",mark=98, phone=789456123)

# profile("pavan", 8978140742)
def profile(name, phone):
    txt = " my name is {}. my phone number is {}."
    print(txt.format(name, phone))

profile("pavan",9010619495)

Problem Statement - Given a string S(input consisting) of ‘*’ and ‘#’. 
The length of the string is variable. The task is to find the minimum number of ‘*’ 
or ‘#’ to make it a valid string. The string is considered valid if the number of ‘*’ 
and ‘#’ are equal. The ‘*’ and ‘#’ can be at any position in the string.
Note : The output will be a positive or negative integer based on number of ‘*’ 
and ‘#’ in the input string.


(*>#): positive integer
(#>*): negative integer
(#=*): 0
Example 1:
Input 1:

###***   -> Value of S
Output :

0   → number of * and # are equal




# ! Exception
def profile(name, phone, place="Kadapa"): # error --> because default args should not follow positional param
   if place == "kadapa" or place=="kADAPA" or place=="Kadapa":
     txt="My name is{}. My phone number{}. I got{} marks{}."
     print(txt.format(name,phone,place))
   else:
        print("You are not eligible to Signup")
profile("pavan",9876543210)


# * variable length params
# ! Eg:1
#To pass more then 1 arg to a paremeter means we use variable length args
# To convert normal paremeter to variable length param, add to ther prefix of param

#name="pavan", " hareesh ", " sadugudu "
#print(name)


def profile(*name):
    for val in name:
        print(" My name is",val)
profile("pavan", 'hareesh', 'basha')


# ! Eg:2
def profile (*name, age):
    for val in name:
        print("My name is ",val,"my age is ",age)
profile("pramod", 'name2', 'name3', 26) # error --> age has no args

        
# * keyword variable length args
# ! Eg:1
def price(**price_list):
    print(price_list)

price(shirt=1000, iphone=80000)

d1 = {"a":100, "b":200, "c":300}
d1 = dict(a=100, b=200, c=300)
print(d1)


# n = 5
# {1:1, 2:4, 3:9, 4:16, 5:25}

n = int(input("Enter the number: "))
d1 = {}
for val in range(1, n+1):
    d1[val] = val**2
print(d1)



# n = int(input("Enter the number: "))

d1 = {}
for val in range(1, n+1):
    d1[val] = val**2
print(d1)
# dictl(5)

# ! ----------> object oriented programming
# the paradigms of objects oriented programming are

# class
# objects
#inheritance
#polymorphism
#abstraction
# encapsulation

# ! class is a blue print of an object
# l1 = [1,2,3,4,5,6]

# Eg:2
class c1:
    name1 = "pavan"
    print(name1)
'''


# c = person() # c as object
# The name of creation of an object is called as method
# print(c.name)
    
# ? Eg:3
# create of a method
# when the function is created with a class is called as method

class person:
    def display(method): 
        print("Hello welcome to classes")


p = person()
p.display()

# ? Eg:4
# ! Method with parameter
class person:
    def display(person, name, age):
        print(name,age)
p = person()
p.display("pavan", 21)

# ? Eg:5
class person:
    fname = "pavan" #attribute or static variable
    lname = "p"
    
    def first_name(self):
        print(self.fname)


    def full_name(self):
        print(self.fname+" "+self.lname)

    
p = person()
p.first_name()
p.full_name()


# ? Eg:6
# constructers ---> __init__()
# This is a special method which has the ability to excute iotself without
# calling it manually through the process of instantiation

class profile:    
    def __init__(self):
        print("hey")

        
p = profile() # throught this process
p.__init__()


#1.) Write a Python script to generate and print a dictionary that #contains a number (between 1 and n) in the form (x, x*x). Sample Dictionary (n=5): # Expected Output (1:1, 2:4, 3:9, 4: 16, 5:25)
#2.) Find the uncommon words from 2 strings
##s1 "Hello how are you"
#52 "Hello how is"
#3.) Wrire a code print the 8th fihanochi number








































