class A:
    def f1(self):
        print("A")
class B(A):
    def f2(self):
        print("b")
class C(A):
    def f3(self):
        print("c")
ob=C()
ob.f1()
ob.f3()


# or 
ob =B()
ob.f1()
ob.f2()