#a list contains 20 integers generated randomly.receive a num from the keyword and report pos of that 
#num and occurance of that num in the list

import random
ran_num = [random.randint(1,100) for i in range(20)]
print(ran_num)
search_num = int(input("Enter a num to search for: "))
positions = [index for index, value in enumerate(ran_num) if value ==search_num]
if positions:
    print("pos of the number:",positions)
    print("no of occurance:",len(positions))
else:
    print("The no is not found in the list: ")