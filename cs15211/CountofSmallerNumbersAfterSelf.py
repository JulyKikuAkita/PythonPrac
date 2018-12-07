__source__ = 'https://github.com/kamyu104/LeetCode/blob/master/Python/count-of-smaller-numbers-after-self.py'
# https://leetcode.com/problems/count-of-smaller-numbers-after-self/#/description
# Time:  O(nlogn)
# Space: O(n)
#
# Description: Leetcode # 315. Count of Smaller Numbers After Self
#
# You are given an integer array nums and you have to
# return a new counts array. The counts array has the
# property where counts[i] is the number of smaller
# elements to the right of nums[i].
#
# Example:
#
# Given nums = [5, 2, 6, 1]
#
# To the right of 5 there are 2 smaller elements (2 and 1).
# To the right of 2 there is only 1 smaller element (1).
# To the right of 6 there is 1 smaller element (1).
# To the right of 1 there is 0 smaller element.
# Return the array [2, 1, 1, 0].
#
# Companies
# Google
# Related Topics
# Divide and Conquer Binary Indexed Tree Segment Tree Binary Search Tree
# Similar Questions
# Count of Range Sum Queue Reconstruction by Height Reverse Pairs
#
import unittest
# BIT solution.
class Solution(object):
    def countSmaller(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        def binarySearch(A, target, compare):
            start, end = 0, len(A) - 1
            while start <= end:
                mid = (start + end) / 2
                if compare(target, A[mid]):
                    end = mid - 1
                else:
                    start = mid + 1
            return start

        class BIT(object):
            def __init__(self, n) :
                self.__bit = [0] * n

            def __add__(self, i ,val):
                while i < len(self.__bit):
                    self.__bit[i] += val
                    i += ( i & -i)

            def query(self, i):
                ret = 0
                while i > 0:
                    ret += self.__bit[i]
                    i -= (i & -i)
                return ret

         # Get the place (position in the ascending order) of each number.
        sorted_nums, places = sorted(nums), [0] * len(nums)
        for i ,num in enumerate(nums):
            places[i] = binarySearch(sorted_nums, num, lambda x, y : x <= y)

        # Count the smaller elements after the number.
        ans, bit = [0] * len(nums), BIT(len(nums) + 1)
        for i in reversed(xrange(len(nums))):
            ans[i] = bit.query(places[i])
            bit.__add__(places[i] + 1, 1)
        return ans

# Time:  O(nlogn)
# Space: O(n)
# BST solution.
class Solution2(object):
    def countSmaller(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = [0] * len(nums)
        bst = self.BST()
        # Insert into BST and get left count.
        for i in reversed(xrange(len(nums))):
            bst.insertNode(nums[i])
            res[i] = bst.query(nums[i])
        return res

    class BST(object):
        class BSTreeNode(object):
            def __init__(self, val):
                self.val = val
                self.count = 0
                self.left = self.right = None

        def __init__(self):
            self.root = None

        # Insert node into BST.
        def insertNode(self, val):
            node = self.BSTreeNode(val)
            if not self.root:
                self.root = node
                return
            curr = self.root
            while curr:
                # Insert left if smaller.
                if node.val < curr.val:
                    curr.count += 1 # Increase the number of left children.
                    if curr.left:
                        curr= curr.left
                    else:
                        curr.left = node
                        break
                else: # Insert right if larger or equal.
                    if curr.right:
                        curr= curr.right
                    else:
                        curr.right = node
                        break

        # Query the smaller count of the value.
        def query(self, val):
            count = 0
            curr = self.root
            while curr:
                #Insert left
                if val < curr.val:
                    curr = curr.left
                elif val > curr.val:
                    count += 1 + curr.count # Count the number of the smaller nodes.
                    curr = curr.right
                else:  # Equal
                    return count + curr.count
            return 0

# MergeSort
# Thought: https://discuss.leetcode.com/topic/31162/mergesort-solution
# 128ms 64.78%
class Solution3(object):
    def countSmaller(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        def sort(enum):
            half = len(enum) / 2
            if half:
                left, right = sort(enum[:half]), sort(enum[half:])
                for i in range(len(enum))[::-1]:
                    if not right or left and left[-1][1] > right[-1][1]:
                        smaller[left[-1][0]] += len(right)
                        enum[i] = left.pop()
                    else:
                        enum[i] = right.pop()
            return enum
        smaller = [0] * len(nums)
        sort(list(enumerate(nums)))
        return smaller

class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)

if __name__ == '__main__':
    unittest.main()

Java = '''
Thought:

1. building BST:
Every node will maintain a val sum recording the total of number on it's left bottom side,
dup counts the duplication. For example, [3, 2, 2, 6, 1], from back to beginning,we would have:

                1(0, 1)
                     \
                     6(3, 1)
                     /
                   2(0, 2)
                       \
                        3(0, 1)
When we try to insert a number,
the total number of smaller number would be adding dup and sum of the nodes where we turn right.
for example, if we insert 5,
it should be inserted on the way down to the right of 3,
the nodes where we turn right is 1(0,1), 2,(0,2), 3(0,1), so the answer should be (0 + 1)+(0 + 2)+ (0 + 1) = 4

if we insert 7, the right-turning nodes are 1(0,1), 6(3,1), so answer should be (0 + 1) + (3 + 1) = 5

# 5ms 97.81%
class Solution {
    class Node {
        Node left, right;
        int val, sum, dup = 1;
        public Node(int v, int s) {
            val = v;
            sum = s;
        }
    }
    public List<Integer> countSmaller(int[] nums) {
        Integer[] ans = new Integer[nums.length];
        Node root = null;
        for (int i = nums.length - 1; i >= 0; i--) {
            root = insert(nums[i], root, ans, i, 0);
        }
        return Arrays.asList(ans);
    }
    private Node insert(int num, Node node, Integer[] ans, int i, int preSum) {
        if (node == null) {
            node = new Node(num, 0);
            ans[i] = preSum;
        } else if (node.val == num) {
            node.dup++;
            ans[i] = preSum + node.sum;
        } else if (node.val > num) {
            node.sum++;
            node.left = insert(num, node.left, ans, i, preSum);
        } else {
            node.right = insert(num, node.right, ans, i, preSum + node.dup + node.sum);
        }
        return node;
    }
}

# building BST
# 10ms 58.31%
class Solution {
    public List<Integer> countSmaller(int[] nums) {
        List<Integer> result = new ArrayList<>();
        Tree tree = new Tree();
        for (int i = nums.length - 1; i >= 0; i--) {
            result.add(tree.insert(nums[i]));
        }
        Collections.reverse(result);
        return result;
    }

    private class Tree {
        private TreeNode root;

        private int insert(int val) {
            if (root == null) {
                root = new TreeNode(val);
                return 0;
            }
            int count = 0;
            TreeNode cur = root;
            while (true) {
                if (cur.val > val) {
                    cur.leftCount++;
                    if (cur.left != null) {
                        cur = cur.left;
                    } else {
                        cur.left = new TreeNode(val);
                        break;
                    }
                } else if (cur.val < val) {
                    count += cur.leftCount + cur.selfCount;
                    if (cur.right != null) {
                        cur = cur.right;
                    } else {
                        cur.right = new TreeNode(val);
                        break;
                    }
                } else {
                    cur.selfCount++;
                    count += cur.leftCount;
                    break;
                }
            }
            return count;
        }
    }

    private class TreeNode {
        private TreeNode left;
        private TreeNode right;
        private int val;
        private int leftCount;
        private int selfCount;

        TreeNode(int val) {
            this.val = val;
            this.selfCount = 1;
        }
    }
}

# BIT
# 3ms 100%
public class Solution {
    public List<Integer> countSmaller(int[] nums) {
         if (nums == null || nums.length == 0) {
             return new ArrayList<Integer>();
         }
         makePositive(nums);
         int max = findMax(nums);
         int[] tree = new int[max + 1];
         Integer[] result = new Integer[nums.length];
         for (int i = nums.length - 1; i >= 0; i--) {
             result[i] = findResult(nums[i], tree);
             updateTree(nums[i] + 1, tree);
         }
         return Arrays.asList(result);
    }

    private void makePositive(int[] nums) {
        int minus = 0;
        for (int num : nums) {
            minus = Math.min(minus, num);
        }
        if (minus < 0) {
            minus = -minus + 1;
            for (int i = 0; i < nums.length; i++) {
                nums[i] += minus;
            }
        }
    }

    private int findMax(int[] nums) {
        int max = 0;
        for (int num : nums) {
            max = Math.max(max, num);
        }
        return max;
    }

    private void updateTree(int index, int[] tree) {
        while (index < tree.length && index > 0) {
            tree[index]++;
            index += index & (-index);
        }
    }

    private int findResult(int index, int[] tree) {
        int result = 0;
        while (index > 0) {
            result += tree[index];
            index &= index - 1;
        }
        return result;
    }
}


2.Traverse from the back to the beginning of the array, maintain an sorted array of numbers have been visited.
Use findIndex() to find the first element in the sorted array which is larger or equal to target number.
For example, [5,2,3,6,1], when we reach 2, we have a sorted array[1,3,6], findIndex() returns 1,
which is the index where 2 should be inserted and is also the number smaller than 2.
Then we insert 2 into the sorted array to form [1,2,3,6].
Due to the O(n) complexity of ArrayList insertion,
the total runtime complexity is not very fast, but anyway it got AC for around 53ms.

# 34ms 28.40%
class Solution {
    public List<Integer> countSmaller(int[] nums) {
        Integer[] ans = new Integer[nums.length];
        List<Integer> sorted = new ArrayList<Integer>();
        for (int i = nums.length - 1; i >= 0; i--) {
            int index = findIndex(sorted, nums[i]);
            ans[i] = index;
            sorted.add(index, nums[i]);
        }
        return Arrays.asList(ans);
    }
    private int findIndex(List<Integer> sorted, int target) {
        if (sorted.size() == 0) return 0;
        int start = 0;
        int end = sorted.size() - 1;
        if (sorted.get(end) < target) return end + 1;
        if (sorted.get(start) >= target) return 0;
        while (start + 1 < end) {
            int mid = start + (end - start) / 2;
            if (sorted.get(mid) < target) {
                start = mid;
            } else {
                end = mid;
            }
        }
        if (sorted.get(start) >= target) return start;
        return end;
    }
}

3. MergeSort:

The basic idea is to do merge sort to nums[].
To record the result, we need to keep the index of each number in the original array.
So instead of sort the number in nums, we sort the indexes of each number.

Example: nums = [5,2,6,1], indexes = [0,1,2,3]
After sort: indexes = [3,1,0,2]

While doing the merge part, say that we are merging left[] and right[], left[] and right[] are already sorted.

We keep a rightcount to record how many numbers from right[] we have added and keep an array count[] to record the result.

When we move a number from right[] into the new sorted array, we increase rightcount by 1.

When we move a number from left[] into the new sorted array, we increase count[ index of the number ] by rightcount.

# 6ms 87.08%
class Solution {
    int[] count;
    public List<Integer> countSmaller(int[] nums) {
        List<Integer> res = new ArrayList<Integer>();

        count = new int[nums.length];
        int[] indexes = new int[nums.length];
        for(int i = 0; i < nums.length; i++){
            indexes[i] = i;
        }
        mergesort(nums, indexes, 0, nums.length - 1);
        for(int i = 0; i < count.length; i++){
            res.add(count[i]);
        }
        return res;
    }
    private void mergesort(int[] nums, int[] indexes, int start, int end){
        if(end <= start){
            return;
        }
        int mid = (start + end) / 2;
        mergesort(nums, indexes, start, mid);
        mergesort(nums, indexes, mid + 1, end);

        merge(nums, indexes, start, end);
    }
    private void merge(int[] nums, int[] indexes, int start, int end){
        int mid = (start + end) / 2;
        int left_index = start;
        int right_index = mid+1;
        int rightcount = 0;
        int[] new_indexes = new int[end - start + 1];

        int sort_index = 0;
        while(left_index <= mid && right_index <= end){
            if(nums[indexes[right_index]] < nums[indexes[left_index]]){
                new_indexes[sort_index] = indexes[right_index];
                rightcount++;
                right_index++;
            }else{
                new_indexes[sort_index] = indexes[left_index];
                count[indexes[left_index]] += rightcount;
                left_index++;
            }
            sort_index++;
        }
        while(left_index <= mid){
            new_indexes[sort_index] = indexes[left_index];
            count[indexes[left_index]] += rightcount;
            left_index++;
            sort_index++;
        }
        while(right_index <= end){
            new_indexes[sort_index++] = indexes[right_index++];
        }
        for(int i = start; i <= end; i++){
            indexes[i] = new_indexes[i - start];
        }
    }
}
'''






