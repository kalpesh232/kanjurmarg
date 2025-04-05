

str1 = "cat 12 dog 35 bird 9"
words = str1.split()
numbers = sorted([int(w) for w in words if w.isdigit()])
strings = [w for w in words if not w.isdigit()]
result = numbers + strings
print('2 : ', result)


