

#Task 06: Matrix Compression

def compress_matrix(mat):
  row,col= (len(mat),len(mat[0]))
  new_arr= np.zeros((row//2, col//2),dtype=int)
  x=0
  y=0
  for i in range(0,row,2):
    for j in range (0,col,2):
       new_arr[x][y]= mat[i][j] + mat[i+1][j] + mat[i][j+1] + mat[i+1][j+1]
       y+=1
    x+=1
    y=0
  return new_arr

matrix=np.array([[1,2,3,4],
                 [5,6,7,8],
                 [1,3,5,2],
                 [-2,0,6,-3]
                 ])
print_matrix(matrix)
print("...............")
returned_array=compress_matrix(matrix)
print_matrix(returned_array)
#This should print

#|  14  |  22 |
#--------------
#|  2  |  10  |
#--------------