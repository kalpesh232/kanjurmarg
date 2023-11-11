# attributes -> variable
# behaviour -> methods(fun)

# class computer:
#     def config(self):
#         print("i4, 4gb, 50mp")

# comp1 = computer()
# comp2 = computer()
# # print(type(comp1))
# computer.config(comp2)
# comp1.config()

class myclass:
    x = 5
    print('xxxx', x)
    # self predefined instance of class that tells you belong to this class
    def __init__(self,name,age):
        # variables of class
        self.naav = name
        self.vy = age

    def foo(self):
        print('naav : ',self.naav)
        print('self.vy : ', self.vy)


m = myclass('kalpesh',30)
m.vy = 31
del m.vy
m.x = 10
m.foo()
print(m.naav)
print(m.vy)
print(m.x)