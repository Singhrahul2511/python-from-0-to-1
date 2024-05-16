names = ['anil','amol','aditya','avi','alka']
names.insert(2,'anju')
names.append('Zulu')
names.remove('avi')
index_aditya = names.index('aditya')
names[index_aditya]= 'Rahul'
names.sort()
rev_names = list(reversed(names))
rev_names.sort()
print(rev_names)
