class employee:
    language = "python"
    salary = 1299999

    def getinfo(self):
        print(f"the language is {self.language}. the salary is {self.salary}")
    def greet(self):
        print("good morning: ")

    @staticmethod
    def hello():
        print("hello rahul!: ")


harry = employee()
harry.greet()
harry.getinfo()
harry.hello()