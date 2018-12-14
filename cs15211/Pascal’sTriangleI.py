__source__ = 'https://leetcode.com/problems/pascals-triangle/'
# https://github.com/kamyu104/LeetCode/blob/master/Python/pascals-triangle.py
# Time:  O(n^2)
# Space: O(n)
# Array
#
# Description: Leetcode # 118. Pascal's Triangle
#
# Given numRows, generate the first numRows of Pascal's triangle.
#
# For example, given numRows = 5,
# Return
#
# [
#      [1],
#     [1,1],
#    [1,2,1],
#   [1,3,3,1],
#  [1,4,6,4,1]
# ]
#
# Companies
# Apple Twitter
# Related Topics
# Array
# Similar Questions
# Pascal's Triangle II
#
import unittest
class Solution:
    # @return a list of lists of integers
    def generate(self, numRows):
        result = []
        for i in xrange(numRows):
            result.append([])
            for j in xrange(i + 1):
                if j in (0, i):
                    result[i].append(1)
                    print i, j, result
                else:
                    result[i].append(result[i-1][j] + result[i-1][j-1])
        return result

if __name__ == "__main__":
    print Solution().generate(5)

class SolutionOther:
    # @return a list of lists of integers
    def generate(self, numRows):
        ans = [ 0 for n in range(numRows)]

        for i in range(0, numRows):
            ans[i]= [0 for i in range(i+1)]
            #print i, ans
            ans[i][0] = ans[i][i] = 1
            for j in range(1,i):
                ans[i][j] = ans[i-1][j-1] + ans[i-1][j]

        return ans

class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)
        test = SolutionOther()
        print test.generate(5)

if __name__ == '__main__':
    unittest.main()

Java = '''
# Thought: https://leetcode.com/problems/pascals-triangle/solution/
#
# 0ms 100%
class Solution {
    public List<List<Integer>> generate(int numRows) {
        List<List<Integer>> result = new ArrayList<>();
        if (numRows <= 0) {
            return result;
        }
        List<Integer> prev = new ArrayList<>();
        prev.add(1);
        result.add(prev);
        for (int i = 1; i < numRows; i++) {
            List<Integer> cur = new ArrayList<>();
            cur.add(1);
            for (int j = 0; j < prev.size() - 1; j++) {
                cur.add(prev.get(j) + prev.get(j + 1));
            }
            cur.add(1);
            result.add(cur);
            prev = cur;
        }
        return result;
    }
}

# 1ms 59.94%
class Solution {
    public List<List<Integer>> generate(int numRows) {
        List<List<Integer>> result = new ArrayList<>();
        if (numRows <= 0) return result;
        List<Integer> cur = new ArrayList<>();
        for( int i = 0; i < numRows; i++) {
            cur.add(0,1);
            for (int j = 1; j < cur.size() - 1; j++) {
                cur.set(j, cur.get(j) + cur.get(j + 1));
            }
            result.add(new ArrayList<>(cur));
        }
        return result;
    }
}
'''