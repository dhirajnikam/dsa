# What a strong candidate says:
# "Does a shared email always mean the same person, even if names differ, and is it
#  transitive? Can two people share a name? Then names are labels, emails are the identity.
#  This is connected components over accounts: an email seen in two accounts unions them.
#  Union-find with path compression; afterwards group emails by root and sort. Sorting
#  dominates at O(N log N)."
from collections import defaultdict


def accounts_merge(accounts):
    # O(N alpha(N) + N log N) time, O(N) space, N = total emails
    # Union account indices through shared emails, then bucket every email under its
    # root account and emit [name] + sorted emails per bucket.
    parent = list(range(len(accounts)))

    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    owner = {}
    for i, acc in enumerate(accounts):
        for email in acc[1:]:
            if email in owner:
                parent[find(i)] = find(owner[email])
            else:
                owner[email] = i

    groups = defaultdict(set)
    for email, i in owner.items():
        groups[find(i)].add(email)
    return [[accounts[root][0]] + sorted(emails) for root, emails in groups.items()]
