M = [[25, -5, -20, 5],
     [-5, 10,  -4, 0],
     [-5, -4,  -9, 0]]

[print(row) for row in M]
print(M)
def print_matrix(m):
    [print(row) for row in m]
def set_diagonal_cell_to_one(m, col):
    for i in range(len(m[col])):
        m[col][i] /= m[col][col]


def set_column_to_zero(m, row, col):
    multiplier = m[row][col]
    for i in range(len(m[row])):
        m[row][i] -= multiplier * m[col][i]   # zero out column zero

def gaussian(m):
    for i in range(len(m)):
        set_diagonal_cell_to_one(m,i)
        print('i = ', i)
        print_matrix(m)
        for row in range(len(m)):
            if row != i:
                set_column_to_zero(m,row,i)
                print('row = ', row)
                print_matrix(m)
print(gaussian(M))