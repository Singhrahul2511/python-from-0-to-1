#suppose a list contains several words.write a program to create a list of 1st char
#of each word present in the list

words = ['rahul','rohit','munna','golu']
f_char =[]
for word in words:
    f_char.append(word[0])
print(f"1st char is {f_char}: ")
