import os
import json 
import pip
from sys import platform

myjsonfile = open('req.json', 'r')
jsondata = myjsonfile.read()
# print(jsondata)

obj = json.loads(jsondata)
dependencies = obj["Dependencies"]
# print( dependencies )

_all_ = ["beautifulsoup4==4.4.1", "boto==2.48.0", "bz2file==0.98", "numpy"]
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

install(dependencies)