def setZeros(matrix):
    rows=len(matrix)
    cols=len(matrix[0])

    first_rows_zero=False
    first_cols_zero=False

    #check if first col has zero
    for i in range(rows):
        if matrix[i][0]==0:
            first_rows_zero=True
            
    for j in range(cols):
        if matrix[0][j]==0:
            first_cols_zero=True
            
    #mark rows and col to be zero        
    for i in range(1, rows):
        for j in range(1, cols):
            if matrix[i][j]==0:
                matrix[i][0]=0
                matrix[0][j]=0
    for i in range(1, rows):
        for j in range(1, cols):
            if matrix[i][0]==0 or matrix[0][j]==0:
                matrix[i][j]=0
    if first_rows_zero:
        for j in range(cols):
            matrix[0][j]=0
    if first_cols_zero:
        for i in range(rows):
            matrix[i][0]=0
    return matrix
matrix = [
  [1, 1, 1],
  [1, 0, 1],
  [1, 1, 1]
]
print(setZeros(matrix))
