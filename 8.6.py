mat1 =[[1,2,3,4],[5,6,7,8],[9,10,11,12]]
mat2 =[[1,2,3,4],[5,6,7,8],[9,10,11,12]]
mat3 =[[0,0,0,0],[0,0,0,0],[0,0,0,0]]
#itrate through row
for i in range(len(mat1)):
    #itrate through column
    for j in range(len(mat1[0])):
        mat3[i][j] = mat1[i][j]+mat2[i][j]
print(mat3)
