
# Task 05: Row Rotation Policy of BRACU Classroom
def row_rotation(exam_week, seat_status):
    row, col = (len(seat_status),len(seat_status[0]))
    week = 1
    while week < exam_week:
        temp = [seat_status[row - 1][j] for j in range(col)]
        for i in range(row - 1, 0, -1):
            for j in range(col):
                seat_status[i][j] = seat_status[i - 1][j]
        for j in range(col):
            seat_status[0][j] = temp[j]

        week += 1
    print("Modified Seat Status after row rotation:")
    for i in range(row):
        for j in range(col):
            print(seat_status[i][j], end=" ")
        print()
    for i in range(row):
        for j in range(col):
            if seat_status[i][j] == "AA":
                return i + 1
seat_status = np.array([
    ['A', 'B', 'C', 'D', 'E'],
    ['F', 'G', 'H', 'I', 'J'],
    ['K', 'L', 'M', 'N', 'O'],
    ['P', 'Q', 'R', 'S', 'T'],
    ['U', 'V', 'W', 'X', 'Y'],
    ['Z', 'AA', 'BB', 'CC', 'DD']
])

seat_status = np.array([[ 'A' , 'B' , 'C' , 'D' , 'E'],
                  ['F' , 'G' , 'H' , 'I' , 'J'],
                  ['K' , 'L' , 'M' , 'N' , 'O'],
                  ['P' , 'Q' , 'R' , 'S' , 'T'],
                  ['U' , 'V' , 'W' , 'X' , 'Y'],
                  ['Z' , 'AA' , 'BB' , 'CC' , 'DD']])
exam_week=3
print_matrix(seat_status)
print()
row_number=row_rotation(exam_week, seat_status) #This should print modified seat status after rotation
print(f'Your friend AA will be on row {row_number}') #This should print Your friend AA will be on row 2