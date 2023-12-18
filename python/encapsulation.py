# ---------------------------------- Protected Variable
class A:
    def __init__(self,a):
        self.__a = a

    def Show_A(self):
        print('Show B : ', self.__a)

class B(A):
    def __init__(self,b):
        super().__init__(b)
        print('b___________',b)
        self.__b = b

    def Show_B(self):
        # print('Show B : ', self.__a)
        print('Show B : ', self._A.__a)

x = B(20)
x.Show_B()

# ------------------------------------ Private Variable

# class A:
#     def __init__(self,a):
#         self._a = a

#     def showA(self):
#         print('Private Variable : ', self._a)

# class B(A):
#     def __init__(self,b):
#         super().__init__(b)
#         self._b = b

#     def showB(self):
#         print('Show B : ', self._b)

# obj = B(30)
# obj.showB()