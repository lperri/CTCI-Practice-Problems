# zero matrix: if an element in an MxN matrix is 0, its entire row and column should get set to zero
from typing import List

def set_row_col_to_zero(matrix: List[List[int]]) -> List[List[int]]:
    # mark rows and cols to be set to zero at end
    # interesting catch -- must be set to zero at end as opposed
    # to during the iteration because if there are more than one zero, you will impact other rows
    rows_to_be_zeroed, cols_to_be_zeroed = set(), set()

    for i, row in enumerate(matrix):
        for j, val in enumerate(row):
            if val == 0:
                rows_to_be_zeroed.add(i)
                cols_to_be_zeroed.add(j)

    for i, row in enumerate(matrix):
        for j, val in enumerate(row):
            if i in rows_to_be_zeroed or j in cols_to_be_zeroed:
                matrix[i][j] = 0
    print(rows_to_be_zeroed, cols_to_be_zeroed)
    return matrix


# time complexity: O(mn), space O(m+n)

if __name__ == "__main__":
    test_matrix = [[1,2,3,0], [5,6,7,8], [9,10,11,12], [13,14,15,16]]
    empty_matrix = [[]]
    one_matrix = [[1]]
    print(set_row_col_to_zero(test_matrix))