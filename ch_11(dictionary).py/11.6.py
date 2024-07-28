#write a prog to join two dict of having boys and girl with respective age
boys = {'rahul':23,"rohit":16,'ram':41}
girls = {'pinki':45,'sarada':55}
combine ={**boys,**girls}
print(combine)

#method 2
boys = {'ram':42,'sonu':23}
girl = {'rinki':32,'pinki':21}
combine ={}
for d in(boys,girl):
    combine.update(d)
print(combine)