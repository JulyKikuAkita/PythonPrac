__author__ = 'July'
# https://github.com/kamyu104/LeetCode/blob/master/Python/next-permutation.py
# Time:  O(n)
# Space: O(1)
# Array
#
# Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.
#
# If such arrangement is not possible, it must rearrange it as the lowest possible order (ie, sorted in ascending order).
#
# The replacement must be in-place, do not allocate extra memory.
#
# Here are some examples. Inputs are in the left-hand column and its corresponding outputs are in the right-hand column.
# 1,2,3 -> 1,3,2
# 3,2,1 -> 1,2,3
# 1,1,5 -> 1,5,1
#

class Solution:
    # @param num, a list of integer
    # @return a list of integer
    def nextPermutation(self, num):
        k, l = -1, 0

        #find the first item in ascending order
        for i in xrange(len(num) - 1):
            if num[i] < num[i+1]:
                k = i
        # if decending order, return reversed num
        if k == -1:
            return num[::-1]

        #find first number > num[k]
        for i in xrange(len(num)):
            if num[i] > num[k]:
                l = i
        #switch num[k] and num[l] and return num to k and reversed num to k
        num[k], num[l] = num[l], num[k]
        print num, k , l, num[:k+1], num[:k:-1]
        return num[:k+1] + num[:k:-1]

if __name__ == "__main__":
    num = [1, 4, 3, 2]
    #num = Solution().nextPermutation(num)
    #print num
    #num = Solution().nextPermutation(num)
    #print num
    #num = Solution().nextPermutation(num)
    #print num

    test = [1,2,3]
    #print test[:0:-1]
    #print test[:1]
    print Solution().nextPermutation(test)

class SolutionOther:
    # @param num, a list of integer
    # @return a list of lists of integers
    def nextPermutation(self, num):
        for i in range(len(num)-2, -1, -1):
            #print "this round start with i=",i, num[i], num[i+1]
            if num[i] < num[i+1]:
                break
        else:
            num.reverse()
            return num

        for j in range(len(num)-1, i, -1):
            #print "j=", j,"i= ",i
            if num[j] > num[i]:
                num[i], num[j] = num[j], num[i]
                break

        for j in range(0, (len(num) - i) //2):
            #print "j=", j,"(len(num) - i) //2= ",(len(num) - i) //2
            num[i+j+1], num[len(num)-j-1] = num[len(num)-j-1], num[i+j+1]

        return num

#test
test = SolutionOther()
print test.nextPermutation([6,7,5,3,5,6,2,9,1,2,7,0,9])

#java
js = '''
public class Solution {
    public void nextPermutation(int[] nums) {
        if (nums == null || nums.length < 2) {
            return;
        }
        int left = nums.length - 2;
        while (left >= 0 && nums[left] >= nums[left + 1]) {
            left--;
        }
        if (left < 0) {
            reverse(nums, 0, nums.length - 1);
            return;
        }
        int right = nums.length - 1;
        while (nums[right] <= nums[left]) {
            right--;
        }
        swap(nums, left, right);
        reverse(nums, left + 1, nums.length - 1);
    }

    private void reverse(int[] nums, int start, int end) {
        while (start < end) {
            swap(nums, start, end);
            start++;
            end--;
        }
    }

    private void swap(int[] nums, int left, int right) {
        int tmp = nums[left];
        nums[left] = nums[right];
        nums[right] = tmp;
    }
}
'''