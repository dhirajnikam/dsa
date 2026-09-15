"""
Problem: Complexity quiz
Difficulty: Easy | Topic: reading code and naming its Big-O

Each function below corresponds to a snippet. Return the TIME complexity as a string using exactly
one of these spellings:
  "O(1)", "O(log n)", "O(sqrt n)", "O(n)", "O(n log n)", "O(n^2)", "O(n^3)", "O(2^n)", "O(n!)",
  "O(n + m)", "O(n * m)", "O(n * k)", "O(n log k)"
Where a snippet has two inputs, n and m (or n and k) are their sizes.

q01:  for x in nums: total += x
q02:  for i in range(n): for j in range(n): grid[i][j] = 0
q03:  while n > 1: n //= 2
q04:  nums.sort(); for x in nums: ...
q05:  for x in a: ...   then separately   for y in b: ...      (len(a) = n, len(b) = m)
q06:  def f(n): return 1 if n < 2 else f(n-1) + f(n-2)       (naive Fibonacci)
q07:  lo, hi = 0, len(a) - 1; while lo <= hi: mid = ...; halve the range   (binary search)
q08:  s = ""; for x in nums: s += str(x)                     (string concatenation in a loop)
q09:  for x in nums: if x in other_list: ...                  (len(nums) = n, len(other_list) = m)
q10:  for x in nums: if x in other_set: ...                   (set membership)
q11:  for i in range(n): for j in range(i, n): for k in range(j, n): ...
q12:  i = 2; while i * i <= n: i += 1
q13:  for x in nums: heapq.heappush(h, x); if len(h) > k: heapq.heappop(h)   (len(nums) = n)
q14:  from itertools import permutations; for p in permutations(nums): ...
q15:  for mask in range(1 << n): for i in range(n): if mask >> i & 1: ...
q16:  for i in range(n): j = n; while j > 0: j -= 2
q17:  d = {}; for x in nums: d[x] = d.get(x, 0) + 1
q18:  for row in grid: for cell in row: ...                   (n rows, m columns)
q19:  def f(a): if len(a) <= 1: return a; mid = len(a)//2; return merge(f(a[:mid]), f(a[mid:]))  (merge is linear)
q20:  for x in nums: nums2.insert(0, x)                       (insert at the front of a list, n items)

Hints:
8. Each += copies the whole string built so far.
15. 2^n masks times n bits is n * 2^n. The list has no such entry: answer "O(2^n)" (dropping the polynomial factor next to an exponential is a common interview convention; say "n times 2^n" out loud).
16. The inner loop is n/2 iterations, still linear.
19. Merge sort recurrence.
"""


def q01() -> str: raise NotImplementedError
def q02() -> str: raise NotImplementedError
def q03() -> str: raise NotImplementedError
def q04() -> str: raise NotImplementedError
def q05() -> str: raise NotImplementedError
def q06() -> str: raise NotImplementedError
def q07() -> str: raise NotImplementedError
def q08() -> str: raise NotImplementedError
def q09() -> str: raise NotImplementedError
def q10() -> str: raise NotImplementedError
def q11() -> str: raise NotImplementedError
def q12() -> str: raise NotImplementedError
def q13() -> str: raise NotImplementedError
def q14() -> str: raise NotImplementedError
def q15() -> str: raise NotImplementedError
def q16() -> str: raise NotImplementedError
def q17() -> str: raise NotImplementedError
def q18() -> str: raise NotImplementedError
def q19() -> str: raise NotImplementedError
def q20() -> str: raise NotImplementedError


if __name__ == "__main__":
    norm = lambda s: s.replace(" ", "").lower()
    expected = {
        q01: "O(n)", q02: "O(n^2)", q03: "O(log n)", q04: "O(n log n)", q05: "O(n + m)",
        q06: "O(2^n)", q07: "O(log n)", q08: "O(n^2)", q09: "O(n * m)", q10: "O(n)",
        q11: "O(n^3)", q12: "O(sqrt n)", q13: "O(n log k)", q14: "O(n!)", q15: "O(2^n)",
        q16: "O(n^2)", q17: "O(n)", q18: "O(n * m)", q19: "O(n log n)", q20: "O(n^2)",
    }
    wrong = [q.__name__ for q, ans in expected.items() if norm(q()) != norm(ans)]
    assert not wrong, f"wrong answers: {wrong}"
    print("ok")
