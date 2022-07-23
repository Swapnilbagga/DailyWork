class A:
    def __init__(self):
        print("a")
    def car(self,name):
        self.name=name
        print(name)

class B(A):
    def __init__(self):
        super().__init__()
    def parts(self):
        print("tyre,handle,headlights.....etc")
ob=B()
ob.car("ferrari")
ob.parts()