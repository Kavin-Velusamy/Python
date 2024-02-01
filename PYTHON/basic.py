
numbers = input("Enter 4 numbers without spaces: ")
total = 0
l= []

for digit in numbers:
    total += int(digit)
    l.append(int(digit))
print("Sum of the numbers:",total)
print("List of individual digits:",l)

# x=2123
# name='kavin'
# def add(x,name):
#     print('The sum is:',x+name)
    
# def Product(x,name):
#     print("The product is :",x*name)

##Basic of python

# int=3534654
# string="any value" (Double arrow mark)
# float=34.44     #decimal value
# List=["kavin","jai",123,34]    #list inside string
# set={'nivash','pravin','kavin'}
# Dictionary={'name':'kavin','age':19,'gender':'male'}
# Tuple=("kavin","pravin","nivash")
#boolean=true,false

#String=Tuple= immutable(we cannot change the value)
#List= mutable 

# Booleans

# a = 200
# b = 33
# if b > a:
#   print("b is greater than a")
# else:
#   print("b is not greater than a")           # b is not greater than a
# print(10>9)              # True
    

# string methods

# a = "Hello, World!"
# print(a[1])               # Ans :e             

# a = "Hello, World!"
# print(len(a))              #Ans: 13

# txt = "The best things in life are free!"
# print("free" in txt)          # True


# String Slicing 

# b = "Hello, World!"
# print(b[2:5])                   # Ans:llo

# b = "Hello, World!"
# print(b[-5:-2])                   Ans:rld


# Modify String

# a = "Hello, World!"              
# print(a.upper())                 # Ans:HELLO, WORLD!
# print(a.lower())                 #   Ans:hello, world!
# a = " Hello, World! "
# print(a.strip())                 #  Hello, World!            
# a = "Hello, World!"
# print(a.replace("H", "J"))       #  Jello, World!

# etc

# concatenate string

# a = "Hello"
# b = "World"
# c = a + b
# print(c)                         # Ans :HelloWorld

# a = "Hello"
# b = "World"
# c = a + " " + b
# print(c)                            #  Hello World

# Format string
# age = 36
# txt = "My name is John, and I am {}"
# print(txt.format(age))                  # My name is John, and I am 36



# Operators

# +   Addition	x + y	
# -	Subtraction	x - y	
# *	Multiplication	x * y	
# /	Division	x / y	
# %	Modulus	x % y	
# **	Exponentiation	x ** y	
# //	Floor division	x // y	
# Python Assignment Operators
# Assignment operators are used to assign values to variables:

# Operator	Example	Same As	Try it
# =	x = 5	x = 5	
# +=	x += 3	x = x + 3	
# -=	x -= 3	x = x - 3	
# *=	x *= 3	x = x * 3	
# /=	x /= 3	x = x / 3	
# %=	x %= 3	x = x % 3	
# //=	x //= 3	x = x // 3	
# **=	x **= 3	x = x ** 3	
# &=	x &= 3	x = x & 3	
# |=	x |= 3	x = x | 3	
# ^=	x ^= 3	x = x ^ 3	
# >>=	x >>= 3	x = x >> 3	
# <<=	x <<= 3	x = x << 3	
# Python Comparison Operators
# Comparison operators are used to compare two values:

# Operator	Name	Example	Try it
# ==	Equal	x == y	
# !=	Not equal	x != y	
# >	Greater than	x > y	
# <	Less than	x < y	
# >=	Greater than or equal to	x >= y	
# <=	Less than or equal to	x <= y	



# List

# thislist = ["apple", "banana", "cherry"]
# print(thislist)                            #   ['apple', 'banana', 'cherry']


# Changes item  LIST

# thislist = ["apple", "banana", "cherry"]
# thislist[1] = "blackcurrant"
# print(thislist)                         #  ['apple', 'blackcurrant', 'cherry']


# thislist = ["apple", "banana", "cherry"]
# thislist.insert(2, "watermelon")
# print(thislist)                          #  ['apple', 'banana', 'watermelon', 'cherry']


# Add item list

