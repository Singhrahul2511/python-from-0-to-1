#write a prog to create three dict and concatinate them to create four dict

d1 ={'mango':30,'guava':24}
d2 = {'apple':23,'banana':21}
d3 = {'kivi':34,'pinapple':54}
d4 ={}
for d in (d1,d2,d3):
    d4.update(d)
print(d4)

#one more way dict unpacking technique
d5 = {**d1,**d2,**d3}
print(d5)
