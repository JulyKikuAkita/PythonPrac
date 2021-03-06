__source__ = 'https://leetcode.com/problems/majority-element/'
# https://github.com/kamyu104/LeetCode/blob/master/Python/majority-element.py
# Time:  O(n)
# Space: O(1)
#
# Description: Leetcode # 169. Majority Element
#
# Given an array of size n, find the majority element.
# The majority element is the element that appears more than [n/2] times.
#
# You may assume that the array is non-empty and the majority element always exist in the array.
# Companies
# Adobe Zenefits
# Related Topics
# Array Divide and Conquer Bit Manipulation
# Similar Questions
# Majority Element II
#
#
import unittest
class Solution:
    # @param num, a list of integers
    # @return an integer
    def majorityElement(self, num):
        idx, cnt = 0, 1

        for i in xrange(1, len(num)):
            print i, idx, cnt
            if num[idx] == num[i]:
                cnt += 1
            else:
                cnt -= 1
                if cnt == 0:
                    idx = i
                    cnt = 1
        return num[idx]

# test
class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)
        print Solution().majorityElement([1, 2, 3, 4, 5, 5, 5, 5, 5, 5, 6])

if __name__ == '__main__':
    unittest.main()

Java = '''
# Thought: https://leetcode.com/problems/majority-element/solution/
#
Java solutions (sorting, hashmap, moore voting, bit manipulation).

# Sorting
# 5ms 67.62%
class Solution {
    public int majorityElement(int[] nums) {
        Arrays.sort(nums);
        return nums[nums.length/2];
    }
}

# Hashtable
# 25ms 24%
class Solution {
    public int majorityElement(int[] nums) {
        Map<Integer, Integer> myMap = new HashMap<Integer, Integer>();
        //Hashtable<Integer, Integer> myMap = new Hashtable<Integer, Integer>();
        int ret=0;
        for (int num: nums) {
            if (!myMap.containsKey(num))
                myMap.put(num, 1);
            else 
                myMap.put(num, myMap.get(num)+1);
            if (myMap.get(num)>nums.length/2) {
                ret = num;
                break;
            }
        }
        return ret;
    }
}

# Bit manipulation
# 7ms 47.62%
class Solution {
    public int majorityElement(int[] nums) {
        int[] bit = new int[32];
        for (int num: nums)
            for (int i=0; i<32; i++)
                if ((num>>(31-i) & 1) == 1)
                    bit[i]++;
        int ret=0;
        for (int i=0; i<32; i++) {
            bit[i]=bit[i]>nums.length/2?1:0;
            ret += bit[i]*(1<<(31-i));
        }
        return ret;
    }
}

# Moore voting algorithm
# 3ms 100%
class Solution {
    public int majorityElement(int[] nums) {
        int res = nums[0], count = 1;
        for (int i = 1; i < nums.length; i++) {
            if (res == nums[i]) {
                count++;
            } else {
                count--;
                if(count == 0) {
                    res= nums[i];
                    count = 1;
                }
            }
        }
        return res; 
    }
}

# 3ms 100%
class Solution {
    public int majorityElement(int[] nums) {
        int count=0, ret = 0;
        for (int num: nums) {
            if (count==0)
                ret = num;
            if (num!=ret)
                count--;
            else
                count++;
        }
        return ret;
    }
}
'''


