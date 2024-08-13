i=1
while(i<=4):
    j=1
    while(j<=4):
        k=1
        while(k<=4):
            if(i==j or j==k or k==i):
                k =k+1
                continue
            else:
                print(i,j,k)

            k+=1

            j+=1
        i+=1            