myls = []
str1 = "cat 12 dog 35 bird 9"
x = str1.split(' ')
for i in x:
    try:
        y = int(i)
        print(y)
        myls.append(y)
    except Exception as e :
        myls.append(i)
int_ls = []
str_ls = []
for i in myls:
    if isinstance(i, int):
        int_ls.append(i)
    elif isinstance(i,str):
        str_ls.append(i)
    else:
        pass
int_ls.sort()
result = [*int_ls, *str_ls]
print(result)
result_str = ''
for j in result:
    result_str += str(j) + ' '
print(result_str)


print('-------------')

# import re

str1 = "cat 12 dog 35 bird 9"
words = str1.split()


# Separate numbers and words
numbers = sorted([int(w) for w in words if w.isdigit()])
strings = [w for w in words if not w.isdigit()]
print("strings : ", strings)

# Join them back into a string
result = " ".join(map(str, numbers + strings))
print('1 : ', result)

result = [*numbers, *strings]
print('2 : ', result)


