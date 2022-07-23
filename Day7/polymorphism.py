class A:
    a=10
    b=20
    def __init__(self):
        print('a')
    def m1(self):
        print('M1')
class B(A):
    a=4
    b=5
    def m1(self):
        print("B class")
ob=B()
ob.m1()