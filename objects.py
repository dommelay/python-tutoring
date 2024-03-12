# CLASS, INSTANCE, AND LOCAL VARIABLES
class A:
    # class variables
    x = 0
    y = 7
    # instance variable
    def __init__(self, a):
        self.x = a
        A.x += 1
print(A.x) # 0
print(A.y) # 7
a1 = A(3)
print(a1.x) # 3
print(A.x) # 1, incremented once
A.y = 9
print(a1.y) # 9
a2 = A(5)
print(a2.x, A.x, a2.y) # 5, 2, 9

class A:
    x = 0
    def __init__(self, a):
        self.x = a
        x = A.x + 1  
        # x is a local variable
        print(x) # 1
a2 = A(7)
print(a2.x, A.x) # 7, 0
