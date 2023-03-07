
# # constructor is a init function
# # method 
# # variable
    

# # # creating multiple object in simple program


# # class student :
# #     def __init__(self,n,o):
# #         self.name=n
# #         self.no=o


# class student :
#     def __init__(self,n,o):
#         self.name=n
#         self.no=o
        
#     def details(self):
#         print("my name is",self.name)
#         print("my no is",self.no)
    
    
# print('*'*20)
# s=student ('erevv',34)
# s.details()
# print(s.name,s.no)        # outside of instance variable

# print('*'*20)
# s2=student('eiopov',2354)
# s2.details()
# print('*'*20)

# s3=student('egdfbh',24)
# s3.details()
# print('*'*20)





# class student:
#     def __init__(self):
#         print(id(self))
        
        
#     @staticmethod
#     def findavg(x,y):
#         print("Average",(x+y)/2)
        
         
# s=student()
# # print(id(s))
# s.findavg(10,20)



# # instance variable
# class student:
#     def __init__(self,n,o):
#         self.name=n
#         self.no=o
        
#     def info(self):
#         self.mark=49
#         x=45                             # local variable
        
# s=student("ferfc",24)
# s.info()       
# s.a=10
# print(s.__dict__)



# # delete the self variable and object reference



# class cs:
#     def __init__(self):
#         self.a=12
#         self.b=3
#         self.f=4
        
#     def delete (self):
#         del self.a
#         del self.f
        
# s=cs()
# print(s.__dict__)
# print('*'*20)

# s.delete()
# print(s.__dict__)
# print('*'*20)

# del s.b
# print(s.__dict__)
# print('*'*20)





# class cs:
#     def __init__(self):
#         self.a=12
#         self.b=3
#         self.f=4
        
#     # def delete (self):
#     #     del self.a
        
# s=cs()  
# s1=cs()
# print(s.__dict__)
# print('*'*20)
# del s.b
# print(s.__dict__ )
# print('*'*20)
# del s1.a
# print(s1.__dict__ )





# class cs:
#     def __init__(self):
#         self.a=12
#         self.b=3
#         self.f=4
        
# s=cs()
# s1=cs()
# s.a=35435
# s1.f=7688
# print(s.a,s.b,s.f)
# print(s1.a,s1.b,s1.f)


# class test:
#     a=10                      # static variable     
#     def __init__(self):
#         test.a=20
        
#     @classmethod
#     def m1(self):
#         self.a =30
#         test.a=40
        
        
#     @staticmethod
#     def m2():
#         test.a=50
    
    
    
# t=test()
# t.m1()
# t.m2()
# t.a=60
# print(test.a)
# print(t.a)




# delete  inside of static variable

# class test:
#     a=20
#     def __init__(self):
#         del test.a
        
        

# print(test.__dict__)
# t=test()
# print(test.__dict__)


# delete outside 

# class test:
#     a=20
#     b=20
    
# t=test()
# del test.a
# print(test.b)
# del test.b





# class test:
#     a=10
#     def m1(self):
#         self.y=20 
        
# t1=test()
# t2=test()
# test.a=3445
# test.y=6778
# print(test.a,test.y)






# class test:
#     a=10
#     def __init__(self):
#         self.y=20 
        
# t1=test()
# t2=test()
# print(t1.a,t1.y)
# print(t2.a,t2.y)
# print('*'*20) 
# t1.a=3445
# t2.y=6778
# print(t1.a,t1.y)
# print(t2.a,t2.y)




# class test:
#     x=10
#     def __init__(self):
#         self.y=20
        
# t1=test()
# t2=test()
# print(t1.x,t1.y)
# print(t2.x,t2.y)
# print('*'*20)
# test.x=454
# t1.y=999
# print(t1.x,t1.y)
# print(t2.x,t2.y)



# local variable


# class test:
#     def m1(self):
#         a=100
#         print(a)
        
#     def m2(self):
#         b=30
#         print(b)
        
