# a = [1,2,3]
# b = [3,4,5]

# print(set(b) - set(a), set(a) - set(b))
count = 0
x = [1,2,3,4]
for i in range(len(x)):
    for j in range(len(x)):
        if x[i] == x[j] :
            count += 1
       
print('count : ', count)
if count > 4 :
    print('true')
else :
    print('false')