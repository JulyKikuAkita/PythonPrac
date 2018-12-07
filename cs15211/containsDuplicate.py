__source__ = 'https://leetcode.com/problems/contains-duplicate/description/'
# https://github.com/kamyu104/LeetCode/blob/master/Python/contains-duplicate.py
# Time:  O(n)
# Space: O(n)
#
# Description: Leetcode # 217. Contains Duplicate
#
# Given an array of integers, find if the array contains any duplicates.
# Your function should return true if any value appears at least twice in the array,
# and it should return false if every element is distinct.
#
# Companies
# Palantir Airbnb Yahoo
# Related Topics
# Array Hash Table
# Similar Questions
# Contains Duplicate II Contains Duplicate III
#
import unittest
class Solution:
    # @param {integer[]} nums
    # @return {boolean}
    def containsDuplicate(self, nums):
        return len(nums) > len(set(nums))

class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)
        print Solution().containsDuplicate([12344555,12344555])

if __name__ == '__main__':
    unittest.main()

Java = '''
# Thought: https://leetcode.com/problems/contains-duplicate/solution/

# avoid, overflow
# 2ms 99.57%
class Solution {
    public boolean containsDuplicate(int[] nums) {
        int min = Integer.MAX_VALUE;
        int max = Integer.MIN_VALUE;
        for (int num : nums) {
            min = Math.min(min, num);
            max = Math.max(max, num);
        }
        boolean[] visited = new boolean[max - min + 1];
        for (int num : nums) {
            int index = num - min;
            if (visited[index]) {
                return true;
            } else {
                visited[index] = true;
            }
        }
        return false;
    }
}

Approach #2 (Sorting) [Accepted]
# Time:  O(n log n )
# Space: O(1)

# 3ms 99.52%
class Solution {
   public boolean containsDuplicate(int[] nums) {
        Arrays.sort(nums);
        for (int i = 0; i < nums.length - 1; ++i) {
            if (nums[i] == nums[i + 1]) return true;
        }
        return false;
    }
}

Approach #3 (Hash Table) [Accepted]
# 8ms 80.46%
class Solution {
    public  boolean containsDuplicate(int[] nums) {
		 Set<Integer> set = new HashSet<Integer>();
		 for(int i : nums)
			 if(!set.add(i))// if there is same
				 return true;
		 return false;
	 }
}

# 13ms 48.37%
class Solution {
    public boolean containsDuplicate(int[] nums) {
        Set<Integer> set = new HashSet<>();
        for (int num : nums) {
            set.add(num);
        }
        return set.size() != nums.length;
    }
}

# 16ms 37.85%
class Solution {
    public boolean containsDuplicate(int[] nums) {
        Set<Integer> set = new HashSet<>();
        for (int num : nums) {
            if (set.contains(num)) {
                return true;
            } else {
                set.add(num);
            }
        }
        return false;
    }
}
'''
