#program to obtain median value of list of num without distributing order of num in list

lst =[1,2]
lst.sort()
sort_lst =lst
length = len(sort_lst)
if(length%2==1):
    median =sort_lst[length//2]
else:
    mid_rit = sort_lst[length//2-1]
    mid_lft =sort_lst[length//2]
    median = (mid_lft+mid_rit)/2
print(f"median is {median}")
    