# thislist = ["apple", "banana", "cherry"]
# thislist.append("orange")
# print(thislist)                       # ['apple', 'banana', 'cherry', 'orange']
 
 
# thislist = ["apple", "banana", "cherry"]
# thislist.insert(1, "orange")
# print(thislist)                        #   ['apple', 'orange', 'banana', 'cherry']
 
 
# thislist = ["apple", "banana", "cherry"]
# tropical = ["mango", "pineapple", "papaya"]
# thislist.extend(tropical)
# print(thislist)                  # ['apple', 'banana', 'cherry', 'mango', 'pineapple', 'papaya']
 
 
# thislist = ["apple", "banana", "cherry"]
# thistuple = ("kiwi", "orange")
# thislist.extend(thistuple)
# print(thislist)                    # ['apple', 'banana', 'cherry', 'kiwi', 'orange']
 
 
# Remove item

# thislist = ["apple", "banana", "cherry"]
# thislist.remove("banana")
# print(thislist)                     #  ['apple', 'cherry']


# thislist = ["apple", "banana", "cherry"]
# thislist.pop(1)
# print(thislist)                  # ['apple', 'cherry']      
 
# thislist = ["apple", "banana", "cherry"]
# thislist.pop()
# print(thislist)                   # ['apple', 'banana']
 
 
# thislist = ["apple", "banana", "cherry"]
# del thislist[0]
# print(thislist)                     # ['banana', 'cherry']
 
# thislist = ["apple", "banana", "cherry"]
# del thislist                          # Empty


# thislist = ["apple", "banana", "cherry"]
# thislist.clear()
# print(thislist)                          # []

# Looping 

 
# thislist = ["apple", "banana", "cherry"]
# for i in range(len(thislist)):
#   print(thislist[i])

 
#  Sort the list

# thislist = [100, 50, 65, 82, 23]
# thislist.sort()                            # [23, 50, 65, 82, 100]
# print(thislist)


#  Join the list

# list1 = ["a", "b", "c"]
# list2 = [1, 2, 3]

# list3 = list1 + list2
# print(list3)                             # ['a', 'b', 'c', 1, 2, 3]
 
 
# list1 = ["a", "b" , "c"]
# list2 = [1, 2, 3]

# for x in list2:
#   list1.append(x)
# print(list1)                         #  ['a', 'b', 'c', 1, 2, 3]
 
 
# list1 = ["a", "b" , "c"]
# list2 = [1, 2, 3]
# list1.extend(list2)
# print(list1)                          #  ['a', 'b', 'c', 1, 2, 3]
 
 
 
#  Tuple 


# thistuple = tuple(("apple", "banana", "cherry"))
# print(thistuple)                      #  ('apple', 'banana', 'cherry')


# change tuple values
 
# x = ("apple", "banana", "cherry")
# y = list(x)
# y[1] = "kiwi"
# x = tuple(y)
# print(x)                            # ('apple', 'kiwi', 'cherry')

# Add items

# thistuple = ("apple", "banana", "cherry")
# y = list(thistuple)
# y.append("orange")
# thistuple = tuple(y)

# print(thistuple)                   #  ('apple', 'banana', 'cherry', 'orange')

    
# thistuple = ("apple", "banana", "cherry")
# y = ("orange",)
# thistuple += y

# print(thistuple)                     #   ('apple', 'banana', 'cherry', 'orange')
    

# Remove items


# thistuple = ("apple", "banana", "cherry")
# y = list(thistuple)
# y.remove("apple")
# thistuple = tuple(y)
# print(thistuple)                        # ('banana', 'cherry')
    
# Looping

# thistuple = ("apple", "banana", "cherry")                 #Ans:  apple
                                                            #     banana
                                                            #     cherry
# # for x in thistuple: 
#   print(x)


# i=1
# while i<10:
#     print(i)
#     if i==6:
#         break;
#     i+=1
    
    
# While loop

# thistuple = ("apple", "banana", "cherry")
# i = 0                                                   # apple
# while i < len(thistuple):                                # banana
#   print(thistuple[i])                                     # cherry
#   i = i + 1



# Dictionary
 
 
# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# print(thisdict["brand"])                  # Ford
 
 
# thisdict = dict(name = "John", age = 36, country = "Norway")
# print(thisdict)                       #  {'name': 'John', 'age': 36, 'country': 'Norway'}
 
   
   
# car = {
# "brand": "Ford",
# "model": "Mustang",
# "year": 1964
# }
# x = car.keys()
# print(x) #before the change
# car["color"] = "white"
# print(x)                       #dict_keys(['brand', 'model', 'year'])
                                   # dict_keys(['brand', 'model', 'year', 'color'])



