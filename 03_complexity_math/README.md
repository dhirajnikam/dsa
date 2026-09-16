# How much work does an algorithm do?

[Start here](../README.md) · [Learning path](../ROADMAP.md) · [Checkpoint](CHECKPOINT.md)

**Before this lesson:** Loops and functions from chapter 00. Start with operation counting; maths extras can wait.

**Today:** understand one idea, trace one example, then attempt one function. Reading the entire exercise list is optional.

## The theory

**Time complexity** describes how the number of operations grows with input size n. **Auxiliary space** counts additional storage, including recursive calls. Big-O is an upper growth bound, not a stopwatch reading or an interview readiness score.

One lookup by list index is O(1). Visiting all n items is O(n). Checking every pair can be O(n²). Repeatedly halving a positive search range takes O(log n) steps. Consecutive loops add their costs; nested loops require counting how often the inner work actually happens. Two nested loops are not automatically quadratic.

For two independent input sizes n and m, keep both: O(n+m) or O(nm). A copied slice takes time and space proportional to its length. A recursive algorithm has active calls in memory even when you never create a list.

**Recursion** solves a problem using smaller instances, with a base case that stops. Memoization saves repeated results. Iteration can often keep only the recent results.

For the optional maths exercises: GCD is the greatest shared divisor; LCM is the smallest shared positive multiple (zero requires a separate case). Remainders let Euclid repeatedly shrink the divisor problem. Exponentiation by squaring halves the exponent. A sieve marks multiples to find primes. Bits are base-two digits; AND tests shared bits, OR sets bits, and XOR cancels equal bit values. Modular inverses exist only under the relevant coprimality conditions; the prime-modulus shortcut has additional assumptions.

## Walk through a small example

If a list grows from 10 to 20 items, a scan roughly doubles its visits. Checking all unordered pairs grows from 45 to 190 comparisons. A halving search only needs roughly one additional decision. Count work first; do not infer it from indentation alone.

## Watch for

Ignoring slices or membership scans inside loops; dropping a second input size; forgetting call-stack space; treating a machine-dependent runtime threshold as a theorem.

## Your next small step

Open [count operations](problems/01_count_operations.py). Read its input/output contract before the hints. Write your own trace, then implement one function.

```bash
python learn.py check 03/01
```

Run commands from the repository root. After the code passes, cover it and explain the idea; a green test alone does not prove understanding. Try the [checkpoint](CHECKPOINT.md) before moving on.

<details>
<summary>Browse all exercises in this chapter when you need more practice</summary>

- [Count the operations](problems/01_count_operations.py)
- [gcd and lcm](problems/02_gcd_lcm.py)
- [Fast exponentiation and modular arithmetic](problems/03_fast_power_mod.py)
- [Primes](problems/04_sieve_primes.py)
- [Bit tricks](problems/05_bit_tricks.py)
- [Recursion basics](problems/06_recursion_basics.py)
- [Fibonacci three ways](problems/07_fibonacci_three_ways.py)
- [Complexity quiz](problems/08_complexity_quiz.py)

</details>
