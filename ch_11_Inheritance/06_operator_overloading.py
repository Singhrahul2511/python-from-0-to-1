class Number:
    def __init__(self,n):
        self.n = n

    def __add__(self,num):
        return self.n +num.n
    #before this def__add__ if you will try to sum then it will not execute it will show unsupported file
n = Number(1)
m= Number(2)
print(n+m)
        