# 1.7 Write an algorithm such that if an element in an
# MxN matrix is 0, its entire row and column are set to 0


def matrix_set_zero(mat):

    nrow = len(mat)
    ncol = len(mat[0])

    row_tracker = [0 for _ in range(nrow)]
    col_tracker = [0 for _ in range(ncol)]

    for x in range(0, nrow):
        for y in range(0, ncol):
            if mat[x][y] == 0:
                row_tracker[x] = 1
                col_tracker[y] = 1

    for x in range(nrow):
        for y in range(ncol):
            if row_tracker[x] == 1 or col_tracker[y] == 1:
                mat[x][y] = 0

if __name__ == "__main__":
    mat1 = [[1, 2, 3], [4, 0, 5], [0, 7, 10]]
    mat1set0 = [[0, 0, 3], [0, 0, 0], [0, 0, 0]]

    matrix_set_zero(mat1)
    print(mat1 == mat1set0)

    mat2 = [
        [1, 2, 3, 4],
        [0, 1, 2, 5],
        [2, 1, 3, 0]
    ]
    mat2set0 = [
        [0, 2, 3, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0]
    ]

    matrix_set_zero(mat2)
    print(mat2 == mat2set0)
