# ---------- P

def sort_fun(temp,p_shock,i,j):
    temp = p_shock[i]
    p_shock[i] = p_shock[j]
    p_shock[j] = temp

    return p_shock

order_by = int(input('1 for  Ascending  and 2 for Descending  ! Enter input : '))
total_shock = int(input('How many shock P You want to compare : '))
p_shock = []
for i in range(total_shock):
    enterP = float(input('Enter P :'))
    p_shock.append(enterP)
avg_p = sum(p_shock)/total_shock
print(f'Avg. P {avg_p}')
temp = 0
for i in  range(len(p_shock)):
    for j in range(len(p_shock)):
        print('order_by : ', order_by)
        print('order_by T : ', type(order_by))
        if order_by == 1 :
            if p_shock[i] < p_shock[j] :
                p_shock = sort_fun(temp,p_shock,i,j)
        elif order_by == 2 : 
            if p_shock[i] > p_shock[j] :
                p_shock = sort_fun(temp,p_shock,i,j)
near_value = []
if total_shock % 2 != 0 :
    print(f'Middel P shock : {p_shock[total_shock//2]}')
else:
    near_value.append(avg_p - p_shock[total_shock//2 - 1])
    near_value.append(avg_p - p_shock[total_shock//2])

print(p_shock)
print(p_shock[ total_shock//2 - 1 : total_shock//2 + 1 ])
if near_value :
    print(near_value)


