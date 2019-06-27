# 1.6 Given an image represented by an
# NxN matrix, where each pixel in the image is 4 bytes,
# write a method to rotate image by 90 ( write a program
# for both clockwise and anticlockwise rotation). Can you do
# this in place?


def matrix_clockwise_rotation(matrix):

    nrow = len(matrix)
    ncol = len(matrix[0])

    if nrow != ncol:
        raise Exception("Given matrix must be square matrix")

    last = nrow - 1

    # Number of layers
    for x in range(0, nrow//2):

        # Swap 4 element in a group
        for y in range(x, last - x):
            temp = matrix[x][y]
            matrix[x][y] = matrix[last-y][x]
            matrix[last-y][x] = matrix[last-x][last-y]
            matrix[last-x][last-y] = matrix[y][last-x]
            matrix[y][last-x] = temp


def matrix_anticlockwise_rotation(matrix):
    nrow = len(matrix)
    ncol = len(matrix[0])

    if nrow != ncol:
        raise Exception("Given matrix must be square matrix")

    last = nrow - 1

    for x in range(0, nrow//2):
        for y in range(x, last - x):
            temp = matrix[x][y]
            matrix[x][y] = matrix[y][last-x]
            matrix[y][last-x] = matrix[last-x][last -y ]
            matrix[last - x][last-y] = matrix[last - y][x]
            matrix[last - y][x] = temp

if __name__ == "__main__":
    mat1 = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12],
        [13, 14, 15, 16]
    ]
    mat1ClockRotation = [
        [13, 9, 5, 1],
        [14, 10, 6, 2],
        [15, 11, 7, 3],
        [16, 12, 8, 4]
    ]
    mat2 = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12],
        [13, 14, 15, 16]
    ]

    mat2AntiClockRotation = [
        [4, 8, 12, 16],
        [3, 7, 11, 15],
        [2, 6, 10, 14],
        [1, 5, 9, 13]
    ]

    matrix_clockwise_rotation(mat1)
    print(mat1 == mat1ClockRotation)

    matrix_anticlockwise_rotation(mat2)
    print(mat2 == mat2AntiClockRotation)
