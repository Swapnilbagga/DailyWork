from  abc import ABC, abstractmethod 
class A(ABC):
    @abstractmethod
    def m1(self):
        print("a")
# ob=A()        
# ob.m1             # line 6 and 7 will give error
class B(A):         #as we cannot call abstract method so we will extend this method to another class B
    def m1(self):
        print("a")
ob=B()
ob.m1()