d1 = {'1':'apple', '2':'banana', '3':'orange', 'A':'B'}
print('d1 : ', d1)
print('d1 : ', type(d1))
# print('d1 : ', d1[3])
print(d1.get('3'))
z = d1.items()
print('z : ', z)
print('z : ', type(z))
print('z : ', len(z))
d1['3'] = 'kiwi'
print('d1 : ', d1)
# d1.pop('3')
print('d1 : ', d1)
# d1.popitem()
print('d1 : ', d1)
# del d1['1']
print('d1 : ', d1)
l = d1.keys()
print('lll : ', l)