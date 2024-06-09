#a lst contains roll number,names and age of student .write a python prg to gather
#all the name of this list to another list

lst =[('A101','Rahul',20),('A102','Rohit',17),('A103','sonu',23)]
nlst =[]
for ele in lst:
    nlst = nlst+[ele[1]]
print(nlst)