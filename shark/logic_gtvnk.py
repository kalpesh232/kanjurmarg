# ################### P 
# def sort_fun(temp,p_shock,i,j):
#     temp = p_shock[i]
#     p_shock[i] = p_shock[j]
#     p_shock[j] = temp

#     return p_shock

# order_by = int(input('1 for  Ascending  and 2 for Descending  ! Enter input : '))
# total_shock = int(input('How many shock P You want to compare : '))
# p_shock = []
# for i in range(total_shock):
#     enterP = float(input('Enter P :'))
#     p_shock.append(enterP)
# avg_p = sum(p_shock)/total_shock
# print(f'Avg. P {avg_p}')
# temp = 0
# for i in  range(len(p_shock)):
#     for j in range(len(p_shock)):
#         if order_by == 1 :
#             if p_shock[i] < p_shock[j] :
#                 p_shock = sort_fun(temp,p_shock,i,j)
#         elif order_by == 2 : 
#             if p_shock[i] > p_shock[j] :
#                 p_shock = sort_fun(temp,p_shock,i,j)
# near_value = []
# if total_shock % 2 != 0 :
#     print(f'Middel P shock : {p_shock[total_shock//2]}')
# else:
#     near_value.append(avg_p - p_shock[total_shock//2 - 1])
#     near_value.append(avg_p - p_shock[total_shock//2])

# print(p_shock)
# print(p_shock[ total_shock//2 - 1 : total_shock//2 + 1 ])
# if near_value :
#     print(near_value)

# ####################### IV
# final_iv = {}
# Qtr_Rs_Cr = {}
# Qtr_Var = {}
# sheet = {}

# for i in range(1,3):
#     cp = int(input(f'Enter your CP for {i} : ', ))
#     iv = int(input(f'Enter your IV for {i}: ', ))

#     nqrc = float(input(f'Enter your NP Qtr Rs.Cr. for {i} : ', ))
#     sqrc = float(input(f'Enter your Sales Qtr Rs.Cr. for {i}: ', ))

#     qpv = float(input(f'Enter your Qtr Profit Var % for {i} : ', ))
#     qsv = float(input(f'Enter your Qtr Sales Var % for {i}: ', ))

#     te = float(input(f'Enter your Total Equity for {i} : ', ))
#     tl = float(input(f'Enter your Total Liabilities for {i}: ', ))

#     pro = iv - cp
#     print(pro)
#     pro1 = pro / cp
#     pro2 = pro1 * 100

#     qtr =nqrc + sqrc
#     qv = qpv+qsv
#     f = te / tl
#     f1 = f * 100

#     final_iv[i] = pro2
#     Qtr_Rs_Cr[i] = qtr
#     Qtr_Var[i] = qv
#     sheet[i] = f1

# print('final_iv : ', final_iv)
# print('Qtr_Rs_Cr : ', Qtr_Rs_Cr)
# print('Qtr_Var : ', Qtr_Var)
# print('sheet : ', sheet)

#  ##################### QR

numbers_list  = "20.30	21.61	23.98	16.90	21.80	18.88	31.82	38.11	42.41	"
# Replace commas with empty strings and split the string into a list of numbers
if '%' in numbers_list :
    ls = numbers_list .replace('%', '').split()
else:
    ls = numbers_list .replace(',', '').split()

# Convert each element in the list to an integer
ls = [float(num) for num in ls]
c = 0
for x in range(len(ls)):
    try:
        if ls[x] < ls[x+1]:
            c += 1
        elif ls[x] > ls[x+1]:
            c -= 1
    except Exception as e:
        print(f'Error : {str(e)}')
    finally:
        print('Result : ', c)