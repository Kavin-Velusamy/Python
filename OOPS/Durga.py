
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




# delete the static variable

class test:
    a=20
    def __init__(self):
        del test.a
        
        

print(test.__dict__)
t=test()
print(test.__dict__)









