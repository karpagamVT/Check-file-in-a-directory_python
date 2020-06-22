import os
def find(name):
    count=0
    for root,dirs,files in os.walk('D:\\'):
        if name in files:
            print(root,name)
            count+=1
            print(count)
    print(os.path.abspath(name))
    print()
    print("yes we found the file")
    input()
try:
    s=input("name: ")
    find(s)
except:
    print("Error")
