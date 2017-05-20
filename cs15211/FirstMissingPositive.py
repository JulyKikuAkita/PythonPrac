__author__ = 'July'
# https://github.com/kamyu104/LeetCode/blob/master/Python/first-missing-positive.py
# Time:  O(n)
# Space: O(1)
#
# Given an unsorted integer array, find the first missing positive integer.
#
# For example,
# Given [1,2,0] return 3,
# and [3,4,-1,1] return 2.
#
# Your algorithm should run in O(n) time and uses constant space.
#  Array

class Solution:
    # @param A, a list of integers
    # @return an integer
    def firstMissingPositive(self, A):
        i = 0
        while i < len(A):
            print "i = ", i, A[i], A[A[i] - 1], A
            if A[i] > 0 and A[i] - 1 < len(A) and A[i] != A[A[i] - 1]:
                A[A[i] - 1], A[i] = A[i], A[A[i] - 1]
            else:
                i += 1
        for i, integer in enumerate(A):
            print i, integer
            if integer != i + 1:
                return i + 1
        return len(A) + 1

class Solution2:
    # @param A, a list of integers
    # @return an integer
    def firstMissingPositive(self, A):
        L = len(A)
        for i in range(L) :
            #print "i =", i, A[i], A[A[i] - 1]
            while A[i] > 0 and A[i] <= L and A[i] != A[A[i]-1] and i != A[i] - 1:
                temp = A[A[i] - 1]
                A[A[i] - 1] = A[i]
                A[i] = temp
                print A
                #A[i], A[A[i] - 1] = A[A[i] - 1], A[i]  dosen't work

        for i in range(L):
            if i != A[i] - 1:
                print i, A[i] - 1,  A
                return i+1
        #print L
        return L+1

#test
test = Solution2()
#print test.firstMissingPositive([1,2,0])
#print test.firstMissingPositive([3,4,-1,1])
#print test.firstMissingPositive([2,1])

if __name__ == "__main__":
    #print Solution().firstMissingPositive([1,2,0])
    #print Solution().firstMissingPositive([3,4,-1,1])
    print Solution().firstMissingPositive([-1,0,1])

#java
js  = '''
public class Solution {
    public int firstMissingPositive(int[] nums) {
        int index = 0;
        while (index < nums.length) {
            if (nums[index] != index + 1 && nums[index] > 0 && nums[index] <= nums.length && nums[index] != nums[nums[index] - 1]) {
                swap(nums, index, nums[index] - 1);
            } else {
                index++;
            }
        }
        for (int i = 0; i < nums.length; i++) {
            if (nums[i] != i + 1) {
                return i + 1;
            }
        }
        return nums.length + 1;
    }

    private void swap(int[] nums, int i, int j) {
        int tmp = nums[i];
        nums[i] = nums[j];
        nums[j] = tmp;
    }
}
'''