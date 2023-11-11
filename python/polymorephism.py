# class add:
    
#     def sum(self,a,b,c):
#         print('hello')
#         print(a+b+c)
#     def sum(self,a,b):
#         print('hi')
#         print(a+b)
# a = add()
# a.sum(1,23,3)

# method overloading not sppoerted in python because python is interperted launguage

class A:
    def sum(self,a,b):
        print('A :',  a+b)
class B(A):
    def sum(self,a,b):
        super().sum(50,60)
        print('B : ',  a+b)
class C(B):
    def sum(self,a,b):
        super().sum(30,40)
        print('C : ', a+b)
c = C()
c.sum(10,20)
