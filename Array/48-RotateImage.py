def rotate(matrix):

    for i in range(0,len(matrix)):
        for j in range(i+1, len(matrix)):
            matrix[i][j], matrix[j][i]=matrix[j][i], matrix[i][j]
    for row in matrix:
        row.reverse()
    return matrix

matrix=[[1,2,3],[4,5,6],[7,8,9]]
print(rotate(matrix))
