#a lst contains 5 string .write program to convert all these string to uppercase

lst= ['rahul','kundan','Vikash','Rohit','ram']
new_lst =[]
for i in lst:
    if(i.islower() or i.isupper):
        print(i.upper())
        new_lst.append(i.upper())
print(f"new is: {new_lst}")