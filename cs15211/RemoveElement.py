__author__ = 'July'
# https://github.com/kamyu104/LeetCode/blob/master/Python/remove-element.py
# Time:  O(n)
# Space: O(1)
# Array
#
# Given an array and a value, remove all instances of that value in place and return the new length.
#
# The order of elements can be changed. It doesn't matter what you leave beyond the new length.
#

class Solution:
    # @param    A       a list of integers
    # @param    elem    an integer, value need to be removed
    # @return an integer
    def removeElement(self, A, elem):
        i, last = 0, len(A) - 1
        while i <= last:
            if A[i] == elem:
                A[i], A[last] = A[last], A[i]
                last -= 1
            else:
                i += 1
        return last + 1

if __name__ == "__main__":
    A = [1, 2, 3, 4, 5, 2, 2]
    print Solution().removeElement(A, 2) , A

class SolutionOther:
    # @param    A       a list of integers
    # @param    elem    an integer, value need to be removed
    # @return an integer
    def removeElement(self, A, elem):
        answer =0
        for i in range(len(A)):
            if A[i] != elem:
                A[answer]=A[i]
                answer += 1
        return answer



t1 = SolutionOther()
print t1.removeElement([1,1,1],1)
print t1.removeElement([1, 2, 3, 4, 5, 2, 2], 2)

#java
js = '''
public class Solution {
    public int removeElement(int[] nums, int val) {
        int end = nums.length;
        for (int i = 0; i < end; i++) {
            if (nums[i] == val) {
                swap(nums, i--, --end);
            }
        }
        return end;
    }

    private void swap(int[] nums, int i, int j) {
        int tmp = nums[i];
        nums[i] = nums[j];
        nums[j] = tmp;
    }
}
'''