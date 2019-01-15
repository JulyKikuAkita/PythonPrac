__source__ = 'https://leetcode.com/problems/range-sum-query-mutable/'
# https://github.com/kamyu104/LeetCode/blob/master/Python/range-sum-query-mutable.py
# Time:  ctor:   O(n),
#        update: O(logn),
#        query:  O(logn)
# Space: O(n)
#
# Description: Leetcode # 307. Range Sum Query - Mutable
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
# Related Topics
# Binary Indexed Tree Segment Tree
# Similar Questions
# Range Sum Query - Immutable Range Sum Query 2D - Mutable
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
            root = self._SegmentTreeNode(start, end, 0)

            # If start equals to end, there will be no children for this node.
            if start == end:
                root.sum = nums[start]
                return root

            # Left child: start=nums.left, end=(nums.left + nums.right) / 2.
            root.left = buildHelper(nums, start, (start + end) / 2)

            # Right child: start=(nums.left + nums.right) / 2 + 1, end=nums.right.
            root.right = buildHelper(nums, (start + end) / 2 + 1, end)

            # Update sum.
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
            root.sum =  (root.left.sum if root.left else 0) + \
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
            self.start, self.end, self.sum = i, j, s

# Time:  ctor:   O(nlogn),
#        update: O(logn),
#        query:  O(logn)
# Space: O(n)
# Binary Indexed Tree (BIT) solution.
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
                i -= (i & -i)
            return ret

        ret = sumRegion_bit(j)
        if i > 0:
            ret -= sumRegion_bit(i - 1)
        return ret

    def __add(self, i, val):
        i += 1
        while i <= len(self.__nums):
            self.__bit[i] += val
            i += (i & -i)

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
# Thought: https://leetcode.com/problems/range-sum-query-mutable/solution/

# Segment tree
# 116ms 34.58%
class NumArray {
    int[] nodes;
    int length;

    public NumArray(int[] nums) {
        length = nums.length;
        if (length == 0) {
            nodes = new int[0];
            return;
        }
        int nodesLen = length == 1 ? 1 : (int) Math.pow(2, Math.ceil(Math.log(2 * length - 1) / Math.log(2))) - 1;
        nodes = new int[nodesLen];
        buildTree(nums, 0, length - 1, 0);
    }

    void update(int i, int val) {
        update(i, val, 0, length - 1, 0);
    }

    public int sumRange(int i, int j) {
        return sumRange(i, j, 0, length - 1, 0);
    }

    private int buildTree(int[] nums, int start, int end, int nodeIndex) {
        if (start == end) {
            nodes[nodeIndex] = nums[start];
        } else {
            int mid = start + (end - start) / 2;
            int left = buildTree(nums, start, mid, (nodeIndex + 1) * 2 - 1);
            int right = buildTree(nums, mid + 1, end, (nodeIndex + 1) * 2);
            nodes[nodeIndex] = left + right;
        }
        return nodes[nodeIndex];
    }

    private void update(int i, int val, int start, int end, int nodeIndex) {
        if (start == end) {
            nodes[nodeIndex] = val;
        } else {
            int mid = start + (end - start) / 2;
            if (start <= i && i <= mid) {
                update(i, val, start, mid, (nodeIndex + 1) * 2 - 1);
            } else {
                update(i, val, mid + 1, end, (nodeIndex + 1) * 2);
            }
            nodes[nodeIndex] = nodes[(nodeIndex + 1) * 2 - 1] + nodes[(nodeIndex + 1) * 2];
        }
    }

    private int sumRange(int i, int j, int start, int end, int nodeIndex) {
        if (j < start || i > end) {
            return 0;
        } else if (i <= start && end <= j) {
            return nodes[nodeIndex];
        }
        int mid = start + (end - start) / 2;
        return sumRange(i, j, start, mid, (nodeIndex + 1) * 2 - 1) + sumRange(i, j, mid + 1, end, (nodeIndex + 1) * 2);
    }
}


// Your NumArray object will be instantiated and called as such:
// NumArray numArray = new NumArray(nums);
// numArray.sumRange(0, 1);
// numArray.update(1, 10);
// numArray.sumRange(1, 2);

/**
 * Binary Indexed Trees (BIT or Fenwick tree):
 * https://www.topcoder.com/community/data-science/data-science-
 * tutorials/binary-indexed-trees/
 *
 * Example: given an array a[0]...a[7], we use a array BIT[9] to
 * represent a tree, where index [2] is the parent of [1] and [3], [6]
 * is the parent of [5] and [7], [4] is the parent of [2] and [6], and
 * [8] is the parent of [4]. I.e.,
 *
 * BIT[] as a binary tree:
 *            ______________*
 *            ______*
 *            __*     __*
 *            *   *   *   *
 * indices: 0 1 2 3 4 5 6 7 8
 *
 * BIT[i] = ([i] is a left child) ? the partial sum from its left most
 * descendant to itself : the partial sum from its parent (exclusive) to
 * itself. (check the range of "__").
 *
 * Eg. BIT[1]=a[0], BIT[2]=a[1]+BIT[1]=a[1]+a[0], BIT[3]=a[2],
 * BIT[4]=a[3]+BIT[3]+BIT[2]=a[3]+a[2]+a[1]+a[0],
 * BIT[6]=a[5]+BIT[5]=a[5]+a[4],
 * BIT[8]=a[7]+BIT[7]+BIT[6]+BIT[4]=a[7]+a[6]+...+a[0], ...
 *
 * Thus, to update a[1]=BIT[2], we shall update BIT[2], BIT[4], BIT[8],
 * i.e., for current [i], the next update [j] is j=i+(i&-i) //double the
 * last 1-bit from [i].
 *
 * Similarly, to get the partial sum up to a[6]=BIT[7], we shall get the
 * sum of BIT[7], BIT[6], BIT[4], i.e., for current [i], the next
 * summand [j] is j=i-(i&-i) // delete the last 1-bit from [i].
 *
 * To obtain the original value of a[7] (corresponding to index [8] of
 * BIT), we have to subtract BIT[7], BIT[6], BIT[4] from BIT[8], i.e.,
 * starting from [idx-1], for current [i], the next subtrahend [j] is
 * j=i-(i&-i), up to j==idx-(idx&-idx) exclusive. (However, a quicker
 * way but using extra space is to store the original array.)
 */
#
# BIT:
# 96ms 46.67%
class NumArray {
	int[] nums;
	int[] BIT;
	int n;

	public NumArray(int[] nums) {
		this.nums = nums;

		n = nums.length;
		BIT = new int[n + 1];
		for (int i = 0; i < n; i++)
			init(i, nums[i]);
	}

	public void init(int i, int val) {
		i++;
		while (i <= n) {
			BIT[i] += val;
			i += (i & -i);
		}
	}

	void update(int i, int val) {
		int diff = val - nums[i];
		nums[i] = val;
		init(i, diff);
	}

	public int getSum(int i) {
		int sum = 0;
		i++;
		while (i > 0) {
			sum += BIT[i];
			i -= (i & -i);
		}
		return sum;
	}

	public int sumRange(int i, int j) {
		return getSum(j) - getSum(i - 1);
	}
}

// Your NumArray object will be instantiated and called as such:
// NumArray numArray = new NumArray(nums);
// numArray.sumRange(0, 1);
// numArray.update(1, 10);
// numArray.sumRange(1, 2);

'''
