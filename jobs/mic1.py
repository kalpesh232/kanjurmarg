
"""
You are given a string like "cat 12 dog 35 bird 9".
Write a Python program to extract only the numbers, sort them, and then append the remaining words at the end of the list.
"""
str1 = "cat 12 dog 35 bird 9"
words = str1.split()
numbers = sorted([int(w) for w in words if w.isdigit()])
strings = [w for w in words if not w.isdigit()]
result = numbers + strings
print('2 : ', result)


