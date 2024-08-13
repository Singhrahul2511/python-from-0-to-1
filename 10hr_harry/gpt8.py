with open("number.txt","w") as f:
    numbers = [1,2,3,4,5,6,7,8,9,10]
    for number in numbers:
        f.write(f"{number}")


with open("number.txt",) as f:
    content = f.readlines()

numbers = [int(line.strip()) for line in content]
summation = sum(numbers)
with open("result.txt", "w") as f:
    f.write(str(summation))
