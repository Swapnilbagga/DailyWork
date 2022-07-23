# protected varisble is used in child class only.
class A:
    def __init__(self):
        self._a=20
class B(A):
    def __init__(self):
        super().__init__()
        print(self._a)
    def display(self):
        print(self._a)
ob=B()
ob.display()
