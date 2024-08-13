#write a program that convert list of fahrenheit into equivalent celsius degree.


F= [12, 24, 33.6, 40]
cel_tem = [(f-32)*5/9 for f in F]
print("Temperature in celsius: ")
for i in range(len(F)):
    print(f"{F[i]} fahrenheit is equivalent to {cel_tem[i]:.2f} celsius.")