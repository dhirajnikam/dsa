def set_zeroes(matrix):
    # O(m*n) time, O(1) space
    # Row 0 / column 0 double as flag arrays for the inner cells; two booleans remember
    # whether row 0 / column 0 themselves must be zeroed. Wipe inner cells first, edges last.
    rows, cols = len(matrix), len(matrix[0])
    zero_row0 = any(v == 0 for v in matrix[0])
    zero_col0 = any(matrix[r][0] == 0 for r in range(rows))
    for r in range(1, rows):
        for c in range(1, cols):
            if matrix[r][c] == 0:
                matrix[r][0] = matrix[0][c] = 0
    for r in range(1, rows):
        for c in range(1, cols):
            if matrix[r][0] == 0 or matrix[0][c] == 0:
                matrix[r][c] = 0
    if zero_row0:
        matrix[0] = [0] * cols
    if zero_col0:
        for r in range(rows):
            matrix[r][0] = 0
