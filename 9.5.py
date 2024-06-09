#do the following for this

#1 add ! to the tuple
tpl = ['r','a','h','u','l','k','u','m','a','r']
ntpl=['!',]
tpl =tpl+ntpl
print(tpl)

#converting tpl into string

s =''.join(tpl)
print(s)

#extract u,l from tpl
t =tpl[3:5]
print(t)

#count num of time r occure

count =tpl.count('r')
print(count)

#check k exist or not

print('k' in tpl)

#convert tuple to a list
lst =list(tpl)
print(lst)

#tuple is immutable so we can not remove ele fro it
#need to split tuple and eliminate unwanted ele and then merge tpl

tpl = tpl[:3]+tpl[7:]
print(tpl)