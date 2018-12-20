__source__ = 'https://leetcode.com/problems/next-permutation/'
# https://github.com/kamyu104/LeetCode/blob/master/Python/next-permutation.py
# Time:  O(n)
# Space: O(1)
# Array
#
# Description: Leetcode # 31. Next Permutation
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
# Companies
# Google
# Related Topics
# Array
# Similar Questions
# Permutations Permutations II Permutation Sequence Palindrome Permutation II
# similar with https://leetcode.com/problems/next-greater-element-iii/description/
#
import unittest
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
class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)
        test = SolutionOther()
        print test.nextPermutation([6,7,5,3,5,6,2,9,1,2,7,0,9])

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

if __name__ == '__main__':
    unittest.main()

Java = '''
Thought: https://leetcode.com/problems/next-permutation/solution/

My idea is for an array:

Start from its last element, traverse backward to find the first one with index i 
that satisfy num[i-1] < num[i].
So, elements from num[i] to num[n-1] is reversely sorted.
To find the next permutation, we have to swap some numbers at different positions, 
to minimize the increased amount,
we have to make the highest changed position as high as possible.
Notice that index larger than or equal to i is not possible as num[i,n-1] is reversely sorted.
So, we want to increase the number at index i-1, clearly,
swap it with the smallest number between num[i,n-1] that is larger than num[i-1].
For example, original number is 121543321, we want to swap the '1' at position 2 with '2' at position 7.
The last step is to make the remaining higher position part as small as possible,
we just have to reversely sort the num[i,n-1]
The following is my code:

# 13ms 32.79%
class Solution {
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
#
# 在当前序列中，从尾端往前寻找两个相邻元素，前一个记为first，后一个记为second，并且满足first 小于 second。
# 然后再从尾端寻找另一个元素number，如果满足first 小于number，即将第first个元素与number元素对调，并将second元素之后（
# 包括second）的所有元素颠倒排序，即求出下一个序列
#
# example:
# 6，3，4，9，8，7，1
# 此时 first ＝ 4，second = 9
# 从尾巴到前找到第一个大于first的数字，就是7
# 交换4和7，即上面的swap函数，此时序列变成6，3，7，9，8，4，1
# 再将second＝9以及以后的序列重新排序，让其从小到大排序，使得整体最小，即reverse一下（因为此时肯定是递减序列）
# 得到最终的结果：6，3，7，1，4，8，9


# 8ms 98.66%
class Solution {
    public void nextPermutation(int[] nums) {
        int left = nums.length-1;
        int right = nums.length-1;
        while(left>0 && nums[left]<=nums[left-1]) {
            left--;
        }
        int index=left-1;
        if(index>=0) {
            while(left<nums.length && nums[left]>nums[index]) {
                left++;
            }
            swap(nums, index, left-1);
        }
        left=index+1;
        while(left<right) {
            swap(nums, left++, right--);
        }
    }
    private void swap(int[] nums, int a, int b) {
        int temp = nums[a];
        nums[a] = nums[b];
        nums[b] = temp;
    }
}
'''

