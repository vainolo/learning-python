class A:
    def f1(self):
        print "Function f1 in A"
    
class B(A):
    def f2(self):
        print "Function f2 in B"

b = B()
b.f1()
b.f2()

class C(A):
    def f1(self):
        print "Function f1 in C"

c = C()
c.f1()
A.f1(c)