# car = {
# "brand": "Ford",
# "model": "Mustang",
# "year": 1964
# }
# x = car.values()
# print(x) #before the change
# car["year"] = 2020
# print(x)                         #  dict_values(['Ford', 'Mustang', 1964])
# #                                    #  dict_values(['Ford', 'Mustang', 2020])#           

# car = {
# "brand": "Ford",
# "model": "Mustang",
# "year": 1964
# }
# x = car.items()
# print(x) #before the change
# car["year"] = 2020
# print(x)                         # dict_items([('brand', 'Ford'), ('model', 'Mustang'), ('year', 1964)])
#                                    # dict_items([('brand', 'Ford'), ('model', 'Mustang'), ('year', 2020)])

# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# if "model" in thisdict:                  # Yes, 'model' is one of the keys in the thisdict dictionary
#   print("Yes, 'model' is one of the keys in the thisdict dictionary")


# thisdict =	{
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# thisdict["year"] = 2018
# print(thisdict)                           # {'brand': 'Ford', 'model': 'Mustang', 'year': 2018}


# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# thisdict.update({"year": 2020})
# print(thisdict)                          # {'brand': 'Ford', 'model': 'Mustang', 'year': 2020}

# Add item

# thisdict =	{
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# thisdict["color"] = "red"
# print(thisdict)                           # {'brand': 'Ford', 'model': 'Mustang', 'year': 1964, 'color': 'red'}


# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# thisdict.update({"color": "red"})
# print(thisdict)                          #  {'brand': 'Ford', 'model': 'Mustang', 'year': 1964, 'color': 'red'}

# thisdict =	{
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# thisdict.pop("model")
# print(thisdict)                           # {'brand': 'Ford', 'year': 1964}


# Delete item

# thisdict =	{
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# thisdict.popitem()
# print(thisdict)                         # {'brand': 'Ford', 'model': 'Mustang'}

# thisdict =	{
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# del thisdict["model"]
# print(thisdict)                           # {'brand': 'Ford', 'year': 1964}


# thisdict =	{
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# thisdict.clear()
# print(thisdict)                           #  {}
# 


# thisdict =	{
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# del thisdict["model"]
# print(thisdict)                    #   {'brand': 'Ford', 'year': 1964}


# Nested loop  Dictionary

# myfamily = {
#   "child1" : {
#     "name" : "Emil",
#     "year" : 2004
#   },
#   "child2" : {
#     "name" : "Tobias",
#     "year" : 2007
#   },
#   "child3" : {
#     "name" : "Linus",
#     "year" : 2011
#   }
# }
                    #Ans:  {'child1': {'name': 'Emil', 'year': 2004}, 'child2': {'name': 'Tobias', 'year': 2007},
                    #    'child3': {'name': 'Linus', 'year': 2011}}
# print(myfamily)



# sets

# thisset = {"apple", "banana", "cherry", "apple"}
# print(thisset)                         # {'banana', 'apple', 'cherry'} 


# Add set item

# thisset = {"apple", "banana", "cherry"}

# for x in thisset:
#   print(x)                                 # apple
                                            # banana
                                            # cherry
  
# thisset = {"apple", "banana", "cherry"}
# thisset.add("orange")
# print(thisset)                             # {'cherry', 'orange', 'banana', 'apple'}
 

# thisset = {"apple", "banana", "cherry"}
# tropical = {"pineapple", "mango", "papaya"}
# thisset.update(tropical)
# print(thisset)                       # {'apple', 'mango', 'cherry', 'pineapple', 'banana', 'papaya'}            




# thisset = {"apple", "banana", "cherry"}
# mylist = ["kiwi", "orange"]
# thisset.update(mylist)
# print(thisset)                        # {'banana', 'cherry', 'apple', 'orange', 'kiwi'}                    


# Remove set item

# thisset = {"apple", "banana", "cherry"}
# thisset.remove("banana")
# print(thisset)                               # {'apple', 'cherry'}


# thisset = {"apple", "banana", "cherry"}
# thisset.discard("banana")
# print(thisset)                              # {'cherry', 'apple'}


# thisset = {"apple", "banana", "cherry"}
# x = thisset.pop()
# print(x) #removed item
# print(thisset) #the set after removal             #  cherry
                                                   # {'apple', 'banana'}


# thisset = {"apple", "banana", "cherry"}
# thisset.clear()
# print(thisset)                                  # set()


# If else

