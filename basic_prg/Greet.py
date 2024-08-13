#write a program to greet all the person name in list l1 and which start with S

l1 =["harry","sohan","sachin","rahul"]
for name in l1:
    if(name.startswith('s') or name.startswith('S')):
        print(name)