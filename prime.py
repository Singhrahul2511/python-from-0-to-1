a =int(input("Enter a number to check: "))
if(a==1 or a==0):
    print("not prime: ")
else:
    print("Enter another number to check: ")
i=2
while(i<=a-1):
    if(a%i==0):
        print("number isn't prime: ")
        break
    i +=1
else:
    print(f"number {a} is prime: ")


#using for loop

# a =int(input('Enter number: '))
# i=2
# for i in range(2,a-1):
#     if(a%1==0):
#         print(f"num {a} isn't prime: ")
#         break
#     i =i+1
# else:
#     print("it's prime number: ")