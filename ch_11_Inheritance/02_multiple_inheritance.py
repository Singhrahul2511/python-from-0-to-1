class Employee:
    company = "ITC"
    name = "Rahul"
    def show(self):
        print(f"The name of employee is {self.name} and company name is {self.company}")

class coder:
    language = "python"
    def printLanguage(self):
        print(f"out of all lan here is  your lan : {self.language}")


class programmer(Employee,coder):
    company= "ITC Infotech"
    def showlanguage(self):
        print(f"the name is {self.company} and he is good with {self.language} language")

a =Employee()
b= programmer()
b.show()
b.printLanguage()
b.showlanguage()