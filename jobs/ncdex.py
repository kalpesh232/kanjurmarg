"""
Write a Python script that checks all files in a folder named "source" and copies only those files that contain today’s date (day only) in their filename to another folder "dist1/".
"""

import os
import datetime
import shutil

myPath = "source"
destination = "dist1/"
files = os.listdir(myPath)
current_date = datetime.datetime.now()
print(current_date)
# dt = current_date.strftime("%d%m%Y")
dt1  = current_date.strftime("%d")
print(dt1)

for i in files:
    if dt1 in i:
        shutil.copy(myPath +'/'+i,destination)
        print(i)