__source__ = 'https://leetcode.com/problems/first-missing-positive/'
# https://github.com/kamyu104/LeetCode/blob/master/Python/first-missing-positive.py
# Time:  O(n)
# Space: O(1)
#
# Description: Leetcode # 41. First Missing Positive
#
# Given an unsorted integer array, find the first missing positive integer.
#
# For example,
# Given [1,2,0] return 3,
# and [3,4,-1,1] return 2.
#
# Your algorithm should run in O(n) time and uses constant space.
#
# Related Topics
# Array
# Similar Questions
# Missing Number Find the Duplicate Number Find All Numbers Disappeared in an Array
#
import unittest
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
class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)
        test = Solution2()
        #print test.firstMissingPositive([1,2,0])
        #print test.firstMissingPositive([3,4,-1,1])
        #print test.firstMissingPositive([2,1])
        #print Solution().firstMissingPositive([1,2,0])
        #print Solution().firstMissingPositive([3,4,-1,1])
        print Solution().firstMissingPositive([-1,0,1])

if __name__ == '__main__':
    unittest.main()

Java = '''
# Thought: https://leetcode.com/problems/first-missing-positive/solution/
# https://leetcode.windliang.cc/leetCode-41-First-Missing-Positive.html
# 5ms 100%
class Solution {
    public int firstMissingPositive(int[] nums) {
        int n = nums.length;
    
        // 1. mark numbers (num < 0) and (num > n) with a special marker number (n+1) 
        // (we can ignore those because if all number are > n then we'll simply return 1)
        for (int i = 0; i < n; i++) {
            if (nums[i] <= 0 || nums[i] > n) {
                nums[i] = n + 1;
            }
        }
        // note: all number in the array are now positive, and on the range 1..n+1

        // 2. mark each cell appearing in the array, by converting the index for that number to negative
        for (int i = 0; i < n; i++) {
            int num = Math.abs(nums[i]);
            if (num > n) {
                continue;
            }
            num--; // -1 for zero index based array (so the number 1 will be at pos 0)
            if (nums[num] > 0) { // prevents double negative operations
                nums[num] = -1 * nums[num];
            }
        }

        // 3. find the first cell which isn't negative (doesn't appear in the array)
        for (int i = 0; i < n; i++) {
            if (nums[i] >= 0) {
                return i + 1;
            }
        }

        // 4. no positive numbers were found, which means the array contains all numbers 1..n
        return n + 1;
    }
}
# https://leetcode.com/problems/first-missing-positive/discuss/17214/Java-simple-solution-with-documentation
# Numbers greater then n can be ignored because the missing integer must be in the range 1..n+1
# If each cell in the array were to contain positive integers only, 
# we can use the negative of the stored number as a flag to mark something 
# (in this case the flag indicates this index was found in some cell of the array)

# match nums[i] with i //nums[index] = index + 1
# index based swap
# 5ms 100%
class Solution {
    public int firstMissingPositive(int[] nums) {
        int index = 0;
        while (index < nums.length) {
            if (nums[index] > 0 && nums[index] <= nums.length
            && nums[index] != index + 1 && nums[index] != nums[nums[index] - 1]) {
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
# https://leetcode.com/problems/first-missing-positive/discuss/17126/Beat-100-Fast-Elegant-Java-Index-Based-Solution-with-Explanation
# index based swap
# 5ms 100%
class Solution {
    public int firstMissingPositive(int[] nums) {
        int i = 0, n = nums.length;
        while (i < n) {
            // If the current value is in the range of (0,length) and it's not at its correct position, 
            // swap it to its correct position.
            // Else just continue;
            if (nums[i] >= 0 && nums[i] < n && nums[nums[i]] != nums[i])
                swap(nums, i, nums[i]);
            else
                i++;
        }
        int k = 1;

        // Check from k=1 to see whether each index and value can be corresponding.
        while (k < n && nums[k] == k) k++;

        // If it breaks because of empty array or reaching the end. K must be the first missing number.
        if (n == 0 || k < n)
            return k;
        else   // If k is hiding at position 0, K+1 is the number. 
            return nums[0] == k ? k + 1 : k;

    }

    private void swap(int[] nums, int i, int j) {
        int temp = nums[i];
        nums[i] = nums[j];
        nums[j] = temp;
    }
}
# https://leetcode.com/problems/first-missing-positive/discuss/17135/Java-solution-with-integers-encode-trick-explained
# encoding based swap
# 8ms 21.53%
class Solution {
    public int firstMissingPositive(int[] nums) {
        int n = nums.length;
        int m = n + 1;
        
        for (int i = 0; i < n; i++) {
            if (nums[i] <= 0 || nums[i] > n) nums[i] = 0;
        }
        
        for (int i = 0; i < n ; i++) {
            int prev = nums[i] % m;
            if (prev > 0) nums[prev - 1] = (prev * m) + nums[prev - 1] % m;
        }
        
        for (int i = 0; i < n ; i++) {
            if (nums[i] / m != i + 1) return i + 1;
        }
        return m;
    }
}

'''