# a = 200
# b = 33
# if b > a:
#   print("b is greater than a")
# elif a == b:
#   print("a and b are equal")
# else:
#   print("a is greater than b")             #  a is greater than b

# While Loop

# i = 1
# while i < 6:
#   print(i)
#   i += 1                         #  1 2 3 4 5              

# i = 1
# while i < 6:
#   print(i)
#   if i == 3:
#     break
#   i += 1                     #   1 2 3 

# i = 0
# while i < 6:
#   i += 1
#   if i == 3:
#     continue
#   print(i)                 # 1 2 3 4 5 6


# Looping

# fruits = ["apple", "banana", "cherry"]
# for x in fruits:                      #   apple
                                        #    banana
                                        #  cherry
#   print(x)                            


# fruits = ["apple", "banana", "cherry"]
# for x in fruits:
#   print(x) 
#   if x == "banana":                  #   apple
#                                     #   banana
#     break


# fruits = ["apple", "banana", "cherry"]
# for x in fruits:
#     if x == "banana":
#         break
#     print(x)                    #    apple


# Range Function

# for x in range(6):
#   print(x,end= " ")               #  0 1 2 3 4 5


# Function

# def my_function(*kids):
#   print("The youngest child is " + kids[2])
# my_function("Emil", "Tobias", "Linus")              #   The youngest child is Linus


# def my_function(**kid):
#   print("His last name is " + kid["lname"])
# my_function(fname = "Tobias", lname = "Refsnes")        # His last name is Refsnes


# def my_function(food):
#   for x in food:
#     print(x)
# food = ["apple", "banana", "cherry"]
# my_function(food)


# def my_function(x):
#   return 5 * x
# print(my_function(3))
# print(my_function(5))
# print(my_function(9))                   #  15 25 45


# # Inside function Argument or parameter

# def my_function(fname, lname):
#   print(fname + " " + lname)

# my_function("Emil", "Refsnes")                    # Emil Refsnes




# Time complexity

# # Big 0 notation
# 0(1)  constant 
# 0(n)  Linear 
# 0(logN)  lograthmic
# 0(NlogN)  Linear lograthmic
# 0(n^2)  Quadratic
# 0(n^3)
# 2^n

# omega 
# Theta


# # 0(1)  It will print Exactly 10 'Hi' so it is constant term
# print("Hi")
# print("Hi")
# print("Hi")
# print("Hi")
# print("Hi")

# a=2
# b=20
# c=a+b
# print(c)
# print(2+20)

# l=[1,2,3,4,5]
# a=2
# print(l[0])
# print(l[1])



# # 0(n) The length of the list is n numbers 
# ,so it is o(n)

# l=[1,2,3,4,5]
# for i in l:
#     print(i)
# print(l)

# Best case  (It shows at fist itself)
# Average case   (It shows at middle)
# wrost case    (it shows at last)

# l=[1,2,3,4,5,]
# for i in l:
#     if i==2:
#         print("True")
#         break


# 0(logN) 


# 0(NlogN)  Merge sort



# 0(n^2)

# l=[1,2,3,4,5]
# for i in l:
#     for j in l:
#         print(i,j)
    






##variable 

# print ("hello world")    # print()- inbulit function
# name="kavin22012004"     # name= variable (we can store the values)  # string ("set of character")-command 
# print("Hi" + name)
# name="john" 
# print ("hi",name )
# price=45
# amount=34.5             #float value
# child = False           #booleam
# print(child)
# print(price)


###string handling

# code="python learning"
# work="'string'"
# name="in github"
# print(work)     
# # print(code.upper())         # fully captial letter 
# print(code.lower())         #fully small letter
# print(code.capitalize())    #first letter capital
# print(code.title())         #firat letter and space after the letter is capital
# print(code +" " + name + work)   #connecting the words or numbers
# print(code+" "+name)        #space of the words
# print("python \nlearning")    #this will print in next line
# print("python \t learning") #giving the the double space of the words
# print(code.isupper())        #if all the letter is upper(true)
# print(code.islower())        #if all the letter is lower ()
# print(len(code))             #finding the index of the word
# print(code.find("n"))        #finding the letter (n)
# print(code.count("n"))      #counting the letter (n)
# print(code.replace("a","s")) #replacing the words
# print(code.isalpha())        #finding all the the letter is alpha letter
# print(code.isdigit())
# print(code*5 )              


# ## multiple assignment in single line

