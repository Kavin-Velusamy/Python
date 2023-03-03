



class student :
    def __init__(self,name,no):
        self.name=name
        self.no=no
        
    def details(self):
        print("my name is",self.name)
        print("my no is",self.no)
       
s=student ('erevv',34)
print(s.name,s.no) 
s.details()