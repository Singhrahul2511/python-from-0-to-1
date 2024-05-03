import math
a =int(input("Enter the 1st side: "))
b =int(input("Enter the 2nd side: "))
c=int(input("Enter the 3rd side: "))
if(a+b>c and b+c>a and c+a>b):
    print("valid triangle: ")

    cos_b =(a^2+c^2-b^2)/(2*a*c)
    cos_c =(a^2+b^2-c^2)/(2*a*b)
    cos_A = (b^2+c^2-a^2)/(2*b*c)
    #converting radian to degree

    Angle_B = math.acos(cos_b)
    Angle_C = math.acos(cos_c)
    Angle_A = math.acos(cos_A)


    Angle_B_deg = int(math.degrees(Angle_B)+0.5)
    #converting radian to degree
    Angle_C_deg = int(math.degrees(Angle_C)+0.5)
    Angle_A_deg = int(math.degrees(Angle_A)+0.5)

    print(f"Angle_A {Angle_A}","degree")
    print(f"Angle_B {Angle_B}","degree")
    print(f"Angle_C {Angle_C}","degree")
else:
    print("enter the sides so that sum of two side of a trianle should be greater than the 3rd side: ")
