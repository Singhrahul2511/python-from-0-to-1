#a list contains name of girls and boys as tuples.python program to find out  the
#no of boys an gorls

lst =['somya','nisha','rinki',('rahul',),('rohit',),('sonu',)]
boys = 0
girls =0
for ele in lst:
    if isinstance(ele,tuple):
        boys +=1
    else:
        girls +=1

print('Boys = ',boys,'Girls = ',girls)