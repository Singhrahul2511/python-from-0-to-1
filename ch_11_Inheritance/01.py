class Employee:
    company = "ITC"
    name = "Rahul"
    language = "python"
    def show(self):
        print(f"the name of the Employee is {self.name} and company is {self.company}")

# class programmer:
#     company = "ITC Infotech"
#     def show(self):
#         print(f"the name is {self.name} and the slary is {self.salary}")

#     def showLanguage(self):
#         print(f"the name is {self.name} and he is good with {self.language} language")

#instead of doing this i can use inheritance here to inherite the Employee class so that i will not
#need to change the things again and again

class programmer(Employee):
    company = 'ITC Infotech'
    name = "Rahul"
    def showLanguage(self):
        print(f"the name is {self.company} and he is good with {self.language} language ")

a =Employee()
b =programmer()
print(a.company,b.company)
b.show()
b.showLanguage()