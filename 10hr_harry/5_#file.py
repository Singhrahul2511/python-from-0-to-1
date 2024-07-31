words = ("dunky", "bad","nice")
with open("hash.txt","r") as f:
    content = f.read()

for word in words:
    contentnew = content.replace(word,"#"* len(word))


with open("hash.txt", "w") as f:
    f.write(contentnew)