# t=test()
# t.m1()
# t.m2()


# class test:
    
#     def average(self,l):
#         l=sum(l)/len(l) 
#         print("the average is",l)
        
        
# t=test()   
# t.average([10,20,30,40])



# x=100         #  global variable
# class test:
#     x=300
#     def m1(self):
#         x=545
#         print(x)
#         print(self.x)
        
#     def m2(self):
#         print(x)
#         print(test.x)
        
# t=test()
# t.m1()
# t.m2()



# class test:
#     def m1(self):
#         global x
#         x=545
#         print(x)
        
        
#     def m2(self):
#         print(x)
        
# t=test()
# t.m1()
# t.m2()



# # Using instance method use 'self' argument

# def m1(self):
#     self.x
    
# # Using class method use'@classmethod' 

# @classmethod
# def m1(self,cls):
#     cls.x
    
# # Use '@staticmethod' for this process

# def add(x,y):
#     print(x+y) 



     
# # # Application of Banking process
# # import sys

# class customer:
    
#     bankname='KVB'
    
#     def __init__(self,name,balance=0):
#         self.name=name
#         self.balance=balance
        
#     def deposit(self,amt):
#         self.balance=self.balance+amt
#         print("The Total  Account balance is :",self.balance)
        
#     def withdraw(self,amt):
#         if amt>self.balance:
#             print("Insufficient amount cannot perform the operation")
#             exit()
#         else:
#             self.balance=self.balance-amt
#             print("After withdraw the amount The balance is:",self.balance)
            
#     # def withdraw(self,amt):
#     #     if amt>self.balance:
#     #         print("Insufficient amount cannot perform the operation")
#     #         sys.exit()
            
#     #     self.balance=self.balance-amt
#     #     print("After withdraw the amount The balance is:",self.balance)
            
            
# print("Welcome the ",customer.bankname)
# name=input("enter the name :")
# c=customer(name)

# while True:
#     print("d-Deposit\nw-Withdraw\ne-Exit")
#     option=input("Enter Your option :")
#     if option=="d":
#         amt=int(input("Enter the amount to deposit :"))
#         c.deposit(amt)
        
#     elif option=="w":
#         amt=int(input("Enter the amount to withdraw:"))
#         c.withdraw(amt)
        
#     elif option=="e":
#         print("Thank you for Banking ")
#         exit()
        
#     else:
#         print("Invalid option\nPlease choose the correct option")
        
    
        
        
# class students:
#     def __init__(self,name,mark):
#         self.name=name
#         self.mark=mark
        
#     def display(self):
#         print("The student name is :",self.name)
#         print("The student mark is :",self.mark)
        
#     def grade(self):
        
#         if self.mark>=80:
#             print("o")
            
#         elif self.mark>=60:
#             print("A")
            
#         elif self.mark>=40:
#             print("B")
            
#         else:
#             print("Fail")
            
            
# n=int(input("Enter the students :"))
# # count=1 
# #while(count<=n):
    
# for i in range (n):
#     name=input("Enter the student name :")
#     mark=int(input("Enter the mark:"))
#     n=students(name,mark)
#     n.display()
#     n.grade()
#     # count=count+1


        
        
# class Animal:
#     legs=4
    
#     @classmethod
#     def walk(cls,name):
#         print('{} walks with {} legs'.format(name,cls.legs))
        
# Animal.walk('Dog')
# Animal.walk('cat')
        
        
        
        
        
        
# class Test:
#     count=0
#     def __init__(self):
#         Test.count=Test.count+1
        
        
#     @classmethod
#     def Noofobject(cls):
#         print("No of object created",cls.count)
        
# t1=Test()
# t2=Test()
# t3=Test()
# t4=Test()
# t5=Test()
# t6=Test()
# Test.Noofobject()

        
        
        

        
        
        
# class Maths:
    
