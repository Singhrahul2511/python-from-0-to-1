#in this program i need to define that a given point is lie on x-axis ,y-axis or on origin
x =int(input("Enter x-corr of axis: "))
y =int(input("Enter y-corr of axis: "))
if(x==0 and y==0):
    print("points are on origin: ")
elif(x==0 and y>0):
    print("point will be on y-axis: ")
elif(y==0 and x>0):
    print("points are on x-axis: ")
elif(x>0 and y>0):
    print("point in in 1st corr.")
elif(x<0 and y>0):
    print("in 2nd corr.")
elif(y<0 and x>0):
    print("point are in 4th corr.")
else:
    print("points are in 3rd corr.")
