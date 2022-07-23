class A:
    __a=10
    def __sum(self):
        print(self.__a)    #here __sum is private so we hv extended it in another func. (display) 
    def display(self):
        ob=A()
        ob.__sum()
        print("display")
ob=A()
ob.display()