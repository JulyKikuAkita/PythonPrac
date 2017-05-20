__author__ = 'July'
# https://github.com/kamyu104/LeetCode/blob/master/Python/remove-duplicates-from-sorted-array.py
# Time:  O(n)
# Space: O(1)
# Array
#
# Given a sorted array, remove the duplicates in place such that each element appear only once and return the new length.
#
# Do not allocate extra space for another array, you must do this in place with constant memory.
#
# For example,
# Given input array A = [1,1,2],
#
# Your function should return length = 2, and A is now [1,2].
# Microsoft Bloomberg Facebook
# Hide Tags Array Two Pointers


class Solution:
    # @param a list of integers
    # @return an integer
    def removeDuplicates(self, A):
        if not A:
            return 0
        last, i = 0, 1
        while i < len(A):
            if A[last] != A[i]:
                last += 1
                A[last] = A[i]
            i += 1
        return last + 1

if __name__ == "__main__":
    print Solution().removeDuplicates([1, 1, 2])

class SolutionOther:
    # @param a list of integers
    # @return an integer
    def removeDuplicates(self, A):
        if len(A) == 0:
            return 0
        cur = 1
        for i in range(1, len(A)):
            if A[i] != A[i-1]:
                A[cur] = A[i]
                cur += 1
        return cur

# java solution
# http://www.programcreek.com/2013/01/leetcode-remove-duplicates-from-sorted-array-java/
#test
test = SolutionOther()
print test.removeDuplicates([0,1,1,1,2,3])

#java
js = '''
public class Solution {
    public int removeDuplicates(int[] nums) {
        int end = 0;  //if end = 1 ;
        for (int i = 1; i < nums.length; i++) {
            if (nums[i] != nums[end]) {
                nums[++end] = nums[i];
                // nums[end++] = nums[i]; // if end == 1
            }
        }
        return end + 1;
        // return end;
    }
}


public class Solution {
    public int removeDuplicates(int[] nums) {
        if( nums == null || nums.length == 0) return 0;

        int last = 1;
        int cur = 1;

        while ( cur < nums.length) {
            if (nums[cur] != nums[last - 1]){
                nums[last++] = nums[cur];
            }
            cur++;
        }
        return last;
    }
}
'''