#     @staticmethod
#     def Add(x,y):
#         print("the sum of two no is",x+y)
        
        
#     @staticmethod
#     def Sub(x,y):
#         print("the sub of two no is",x-y)
        
        
#     @staticmethod
#     def Average(x,y):
#         print("the Average  of two no is",(x+y)/2)
        
        
# Maths.Add(10,20)
# Maths.Sub(10,20)
# Maths.Average(10,20)
        
        
        
        
        
# # static method
            
# class method:
    
#     # @staticmethod
#     def m1(x):
#         print("some thing",x)
   
# method.m1(10)     
# # t=method()
# # t.m1(10)
 
 
        
# class method:
    
#     @staticmethod
#     def m1(x):
#         print("some thing",x)
   
   
# method.m1(10)         
        
        
        
 
        
# class method:
    
#     def m1():
#         print("some thing")
   
# method.m1()         
        
        
        
# #  Inner classes
        
        
# class Employee:
#     def __init__(self,no,name,sal):
#         self.no=no
#         self.name=name
#         self.sal=sal
        
#     def Display(self):
#         print("Employee no is :",self.no)  
#         print("Employee name id :",self.name)
#         print("Emlpoyeen salary is :",self.sal)
        
        
# class Test:
#     def Modify(emp):
#         emp.sal=emp.sal+10000
#         emp.Display()
        
# A=Employee(123456,'kavin',40000)
# Test.Modify(A)
          
      
# # # Inner class creation 

  
# class outer:
#     def __init__(self):
#         print("Outer class creating")
        
#     class inner:
#         def __init__(self):
#             print("Inner class creation")
            
#         def m1(self):
#             print("Inner class method")
            
# # o=outer()
# # I=o.inner()
# # I.m1()

# # i=outer().inner()
# # i.m1()             
        
# outer().inner().m1()       
        
        
        
        
# class person:
    
#     def __init__(self):
#         self.name='Kavin'
#         self.dob=self.DOB()  
        
#     def display(self):
#         print("My name is :",self.name)
#         self.dob.Display()
        
#     class DOB:
        
#         def __init__(self):
#             self.d=22
#             self.m=1
#             self.y=2004
            
#         def Display(self):
#             print("DOB={}/{}/{}".format(self.d,self.m,self.y)) 
            
            
# p=person()
# p.display()

        
# Another method
        
        
# class person:
    
#     def __init__(self,name,d,m,y):
#         self.name=name
#         self.dob=self.DOB(d,m,y)  
        
#     def display(self):
#         print("My name is :",self.name)
#         self.dob.Display()
        
#     class DOB:
        
#         def __init__(self,d,m,y):
#             self.d=d
#             self.m=m
#             self.y=y
            
#         def Display(self):
#             print("DOB={}/{}/{}".format(self.d,self.m,self.y)) 
            
            
# p=person("Kavin",22,1,2004)
# p.display()
        
        
   
        # check
     
     
# class person:
    
#     def __init__(self,d,m,y):
#         self.name='Kavin'
#         self.d=22
#         self.m=1
#         self.y=2004
#         # self.dob=self.DOB(d,m,y)  
        
#     def display(self):
#         print("My name is :",self.name)
#         DOB=({}/{}/{}.format(self.d,self.m,self.y))
#         print(DOB)
    
           
# p=person()
# p.display()
        
    
        
        
        
# class Human:
#     def __init__(self):
#         self.head=self.Head()
#         # self.brain=self.Brain()
        
    
#     class Head:
#         def __init__(self):
#             self.brain=self.Brain()
#             print("Head is important")
        
#         class Brain:
#             def __init__(self):
#                 print("In brain we can thick a lot")
                
                
# h=Human()

                

# Nested Method


# class Test:
#     def m1(self):
        
#         def sum(a,b):
#             print("First no :",a)
#             print("Second No :",b)
#             print("the sum is :",a+b)
#             print("the product is :",a-b)
#             print('*'*20)
            
#         sum(10,20)
#         sum(100,200)
#         sum(200,400)
        
# a=Test()
# a.m1()
            
                
            