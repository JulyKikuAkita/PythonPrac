__source__ = 'https://leetcode.com/problems/contains-duplicate-ii/description/'
# https://github.com/kamyu104/LeetCode/blob/master/Python/contains-duplicate-ii.py
# Time:  O(n)
# Space: O(n)
#
# Description: Leetcode # 219. Contains Duplicate II
#
# Given an array of integers and an integer k, return true if
# and only if there are two distinct indices i and j in the array
# such that nums[i] = nums[j] and the difference between i and j is at most k.
#
# Companies
# Palantir Airbnb
# Related Topics
# Array Hash Table
# Similar Questions
# Contains Duplicate Contains Duplicate III
#
import unittest
class Solution:
    # @param {integer[]} nums
    # @param {integer} k
    # @return {boolean}
    def containsNearbyDuplicate(self, nums, k):
        dict = {}
        for i, num in enumerate(nums):
            if num not in dict:
                dict[num] = i
            else:
                 # It the value occurs before, check the difference.
                if i - dict[num] <= k:
                    return True
                # Update the index of the value.
                dict[num] = i
        return False

class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)
        print Solution().containsNearbyDuplicate([1,5,3,4,5], 2)

if __name__ == '__main__':
    unittest.main()

Java = '''
# Thought: https://leetcode.com/problems/contains-duplicate-ii/solution/

# 7ms 98.16%
public class Solution {
    public boolean containsNearbyDuplicate(int[] nums, int k) {
        Set<Integer> set = new HashSet<Integer>();
        for(int i = 0; i < nums.length; i++){
            if(i > k) set.remove(nums[i-k-1]);
            if(!set.add(nums[i])) return true;
        }
        return false;
    }
}

# 9ms 91.32%
class Solution {
    public boolean containsNearbyDuplicate(int[] nums, int k) {
        Map<Integer, Integer> map = new HashMap<Integer, Integer>();
        for (int i = 0; i < nums.length; i++) {
            if (map.containsKey(nums[i])) {
                if (i - map.get(nums[i]) <= k) return true;
            }
            map.put(nums[i], i);
        }
        return false;
    }
}


'''