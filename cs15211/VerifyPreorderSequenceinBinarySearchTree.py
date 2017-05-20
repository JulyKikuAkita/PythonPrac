__author__ = 'July'
# https://github.com/kamyu104/LeetCode/blob/master/Python/verify-preorder-sequence-in-binary-search-tree.py
'''
Given an array of numbers, verify whether it is the correct preorder traversal sequence of a binary search tree.

You may assume each number in the sequence is unique.

Follow up:
Could you do it using only constant space complexity?

Hide Company Tags Zenefits
#  Stack

'''

# Time:  O(n)
# Space: O(1)

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

#java

js = '''
public class Solution {
    public boolean verifyPreorder(int[] preorder) {
        LinkedList<Integer> stack = new LinkedList<Integer>();
        int low = Integer.MIN_VALUE;
        for (int i = 0; i < preorder.length; i++) {
            if (preorder[i] < low) {
                return false;
            }
            while (!stack.isEmpty() && stack.peek() <= preorder[i]) {
                low = stack.pop();
            }
            stack.push(preorder[i]);
        }
        return true;
    }
}

public class Solution {
    public boolean verifyPreorder(int[] preorder) {
        return verifyPreorder(preorder, 0, preorder.length);
    }

    private boolean verifyPreorder(int[] preorder, int start, int end) {
        if (start >= end) {
            return true;
        }
        int rightChild = start + 1;
        while (rightChild < end && preorder[rightChild] < preorder[start]) {
            rightChild++;
        }
        if (rightChild == end) {
            return verifyPreorder(preorder, start + 1, end);
        }
        for (int i = rightChild + 1; i < end; i++) {
            if (preorder[i] < preorder[start]) {
                return false;
            }
        }
        return verifyPreorder(preorder, start + 1, rightChild - 1) && verifyPreorder(preorder, rightChild, end);
    }
}



    public class Solution {
    public boolean verifyPreorder(int[] preorder) {
        int len = preorder.length;
        if (len < 2) {
            return true;
        }
        int min = Integer.MIN_VALUE;
        int max = preorder[0];
        int index = 1;
        while (index < len) {
            while (index < len && preorder[index] < preorder[index - 1]) {
                if (preorder[index] < min) {
                    return false;
                }
                index++;
            }
            if (index < len) {
                if (preorder[index] < max) {
                    min = preorder[index - 1];
                } else {
                    min = max;
                    max = preorder[index];
                }
            }
            index++;
        }
        return true;
    }
}
    '''