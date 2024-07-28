import random
''' 1 for snake
    -1 for water
     0 for gun
'''
computer = random.choice([-1,0,1])
yourstr = input("Enter your choice: ")
youDict = {"s": 1,"w":-1,"g":0}
reversedit = {1: "sanke",-1:"water",0: "gun"}
you = youDict[yourstr]
print(f"you chose {reversedit[you]}\n computer chose {reversedit[computer]}")
if (computer == you):
    print("it's a draw: ")
else:
    if((computer-you)==-1 or (computer-you)==2):
        print("you lose: ")
    else:
        print("you win! ")