# name,age ,weight="kavin",19,52    #types of variable in one line
# print(weight)
# like=dislike=65
# print(dislike) 
# print(like/dislike)
# print(like*dislike)


###Type casting

#otp=3252363
#otp=str(otp)     #type casting
#print("Your otp is" + str(otp))
#print(type(otp))
#count,number=199,"199"
#print(count+1)
# #count="199"
# print(number+"1")

##Assignment 1
# name="Anand"
# leave="15 days"
# year=2021
# print(name,leave,year)

###Assignment 1               #This is correct method
###Dear Anand,
###You have 15 days of Leave Balance for this
###Year(2021)
# name, leave, year ="Anand",15,2021
# print("Dear " + name + ",\nYou have " + str(leave) + " days of Leave Balance for this\nYear("+ str(year)+")")

# name, leave, year ="Anand",15,2021      #### this code is space error beacuse of (,) this  kama
# print("Dear " , name , ",\nYou have " , str(leave) , " days of Leave Balance for this\nYear(", str(year),")")


### Getting the input from the user

# name=input(" Enter your name:")
# print("Hello"+ name)
# height=float(input("Enter the height:"))
# print(type(height))
# height="{:.4f}".format(height/2.54)     ##{} this is for after the float value, 2 digit {:.2},4 digit {:.4}
# print("Your height is "+ str(height) + "cm")
# #print("Your are " + str(height/2.54) + "inches")
# print("Your are " + height + " inches tall")


###Assignment 2
 
# ## Get user input
# ## Name,Email ID and phone number.print the information like this
# ##  ****************************
# ##  UserName: XXXXX
# ##  Email   : XXXXX
# ##  ph      : XXXXX
# ##  ***************************

# Name=input("Enter the name : ")
# Email=input("Enter the email id :")
# Phoneno=input("Enter the Phone Number :")
 
# print("*****************************")

# print("UserName:",Name)
# print("Email :",Email)
# print("Ph :",Phoneno)

# print("*****************************")


# ## This is another type of code 
# ## Assignment 2

# Name=input("Enter the name : ")
# Email=input("Enter the email id :")
# Phoneno=input("Enter the Phone Number :")

# print("*****************************")

# print("UserName :" + Name + "\n   Email :" + Email + "\n      Ph :" + Phoneno )

# print("*****************************")


### Math operation

# a=20
# b=10
# print(a+b , a-b , a*b , a/b , a/50 , b/30 , (a+b)*40 , a+b*30)      ##give output in float (/) division
# print(10/2 , 20*3)
# a=23.5
# print(round(a))      # round is the absolute correct answer
# a=-5
# print(abs(a))        # ABS is the absolute value of a
# a=5
# print(abs(a))
# print(pow(a,4))      # pow is the power of a
# print(a**4)          # this is another mothod of power term
 
# a=55
# b=32
# print(max(a,b))       # maximum value of a,b
# print(min(a,b))       # minimum value of a,b
 
# import math  # math module
# a=45.6
# print(math.ceil(a))    # ceil is the decimal value of a=5
# print(math.floor(a))   # floor is the decimal value of a=4
# print(math.factorial(9))   # factorial of 9
# a=6
# print(a%2)       # it will find the remainder
# print(a%5)
# print(a%9)

### Assignment 3

## Get user input 
## Get the number n fron user.compute and print the follwoing values
## 1.log2(n)
## 2.cos(n)
## 3.e**n

# # print(math.log2(16))
# # print(math.cos(16))
# # print(math.e**16)
# m=input("User input :")
# n=int(m)
# print("1.",int(math.log2(n)), "2.",int(math.cos(n)),"3.",int(math.e**n))


 ### If Else (true/False)conditional 
 
# pwd_correct= True
# if pwd_correct:        #conditional statement
#     print("logged in")
# else:
#     print("incorrect pwd")

## Relational operator

# num=35
# if num<30:            # < lower number           #  == is it equal
#     print("true")     # > higher number          #  != is it not equal
# else:                 # <= same number or lower number
#      print("false")   # >= same number or higher number 

# num=14
# if num%5==0:       # it is divisible by 5 means ,print true
#     print("Multiple of 10")
# else:
#     print("Not multiple of 10")

##Elif ladder

# ind_score=150
# if ind_score>=150:
#     print("india won")
# elif ind_score>=100:
#     print("pak win")
# elif ind_score>=90:
#     print("Aus win")
# else:
#     print("jap win ")

