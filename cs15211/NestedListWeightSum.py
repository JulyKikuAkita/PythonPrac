__source__ = 'https://leetcode.com/problems/nested-list-weight-sum/#/description'
# https://github.com/kamyu104/LeetCode/blob/master/Python/nested-list-weight-sum.py
# Time:  O(n)
# Space: O(h)
# Description:
# Given a nested list of integers, return the sum of all integers in the list weighted by their depth.
#
# Each element is either an integer, or a list -- whose elements may also be integers or other lists.
#
# Example 1:
# Given the list [[1,1],2,[1,1]], return 10. (four 1's at depth 2, one 2 at depth 1)
#
# Example 2:
# Given the list [1,[4,[6]]], return 27. (one 1 at depth 1, one 4 at depth 2, and one 6 at depth 3; 1 + 4*2 + 6*3 = 27)
# Companies
# LinkedIn
# Related Topics
# Depth-first Search
# Similar Questions
# Nested List Weight Sum II Array Nesting
#
# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
class NestedInteger(object):
   def isInteger(self):
       """
       @return True if this NestedInteger holds a single integer, rather than a nested list.
       :rtype bool
       """

   def getInteger(self):
       """
       @return the single integer that this NestedInteger holds, if it holds a single integer
       Return None if this NestedInteger holds a nested list
       :rtype int
       """

   def getList(self):
       """
       @return the nested list that this NestedInteger holds, if it holds a nested list
       Return None if this NestedInteger holds a single integer
       :rtype List[NestedInteger]
       """

class Solution(object):
    def depthSum(self, nestedList):
        """
        :type nestedList: List[NestedInteger]
        :rtype: int
        """
        def depthSumHelper(nestedList, depth):
            res = 0
            for l in nestedList:
                if l.isInteger():
                    res += l.getInteger() * depth
                else:
                    res += depthSumHelper(l.getList(), depth + 1)
            return res
        return depthSumHelper(nestedList, 1)

#Java
Java = '''
Thought: https://leetcode.com/articles/nested-list-weight-sum/

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

 1. DFS 18%
public class Solution {
    public int depthSum(List<NestedInteger> nestedList) {
        return dfs(nestedList, 1);
    }

    public int dfs(List<NestedInteger> nestedList, int depth) {
        int sum = 0;
        for (NestedInteger e :  nestedList) {
            sum += e.isInteger() ? e.getInteger() * depth : dfs(e.getList(), depth + 1);
        }
        return sum;
    }
}

2. BFS 18%
public class Solution {
    public int depthSum(List<NestedInteger> nestedList) {
        int sum = 0;
        Queue<NestedInteger> queue = new LinkedList<>();
        int depth = 1;
        for (NestedInteger ni : nestedList) {
            queue.add(ni);
        }
        while (!queue.isEmpty()) {
            int size = queue.size();
            while (size-- > 0) {
                NestedInteger cur = queue.poll();
                if (cur.isInteger()) {
                    sum += cur.getInteger() * depth;
                } else {
                    for (NestedInteger ni : cur.getList()) {
                        queue.add(ni);
                    }
                }
            }
            depth++;
        }
        return sum;
    }
}
'''