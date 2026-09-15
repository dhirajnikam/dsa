def q01(): return "O(n)"          # single pass
def q02(): return "O(n^2)"        # nested loops over n
def q03(): return "O(log n)"      # halving
def q04(): return "O(n log n)"    # sort dominates the linear scan
def q05(): return "O(n + m)"      # sequential loops over different inputs add
def q06(): return "O(2^n)"        # naive Fibonacci: two recursive calls per level
def q07(): return "O(log n)"      # binary search halves the range
def q08(): return "O(n^2)"        # each += copies the string built so far
def q09(): return "O(n * m)"      # `in list` is O(m) inside an O(n) loop
def q10(): return "O(n)"          # `in set` is O(1)
def q11(): return "O(n^3)"        # three nested dependent loops still ~n^3/6
def q12(): return "O(sqrt n)"     # i grows until i*i > n
def q13(): return "O(n log k)"    # heap of size k, n pushes
def q14(): return "O(n!)"         # all permutations
def q15(): return "O(2^n)"        # n * 2^n; polynomial factor dropped by convention
def q16(): return "O(n^2)"        # inner loop is n/2, still linear, nested in n
def q17(): return "O(n)"          # dict get/set are O(1)
def q18(): return "O(n * m)"      # every cell once
def q19(): return "O(n log n)"    # T(n) = 2T(n/2) + O(n): merge sort
def q20(): return "O(n^2)"        # insert(0) shifts everything: O(n) per insert
