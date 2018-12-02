__source__ = 'https://leetcode.com/problems/3sum-closest/description/'
# https://github.com/kamyu104/LeetCode/blob/master/Python/3sum-closest.py
# Time:  O(n^2)
# Space: O(1)
#
# Description: Leetcode # 16. 3Sum Closest
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
# Companies
# Bloomberg
# Related Topics
# Array Two Pointers
# Similar Questions
# 3Sum 3Sum Smaller
#
import unittest
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

#test
test = Solution2()
num = [1,2,3,4,5,6]
print test.threeSumClosest(num, 16)

class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)
        result = Solution().threeSumClosest([-1, 2, 1, -4], 1)
        print result

if __name__ == '__main__':
    unittest.main()

Java = '''
#Thought:
Similar to 3 Sum problem, use 3 pointers to point current element,
next element and the last element. If the sum is less than target,
it means we have to add a larger element so next element move to the next.

If the sum is greater, it means we have to add a smaller element so last element move to the second last element.
Keep doing this until the end. Each time compare the difference between sum and target,
if it is less than minimum difference so far, then replace result with it, otherwise keep iterating.

#94.73% 10ms
class Solution {
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

#94.73% 10ms
class Solution {
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

# 12ms 75.58% java O(n2)
class Solution {
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

#8ms 99.74%
class Solution {
    public int threeSumClosest(int[] nums, int target) {
        for(int i = 0;;i++){
            if(hasSumOfTarget(nums, target + i)) return target + i;
            if(hasSumOfTarget(nums, target - i)) return target - i;
        }
    }

    public boolean hasSumOfTarget(int[] nums, int target){
        if(nums == null || nums.length < 3) return false;
        Arrays.sort(nums);
        for(int i = 0; i < nums.length - 2; i++){
            int j = i + 1;
            int k = nums.length - 1;
            while(j < k){
                if((nums[j] + nums[k]) == (target - nums[i])){
                    return true;
                }else if((nums[j] + nums[k]) < (target - nums[i])){
                    j++;
                }else{
                    k--;
                }
            }
        }
        return false;
    }
}
'''