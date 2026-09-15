def squares_of_evens(nums):
    return [x * x for x in nums if x % 2 == 0]


def word_lengths(words):
    return {w: len(w) for w in words}


def first_letters(words):
    return {w[0].lower() for w in words if w}


def flatten(matrix):
    return [c for row in matrix for c in row]


def transpose(matrix):
    return [[row[j] for row in matrix] for j in range(len(matrix[0]))]
