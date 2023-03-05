
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





     
