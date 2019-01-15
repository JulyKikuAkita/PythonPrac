__source__ = 'https://leetcode.com/problems/nested-list-weight-sum-ii/'
# https://leetcode.com/problems/nested-list-weight-sum-ii/
# Time:  O(n)
# Space: O(h)
#
# Description: Leetcode # 364. Nested List Weight Sum II
#
# Given a nested list of integers, return the sum of all integers in the list weighted by their depth.
#
# Each element is either an integer, or a list -- whose elements may also be integers or other lists.
#
# Different from the previous question where weight is increasing from root to leaf,
# now the weight is defined from bottom up. i.e., the leaf level integers have weight 1,
# and the root level integers have the largest weight.
#
# Example 1:
# Given the list [[1,1],2,[1,1]], return 8. (four 1's at depth 1, one 2 at depth 2)
#
# Example 2:
# Given the list [1,[4,[6]]], return 17. (one 1 at depth 3, one 4 at depth 2, and one 6 at depth 1; 1*3 + 4*2 + 6*1 = 17)
#
# Companies
# LinkedIn
# Related Topics
# Depth-first Search
# Similar Questions
# Nested List Weight Sum Array Nesting
#

# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger(object):
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """
import unittest
class Solution(object):
    def depthSumInverse(self, nestedList):
        """
        :type nestedList: List[NestedInteger]
        :rtype: int
        """
        def depthSumInverseHelper(list, depth, result):
            if len(result) < depth + 1:
                result.append(0)
            if list.isInteger():
                result[depth] += list.getInteger()
            else:
                for l in list.getList():
                    depthSumInverseHelper(l, depth + 1, result)

        result = []
        for list in nestedList:
            depthSumInverseHelper(list, 0, result)

        sum = 0
        for i in reversed(xrange(len(result))):
            sum += result[i] * (len(result) - i)
        return sum

class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)

if __name__ == '__main__':
    unittest.main()

Java = '''
# Thought:
/**
 * // This is the interface that allows for creating nested lists.
 * // You should not implement it, or speculate about its implementation
 * public interface NestedInteger {
 *
 *     // @return true if this NestedInteger holds a single integer, rather than a nested list.
 *     public boolean isInteger();
 *
 *     // @return the single integer that this NestedInteger holds, if it holds a single integer
 *     // Return null if this NestedInteger holds a nested list
 *     public Integer getInteger();
 *
 *     // @return the nested list that this NestedInteger holds, if it holds a nested list
 *     // Return null if this NestedInteger holds a single integer
 *     public List<NestedInteger> getList();
 * }
 */

# 2ms 100%
class Solution {
    public int depthSumInverse(List<NestedInteger> nestedList) {
        return depthSumInverse(nestedList, getDepth(nestedList));
    }

    private int getDepth(List<NestedInteger> nestedList) {
        int depth = 0;
        for (NestedInteger ni : nestedList) {
            if (ni.isInteger()) {
                depth = Math.max(depth, 1);
            } else {
                depth = Math.max(depth, getDepth(ni.getList()) + 1);
            }
        }
        return depth;
    }

    private int depthSumInverse(List<NestedInteger> nestedList, int weight) {
        int sum = 0;
        for (NestedInteger ni : nestedList) {
            if (ni.isInteger()) {
                sum += ni.getInteger() * weight;
            } else {
                sum += depthSumInverse(ni.getList(), weight - 1);
            }
        }
        return sum;
    }
}

# BFS
# 2ms 100%
class Solution {
    public int depthSumInverse(List<NestedInteger> nestedList) {
        if (nestedList == null || nestedList.size() == 0) {
            return 0;
        }
        LinkedList<NestedInteger> queue = new LinkedList<NestedInteger>();
        queue.addAll(nestedList);

        int sum = 0;
        int weightSum = sum;

        while (!queue.isEmpty()) {
            int size = queue.size();
            for (int i = 0; i < size; i++) {
                NestedInteger curr = queue.poll();
                if (curr.isInteger()) {
                    sum += curr.getInteger();
                } else {
                    queue.addAll(curr.getList());
                }
            }
            weightSum += sum;
        }
        return weightSum;
    }
}

# 2ms 100%
class Solution {
    public int depthSumInverse(List<NestedInteger> nestedList) {
        int unweighted = 0, weighted = 0;
        while (!nestedList.isEmpty()) {
            List<NestedInteger> nextLevel = new ArrayList<>();
            for (NestedInteger ni : nestedList) {
                if (ni.isInteger())
                    unweighted += ni.getInteger();
                else
                    nextLevel.addAll(ni.getList());
            }
            weighted += unweighted;
            nestedList = nextLevel;
        }
        return weighted;
    }
}
'''
