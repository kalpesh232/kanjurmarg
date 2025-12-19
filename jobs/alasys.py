# what is itrater __inter__ 
class Numbers:
    def __init__(self):
        self.items = [1, 2, 3]

    def __iter__(self):
        return iter(self.items)

# using the class in a for loop
for n in Numbers():
    print(n)
