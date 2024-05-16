#suppose a lst contains pos+ and -ve num .write a program to create two lst one of
#+ve and _ve numbers

import random
numbers =[random.randint(-20,20) for i in range(10)]
positive_num = []
negative_num = []
for num in numbers:
    if(num>0):
        positive_num.append(num)
    else:
        negative_num.append(num)

print(f"+ve num is: {positive_num}")
print(f"-ve num is: {negative_num}")