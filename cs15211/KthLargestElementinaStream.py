__source__ = 'https://leetcode.com/problems/kth-largest-element-in-a-stream/description/'
# Time:  O()
# Space: O()
#
# Description: Leetcode # 703. Kth Largest Element in a Stream
#
# Design a class to find the kth largest element in a stream.
# Note that it is the kth largest element in the sorted order, not the kth distinct element.
#
# Your KthLargest class will have a constructor which accepts an integer k and an integer array nums,
# which contains initial elements from the stream. For each call to the method KthLargest.add,
# return the element representing the kth largest element in the stream.
#
# Example:
#
# int k = 3;
# int[] arr = [4,5,8,2];
# KthLargest kthLargest = new KthLargest(3, arr);
# kthLargest.add(3);   // returns 4
# kthLargest.add(5);   // returns 5
# kthLargest.add(10);  // returns 5
# kthLargest.add(9);   // returns 8
# kthLargest.add(4);   // returns 8
# Note:
# You may assume that nums  length >= k-1 and k >= 1.
#
import unittest


class Solution(object):
    pass  # your function here


class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)


if __name__ == '__main__':
    unittest.main()

Java = '''
#Thought: use PQ
# 73ms, 99.79%
class KthLargest {
    private PriorityQueue<Integer> pq;
    private int k;

    public KthLargest(int k, int[] nums) {
        this.k = k;
        this.pq = new PriorityQueue<>();

        for (int num : nums) {
            pq.offer(num);
            if (pq.size() > k)
                pq.poll();
        }
    }

    public int add(int val) {
        pq.offer(val);
        if (pq.size() > k)
            pq.poll();
        return pq.peek();
    }
}

#Thought: use BST
#8.57% 334ms


class KthLargest {
    TreeNode root;
    private int k;

    public KthLargest(int k, int[] nums) {
        this.k = k - 1;
        for (int n : nums) {
            root = insert(root, n);
        }
    }

    public int add(int val) {
        root = insert(root, val);
        return findKthLargest(k, root);
    }

    private int findKthLargest(int k, TreeNode root) {
        if (root == null) return -1;
        if (root.mRightSum == k) return root.mVal;

        if (root.mRightSum > k) {
            return findKthLargest(k, root.right);
        } else {
            return findKthLargest(k - root.mRightSum - 1, root.left);
        }
    }

    private TreeNode insert(TreeNode root, int val) {
        if (root == null) return new TreeNode(val, 0);
        if (val < root.mVal) {
            root.left = insert(root.left, val);
        } else {
            root.mRightSum++;
            root.right = insert(root.right, val);
        }
        return root;
    }

    private class TreeNode {
        int mVal;
        int mRightSum;
        TreeNode left;
        TreeNode right;
        TreeNode(int val, int rightSum) {
            mVal = val;
            mRightSum = rightSum;
        }
    }
}

/**
 * Your KthLargest object will be instantiated and called as such:
 * KthLargest obj = new KthLargest(k, nums);
 * int param_1 = obj.add(val);
 */
'''