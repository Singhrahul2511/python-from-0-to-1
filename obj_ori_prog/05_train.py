from random import randint

class Train:
    def __init__(self,trainNo):
        self.trainNo = trainNo


    def book(self,fro,to):
        print(f"ticket is booked in train no: {self.trainNo} from {fro} to {to}")

    def getstatus(self):
        print(f"Train no : {self.trainNo} is running on time")

    def getFare(self,fro,to):
        print(f"ticket fare in train no: {self.trainNo} from {fro} to {to} is {randint(222,5555)}")

t = Train(12345)
t.book("ghoraha", "delhi")
t.getstatus()
t.getFare("ghoraha","delhi")