with open("log.txt") as f:
    lines = f.readlines()
lineno = 1
for line in lines:
    if("python" in line):
        print("yes python is present: ")
        break
    lineno +=1
else:
    print("no python is not present: ")