#write a program to print the multiplication table of any number.

def multiply(n):
    for i in range(1,11):
        print(f"{n}x {i} = {n*i}")
n  = int(input("Enter a number: "))
print(f"{multiply(n)}")