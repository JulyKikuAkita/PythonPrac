__source__ = 'https://leetcode.com/problems/paint-fence/#/description'
# https://github.com/kamyu104/LeetCode/blob/master/Python/paint-fence.py
# Time:  O(n)
# Space: O(1)
#
# Description: 276. Paint Fence
#
# There is a fence with n posts, each post can be painted with one of the k colors.
#
# You have to paint all the posts such that no more than two adjacent fence posts have the same color.
#
# Return the total number of ways you can paint the fence.
#
# Note:
# n and k are non-negative integers.
#
# Companies
# Google
# Related Topics
# Dynamic Programming
# Similar Questions
# House Robber House Robber II Paint House Paint House II
#

import unittest
# DP solution with rolling window.
class Solution(object):
    def numWays(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        if n == 0:
            return 0
        elif n == 1:
            return k
        ways = [0] * 3
        ways[0] = k
        ways[1] = (k - 1) * ways[0] + k
        for i in xrange(2, n):
            ways[i % 3] = (k-1) * ( ways[(i-1) % 3 ] + ways[(i-2) % 3 ] )
        return ways[(n-1) % 3]

# Time:  O(n)
# Space: O(n)
# DP solution.
class Solution2(object):
    def numWays(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        if n == 0:
            return 0
        elif n == 1:
            return k
        ways = [0] * n
        ways[0] = k
        ways[1] = (k - 1) * ways[0] + k
        for i in xrange(2, n):
            ways[i] = (k - 1) * (ways[i - 1] + ways[i - 2])
        return ways[n - 1]

class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)

if __name__ == '__main__':
    unittest.main()

Java = '''
#Thought: https://discuss.leetcode.com/topic/23426/o-n-time-java-solution-o-1-space

We divided it into two cases.

the last two posts have the same color, the number of ways to paint in this case is sameColorCounts.

the last two posts have different colors, and the number of ways in this case is diffColorCounts.

The reason why we have these two cases is that we can easily compute both of them, and that is all I do.
When adding a new post, we can use the same color as the last one (if allowed) or different color.
If we use different color, there're k-1 options, and the outcomes shoule belong to the diffColorCounts category.
If we use same color, there's only one option, and we can only do this when the last two have different colors
(which is the diffColorCounts). There we have our induction step.

Here is an example, let's say we have 3 posts and 3 colors. The first two posts we have 9 ways to do them,
(1,1), (1,2), (1,3), (2,1), (2,2), (2,3), (3,1), (3,2), (3,3). Now we know that

diffColorCounts = 6;
And

sameColorCounts = 3;
Now for the third post, we can compute these two variables like this:

If we use different colors than the last one (the second one), these ways can be added into diffColorCounts,
so if the last one is 3, we can use 1 or 2, if it's 1, we can use 2 or 3, etc. Apparently there are
(diffColorCounts + sameColorCounts) * (k-1) possible ways.

If we use the same color as the last one, we would trigger a violation in these three cases (1,1,1), (2,2,2)
and (3,3,3). This is because they already used the same color for the last two posts.
So is there a count that rules out these kind of cases? YES, the diffColorCounts.
So in cases within diffColorCounts, we can use the same color as the last one without worrying about triggering the violation.
And now as we append a same-color post to them, the former diffColorCounts becomes the current sameColorCounts.

Then we can keep going until we reach the n. And finally just sum up these two variables as result.

Hope this would be clearer.
#5.96% 0ms
public class Solution {
    public int numWays(int n, int k) {
        if (n == 0) {
            return 0;
        } else if (n == 1) {
            return k;
        }
        int same = 1;
        int notSame = k - 1;
        for (int i = 2; i < n; i++) {
            int sum = same * (k - 1) + notSame * k;
            same = notSame;
            notSame = sum - same;
        }
        return (same + notSame) * k;
    }
}

#5.96% 0ms
public class Solution {
    public int numWays(int n, int k) {
        if(n == 0) return 0;
        else if(n == 1) return k;
        int diffColorCounts = k*(k-1);
        int sameColorCounts = k;
        for(int i=2; i<n; i++) {
            int temp = diffColorCounts;
            diffColorCounts = (diffColorCounts + sameColorCounts) * (k-1);
            sameColorCounts = temp;
        }
        return diffColorCounts + sameColorCounts;
    }
}

#5.96% 0ms
class Solution {
    public int numWays(int n, int k) {
        if (n == 0) return 0;
        else if (n == 1) return k;

        int sameColorCounts = k;
        int diffColorCounts = k * (k - 1);
        //the last two posts have the same color, the number of ways to paint in this case is sameColorCounts.
        //the last two posts have different colors, and the number of ways in this case is diffColorCounts.
        for (int i = 2; i < n; i++) {
            int newDiffColorCounts = (k - 1) * (sameColorCounts + diffColorCounts);
            sameColorCounts = diffColorCounts;
            diffColorCounts = newDiffColorCounts;
        }
        return sameColorCounts + diffColorCounts;
    }
}
'''
