__source__ = 'https://leetcode.com/problems/path-sum-iv/description/'
# Time:  O()
# Space: O()
#
# Description: Leetcode # 666. Path Sum IV
#
# If the depth of a tree is smaller than 5, then this tree can be represented by a list of three-digits integers.
#
# For each integer in this list:
# The hundreds digit represents the depth D of this node, 1 <= D <= 4.
# The tens digit represents the position P of this node in the level it belongs to, 1 <= P <= 8.
# The position is the same as that in a full binary tree.
# The units digit represents the value V of this node, 0 <= V <= 9.
# Given a list of ascending three-digits integers representing a binary with the depth smaller than 5.
# You need to return the sum of all paths from the root towards the leaves.
#
# Example 1:
# Input: [113, 215, 221]
# Output: 12
# Explanation:
# The tree that the list represents is:
#     3
#    / \
#   5   1
#
# The path sum is (3 + 5) + (3 + 1) = 12.
# Example 2:
# Input: [113, 221]
# Output: 4
# Explanation:
# The tree that the list represents is:
#     3
#      \
#       1
#
# The path sum is (3 + 1) = 4.
#
# Companies
# Alibaba
# Related Topics
# Tree
# Similar Questions
# Path Sum Path Sum II Binary Tree Maximum Path Sum Path Sum III
#
import unittest
#39ms
class Solution(object):
    def pathSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        s = {}
        l = {}
        for i in nums[::-1]:
            a, b, c = i / 100, i / 10 % 10, i % 10
            l[a, b] = max(1, l.get((a + 1, b * 2 - 1), 0) + l.get((a + 1, b * 2), 0))
            s[a, b] = s.get((a + 1, b * 2 - 1), 0) + s.get((a + 1, b * 2), 0) + l[a, b] * c
        return s.get((1, 1), 0)

class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)

if __name__ == '__main__':
    unittest.main()

Java = '''
#Thought:
#33.56% 17ms
class Solution {
    private int sum = 0;

    public int pathSum(int[] nums) {
        Map<Integer,Integer> map = new HashMap<>();
        for (int num : nums) {
            map.put(num / 10, num % 10);
        }
        dfs(map, nums[0]/ 10, 0);
        return sum;
    }

    private void dfs(Map<Integer,Integer> map, int root, int pre){
        int level = root / 10;
        int pos = root % 10;
        int left = (level + 1) * 10 + 2 * pos - 1;
        int right = (level + 1) * 10 + 2 * pos;
        int cur = pre + map.get(root);
        if (!map.containsKey(left) && !map.containsKey(right)) {
            sum += cur;
            return;
        }

        if (map.containsKey(left)) dfs(map, left, cur);
        if (map.containsKey(right)) dfs(map, right, cur);
    }
}

#84.12% 14ms
class Solution {
    public int pathSum(int[] nums) {
        Integer[][] A = new Integer[4][8];
        for(int e : nums) {
            A[e / 100 - 1][(e % 100) / 10 - 1] = new Integer(e % 10);
        }
        int res = 0;
        for(int i = 0; i < 4; i++) {
            for(int j = 0; j < 8; j++) {
                if(A[i][j] == null) {
                    continue;
                }
                if(i > 0) {
                    A[i][j] += A[i - 1][j / 2];
                }

                if(i == 3) {
                    res += A[i][j];
                } else if(A[i + 1][j * 2] == null && A[i + 1][j * 2 + 1] == null) {
                    res += A[i][j];
                }
            }
        }
        return res;
    }
}
'''