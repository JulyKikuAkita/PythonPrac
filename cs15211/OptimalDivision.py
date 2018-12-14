__source__ = 'https://leetcode.com/problems/optimal-division/'
# Time:  O(n)
# Space: O(n)
#
# Description: 553. Optimal Division
#
# Given a list of positive integers, the adjacent integers will perform the float division.
# For example, [2,3,4] -> 2 / 3 / 4.
#
# However, you can add any number of parenthesis at any position to change the priority of operations.
# You should find out how to add parenthesis to get the maximum result, and return the corresponding
# expression in string format. Your expression should NOT contain redundant parenthesis.
#
# Example:
# Input: [1000,100,10,2]
# Output: "1000/(100/10/2)"
# Explanation:
# 1000/(100/10/2) = 1000/((100/10)/2) = 200
# However, the bold parenthesis in "1000/((100/10)/2)" are redundant,
# since they don't influence the operation priority. So you should return "1000/(100/10/2)".
#
# Other cases:
# 1000/(100/10)/2 = 50
# 1000/(100/(10/2)) = 50
# 1000/100/10/2 = 0.5
# 1000/100/(10/2) = 2
# Note:
#
# The length of the input array is [1, 10].
# Elements in the given array will be in range [2, 1000].
# There is only one optimal division for each test case.
# Hide Company Tags Amazon
# Hide Tags Math String
#
import unittest
# Python, Straightforward with Explanation (Insightful Approach)
# Regardless of parentheses, every element is either in the numerator or denominator of the final fraction.
# The expression A[0] / ( A[1] / A[2] / ... / A[N-1] ) has every element in the numerator except A[1],
# and it is impossible for A[1] to be in the numerator, so it is the largest.
#  We must also be careful with corner cases.
# 28ms 28%
class Solution(object):
    def optimalDivision(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        A = map(str, nums)
        if len(A) <= 2: return '/'.join(A)
        return '{}/({})'.format(A[0], '/'.join(A[1:]))


class FooTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        pass

    @classmethod
    def tearDownClass(cls):
        pass

    def setupDown(self):
        pass

    def tearDown(self):
        pass

    def test_foo(self):
        self.assertEqual(1, 1)


class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)


if __name__ == '__main__':
    unittest.main()

Java = '''
# Thought: https://leetcode.com/problems/optimal-division/solution/

Easy to understand simple O(n) solution with explanation
X1/X2/X3/../Xn will always be equal to (X1/X2) * Y, no matter how you place parentheses.
i.e no matter how you place parentheses, X1 always goes to the numerator and X2 always goes to the denominator.
Hence you just need to maximize Y. And Y is maximized when it is equal to X3 *..*Xn.
So the answer is always X1/(X2/X3/../Xn) = (X1 *X3 *..*Xn)/X2

# 5ms 59.76%
class Solution {
    public String optimalDivision(int[] nums) {
        if (nums == null || nums.length == 0) return null;
        StringBuilder sb = new StringBuilder();
        sb.append(nums[0]);
        for (int i = 1; i < nums.length; i++) {
            if (i == 1 && nums.length > 2) {
                sb.append("/(").append(nums[i]);
            } else {
                sb.append("/").append(nums[i]);
            }
        }
        return nums.length > 2 ? sb.append(")").toString() : sb.toString();
    }
}

# backtracking
# TLE
class Solution {
    class Result {
        String str;
        double val;
    }

    public String optimalDivision(int[] nums) {
        int len = nums.length;
        return getMax(nums, 0, len - 1).str;
    }

    private Result getMax(int[] nums, int start, int end) {
        Result r = new Result();
        r.val = -1.0;

        if (start == end) {
            r.str = nums[start] + "";
            r.val = (double)nums[start];
        }
        else if (start + 1 == end) {
            r.str = nums[start] + "/" + nums[end];
            r.val = (double)nums[start] / (double)nums[end];
        }
        else {
            for (int i = start; i < end; i++) {
                Result r1 = getMax(nums, start, i);
                Result r2 = getMin(nums, i + 1, end);
                if (r1.val / r2.val > r.val) {
                    r.str = r1.str + "/" + (end - i >= 2 ? "(" + r2.str + ")" : r2.str);
                    r.val = r1.val / r2.val;
                }
            }
        }

        System.out.println("getMax " + start + " " + end + "->" + r.str + ":" + r.val);
        return r;
    }

    private Result getMin(int[] nums, int start, int end) {
        Result r = new Result();
        r.val = Double.MAX_VALUE;

        if (start == end) {
            r.str = nums[start] + "";
            r.val = (double)nums[start];
        }
        else if (start + 1 == end) {
            r.str = nums[start] + "/" + nums[end];
            r.val = (double)nums[start] / (double)nums[end];
        }
        else {
            for (int i = start; i < end; i++) {
                Result r1 = getMin(nums, start, i);
                Result r2 = getMax(nums, i + 1, end);
                if (r1.val / r2.val < r.val) {
                    r.str = r1.str + "/" + (end - i >= 2 ? "(" + r2.str + ")" : r2.str);
                    r.val = r1.val / r2.val;
                }
            }
        }

        System.out.println("getMin " + start + " " + end + "->" + r.str + ":" + r.val);
        return r;
    }
}

'''