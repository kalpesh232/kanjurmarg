# myStr = "Django is powerful"
# myLssplit = myStr.split()
# myLssplit.sort(reverse=True)
# result = ' '.join(myLssplit)
# print('result : ', result)

# Multiprocessing
from multiprocessing import Process
import time
import os 

def task_number():
    print(f"[Numbers Task] Running in Process ID: {os.getpid()}")
    for i in range(10):
        print(f"[Numbers Task] Number: {i}")
        time.sleep(1)

def task_letter():
    print(f"[Letter Task Task] Running in Process ID: {os.getpid()}")
    for i in ["A","B","C","D","E","F","G","H"]:
        print(f"[Letter Task] Number: {i}")
        time.sleep(1)

if __name__ == '__main__':
    p1 = Process(target=task_number)
    p2 = Process(target=task_letter)

    print("Starting both processes...\n")

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    print("\nBoth processes finished!")