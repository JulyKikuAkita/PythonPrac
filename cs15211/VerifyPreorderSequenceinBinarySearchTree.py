__source__ = 'https://leetcode.com/problems/verify-preorder-sequence-in-binary-search-tree/description/'
# https://github.com/kamyu104/LeetCode/blob/master/Python/verify-preorder-sequence-in-binary-search-tree.py
# Time:  O(n)
# Space: O(1)]
# Stack
#
# Description: Leetcode # 217. Contains Duplicate
#
# Given an array of numbers, verify whether it is the correct preorder traversal sequence of a binary search tree.
#
# You may assume each number in the sequence is unique.
#
# Follow up:
# Could you do it using only constant space complexity?
#
# Hide Company Tags Zenefits
# Companies
# Zenefits
# Related Topics
# Tree Stack
# Similar Questions
# Binary Tree Preorder Traversal
#
import unittest
class Solution:
    # @param {integer[]} preorder
    # @return {boolean}
    def verifyPreorder(self, preorder):
        low = float("-inf")
        i = -1

        for p in preorder:
            if p < -1:
                return False
            while i >= 0 and p > preorder[i]:
                low = preorder[i]
                i -= 1
            i += 1
            preorder[i] = p
        return True

# Time:  O(n)
# Space: O(h)
class Solution2:
    # @param {integer[]} preorder
    # @return {boolean}
    def verifyPreorder(self, preorder):
        low = float("-inf")
        path = []
        for p in preorder:
            if p < low:
                return False
            while path and p > path[-1]:
                low = path[-1]
                path.pop()
            path.append(p)
        return True

class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)

if __name__ == '__main__':
    unittest.main()

Java = '''
#Thought:
[10,7,4,8,6,40,23] should be false

#36.34% 37ms
public class Solution {
   public boolean verifyPreorder(int[] preorder) {
        int low = Integer.MIN_VALUE;
        Stack<Integer> path = new Stack();
        for (int p : preorder) {
            if (p < low)
                return false;
            while (!path.empty() && p > path.peek())
                low = path.pop();
            path.push(p);
        }
        return true;
    }
}

#83.76% 4ms
public class Solution {
    public boolean verifyPreorder(int[] preorder) {
        int index = -1;
        int min = Integer.MIN_VALUE;
        for (int i = 0; i < preorder.length; i++) {
            if (preorder[i] < min) {
                return false;
            }
            while (index >= 0 && preorder[index] < preorder[i]) {
                min = preorder[index--];
            }
            preorder[++index] = preorder[i];
        }
        return true;
    }
}

//assume no duplicate  (since bst doesnt allow duplicate)
//we have to do it in place
//slow = is the virtual stack that we maintained if we the array index we traverse is smaller than the previous one
//means that we are still traversing to the left subtree,
//if we found out the current index is bigger than the previous one we traverse it means that we are on the right
//subtree or the right hand side of the bst so we simply pop out all the elements in the stack that is smaller
//than the current index also use the popped value as the new min (since we are in right subtree means we must
//never come across a smaller number)
// fast = index that traverse through the array

#83.76% 4ms
class Solution {
    public boolean verifyPreorder(int[] preorder) {
        //min
        int min = Integer.MIN_VALUE, slow = -1;

        for(int fast : preorder){
            if(min > fast){
                return false;
            }

            while(slow >= 0 && fast > preorder[slow]){
                min = preorder[slow--];
            }

            preorder[++slow] = fast;
        }
        return true;
    }
}
'''