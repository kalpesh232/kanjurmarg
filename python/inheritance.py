# class A:
#     def __init__(self):
#         print('Show in Class A')
# class B(A):
#     def __init__(self):
#         print('Show in Class B')
#         super().__init__()
#         pass
# b = B()

# class A:
#     def __init__(self):
#         print('Show in Class A')
# class B(A):
#     def __init__(self):
#         print('Show in Class B')
#         super().__init__()
#         pass
# class C(B):
#     def __init__(self):
#         super().__init__()
#         print('Show in Class C')
# b = C()

# class A:
#     def __init__(self):
#         print('Show in Class A')
# class B:
#     def __init__(self):
#         print('Show in Class B')
#         super().__init__()
# class C(B,A):
#     def __init__(self):
#         super().__init__()
#         print('Show in Class C')
# b = C()

# ====== hierarchical
# class A:
#     def __init__(self):
#         print('Show in Class A')
#     def B1(self):
#         print('Show in Class B1')

# class B(A):
#     def __init__(self):
#         print('Show in Class B')
#         super().__init__()

# class C(A):
#     def __init__(self):
#         super().__init__()
#         print('Show in Class C')
# c = C()
# c.B1()
# b = B()

class A:
    def __init__(self):
        print('Show in Class A')
class B(A):
    def __init__(self):
        print('Show in Class B')
        super().__init__()
class C(A):
    def __init__(self):
        super().__init__()
        print('Show in Class C')
class D(C,B):
    def __init__(self):
        super().__init__()
        print('Show in Class D')
d = D()
# b = B()