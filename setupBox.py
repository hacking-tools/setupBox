# Adding File to /etc/hosts
#!/usr/bin/env python3
import os
boxName = input("What is the box name? ")
boxIP = input("What is the box IP? ")
boxNameHTB = boxName + ".htb"
hostIP = boxNameHTB + ":" + boxIP
try:
    os.system("hostsman -i " + hostIP)
except:
    print("Box already added to /etc/hosts")
print("Added " + boxNameHTB + " to /etc/hosts ")
