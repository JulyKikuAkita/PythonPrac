__source__ = 'https://leetcode.com/problems/range-sum-query-immutable/description/'
# https://github.com/kamyu104/LeetCode/blob/master/Python/range-sum-query-immutable.py
# Time:  ctor:   O(n),
#        update: O(logn),
#        query:  O(logn)
# Space: O(n)
#
# Description: Leetcode # 303. Range Sum Query - Immutable
#
# Given an integer array nums, find the sum of
# the elements between indices i and j (i <= j), inclusive.
#
# The update(i, val) function modifies nums by
# updating the element at index i to val.
# Example:
# Given nums = [1, 3, 5]
#
# sumRange(0, 2) -> 9
# update(1, 2)
# sumRange(0, 2) -> 8
# Note:
# The array is only modifiable by the update function.
# You may assume the number of calls to update
# and sumRange function is distributed evenly.
#
# Companies
# Palantir
# Related Topics
# Dynamic Programming
# Similar Questions
# Range Sum Query 2D - Immutable Range Sum Query - Mutable Maximum Size Subarray Sum Equals k
#
import unittest
# Segment Tree solutoin.
class NumArray(object):
    def __init__(self, nums):
        """
        initialize your data structure here.
        :type nums: List[int]
        """
        # Build segment tree.
        self.__nums = nums
        def buildHelper(nums, start, end):
            if start > end:
                return None

            # The root's start and end is given by build method.
            root = self.__SegmentTreeNode(start, end, 0)

            # If start equals to end, there will be no children for this node.
            if start == end:
                root.sum = nums[start]
                return root

            # Left child: start=nums.left, end=(nums.left + nums.right) / 2.
            root.left = buildHelper(nums, start, (start + end) / 2)

            # Right child: start=(nums.left + nums.right) / 2 + 1, end=nums.right.
            root.right = buildHelper(nums, (start + end) /2 + 1, end)

            #Update sum.
            root.sum = (root.left.sum if root.left else 0) + \
                       (root.right.sum if root.right else 0)
            return root
        self.__root = buildHelper(nums, 0, len(nums) - 1)

    def update(self, i, val):
        """
        :type i: int
        :type val: int
        :rtype: int
        """
        def updateHelper(root, i, val):
            # Out of range.
            if not root or root.start > i or root.end < i:
                return

            # Change the node's value with [i] to the new given value.
            if root.start == i and root.end == i:
                root.sum = val
                return

            updateHelper(root.left, i, val)
            updateHelper(root.right, i, val)

            # Update sum.
            root.sum = (root.left.sum if root.left else 0) + \
                       (root.right.sum if root.right else 0)

        if self.__nums[i] != val:
            self.__nums[i] = val
            updateHelper(self.__root, i, val)

    def sumRange(self, i, j):
        """
        sum of elements nums[i..j], inclusive.
        :type i: int
        :type j: int
        :rtype: int
        """
        def sumRangeHelper(root, start, end):
            # Out of range.
            if not root or root.start > end or root.end < start:
                return 0

            # Current segment is totally within range [start, end]
            if root.start >= start and root.end <= end:
                return root.sum
            return sumRangeHelper(root.left, start, end) + \
                    sumRangeHelper(root.right, start, end)
        return sumRangeHelper(self.__root, i, j)

    class _SegmentTreeNode:
        def __init__(self, i, j, s):
            self.start, self.end, self.sum = i, j ,s

# Time:  ctor:   O(nlogn),
#        update: O(logn),
#        query:  O(logn)
# Space: O(n)
# Binary Indexed Tree (BIT) solution.
# 129ms
class NumArray2(object):
    def __init__(self, nums):
        """
        initialize your data structure here.
        :type nums: List[int]
        """
        # Build segment tree.
        if not nums:
            return
        self.__nums = nums
        self.__bit = [0] * (len(self.__nums) + 1)
        for i, num in enumerate(self.__nums):
            self.__add(i, num)

    def update(self, i, val):
        """
        :type i: int
        :type val: int
        :rtype: int
        """
        if val - self.__nums[i]:
            self.__add(i, val - self.__nums[i])
            self.__nums[i] = val

    def sumRange(self, i, j):
        """
        sum of elements nums[i..j], inclusive.
        :type i: int
        :type j: int
        :rtype: int
        """
        def sumRegion_bit(i):
            i += 1
            ret = 0
            while i > 0:
                ret += self.__bit[i]
                i -= (i & -i)  # i & bitwise and -i = 1
            return ret

        ret = sumRegion_bit(j)
        if i > 0:
            ret -= sumRegion_bit(i - 1)
        return ret

    def __add(self, i , val):
        i += 1
        while i <= len(self.__nums):
            self.__bit[i] += val
            i += ( i & -i)

