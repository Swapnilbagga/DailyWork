# heirarical + multiple
class A:
    def f1(self):
        print("A")
class B(A):
    def f2(self):
        print("b")
class C(A):
    def f3(self):
        print("c")
class D(C,B):
    def f4(self):
        print("D")
ob=D()
ob.f1()
ob.f2()
ob.f3()
ob.f4()