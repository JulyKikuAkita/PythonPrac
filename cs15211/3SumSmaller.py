__author__ = 'July'
'''
Given an array of n integers nums and a target, find the number of index triplets i, j, k
with 0 <= i < j < k < n that satisfy the condition nums[i] + nums[j] + nums[k] < target.

For example, given nums = [-2, 0, 1, 3], and target = 2.

Return 2. Because there are two triplets which sums are less than 2:

[-2, 0, 1]
[-2, 0, 3]
Follow up:
Could you solve it in O(n2) runtime?

# Google
# Hide Tags Array Two Pointers
# Hide Similar Problems (M) 3Sum (M) 3Sum Closest

'''

# Time:  O(n^2)
# Space: O(1)

class Solution:
    # @param {integer[]} nums
    # @param {integer} target
    # @return {integer}
    def threeSumSmaller(self, nums, target):
        nums.sort()
        n = len(nums)

        count, k = 0, 2
        while k < n:
            i, j = 0, k-1
            while i < j: # Two Pointers, linear time.
                if nums[i] + nums[j] + nums[k] >= target:
                    j -= 1
                else:
                    count += (j - i)
                    i += 1
            k += 1
        return count


#java
js2 = 64.11% '''
public class Solution {
    public int threeSumSmaller(int[] nums, int target) {
        int result = 0;
        if (nums == null || nums.length < 3) {
            return result;
        }
        Arrays.sort(nums);
        for (int i = 0; i < nums.length - 2; i++) {
            int start = i + 1;
            int end = nums.length - 1;
            int max = target - nums[i];
            while (start < end) {
                int sum = nums[start] + nums[end];
                if (sum < max) {
                    result += end - start;
                    start++;
                } else {
                    end--;
                }
            }
        }
        return result;
    }
}
'''
js1 = 40.53% '''
public class Solution {
    public int threeSumSmaller(int[] nums, int target) {
        if (nums.length < 3) {
            return 0;
        }
        int result = 0;
        Arrays.sort(nums);
        for (int i = 0; i < nums.length - 2; i++) {
            int curTarget = target - nums[i];
            int j = i + 1;
            int k = nums.length - 1;
            while (j < k) {
                if (nums[j] + nums[k] >= curTarget) {
                    k--;
                } else {
                    result += k - j;
                    j++;
                }
            }
        }
        return result;
    }
}
'''
js = '''
public class Solution {
    public int threeSumSmaller(int[] nums, int target) {
        int len = nums.length;
        if (len < 3) {
            return 0;
        }
        Arrays.sort(nums);
        int result = 0;
        for (int i = 0; i < len - 2; i++) {
            int j = i + 1;
            int k = len - 1;
            int max = target - nums[i];
            while (j < k) {
                if (nums[j] + nums[k] < max) {
                    result += k - j;
                    j++;
                } else {
                    k--;
                }
            }
        }
        return result;
    }
}
'''