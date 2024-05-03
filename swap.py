# #swappimg of two number without using any kind of third var or not to perform any 
# #arithmetic operation on a and b

# a =1
# b =2
# print(f"before swap {a}, {b}: ")

# a = a^b
# b =a^b
# a =a^b
# print(f"after swapping {a}, {b}: ")

# #also we can use another approch to solve this problem

a =1
b=2
print(f"Before swapping {a}, {b}")
(a,b)  = (b,a)#here i am using tuple to swap two values
print(f"After swappimg {a}, {b}: ")