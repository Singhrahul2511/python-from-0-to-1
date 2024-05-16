#creating a list of 5 odd number
a =[1,3,5,7,9]
print(a)
#creating a list of 5 even number
b =[2,4,6,8,10]
print(b)
#combining two list
c =a+b
print(c)
#add prime number at the biggning of the list

num= [11,17,29]+c
print(num)

length = len(num)
print(length)
#replace 3 num of list with 100,200,300

num[length-3:length] = [100,200,300]
print(num)

#delete all ele of list
a[:] = []
print(a)

#delete entire list

del a