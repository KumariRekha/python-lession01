class A:
    def __init__(self) :
        print("in A init")
    def method1(self):
        print("method 1 working")
    def method2(self):
        print("method2 working")
class B():     
    
    def __init__(self) :
        print("in B init")
    def method3(self):
        print("method 3 working")
    def method2(self):
        print("method 2 working")
    
class C(A,B):     
    def __init__(self) :
        super().__init__()  
        print("in C init")
    def method4(self):
        print("method 4 working")
    def method8(self):
        print("method 8 working")
a1=C()
