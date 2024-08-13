#accessing of tuple

tpl = (12,'Rahul',6.4,int(True))
print(tpl)

msg =('like','shere','subscribe','join')
print(msg[1],msg[3])

#looping in tuple

tpl = (912,34,53,21,34)
i=0

while i<len(tpl):
    print(tpl[i])
    i +=1
for n in tpl:
    if(n==1):
        break
print(tpl)

#use of enumerate() function

tpl = (10,20,30,40,50)
for index,n in enumerate(tpl):
    print(index,n)