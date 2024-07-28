student = {100:'ajay',350:'ramesh',349:'rahul'}
rollno = int(input("Enter roll no: "))
name = student.get(rollno,'student')
print(f"congratulations {name}!")
rollno = int(input("Enter roll no: "))
name = student.get(rollno,'student')
print('congratulation {name}!')