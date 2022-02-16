import os
import json 
import pip
from sys import platform
import threading

## Q. make sure that the code des'nt  crash anywhere
## Sol. => * surround code in a try catch block and print the error
##         * case 1: wrong file, throws exception ( No such file or directory: 'req1111.json' )
##         * case 2: the file is empty throws exception ( Expecting value: line 1 column 1 (char 0) )
##         * case 3: the file's data is not in json format throws exception (Expecting property name 
##                   enclosed in double quotes: line 1 column 1 (char 0) )

## Q. file can be huge ....limit memory usage  ``     => iterate one by one
## Sol. => * using an iterator as it is faster and has better memory efficiency
##         * allows a user to process every element of a json obj. individually

## --------------> parallel exe.
## Sol. => * idea is to create 2-threads that will process the same file simultaneously
##         * thread1 handles first half of packages
##         * thread2 handles other half of packages
 
try:
    myjsonfile = open('req.json', 'r')
    jsondata = myjsonfile.read() ## loads data as a string
    obj = json.loads(jsondata) ## creates json obj from string
    # dependencies = iter( obj["Dependencies"] ) ## creates an iterator for json obj.
    dependencies = obj["Dependencies"]
except Exception as e:
    print("Exception : ", e)
    print("something is not right with file")

# all = ["beautifulsoup4==4.4.1", "boto==2.48.0", "bz2file==0.98", "numpy"]

c = []
def install(packages):
    for package in packages:
        try:
            pip.main(['install', package])
        except :
            print(package, "failed to install")
            c.append( package )
    if len(c) == 0:
        print("All packages installed")
    else:
        print("Failed to install: ")
        for package in c:
            print( package)

l = len(dependencies)
t1 = threading.Thread(target = install, args=(dependencies[:int(l/2)], ))  ## thread1 has first half of packages
t2 = threading.Thread(target = install, args=(dependencies[int(l/2):], ))  ## thread2 has other half of packages

t1.start() ## starts thread1
t2.start() ## starts thread2

t1.join() ## waits for thread1 to finish
t2.join() ## waits for thread2 to finish

print( "------t1 and t2 done exe. !-------")

