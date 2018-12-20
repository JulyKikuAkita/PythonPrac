__source__ = 'https://leetcode.com/problems/reverse-pairs/'
# Time:  O(nlogn) with mersort, o(n^2) with building bit
# Space: O(n)
#
# Description: 493. Reverse Pairs
#
# Given an array nums, we call (i, j) an important reverse pair if i < j and nums[i] > 2*nums[j].
#
# You need to return the number of important reverse pairs in the given array.
#
# Example1:
#
# Input: [1,3,2,3,1]
# Output: 2
# Example2:
#
# Input: [2,4,3,5,1]
# Output: 3
# Note:
# The length of the given array will not exceed 50,000.
# All the numbers in the input array are in the range of 32-bit integer.
# Hide Company Tags Google
# Hide Tags Binary Indexed Tree Segment Tree Binary Search Tree Divide and Conquer
# Hide Similar Problems (H) Count of Smaller Numbers After Self (H) Count of Range Sum
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
# Thought: https://leetcode.com/problems/reverse-pairs/solution/

# General principles behind problems similar to "Reverse Pairs" -thinkging process
# https://discuss.leetcode.com/topic/79227/general-principles-behind-problems-similar-to-reverse-pairs

https://discuss.leetcode.com/topic/78933/very-short-and-clear-mergesort-bst-java-solutions
Very Short and Clear MergeSort & BST Java Solutions

1.
MergeSort

Explanation: In each round, we divide our array into two parts and sort them.
So after "int cnt = mergeSort(nums, s, mid) + mergeSort(nums, mid+1, e); ",
the left part and the right part are sorted and now our only job is to count how many pairs
of number (leftPart[i], rightPart[j]) satisfies leftPart[i] <= 2*rightPart[j].
For example,
left: 4 6 8 right: 1 2 3
so we use two pointers to travel left and right parts. 
For each leftPart[i], if j<=e && nums[i]/2.0 > nums[j],
we just continue to move j to the end, to increase rightPart[j], 
until it is valid. Like in our example,
left's 4 can match 1 and 2; left's 6 can match 1, 2, 3, and left's 8 can match 1, 2, 3. 
So in this particular round,
there are 8 pairs found, so we increases our total by 8.

# 112ms 20.88%
class Solution {
    public int reversePairs(int[] nums) {
        return mergeSort(nums, 0, nums.length - 1);
    }

    private int mergeSort(int[] nums, int s, int e) {
        if (s >= e) return 0;
        int mid = s + (e - s) / 2;
        int cnt = mergeSort(nums, s, mid) + mergeSort(nums, mid + 1, e);
        for (int i = s, j = mid + 1; i<= mid; i++) {
            while(j <= e && nums[i] / 2.0 > nums[j]) j++;
            cnt += j - (mid + 1);
        }
        Arrays.sort(nums, s, e + 1);
        return cnt;
    }
}

Or:
Because left part and right part are sorted, 
you can replace the Arrays.sort() part with a actual merge sort process.
The previous version is easy to write, while this one is faster.

# 81ms 56.87%
class Solution {
    int[] mHelper;
    public int reversePairs(int[] nums) {
        mHelper = new int[nums.length];
        return mergeSort(nums, 0, nums.length - 1);
    }
    
    private int mergeSort(int[] nums, int s, int e) {
        if (s >= e) return 0;
        int mid = s + (e - s) / 2;
        int cnt = mergeSort(nums, s, mid) + mergeSort(nums, mid + 1, e);
        for (int i = s, j = mid + 1; i<= mid; i++) {
            while(j <= e && nums[i] / 2.0 > nums[j]) j++;
            cnt += j - (mid + 1);
        }
        //Arrays.sort(nums, s, e + 1);
        myMerge(nums, s, mid, e);
        return cnt;
    }
    
    private void myMerge(int[] nums, int s, int mid, int e){
        for (int i = s; i <= e; i++) {
            mHelper[i] = nums[i];
        }
        int p1 = s; //pointer for left part
        int p2 = mid + 1;  //pointer for rigtht part
        int i = s; //pointer for sorted array
        while (p1 <= mid || p2 <= e) {
            if (p1 > mid || (p2 <= e && mHelper[p1] >= mHelper[p2])) {
                nums[i++] = mHelper[p2++];
            } else {
                nums[i++] = mHelper[p1++];
            }
        }
    }
}

BST
BST solution is no longer acceptable, because it's performance can be very bad, O(n^2) actually,
for extreme cases like [1,2,3,4......49999], due to the its unbalance, 
but I am still providing it below just FYI.
We build the Binary Search Tree from right to left, and at the same time,
search the partially built tree with nums[i]/2.0. The code below should be clear enough.
Similar to this https://leetcode.com/problems/count-of-smaller-numbers-after-self/. 
But the main difference is:
here, the number to add and the number to search are different (add nums[i], but search nums[i]/2.0),
so not a good idea to combine build and search together.

# TLE
class Solution {
    public int reversePairs(int[] nums) {
        Node root = null;
        int[] cnt = new int[1];
        for(int i = nums.length-1; i>=0; i--){
            search(cnt, root, nums[i]/2.0);//search and count the partially built tree
            root = build(nums[i], root);//add nums[i] to BST
        }
        return cnt[0];
    }

    private void search(int[] cnt, Node node, double target){
        if(node==null) return;
        else if(target == node.val) cnt[0] += node.less;
        else if(target < node.val) search(cnt, node.left, target);
        else{
            cnt[0]+=node.less + node.same;
            search(cnt, node.right, target);
        }
    }

    private Node build(int val, Node n){
        if(n==null) return new Node(val);
        else if(val == n.val) n.same+=1;
        else if(val > n.val) n.right = build(val, n.right);
        else{
            n.less += 1;
            n.left = build(val, n.left);
        }
        return n;
    }

    class Node{
        int val, less = 0, same = 1;//less: number of nodes that less than this node.val
        Node left, right;
        public Node(int v){
            this.val = v;
        }
    }
}

'''
