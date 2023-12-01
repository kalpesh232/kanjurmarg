# #################################### threading

# import time
# import threading

# start_time = time.time()
# def calculate_square(ls):
#     print('calculate sqaure')
#     for i in ls:
#         time.sleep(0.2)
#         print('sqaure : ', i*i)

# def calculate_cube(ls):
#     print('calculate cubes')
#     for i in ls:
#         time.sleep(0.2)
#         print('cubes : ', i*i*i)

# arr = [1,2,3,4,5]

# t = time.time()

# t1 = threading.Thread(target=calculate_square, args=(arr,))
# t2 = threading.Thread(target=calculate_cube, args=(arr,))

# t1.start()
# t2.start()

# t1.join()
# t2.join()

# end_time = time.time()
# #  1.0109827518463135 seconds
# print(f'Time taken for calculate_cube: {end_time - start_time} seconds')

# ################################### multiprocesing

# import time
# import multiprocessing

# square_list = []

# start_time = time.time()
# def calculate_square(ls):
#     global square_list
#     print('calculate sqaure')
#     for i in ls:
#         print('sqaure : ', i*i)
#         square_list.append(i*i)
#     print('Within Sqaure list : ', square_list)

# def calculate_cube(ls):
#     print('calculate cubes')
#     for i in ls:
#         print('cubes : ', i*i*i)

# arr = [1,2,3,4,5]

# t = time.time()
# if __name__ == '__main__':
#     t1 = multiprocessing.Process(target=calculate_square, args=(arr,))
#     t2 =  multiprocessing.Process(target=calculate_cube, args=(arr,))

#     t1.start()
#     t2.start()

#     t1.join()
#     t2.join()

#     end_time = time.time()
#     #  0.22478866577148438 seconds
#     print('Sqaure list : ', square_list)
#     print(f'Time taken for calculate_cube: {end_time - start_time} seconds')

# ####################################### Sharing Data

# import time
# import multiprocessing

# def calculate_square(ls,result,v,q):
#     v.value = 10
#     for idx, val in enumerate(ls):
#         result[idx] = val * val
#         q.put( val * val)
#     print('Within Sqaure list : ', result[:])
#     print('Within value : ', v.value)

# arr = [1,2,3,4,5]

# t = time.time()
# if __name__ == '__main__':

#     # 1. by Array
#     result = multiprocessing.Array('i',5)
#     # 2. by Value
#     # 1. by Array
#     v = multiprocessing.Value('i',5)
#     # 3. bu Queue
#     q = multiprocessing.Queue()

#     t1 = multiprocessing.Process(target=calculate_square, args=(arr,result,v,q))

#     t1.start()
#     t1.join()
    
#     print('Sqaure list : ', result[:])
#     print('Value : ', v.value)
#     while q.empty() is False:
#         print('Queue : ', q.get())

# #################################### lock

import time
import multiprocessing

start_time = time.time()
def deposite(balance,lock):
    for i in range(100):
        time.sleep(0.01)
        # lock.acquire()
        print('deposite : ',balance.value)
        balance.value += 1
        # lock.release()

def withdraw(balance,lock):
    for i in range(100):
        time.sleep(0.01)
        # lock.acquire()
        print('withdraw : ',balance.value)
        balance.value -= 1
        # lock.release()

if __name__ == '__main__':

    balance = multiprocessing.Value('i',200)
    lock = multiprocessing.Lock()

    t1 = multiprocessing.Process(target=deposite, args=(balance,lock))
    t2 =  multiprocessing.Process(target=withdraw, args=(balance,lock))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print('balance.value : ', balance.value)
