class Employee:
    a=1

class Programmer(Employee):
    b=2

class Manager(Programmer):
    c =3
class rahul(Manager):
    d =4
o = Employee()
print(o.a,) # if i will take o.b then it will display an error
o = rahul()
print(o.a,o.b,o.c,o.d)
print(o.a,o.b)