__source__ = 'https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/'
# https://github.com/kamyu104/LeetCode/blob/master/Python/remove-duplicates-from-sorted-array-ii.py
# Time:  O(n)
# Space: O(1)
# Array
#
# Description: Leetcode # 80. Remove Duplicates from Sorted Array II
#
# Follow up for "Remove Duplicates":
# What if duplicates are allowed at most twice?
#
# For example,
# Given sorted array nums = [1,1,1,2,2,3],
#
# Your function should return length = 5, with the first five elements of nums being 1, 1, 2, 2 and 3.
# It doesn't matter what you leave beyond the new length.
#
#
# Companies
# Facebook
# Related Topics
# Array Two Pointers
# 26. Remove Duplicates from Sorted Array
#
import unittest
class Solution:
    # @param a list of integers
    # @return an integer
    def removeDuplicates(self, A):
        if not A:
            return 0
        last, i, same = 0, 1, False
        while i < len(A):
            if A[last] != A[i] or not same:
                same = A[last] == A[i]
                last += 1
                A[last] = A[i]
            i += 1
        return last + 1

class Solution2:
    # @param a list of integers
    # @return an integer
    def removeDuplicatesWithDict(self, A):
        if not A:
            return 0
        dict = {A[i] : 0 for i in xrange(len(A))}
        last = 0
        for i in xrange(len(A)):
            dict[A[i]] += 1
            if dict[A[i]] < 3 or last < 2:
                A[last] = A[i]
                last += 1

        return last

class SolutionOther:
    # @param A a list of integers
    # @return an integer
    def removeDuplicates(self, A):
        ans = 0
        for i in range(len(A)):
            if ans < 2 or A[ans-2] != A[i]:
                A[ans] = A[i]
                ans += 1 #seems not working for [1,1,1]
                #print i, " = ", A, ans
        return ans

class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)
        #test
        test = SolutionOther()
        A = [1,1,1,2,2,3]
        B = [1,1,1]
        print test.removeDuplicates(B), B

        #print Solution().removeDuplicates([1, 1, 1, 2, 2, 3])
        #print Solution2().removeDuplicates([1, 1, 1, 2, 2, 3])
        A= [1, 1, 1, 2, 2, 3]
        print Solution2().removeDuplicatesWithDict(A), A

if __name__ == '__main__':
    unittest.main()

Java = '''
# Thought:

#24.92% 1ms
class Solution {
    public int removeDuplicates(int[] nums) {
        int i = 0;
        for (int n : nums)
            if (i < 2 || n > nums[i-2]) //(allow duplicates up to 2):
                nums[i++] = n;
        return i;
    }
}

# Note, if only allow one duiplicate:
# Remove Duplicates from Sorted Array(no duplicates) :
# https://leetcode.com/problems/remove-duplicates-from-sorted-array/description/
    public int removeDuplicates(int[] nums) {
        int i = 0;
        for(int n : nums)
            if(i < 1 || n > nums[i - 1])
                nums[i++] = n;
        return i;
    }

# 10ms 33.50%
class Solution {
    public int removeDuplicates(int[] nums) {
        int len = nums.length;
        if (len < 2) {
            return len;
        }
        int end = 0;
        boolean hasDuplicate = false;
        for (int i = 1; i < len; i++) {
            if (nums[i] == nums[end]) {
                if (!hasDuplicate) {
                    hasDuplicate = true;
                    nums[++end] = nums[i];
                }
            } else {
                hasDuplicate = false;
                nums[++end] = nums[i];
            }
        }
        return end + 1;
    }
}

Thought: http://tech-wonderland.net/blog/leetcode-remove-duplicates-from-sorted-array-i-and-ii.html
I think both Remove Duplicates from Sorted Array I and II could be solved in a consistent
and more general way by allowing the duplicates to appear k times
(k = 1 for problem I and k = 2 for problem II). Here is my way:
we need a count variable to keep how many times the duplicated element appears,
if we encounter a different element, just set counter to 1, if we encounter a duplicated one,
we need to check this count, if it is already k, then we need to skip it, otherwise,
we can keep this element. The following is the implementation and can pass both OJ:

int removeDuplicates(int A[], int k) {
            if (A.length <= k) return A.length;
            int i = 1, j = 1;
            int cnt = 1;
            while (j < A.length) {
                if (A[j] != A[j-1]) {
                    cnt = 1;
                    A[i++] = A[j];
                }
                else {
                    if (cnt < k) {
                        A[i++] = A[j];
                        cnt++;
                    }
                }
                ++j;
            }
            return i;
    }

'''