# Your NumArray object will be instantiated and called as such:
# numArray = NumArray(nums)
# numArray.sumRange(0, 1)
# numArray.update(1, 10)
# numArray.sumRange(1, 2)
class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)

if __name__ == '__main__':
    unittest.main()

Java = '''
#Thought: https://leetcode.com/articles/range-sum-query-immutable/

#73.20% 213ms
public class NumArray {
    int[] sum;
    public NumArray(int[] nums) {
        int n = nums.length;
        sum = new int[n+1];
        sum[0] = 0;
        for(int i=1;i<=n;i++){
            sum[i] = sum[i-1]+nums[i-1];
        }
    }

    public int sumRange(int i, int j) {
        return sum[j+1]-sum[i];
    }
}

#67.19% 219ms
public class NumArray {
    int[] mSum;
    public NumArray(int[] nums) {
        for (int i = 1; i < nums.length; i++) {
            nums[i] += nums[i - 1];
        }
        mSum = nums;
    }

    public int sumRange(int i, int j) {
        if ( i ==0 ) return mSum[j];
        return mSum[j] - mSum[i-1];
    }
}

// Your NumArray object will be instantiated and called as such:
// NumArray numArray = new NumArray(nums);
// numArray.sumRange(0, 1);
// numArray.sumRange(1, 2);

# BIT
# 34.42% 243ms
public class NumArray {
    int[] mNums;
    int[] mBit;
    public NumArray(int[] nums) {
        mNums = nums;
        mBit = new int[nums.length + 1];
        for (int i = 0; i < nums.length; i++) {
            buildTree(i, nums[i]);
        }
    }

    public int sumRange(int i, int j) {
        return getSum(j) - getSum(i - 1);
    }

    private void buildTree(int i, int val) {
        i++;
        while (i <= mNums.length) {
            mBit[i] += val;
            i += (i & -i);
        }
    }

    private int getSum(int i) {
        i++;
        int sum = 0;
        while ( i > 0) {
            sum += mBit[i];
            i -= (i & -i);
        }
        return sum;
    }
}

# Segment Tree:
#4.82% 414ms
public class NumArray {
    Node mRoot = null;
    public NumArray(int[] nums) {
        mRoot = buildStree(nums, 0, nums.length - 1);
    }

    public int sumRange(int i, int j) {
        return getSum(mRoot, i, j);
    }

    private Node buildStree(int[] nums, int start, int end) {
        if (start > end) return null;
        Node node = new Node(start, end);
        if (start == end) node.mSum = nums[start];
        else {
            int mid = start + (end - start) / 2;
            node.mLeft = buildStree(nums, start, mid);
            node.mRight = buildStree(nums, mid + 1, end);
            node.mSum = node.mLeft.mSum + node.mRight.mSum;
        }
        return node;
    }

    private int getSum(Node node, int i, int j) {
        if (i == node.mStart && j == node.mEnd) return node.mSum;
        else {
            int mid = node.mStart + (node.mEnd - node.mStart) / 2;
            if (j <= mid) { //tricky
                return getSum(node.mLeft, i, j);
            } else if (mid + 1 <= i) { //tricky
                return getSum(node.mRight, i, j);
            } else {
                return getSum(node.mLeft, i, mid) + getSum(node.mRight, mid+1, j);
            }
        }
    }

    class Node{
        int mStart, mEnd, mSum;
        Node mLeft, mRight;
        public Node(int start, int end){
            mStart = start;
            mEnd = end;
            mSum = 0;
            mLeft = mRight = null;
        }
    }
}

'''