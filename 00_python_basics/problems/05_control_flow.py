"""
Problem: Loops and conditions
Difficulty: Warm-up | Topic: for/while, break/continue, nested loops

1. fizzbuzz(n) -> list of strings for 1..n: "Fizz" for multiples of 3,
   "Buzz" for 5, "FizzBuzz" for both, else the number as a string. (LeetCode 412)
2. is_prime(n) -> bool. Trial division up to sqrt(n). n < 2 is not prime.
3. multiplication_table(n) -> n x n list of lists, table[i][j] = (i+1)*(j+1).
4. collatz_steps(n) -> number of steps to reach 1: even -> n/2, odd -> 3n+1.
   collatz_steps(1) == 0, collatz_steps(6) == 8.

Contract details:
n is a non-negative integer for fizzbuzz and multiplication_table.
For collatz_steps, 1 <= n <= 10000. Use integer division for even steps.

Hints:
2. for d in range(2, int(n**0.5) + 1)
3. Nested list comprehension, or two nested for loops with append.
"""


def fizzbuzz(n: int) -> list[str]:
    word_list = []
    for i in range(1, n  + 1):
        if i % 3 == 0 and i % 5 == 0:
            word_list.append("FizzBuzz")
        elif i % 3 == 0:
            word_list.append("Fizz")
        elif i % 5 == 0:
            word_list.append("Buzz")
        else:
            word_list.append(str(i))
    return word_list


def is_prime(n: int) -> bool:
    if n < 2:
        return False
    for d in range(2 , int(n**0.5) + 1):
        if n % d == 0:
            return False
    return True


def multiplication_table(n: int) -> list[list[int]]:
    result = []
    for i in range(1, n + 1):
        row = []
        for j in range(1, n + 1):
            row.append(i * j)
        result.append(row)
    return result    
    


def collatz_steps(n: int) -> int:
    steps = 0
    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            3 * n + 1
        steps += 1
    return steps    



if __name__ == "__main__":
    assert fizzbuzz(15) == ["1", "2", "Fizz", "4", "Buzz", "Fizz", "7", "8", "Fizz", "Buzz", "11", "Fizz", "13", "14", "FizzBuzz"], 'Check: fizzbuzz(15) == ["1", "2", "Fizz", "4", "Buzz", "Fizz", "7", "8", "Fizz", "Buzz", "11", "Fizz", "13", "14", "FizzBuzz"]'
    assert [n for n in range(20) if is_prime(n)] == [2, 3, 5, 7, 11, 13, 17, 19], 'Check: [n for n in range(20) if is_prime(n)] == [2, 3, 5, 7, 11, 13, 17, 19]'
    assert not is_prime(1) and not is_prime(0) and is_prime(97) and not is_prime(99), 'Check: not is_prime(1) and not is_prime(0) and is_prime(97) and not is_prime(99)'
    assert multiplication_table(3) == [[1, 2, 3], [2, 4, 6], [3, 6, 9]], 'Check: multiplication_table(3) == [[1, 2, 3], [2, 4, 6], [3, 6, 9]]'
    assert collatz_steps(1) == 0, 'Check: collatz_steps(1) == 0'
    assert collatz_steps(6) == 8, 'Check: collatz_steps(6) == 8'
    assert collatz_steps(27) == 111, 'Check: collatz_steps(27) == 111'
    # Boundary and misconception checks: predict each result before running.
    assert fizzbuzz(0) == [], 'Check: fizzbuzz(0) == []'
    assert is_prime(-3) is False, 'Check: is_prime(-3) is False'
    assert multiplication_table(0) == [], 'Check: multiplication_table(0) == []'
    matrix = multiplication_table(2)
    matrix[0][0] = 99
    assert matrix[1] == [2, 4], 'Check: matrix[1] == [2, 4]'
    assert collatz_steps(2) == 1, 'Check: collatz_steps(2) == 1'
    assert collatz_steps(3) == 7, 'Check: collatz_steps(3) == 7'
    print("ok")
