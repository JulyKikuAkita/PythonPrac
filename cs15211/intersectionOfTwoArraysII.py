__source__ = 'https://leetcode.com/problems/intersection-of-two-arrays-ii/description/'
# https://github.com/kamyu104/LeetCode/blob/master/Python/intersection-of-two-arrays-ii.py
#
# If the given array is not sorted and the memory is unlimited:
#   - Time:  O(m + n)
#   - Space: O(min(m, n))
# elif the given array is already sorted:
#   if m << n or m >> n:
#     - Time:  O(min(m, n) * log(max(m, n)))
#     - Space: O(1)
#   else:
#     - Time:  O(m + n)
#     - Soace: O(1)
# else: (the given array is not sorted and the memory is limited)
#     - Time:  O(max(m, n) * log(max(m, n)))
#     - Space: O(1)
#
# Description: Leetcode # 350. Intersection of Two Arrays II
#
# Given two arrays, write a function to compute their intersection.
#
# Example:
# Given nums1 = [1, 2, 2, 1], nums2 = [2, 2], return [2, 2].
#
# Note:
# Each element in the result should appear as many times as it shows in both arrays.
# The result can be in any order.
#
# Follow up:
# - What if the given array is already sorted? How would you optimize your algorithm?
# - What if nums1's size is small compared to num2's size? Which algorithm is better?
# - What if elements of nums2 are stored on disk, and the memory is limited such that
#   you cannot load all elements into the memory at once?
#
# Related Topics
# Hash Table Two Pointers Binary Search Sort
# Similar Questions
# Intersection of Two Arrays
#
import collections
import unittest
# If the given array is not sorted and the memory is unlimited.
# Time:  O(m + n)
# Space: O(min(m, n))
# Hash solution.
class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        if len(nums1) > len(nums2):
            return self.intersect(nums2, nums1)

        lookup = collections.defaultdict(int)
        for i in nums1:
            lookup[i] += 1

        res = []
        for i in nums2:
            if lookup[i] > 0:
                res += i,
                lookup[i] -= 1
        return res

# If the given array is already sorted, and the memory is limited, and (m << n or m >> n).
# Time:  O(min(m, n) * log(max(m, n)))
# Space: O(1)
# Binary search solution.
class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        if len(nums1) > len(nums2):
            return self.intersect(nums2, nums1)

        def binary_search(compare, nums, left, right, target):
            while left < right:
                mid = left + (right - left) / 2
                if compare(nums[mid], target):
                    right = mid
                else:
                    left = mid + 1
            return left

        nums1.sort(), nums2.sort()  # Make sure it is sorted, doesn't count in time.

        res = []
        left = 0
        for i in nums1:
            left = binary_search(lambda x, y: x >= y, nums2, left, len(nums2), i)
            if left != len(nums2) and nums2[left] == i:
                res += i,
                left += 1

        return res

# If the given array is already sorted, and the memory is limited or m ~ n.
# Time:  O(m + n)
# Soace: O(1)
# Two pointers solution.
class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        nums1.sort(), nums2.sort()  # Make sure it is sorted, doesn't count in time.

        res = []

        it1, it2 = 0, 0
        while it1 < len(nums1) and it2 < len(nums2):
            if nums1[it1] < nums2[it2]:
                it1 += 1
            elif nums1[it1] > nums2[it2]:
                it2 += 1
            else:
                res += nums1[it1],
                it1 += 1
                it2 += 1

        return res

# If the given array is not sorted, and the memory is limited.
# Time:  O(max(m, n) * log(max(m, n)))
# Space: O(1)
# Two pointers solution.
class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        nums1.sort(), nums2.sort()  # O(max(m, n) * log(max(m, n)))

        res = []

        it1, it2 = 0, 0
        while it1 < len(nums1) and it2 < len(nums2):
            if nums1[it1] < nums2[it2]:
                it1 += 1
            elif nums1[it1] > nums2[it2]:
                it2 += 1
            else:
                res += nums1[it1],
                it1 += 1
                it2 += 1
        return res

class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)

if __name__ == '__main__':
    unittest.main()

Java = '''
#96.32% 3ms
public class Solution {
    public int[] intersect(int[] nums1, int[] nums2) {
        if(nums1 == null || nums2 == null || nums1.length == 0 || nums2.length == 0){
            return new int[0];
        }

        Arrays.sort(nums1);
        Arrays.sort(nums2);
        List<Integer> result = new ArrayList<Integer>();
        int j = 0;
        for(int i = 0; i < nums1.length; i++){
            if(j >= nums2.length){
                break;
            }
            int key = nums1[i];
            while ( j < nums2.length && key >= nums2[j]){
                if(key > nums2[j]){
                    j++;
                }else if(key == nums2[j]){
                    result.add(key);
                    j++;
                    break;
                }
            }

        }

        int[] resultArr = new int[result.size()];
        for(int i = 0; i < result.size(); i++){
            resultArr[i] = result.get(i);
        }
        return resultArr;
    }
}

#39.24% 7ms
public class Solution {
    public int[] intersect(int[] nums1, int[] nums2) {
        if ( nums1 == null || nums2 == null) return new int[0];
        List<Integer> res = new ArrayList<Integer>();
        Map<Integer, Integer> map = new HashMap<>();
        for(int n : nums1) {
            if (!map.containsKey(n)) {
                map.put(n, 0);
            }
            map.put(n, map.get(n) + 1);
        }

        for(int n : nums2) {
            if (map.containsKey(n) && map.get(n) > 0) {
                res.add(n);
                map.put(n, map.get(n) - 1);
            }
        }
        int[] tmp = new int[res.size()];
        for (int i = 0; i < tmp.length ; i++) {
            tmp[i] = res.get(i);
        }
        return tmp;

    }
}
'''