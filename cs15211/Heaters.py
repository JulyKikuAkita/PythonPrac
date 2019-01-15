__source__ = 'https://leetcode.com/problems/heaters/'
# https://github.com/kamyu104/LeetCode/blob/master/Python/heaters.py
# Time:  O((m + n) * logn), m is the number of the houses, n is the number of the heaters.
# Space: O(1)
#
# Description: 475. Heaters
#
# Winter is coming! Your first job during the contest is to
# design a standard heater with fixed warm radius to warm all the houses.
#
# Now, you are given positions of houses and heaters on a horizontal line,
# find out minimum radius of heaters so that all houses could be covered by those heaters.
#
# So, your input will be the positions of houses and heaters seperately,
# and your expected output will be the minimum radius standard of heaters.
#
# Note:
# Numbers of houses and heaters you are given are non-negative and will not exceed 25000.
# Positions of houses and heaters you are given are non-negative and will not exceed 10^9.
# As long as a house is in the heaters' warm radius range, it can be warmed.
# All the heaters follow your radius standard and the warm radius will the same.
# Example 1:
# Input: [1,2,3],[2]
# Output: 1
# Explanation: The only heater was placed in the position 2, and if we use the radius 1 standard,
# then all the houses can be warmed.
# Example 2:
# Input: [1,2,3,4],[1,4]
# Output: 1
# Explanation: The two heater was placed in the position 1 and 4. We need to use radius 1 standard,
# then all the houses can be warmed.
import unittest
import bisect
# 96ms 46.23%
class Solution(object):
    def findRadius(self, houses, heaters):
        """
        :type houses: List[int]
        :type heaters: List[int]
        :rtype: int
        """
        heaters.sort()
        min_radius = 0
        for house in houses:
            equal_or_larger = bisect.bisect_left(heaters, house)
            curr_radius = float("inf")
            if equal_or_larger != len(heaters):
                curr_radius = heaters[equal_or_larger] - house
            if equal_or_larger != 0:
                smaller = equal_or_larger - 1
                curr_radius = min(curr_radius, house - heaters[smaller])
            min_radius = max(min_radius, curr_radius)
        return min_radius

class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)


if __name__ == '__main__':
    unittest.main()

Java = '''
# Thought:

The idea is to leverage decent Arrays.binarySearch() function provided by Java.

For each house, find its position between those heaters
(thus we need the heaters array to be sorted).
Calculate the distances between this house and left heater and right heater,
get a MIN value of those two values.
Corner cases are there is no left or right heater.
Get MAX value among distances in step 2. It's the answer.
Time complexity: max(O(nlogn), O(mlogn)) - m is the length of houses,
n is the length of heaters.

# 16ms 69.43%
class Solution {
    public int findRadius(int[] houses, int[] heaters) {
        Arrays.sort(heaters);
        int result = Integer.MIN_VALUE;

        for (int house : houses) {
            int index = Arrays.binarySearch(heaters, house);
            if (index < 0) {
        	index = -(index + 1); //it returns (-(insertion point) - 1)
            }
            int dist1 = index - 1 >= 0 ? house - heaters[index - 1] : Integer.MAX_VALUE;
            int dist2 = index < heaters.length ? heaters[index] - house : Integer.MAX_VALUE;

            result = Math.max(result, Math.min(dist1, dist2));
        }

        return result;
    }
}

Based on 2 pointers, the idea is to find the nearest heater for each house,
by comparing the next heater with the current heater.

# 15ms 76.22%
class Solution {
    public int findRadius(int[] houses, int[] heaters) {
        Arrays.sort(houses);
        Arrays.sort(heaters);

        int i = 0, res = 0;
        for (int house : houses) {
            while (i < heaters.length - 1 && heaters[i] + heaters[i + 1] <= house * 2) {
                i++;
            }
            res = Math.max(res, Math.abs(heaters[i] - house));
        }

        return res;
    }
}

'''