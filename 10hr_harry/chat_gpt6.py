#write a program that reads the content of the file
#named input,txt and write hem a new file name output.txt

with open("input.txt") as f:
   content =  f.read()

with open("output.txt","w") as f:
    f.write(content)