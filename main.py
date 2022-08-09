import os

lines = os.popen('ls -ltrh ~').readlines()

index = 0
for line in lines:
    print(str(index) + '   ' + line)
    index = index + 1
