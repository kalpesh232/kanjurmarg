# class Animal:
#     def main(self):
#         pass

# class Dog(Animal):
#     def main(self):
#         print('I can Bark')

# class Snake(Animal):
#     def main(self):
#         print('I can hisss')

# d = Dog()
# s = Snake()

# d.main()
# s.main()

from abc import ABC , abstractmethod
class A(ABC):
    @classmethod
    @abstractmethod
    def fun_a():
        pass
class B(A):
    def __init__(self, radius):
        self.radius = radius

    def fun_a(self):
        return 3.14 * self.radius * self.radius

value = 5
a = B(value)
print(a.fun_a())