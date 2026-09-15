def rotate(matrix):
    # O(n^2) time, O(1) space
    # Clockwise 90 degrees = transpose, then reverse every row.
    n = len(matrix)
    for r in range(n):
        for c in range(r + 1, n):
            matrix[r][c], matrix[c][r] = matrix[c][r], matrix[r][c]
    for row in matrix:
        row.reverse()
