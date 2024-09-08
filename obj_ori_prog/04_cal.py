class Calculator:
    def __init__(self,n):
        self.n =n

    def square(self):
        print(f"the square is {self.n*self.n}")
    def cube(self):
        print(f"the cube is {self.n*self.n*self.n}")
    def sq_root(self):
        print(f"the sq_root is {self.n**1/2}")
    @staticmethod
    def hello():
        print("hello there! ")
a = Calculator(4)
a.hello()
a.square()
a.cube()
a.sq_root()