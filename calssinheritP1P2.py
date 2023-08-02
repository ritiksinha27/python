#child will inherit from both parent P1 and P2

class P1:
    a=10
class P2:
    a=7
class C(P2,P1):
    pass

x=C()
print(x.a)