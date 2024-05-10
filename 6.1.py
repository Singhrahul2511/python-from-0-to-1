#write a program to receive 3 sets of principle ,rate and time

i =1
while(i<=3):

    p =float(input('Enter principle: '))
    n= float(input("Enter time: "))
    r =float(input("Enter rate of this: "))
    si=p*n*r/100
    print(f"si is {si}: ")
    i =i+1