#a list contains only +ve or -ve integer.write a program to obtain the num present in the list.
import random
neg_num =[]
num = [random.randint(-20,20) for i in range(10)]
for n in num:
    if(n<0):
        neg_num.append(n)

print(f"list of -ve num is {neg_num}: ")