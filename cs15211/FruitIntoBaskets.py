__source__ = 'https://leetcode.com/problems/fruit-into-baskets/'
# Time:  O(N) where NN is the length of tree
# Space: O(N)
# Sliding Window : This problem is the same as 159 - Longest Substring with At Most Two Distinct Characters
#
# Description: Leetcode # 904. Fruit Into Baskets
#
# In a row of trees, the i-th tree produces fruit with type tree[i].
#
# You start at any tree of your choice, then repeatedly perform the following steps:
#
# Add one piece of fruit from this tree to your baskets.
# If you cannot, stop.
# Move to the next tree to the right of the current tree.
# If there is no tree to the right, stop.
# Note that you do not have any choice after the initial choice of starting tree:
# you must perform step 1, then step 2, then back to step 1, then step 2,
# and so on until you stop.
#
# You have two baskets, and each basket can carry any quantity of fruit,
# but you want each basket to only carry one type of fruit each.
#
# What is the total amount of fruit you can collect with this procedure?
#
# Example 1:
#
# Input: [1,2,1]
# Output: 3
# Explanation: We can collect [1,2,1].
# Example 2:
#
# Input: [0,1,2,2]
# Output: 3
# Explanation: We can collect [1,2,2].
# If we started at the first tree, we would only collect [0, 1].
# Example 3:
#
# Input: [1,2,3,2,2]
# Output: 4
# Explanation: We can collect [2,3,2,2].
# If we started at the first tree, we would only collect [1, 2].
# Example 4:
#
# Input: [3,3,3,1,2,1,1,2,3,3,4]
# Output: 5
# Explanation: We can collect [1,2,1,1,2].
# If we started at the first tree or the eighth tree, we would only collect 4 fruits.
#
#
# Note:
#
# 1 <= tree.length <= 40000
# 0 <= tree[i] < tree.length
#
import unittest

# 88ms 100%
class Solution(object):
    def totalFruit(self, tree):
        """
        :type tree: List[int]
        :rtype: int
        """
        if not tree:
            return 0

        first, second = tree[0], tree[0]
        tmp = 0
        buff = 0
        res = 0

        for fruit in tree:
            if fruit == second:
                tmp += 1
                buff += 1
            elif fruit == first:
                tmp += 1
                first, second = second, first
                buff = 1
            else:
                res = max(res, tmp)
                tmp = buff + 1
                first = second
                second = fruit
                buff = 1
        return max(res, tmp)
class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)


if __name__ == '__main__':
    unittest.main()

Java = '''
# Thought: https://leetcode.com/problems/fruit-into-baskets/solution/
# Sliding Window : This problem is the same as 159 - Longest Substring with At Most Two Distinct Characters
# Complexity Analysis
# Time Complexity: O(N), where N is the length of tree.
# Space Complexity: O(N) 
# 10ms 99.65%
class Solution {
    public int totalFruit(int[] tree) {
        int max = 0, count = 0;
        for (int i = 0, first = 0, second = -1; i < tree.length; i++) {
            count++;
            if (tree[i] == tree[first]) {
                first = i;
            } else if (second == -1 || tree[i] == tree[second]) {
                second = i;
            } else {
                max = Math.max(max, count - 1);
                count = Math.abs(first - second) + 1;
                first = i - 1;
                second = i;
            }
        }
        return Math.max(count ,max);
    }
}

# Using Sliding window map template:
# 139ms 10.51%
class Solution {
    public int totalFruit(int[] tree) {
        if (tree == null || tree.length == 0) return 0;
        int start = 0, end = 0, max = 0;
        Map<Integer, Integer> map = new HashMap<>();
        while (end < tree.length) {
            map.put(tree[end], map.getOrDefault(tree[end], 0) + 1);
            end++;
            while (map.size() > 2) {
                map.put(tree[start], map.get(tree[start]) - 1);
                if (map.get(tree[start]) == 0) map.remove(tree[start]);
                start++;
            }
            max = Math.max(max, end - start);
        }
        return max;
    }
}

# Using Sliding window array template: [bad coding style]
# 13ms 72.53%
class Solution {
    public int totalFruit(int[] tree) {
        int[] map = new int[40001];
        int cnt = 0, max = 0;
        for (int l = 0, r = 0; r < tree.length; r++) {
            if (map[tree[r]]++ == 0) cnt++;
            while (cnt > 2) {
                if (--map[tree[l]] == 0) cnt--;
                l++;
            }
            max = Math.max(max, r - l + 1);
        }
        return max;
    }
}
'''
