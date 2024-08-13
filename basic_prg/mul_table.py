# #write a program to print the mul. table of a given number: 

# i=0
# a= int(input("Enter a number: "))
# for i in range(0,10):
#     i +=1
#     mul_table = a*i
#     print(f"multiple table of {a}*{i} is {mul_table} ")


#problem using while loop:

i =0
a =int(input("Enter the number: "))
while(i<=9):
    i +=1
    mul_table =a*i
    print(f"mult. table of {a} is {a}*{i} = {mul_table}")