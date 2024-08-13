#if there is present anything in a txt file then you can wipe out that content simply
with open("file1.txt","w") as f:
    f.write("")