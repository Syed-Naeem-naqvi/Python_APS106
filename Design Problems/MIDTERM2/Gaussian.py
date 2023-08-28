def multiply_row_by_k(row, k):
    """
    f([1,2,3,4],2) -> [2,4,6,8]
    """
    for i in range(len(row)):
        row[i] = row[i]*k

    return row


# print(multiply_row_by_k([1,2,3,4], 2))


def add_row_multiple(target, to_add, k):
    """
    target  = target + to_add*k
    """
    for i in range(len(target)):
        target[i] = target[i] + to_add[i]*k
    return target


# print(add_row_multiple([1,1,1,1], [1,0,1,0], 2))


def swap_rows(M, a, b):
    """
    a: index of row 1
    b: index of row 2
    M: matrix
    f([[1,2,3,0],[4,5,6,0],[7,8,9,0]], 0, 1) -> [[4,5,6,0],[1,2,3,0],[7,8,9,0]]
    """

    temporary = M[a]
    M[a] = M[b]
    M[b] = temporary
    return M


# print(swap_rows([[1,2,3,0],[4,5,6,0],[7,8,9,0]],0,1))


def gaussian(M):
    """
    The main function, gets output from the first 3
    """
    first_pivot = M[0][0]
    if first_pivot != 1:
        f1_k = 1/first_pivot
        row_1 = M[0]
        M[0] = multiply_row_by_k(f1_k, row_1)

    pass





