with open("file1.txt") as f:
    content1 = f.read()

with open("poem.txt") as f:
    content2 = f.read()

if(content1 == content2):
    print("both are similar: ")
else:
    print("not similer: ")