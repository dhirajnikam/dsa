"""
Problem: Mock interview 6 - Accounts Merge
Difficulty: Medium | Pattern: Union-find (or graph DFS) over emails
Source: LeetCode 721

Interviewer says:
  "We have a list of accounts. Each is a name followed by some emails. Two accounts belong
   to the same person if they share any email. Merge them."

Ask about: can two different people have the same name? Can the same email appear in
accounts with different names (answer: no, an email identifies one person)? Output format
and order? Is merging transitive (A shares with B, B shares with C)? Sizes?

Hints (constraints you should have asked about):
1. accounts[i][0] is the name, the rest are emails. Up to 1000 accounts, up to 10 emails
   each. Same name does NOT imply same person; a shared email does, and it is transitive.
   Each email belongs to exactly one person, so a merged group has a single name.
2. Output: one list per person: [name, sorted emails...]. Groups may be in any order.
3. Union-find over account indices: map email -> first account index seen; when an email
   is seen again, union the two indices. Then collect emails per root, sort, prepend name.
4. Alternative: build a graph email <-> email within each account and DFS; also O(N log N)
   because of the final sort.

Expected: O(N alpha(N) + M log M) time where N = total emails, M = emails per group; O(N) space
"""
from collections import defaultdict


def accounts_merge(accounts: list[list[str]]) -> list[list[str]]:
    raise NotImplementedError


if __name__ == "__main__":
    def norm(result):
        return sorted(result)

    accounts = [
        ["John", "johnsmith@mail.com", "john_newyork@mail.com"],
        ["John", "johnsmith@mail.com", "john00@mail.com"],
        ["Mary", "mary@mail.com"],
        ["John", "johnnybravo@mail.com"],
    ]
    expected = [
        ["John", "john00@mail.com", "john_newyork@mail.com", "johnsmith@mail.com"],
        ["John", "johnnybravo@mail.com"],
        ["Mary", "mary@mail.com"],
    ]
    assert norm(accounts_merge(accounts)) == norm(expected)

    assert accounts_merge([]) == []
    assert accounts_merge([["A", "a@x.com"]]) == [["A", "a@x.com"]]

    chain = [["G", "a@x", "b@x"], ["G", "c@x", "d@x"], ["G", "b@x", "c@x"]]
    assert accounts_merge(chain) == [["G", "a@x", "b@x", "c@x", "d@x"]]

    same_name_different_people = [["Ann", "a1@x"], ["Ann", "a2@x"]]
    assert norm(accounts_merge(same_name_different_people)) == [["Ann", "a1@x"], ["Ann", "a2@x"]]

    dup_within = [["Bo", "b@x", "b@x", "c@x"]]
    assert accounts_merge(dup_within) == [["Bo", "b@x", "c@x"]]

    star = [["S", "hub@x"], ["S", "hub@x", "l1@x"], ["S", "hub@x", "l2@x"], ["S", "l3@x", "hub@x"]]
    assert accounts_merge(star) == [["S", "hub@x", "l1@x", "l2@x", "l3@x"]]
    print("ok")
