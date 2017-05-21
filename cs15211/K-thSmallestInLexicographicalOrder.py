__source__ = 'https://github.com/kamyu104/LeetCode/blob/master/Python/k-th-smallest-in-lexicographical-order.py'
# Time:  O(logn)
# Space: O(logn)

#
# Description:
# Given integers n and k, find the lexicographically k-th smallest integer in the range from 1 to n.
#
# Note: 1 <= k <= n <= 109.
#
# Example:
#
# Input:
# n: 13   k: 2
#
# Output:
# 10
#
# Explanation:
# The lexicographical order is [1, 10, 11, 12, 13, 2, 3, 4, 5, 6, 7, 8, 9],
# so the second smallest number is 10.
#  Hulu

import unittest
class Solution(object):
    def findKthNumber(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        result = 0

        cnts = [0] * 10
        for i in xrange(1, 10):
            cnts[i] = cnts[i - 1] * 10 + 1

        nums = []
        i = n
        while i:
            nums.append(i % 10)
            i /= 10

        total, target = n, 0
        i = len(nums) - 1
        while i >= 0 and k > 0:
            target = target*10 + nums[i]
            start = int(i == len(nums)-1)
            for j in xrange(start, 10):
                candidate = result*10 + j
                if candidate < target:
                    num = cnts[i+1]
                elif candidate > target:
                    num = cnts[i]
                else:
                    num = total - cnts[i + 1]*(j-start) - cnts[i]*(9-j)
                if k > num:
                    k -= num
                else:
                    result = candidate
                    k -= 1
                    total = num-1
                    break
            i -= 1

        return result


# Time:  O(logn * logn)
# Space: O(logn)
class Solution2(object):
    def findKthNumber(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        def count(n, prefix):
            result, number = 0, 1
            while prefix <= n:
                result += number
                prefix *= 10
                number *= 10
            result -= max(number/10 - (n - prefix/10 + 1), 0)
            return result

        def findKthNumberHelper(n, k, cur, index):
            if cur:
                index += 1
                if index == k:
                    return (cur, index)

            i = int(cur == 0)
            while i <= 9:
                cur = cur * 10 + i
                cnt = count(n, cur)
                if k > cnt + index:
                    index += cnt
                elif cur <= n:
                    result = findKthNumberHelper(n, k, cur, index)
                    if result[0]:
                        return result
                i += 1
                cur /= 10
            return (0, index)

        return findKthNumberHelper(n, k, 0, 0)[0]

class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)


if __name__ == '__main__':
    unittest.main()

Java = '''
#Thought: https://discuss.leetcode.com/topic/64624/concise-easy-to-understand-java-5ms-solution-with-explaination
Initially, image you are at node 1 (variable: curr),
the goal is move (k - 1) steps to the target node x. (substract steps from k after moving)
when k is down to 0, curr will be finally at node x, there you get the result.

we don't really need to do a exact k steps preorder traverse of the denary tree,
the idea is to calculate the steps between curr and curr + 1
(neighbor nodes in same level), in order to skip some unnecessary moves.

Main function
Firstly, calculate how many steps curr need to move to curr + 1.

if the steps <= k, we know we can move to curr + 1, and narrow down k to k - steps.

else if the steps > k, that means the curr + 1 is actually behind the target node x in the preorder path,
we can't jump to curr + 1. What we have to do is to move forward only 1 step (curr * 10 is always next preorder node)
and repeat the iteration.

calSteps function

how to calculate the steps between curr and curr + 1?
Here we come up a idea to calculate by level.
Let n1 = curr, n2 = curr + 1.
n2 is always the next right node beside n1's right most node (who shares the same ancestor "curr")
(refer to the pic, 2 is right next to 1, 20 is right next to 19, 200 is right next to 199).

so, if n2 <= n, what means n1's right most node exists, we can simply add the number of nodes from n1 to n2 to steps.

else if n2 > n, what means n (the biggest node) is on the path between n1 to n2, add (n + 1 - n1) to steps.

organize this flow to "steps += Math.min(n + 1, n2) - n1; n1 *= 10; n2 *= 10;"

public class Solution {
    public int findKthNumber(int n, int k) {
        int curr = 1;
        k = k - 1;
        while (k > 0) {
            int steps = calSteps(n, curr, curr + 1);
            if (steps <= k) {
                curr += 1;
                k -= steps;
            } else {
                curr *= 10;
                k -= 1;
            }
        }
        return curr;
    }
    //use long in case of overflow
    public int calSteps(int n, long n1, long n2) {
        int steps = 0;
        while (n1 <= n) {
            steps += Math.min(n + 1, n2) - n1;
            n1 *= 10;
            n2 *= 10;
        }
        return steps;
    }
}
'''