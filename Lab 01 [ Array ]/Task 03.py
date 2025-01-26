
#Task 03: Decryption Process

def decrypt_matrix(matrix):
  row,col= (len(matrix),len(matrix[0]))
  arr_2D= np.zeros((1,col),dtype=int)

  for i in range (col):
    for j in range(row):
     arr_2D[0][i]+= matrix[j][i]

  new_arr= np.zeros((1,col-1),dtype=int)

  for j in range(col-1):
    new_arr[0][j]= arr_2D[0][j+1]-arr_2D[0][j]

  return new_arr


matrix=np.array([[1,3,1],
                 [6,4,2],
                 [5,1,7],
                 [9,3,3],
                 [8,5,4]
                 ])

returned_array=decrypt_matrix(matrix)
print(returned_array)
#This should print [-13, 1]