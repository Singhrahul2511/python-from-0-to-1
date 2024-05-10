#if three points (x1,y1),(x2,y2) and (x3,y3) are given then check they are on same straight line: 
import math
def points_are(x1,y1,x2,y2,x3,y3):
    dis1 = math.sqrt((x2-x1)**2+(y2-y1)**2)
    dis2 =math.sqrt((x3-x2)**2+(y3-y2)**2)
    dis3 =math.sqrt((x1-x3)**2+(y1-y3)**2)
    if(dis1==dis2==dis3):
        print("points are collinear: ")
    else:
        print("points are not collinear: ")
x1=int(input("Enter 1st point: "))
y1=int(input("Enter 1st point: "))
x2=int(input("Enter 2st point: "))
y2=int(input("Enter 2st point: "))
x3=int(input("Enter 3st point: "))
y3=int(input("Enter 3st point: "))
if(points_are(x1,x2,x3,y1,y2,y3)):
    print("points are collinear: ")
else:
    print("points are not collinear: ")