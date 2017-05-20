'''
# https://leetcode.com/forums/viewtopic.php?f=4&t=146&mc_cid=83951cfa08&mc_eid=cad0363a72
Given array a, and b.
Merge them into one array c, keep the order of elements in each array.
There are many possible results for c.
Your solution should randomly generate one of them with same probability.

For example, a = [1], b = [100, 200].
Then possible results may be [1, 100, 200], [100, 1, 200], or, [100, 200, 1].
And your algorithm should have 1/3 probability to generate each of them.

What the complexity of your time / extra space?
What if we treat [1,1] as duplicates?
Let me give another clearer example to illustrate this:
Given a = [1], b = [1, 2].
The possible results may be [1, 1, 2], [1, 1, 2], or [1, 2, 1].
Since two of the results are duplicate, should [1, 1, 2] appears with 1/2 probability instead of 1/3 probability?
If yes, you need to first determine how many duplicate results are there by merging all possibilities, which may be tricky.



Then the probability of choosing the first element from a vs the first element from b is
m/(m+n) and n/(m+n) respectively.
Keep repeating the previous step until one of the array run out of elements (which the probability becomes zero).

Runtime complexity is O(m + n) and no extra space (except for storing the output array c).
'''
from random import *


class Solution:
    a = map(int, raw_input().split())
    b = map(int, raw_input().split())

    def C(self, m, n):
        f = lambda x, y: y <= 0 and 1 or x * f(x - 1, y - 1)
        return f(m, n) / f(n, n)


    def solve(self, a, b):
        l = []
        m, n = len(a), len(b)
        i, j = 0, 0

        while m > 0 and n > 0:
            L1, L2 = self.C(m - 1 + n, m - 1), self.C(m + n - 1, n - 1)
            if randint(1, L1 + L2) > L1:
                l.append(b[j])
                j, n = j + 1, n - 1
            else:
                l.append(a[i])
                i, m = i + 1, m - 1

        if m > 0:
            l += a[i:]
        elif n > 0:
            l += b[j:]

        return l