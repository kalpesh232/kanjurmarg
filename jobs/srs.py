# ----- In Python, class methods and instance methods are called in different ways.
##### 1. Instance Method:
class MyClass:
    def instance_method(self):
        print("This is an instance method.")

# Create an instance of the class
obj = MyClass()

# Call the instance method
obj.instance_method()  # Output: This is an instance method.

class MyClass:
    @classmethod
    def class_method(cls):
        print("This is a class method.")

##### 2. Class Method:
# Call the class method using the class name
MyClass.class_method()  # Output: This is a class method.

# Alternatively, you can call it using an instance
obj = MyClass()
obj.class_method()  # Output: This is a class method.
