# ----------------- super()
class Animal:
    def __init__(self, name):
        self.name = name
    
    def sound(self):
        return "Some sound"

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)   # calling parent constructor
        self.breed = breed

    def sound(self):
        parent_sound = super().sound()   # calling parent method
        return f"{self.name} barks. Parent says: {parent_sound}"

d = Dog("Tommy", "Labrador")
print(d.sound())

