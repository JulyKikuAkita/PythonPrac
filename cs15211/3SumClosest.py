__author__ = 'July'
# https://github.com/kamyu104/LeetCode/blob/master/Python/3sum-closest.py
# Time:  O(n^2)
# Space: O(1)
#
# Given an array S of n integers,
# find three integers in S such that the sum is closest to a given number, target.
# Return the sum of the three integers.
# You may assume that each input would have exactly one solution.
#
# For example, given array S = {-1 2 1 -4}, and target = 1.
#
# The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
#
# Bloomberg
# Hide Tags Array Two Pointers
# Hide Similar Problems (M) 3Sum (M) 3Sum Smaller



class Solution:
    # @return an integer
    def threeSumClosest(self, nums, target):
        nums, result, min_diff, i = sorted(nums), float("inf"), float("inf"), 0
        while i < len(nums) - 2:
            j , k = i + 1, len(nums) - 1
            while j < k:
                diff = nums[i] + nums[j] + nums[k] - target
                if abs(diff) < min_diff:
                    min_diff = abs(diff)
                    result = nums[i] + nums[j] + nums[k]
                if diff < 0:
                    j += 1
                elif diff > 0:
                    k -= 1
                else:
                    return target
            i += 1
            while i < len(nums) - 2 and nums[i] == nums[i - 1]:
                i += 1
        return result


class Solution2:
    # @return an integer
    def threeSumClosest(self, num, target):
        ans = None
        num.sort()

        for i in range(len(num)):
            l, r = i+1, len(num)-1
            while (l < r):
                tempsum = num[l] + num[r] + num[i]
                if ans is None or abs(tempsum - target) < abs(ans - target):
                    ans = tempsum
                if tempsum <= target:
                    l = l + 1
                else:
                    r = r - 1

        return ans

# Java:
# http://www.programcreek.com/2013/02/leetcode-3sum-closest-java/
#test
test = Solution2()
num = [1,2,3,4,5,6]
print test.threeSumClosest(num, 16)

if __name__ == '__main__':
    result = Solution().threeSumClosest([-1, 2, 1, -4], 1)
    print result
#java
js1 = ''' 99.83%
public class Solution {
    public int threeSumClosest(int[] nums, int target) {
        int len = nums.length;
        if (len < 3) {
            return 0;
        }
        long result = target > 0 ? Integer.MIN_VALUE : Integer.MAX_VALUE;
        Arrays.sort(nums);
        int i = 0;
        while (i < len - 2) {
            int curTarget = target - nums[i];
            int j = i + 1;
            int k = len - 1;
            while (j < k) {
                int sum = nums[j] + nums[k];
                if (Math.abs(target - result) > Math.abs(curTarget - sum)) {
                    result = nums[i] + sum;
                }
                if (sum < curTarget) {
                    while (++j < k && nums[j - 1] == nums[j]);
                } else if (sum > curTarget) {
                    while (--k > j && nums[k + 1] == nums[k]);
                } else {
                    return target;
                }
            }
            while (++i < len - 2 && nums[i - 1] == nums[i]);
        }
        return (int) result;
    }
}
'''
js = '''
public class Solution {
    public int threeSumClosest(int[] nums, int target) {
        if (nums == null || nums.length < 3) {
            return 0;
        }
        Arrays.sort(nums);
        int result = nums[0] + nums[1] + nums[2];
        int i = 0;
        while (i < nums.length - 2) {
            int j = i + 1;
            int k = nums.length - 1;
            while (j < k) {
                int curr = nums[i] + nums[j] + nums[k];
                int diff = curr - target;
                result = Math.abs(result - target) < Math.abs(diff) ? result : curr;
                if (diff == 0) {
                    return result;
                }
                if (curr < target) {
                    while (++j < k && nums[j] == nums[j - 1]);
                } else {
                    while (--k > j && nums[k] == nums[k + 1]);
                }
            }
            while (++i < nums.length - 2 && nums[i] == nums[i - 1]);
        }
        return result;
    }
}

java O(n2)
public class Solution {
    public int threeSumClosest(int[] num, int target) {
        int result = num[0] + num[1] + num[num.length - 1];
        Arrays.sort(num);
        for (int i = 0; i < num.length - 2; i++) {
            int start = i + 1, end = num.length - 1;
            while (start < end) {
                int sum = num[i] + num[start] + num[end];
                if (sum > target) {
                    end--;
                } else {
                    start++;
                }
                if (Math.abs(sum - target) < Math.abs(result - target)) {
                    result = sum;
                }
            }
        }
        return result;
    }
}
'''