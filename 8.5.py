#write a program to generate and store in a list of 20 random num in the range 
#10 to 100.from this list delete all those entries ehich have value b/w 20 and 50
#print the remaining list

import random
a =[]
i=1
while i<=20:
    num =random.randint(10,100)
    a.append(num)
    i +=1
print(a)

for num in a:
    if(num>20 or num<50):
        a.remove(num)

print(a)