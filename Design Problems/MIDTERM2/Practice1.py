# Lec 20 examples

def shift_list(L):
    """ (List) -> List
    """
    first = L[0]
    for i in range(len(L)-1):
        L[i] = L[i+1]
    L[-1] = first

    return L


# print(shift_list([1,2,3,4]))

def calculate_student_avg(students):
    """ (List) -> list
    [[70,80,90],[80,90,100]] -> [80,90]
    """
    avgs = []  # Make a return list
    for student in students:
        sum_grades = 0
        for grade in student:
            sum_grades += grade
        avgs.append(sum_grades/len(student))

    return avgs

# print(calculate_student_avg([[70,80,90],[80,90,100]]))


def add_matrices(M, N):
    """ (List) -> List
    M = [[1, 2, 3],
         [2, 4, 6]]
    N = [[4, 3, 2],
         [8, 6, 4]]
    """

    sum_matrix = []
    rows = len(M)
    cols = len(M[0])

    # Need an accumulator

    for i in range(rows):
        sum_matrix.append([0]*cols)

    # Add element wise
    for i in range(rows):
        for j in range(cols):
            sum_matrix[i][j] = M[i][j] + N[i][j]

    return sum_matrix


print(add_matrices([[1, 2, 3],
         [2, 4, 6]], [[1, 2, 3],
         [2, 4, 6]]))

# Matrix multiplication

X = [[2, 2],
     [1, 3]]
Y = [[1, 1],
     [1, 2]]

rows = len(X)
cols = len(X[0])

# Initialize an empty matrix
M = []
for i in range(rows):
    M.append([0]*cols)

print(M)

for i in range(rows):
    for j in range(cols):
        M[i][j] = X[i][0] * Y[0][j] + X[i][1] * Y[1][j]


print(M)


