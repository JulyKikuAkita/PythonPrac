__source__ = 'https://leetcode.com/problems/pascals-triangle-ii/description/'
# https://github.com/kamyu104/LeetCode/blob/master/Python/pascals-triangle-ii.py
# Time:  O(n^2)
# Space: O(n)
# Array
#
# Description: Leetcode # 119. Pascal's Triangle II
# Given an index k, return the kth row of the Pascal's triangle.
#
# For example, given k = 3,
# Return [1,3,3,1].
#
# Note:
# Could you optimize your algorithm to use only O(k) extra space?
#
# Companies
# Amazon
# Related Topics
# Array
# Similar Questions
# Pascal's Triangle
#
import unittest
# 32ms 16.78%
class Solution:
    # @return a list of integers
    def getRow(self, rowIndex):
        result = [1]
        for i in xrange(rowIndex):
        #for i in xrange(1, rowIndex + 1):
            #print [result[j-1] + result[j] for j in xrange(1,i + 1)]
            result = [1] + [result[j-1] + result[j] for j in xrange(1,i + 1)] + [1]
            #result = [1] + [result[j-1] + result[j] for j in xrange(1, i)] + [1]
        return result

class Solution2:
    # @return a list of integers
    def getRow(self, rowIndex):
        result = [0] * (rowIndex + 1)
        print result
        for i in xrange(rowIndex + 1):
            old = result[0] = 1
            for j in xrange(1, i + 1) :
                #print old, result[j], j, old + result[j]
                old, result[j] = result[j], old + result[j]
        return result

class SolutionOther:
    # @return a list of integers
    def getRow(self, rowIndex):
        ans = [ 0 for n in range(rowIndex+1)]
        ans[0] = 1

        for i in range(1, rowIndex+1):
            ans[i]= ans[i-1]*(rowIndex - i + 1) / i
            #print i, ans
        return ans

class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)
        print Solution().getRow(3)
        test = SolutionOther()
        #print test.getRow(5)

if __name__ == '__main__':
    unittest.main()

Java = '''
# Thought:

# 1ms 91.55%
class Solution {
    public List<Integer> getRow(int rowIndex) {
        if (rowIndex < 0) {
            return new ArrayList<>();
        }
        Integer[] arr = new Integer[rowIndex + 1];
        arr[0] = 1;
        for (int i = 1; i <= rowIndex; i++) {
            for (int j = i - 1; j > 0; j--) {
                arr[j] += arr[j - 1];
            }
            arr[i] = 1;
        }
        return Arrays.asList(arr);
    }
}

# 1ms 91.55%
class Solution {
    public List<Integer> getRow(int rowIndex) {
        if (rowIndex < 0) return new ArrayList<>();
        List<Integer> res = new ArrayList<Integer>();
        for (int i = 0; i <= rowIndex; i++) {
            res.add(0, 1);
            for (int j = 1; j <res.size() - 1; j++) {
                res.set(j, res.get(j) + res.get(j + 1));
            }
        }
        return res;
    }
}

# generate half
# 0ms 100%
class Solution {
    public List<Integer> getRow(int rowIndex) {
        List<Integer> result = new ArrayList<>(rowIndex + 1);
        result.add(1);
        for (int i = 1; i <= rowIndex / 2; i++) {
            long t = (long)result.get(i - 1) * (rowIndex - i + 1) / i;
            result.add((int)t);
        }
        for (int i = rowIndex / 2 + 1; i <= rowIndex; i++) {
            result.add(result.get(rowIndex - i));
        }
        return result;
    }
}
'''
