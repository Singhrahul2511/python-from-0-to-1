#for the following dict write a prog to report max and min salary

d = {   

        'rahul':{'salary':100000,'age':22,'height':6},
        'rohit':{'salary':20000,'age':21,'height':5},
        'pinku':{'salary':2000,'age':12,'height':4}
    }
lst = []
for v in d.values():
    lst.append(v['salary'])
print(max(lst))
print(min(lst))