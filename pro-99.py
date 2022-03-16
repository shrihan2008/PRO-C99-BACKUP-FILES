import time
import os 
import shutil
day=30
path=input("Enter a path")
day=time.time()
os.path.exists(path)
if os.path.exists(path)==True:
    os.walk(path)
    os.path.join()
    ctime=os.stat(path).st_ctime
if day<ctime:
    os.remove(path)