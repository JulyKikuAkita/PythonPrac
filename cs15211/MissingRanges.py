__source__ = 'https://leetcode.com/problems/missing-ranges/description/'
# https://github.com/kamyu104/LeetCode/blob/master/Python/missing-ranges.py
# Time:  O(n)
# Space: O(1)
#
# Description: Leetcode # 163. Missing Ranges
#
# Given a sorted integer array where the range of elements are [lower, upper] inclusive,
# return its missing ranges.
#
# For example, given [0, 1, 3, 50, 75], lower = 0 and upper = 99,
# return ["2", "4->49", "51->74", "76->99"].
#
# Companies
# Google
# Related Topics
# Array
# Similar Questions
# Summary Ranges
#
import unittest
class Solution:
    # @param A, a list of integers
    # @param lower, an integer
    # @param upper, an integer
    # @return a list of strings
    def findMissingRanges(self, A, lower, upper):
        ranges = []
        pre = lower - 1

        for i in xrange(len(A) + 1):
            if i == len(A):
                cur = upper + 1
            else:
                cur = A[i]
            if cur - pre >= 2:
                ranges.append(self.getRange(pre + 1, cur - 1))
            pre = cur
        return ranges

    def getRange(self, lower, upper):
        if lower == upper:
            return "{}".format(lower)
        else:
            return "{}->{}".format(lower, upper)

# test
class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)
        arr = [0, 1, 3, 50, 75]
        print Solution().findMissingRanges(arr,0, 99)

if __name__ == '__main__':
    unittest.main()

Java = '''
#Thought: https://leetcode.com/problems/contains-duplicate/solution/

#93.94% 0ms
public class Solution {
    public List<String> findMissingRanges(int[] nums, int lower, int upper) {
        List<String> res = new ArrayList<>();
        for(int i : nums) {
            if(i > lower) res.add(lower+((i-1 > lower)?"->"+(i-1):""));
            if(i == upper) return res; // Avoid overflow
            lower = i+1;
        }
        if(lower <= upper) res.add(lower + ((upper > lower)?"->"+(upper):""));
        return res;
    }
}

#93.94% 0ms
class Solution {
    public List<String> findMissingRanges(int[] nums, int lower, int upper) {
        List<String> res = new ArrayList<String>();
        if (nums.length == 0) {
            addRange(res, lower, upper);
            return res;
        }
        addRange(res, lower, (long)nums[0] - 1);
        for (int i = 1; i < nums.length; i++) {
            addRange(res, (long)nums[i-1] + 1, (long)nums[i] - 1);
        }
        addRange(res, (long)nums[nums.length-1] + 1, upper);
        return res;
    }
    void addRange(List<String> res, long start, long end) {
        if (start > end) {
            return;
        } else if (start == end) {
            res.add(start + "");
        } else {
            res.add(start + "->" + end);
        }
    }
}

Input:
[2147483647]
0
2147483647
Output:
["0->2147483646","-2147483648->2147483647"]
Expected:
["0->2147483646"]

# Overflow:
public class Solution {
    public List<String> findMissingRanges(int[] nums, int lower, int upper) {
        List<String> result = new ArrayList<>();
        int cur = lower;
        for (int num : nums) {
            if (cur < num) {
                result.add(convertToString(cur, num - 1));
                cur = num;
            } else if (cur > num) {
                continue;
            }
            cur++;
        }
        if (cur != upper + 1) {
            result.add(convertToString(cur, upper));
        }
        return result;
    }

    private String convertToString(int lower, int upper) {
        StringBuilder sb = new StringBuilder();
        sb.append(lower);
        if (upper != lower) {
            sb.append("->");
            sb.append(upper);
        }
        return sb.toString();
    }
}
'''