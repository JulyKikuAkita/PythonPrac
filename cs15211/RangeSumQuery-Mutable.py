__author__ = 'July'
# https://github.com/kamyu104/LeetCode/blob/master/Python/range-sum-query-mutable.py
# Time:  ctor:   O(n),
#        update: O(logn),
#        query:  O(logn)
# Space: O(n)
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
#  Segment Tree Binary Indexed Tree

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

#java
# http://algobox.org/walls-and-gates/
js = '''
#BFS
public class Solution {
    static final int[] bit = new int[] {0, 1,0,-1,0};
    public void wallsAndGates(int[][] rooms) {
        if(rooms == null || rooms.length == 0) {
            return ;
        }

        int m = rooms.length;
        int n = rooms[0].length;

        Deque<Grid> queue = new ArrayDeque<>();
        for (int i = 0; i < m; i++){
            for(int j = 0; j < n; j++){
                if(rooms[i][j] == 0){
                    queue.offer(new Grid(i, j, 0));
                }
            }
        }

        while(!queue.isEmpty()){
            Grid cur = queue.poll();

            for(int k = 0; k < 4; k++){
                int x = cur.x + bit[k];
                int y = cur.y + bit[k+1];
                int dis = cur.dis;

                //both works
                //if(x >= 0 && y >= 0 && x < m && y < n && rooms[x][y] > dis + 1  ){
                if(x >= 0 && y >= 0 && x < m && y < n && rooms[x][y] == Integer_MAX_VALUE ){
                    rooms[x][y] = dis + 1;
                    queue.offer(new Grid(x,y,dis+1));
                }
            }

        }
    }


    class Grid{
        int x;
        int y;
        int dis;

        Grid(int i, int j, int dis){
            this.x = i;
            this.y = j;
            this.dis = dis;
        }
    }
}

#DFS
public class Solution {
    static final int[] bit = new int[] {0, 1,0,-1,0};
    private void dfs(int[][] rooms, int x, int y, int m, int n){
        for(int k = 0; k < 4; k++){
                int i = x + bit[k];
                int j = y + bit[k+1];

                 if(i >= 0 && j >= 0 && i < m && j < n && rooms[i][j] > rooms[x][y] + 1  ){
                    rooms[i][j] = rooms[x][y] + 1;
                    dfs(rooms, i, j, m, n);
                }
    }
    }

    public void wallsAndGates(int[][] rooms) {
        if(rooms == null || rooms.length == 0) {
            return ;
        }

        int m = rooms.length;
        int n = rooms[0].length;

        for (int i = 0; i < m; i++){
            for(int j = 0; j < n; j++){
                if(rooms[i][j] == 0){
                    dfs(rooms, i, j , m ,n);
                }
            }
        }


    }

}

#

public class NumArray {
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
'''