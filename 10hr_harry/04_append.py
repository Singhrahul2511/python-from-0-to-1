# st = "hay rahul how are you"
# f = open("myjile.py","a")
# f.write(st)
# f.close()

#you can perform the saame thing by using "with"
with open("file.txt") as f:
    print(f.read())