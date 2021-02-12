# rotate matrix: given an image N x N matrix, each pixel represented by int, rotate 90 degrees
# try to do in place

# clarifying Q: does it matter which direction? -> assume no
from typing import List

def _transpose_matrix(matrix: List[List[int]]) -> List[List[int]]:
    N = len(matrix)
    # matrix is NxN
    for i in range(N):
        # start j at i so that we can stay on the diagonal
        for j in range(i, N):
            # swap across the diagonal
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    return matrix

def _flip_matrix_horizontally(matrix: List[List[int]]) -> List[List[int]]:
    N = len(matrix)
    # we still want to operate row by row
    for i in range(N):
        # but now range for j is [0, N/2] to avoid swapping same elements 2x
        for j in range(N//2):
            matrix[i][j], matrix[i][(N - 1 - j)] = matrix[i][(N - 1 - j)], matrix[i][j]
    return matrix


def rotate_matrix_90_cw(matrix: List[List[int]]) -> List[List[int]]:
    print(_flip_matrix_horizontally(_transpose_matrix(matrix)))


# time complexity: O(N), space O(1) b/c inplace

if __name__ == "__main__":
    matrix = [[1,2,3,4], [5,6,7,8], [9,10,11,12], [13,14,15,16]]
    rotate_matrix_90_cw(matrix)
