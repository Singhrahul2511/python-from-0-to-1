#do the following using python


#1 pack 10 mul of 10 into a tuple
tpl = (10,20,30,40,50,60,70,80,90,100)

#2 unpack the tuple into 10 var,each holds one val
a,b,c,d,e,f,g,h,i,j =tpl
print(tpl)
print(a,b,c,d,e,f,g,h,i,j)
x,_,_,_,_,_,_,_,_,y = tpl
print(x,y,_)
i,*_, = tpl
print(i,j,_)