## Nested if

# #check if the number is three digit number                      # A     B    And       OR     NOT
# #logical operation -and (or) or      # this method is 'and'
#                                                                  T     T     T        T       0 = 1
# num= int(input("Enter the number :"))                          # T     F     F        T       1 = 0
# if num>99 and num<1000 :                                       # F     T     F        T
#     if num%2==0:                                               # F     F     F        F
#         print(str(num),"is the three digit number")
# else:
#     print(str(num) ,"is not a three digit number")  

##This method is OR
# name="kavin"
# if name[0]=="k" or name[0]=="K":
#     print("the name starts with s")


###Bitwise operator
## And , OR , Not , Exor , Leftshift , Rightshift
#  left shift                                                 # Exor
#  00001100 12<<1    it will leave the first no                  # a^b
#  00011000 =24                                                  #  0 0 =0
# Right shift                                                    #  1 0 =1
# 00001100   12>>1                                               #  0 1 =1
# 00000110 = 6                                                   #  1 1 =0


###String slicing

# name="kangani patti"
# print(name[9])              #this will print the index value
# print(name[0:7])
# print(name[2:11])
# print(name[1:12:2])       # this will print one after another value
# print(name[-4])          # this will print in back side
# print(name[::-1])
# print(name[2:-2])
# x=slice(2,-2)
# print(name[x])

####Assignment 4
#str="Happy"
# H                 y
# Ha                py
# Hap               ppy
# Happ              appy
# Happy             Happy

# print("H          "+"y")
# print("Ha         "+"py")
# print("Hap        "+"ppy")
# print("Happ       "+"appy")
# print("Happy      "+"Happy")
# str="Happy"
# print(str[0])
# print(str[:2])
# print(str[:3])
# print(str[:4])
# print(str[:5])
# print(str[-1])
# print(str[-2:])
# print(str[-3:])
# print(str[-4:])
# print(str[-5:])


###List

# cities=["chennai","madurai","thricy" ,"coimbatore","salem"  ]
# val=[1,5,8,5,4,7]
# list=["salem",3 ,"namakkal"]
# print(list[2])
# print(val[4])
# print(cities[3])
# print(cities[:4])
# print(val[-4])
# print(cities)
# cities[2]="Thrichy"         # this will change the letter
# print(cities)      
# cities.append("sivakasi")    #inserting the element in last
# print(cities)
# cities.insert(2,"karur")     # inserting the element inside the place
# print(cities)
# delete=cities.pop()         # this will delete the last element and also say which element is deleted
# print(delete,"has been deleted")
# print(cities)
# del cities[2]             #this will delete the element
# print(cities)
# cities.remove("salem")   # we are giving the place to delete
# print(cities)
# print(sorted(cities))    # this will print in accending order
# print(sorted(val))
# cities.sort()         # this is also sorting  
# print(cities)
# cities.reverse()
# print(cities)       #  we can find how many value in list 
# print(len(cities))


###While Loop

# letter=' '
# while letter.isalpha():
#  letter= input("enter the alphabet:")
# print("You have entered "+letter)

##To print 1 t0 100
# num=0
# while num<=99:
#   num+=1
#   print(num,end=',')


### For loop

# for i in range (1,100):
#     print(i,end=',')

# list=[22,456,34234,566,345]
# for i in list:
#     print(i*i)

# string=(2,35,"kavin",34,556)
# for i in string:
#     print(i)


### simple Game
### I am chossing the number below 10
### reandomly I am chosing any number
### its correct it will print
### its wrong try again

# import random
# n=input("enter the limit:")
# num=random. randint(1,10)
# guess=int(input("can u guess the no I am thinking "))
# while num!=guess :
#     if len(guess)==0:
#         print("list is full")
#     if guess>num:                                                              ### dout
#         print("your guess is higher")
#     else:
#         print("your guess is lower")
#         guess=int(input("try again :"))
# print("you won") 


### Assignment 

##1.Get input number n from user. print all the factor of n
##2. Get a list of to do task from the user and add it to a to_do list.print the list
##3.Given an array of intrgers.find a peak element in it .An array element is the peak if it is NOT samller than its neighbours.
## For corner element ,we need to consider only one neighbour.  Eg in..[3,4,6,7,5] -7 is a peak element.
##4.List=[3,4,5,-2,-1,2,8,0,-4].Move all negative number to the end of list.





