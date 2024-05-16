#write a prog to find mean median and mode of list of 10 numbers.


num = [1,43,22,43,5,67,75,32,86,21,1]
sumn_num = sum(num)
length = len(num)
mean = sumn_num/length
print(mean)
num.sort()
srted_num = num
print(srted_num)
if(length%2==0):
    mid_rit = srted_num[length//2]
    mid_lft = srted_num[length//2-1]
    median = (mid_lft+mid_rit)/2
    print(median)
else:
    median = srted_num[num//2]
    print(median)