# in this we take the private variables
class A:
    __songname="old skool"
    def __init__(self):
        print(self.__songname)
    def __setsongName__(self,songname):
        self.__songname=songname
    def __getsongname__(self):
        return self.__songname
sidhu=A()
sidhu.__setsongName__("old skool")
print(sidhu.__getsongname__())
