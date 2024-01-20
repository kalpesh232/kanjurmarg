import re

pattern = r"^bha"
mystring = "Bhabhyue  kAlpesh H shindE"
# ---------- MATCH
x = re.match(pattern, mystring)
print(x)
# ---------- SEARCH
x1 = re.search('\s', mystring)
print(x1)
print(x1.start())

x2 =  re.search('KALPESH', mystring)
print(x2)
# ---------- REPLACE
print(mystring)
x3 =  re.sub('kalpesh','KALPESH', mystring)
x4 =  re.sub(r"kalpesh","KALPESH", mystring)
x3 =  re.sub('[a-z]','0', mystring)
x4 =  re.sub(r"[a-z]","-", mystring)
print(x3)
print(x4)

