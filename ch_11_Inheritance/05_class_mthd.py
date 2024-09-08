class Employee:
    a=2
    @classmethod

    # def show(self):
    def show(cls):
        print(f"the class attribute of a is {cls.a}")
e = Employee()
e.a =45
e.show()
#so it's not showing 2 as a class attribute and it's showing instance attribute.
#so to avoid this i will use class decoraters

