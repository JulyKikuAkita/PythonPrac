__source__ = 'https://leetcode.com/problems/koko-eating-bananas/'
# Time:  O(NlogW)
# Space: O(1)
#
# Binary Search
# Description: Leetcode # 875. Koko Eating Bananas
#
# Koko loves to eat bananas.  There are N piles of bananas, the i-th pile has piles[i] bananas.
# The guards have gone and will come back in H hours.
#
# Koko can decide her bananas-per-hour eating speed of K.
# Each hour, she chooses some pile of bananas,
# and eats K bananas from that pile.
#
# If the pile has less than K bananas,
# she eats all of them instead,
# and won't eat any more bananas during this hour.
#
# Koko likes to eat slowly, but still wants to finish eating all the bananas before the guards come back.
#
# Return the minimum integer K such that she can eat all the bananas within H hours.
# Example 1:
#
# Input: piles = [3,6,7,11], H = 8
# Output: 4
# Example 2:
#
# Input: piles = [30,11,23,4,20], H = 5
# Output: 30
# Example 3:
#
# Input: piles = [30,11,23,4,20], H = 6
# Output: 23
#
#
# Note:
#
# 1 <= piles.length <= 10^4
# piles.length <= H <= 10^9
# 1 <= piles[i] <= 10^9
#
import unittest

#256 ms 74.84%

class Solution(object):
    def minEatingSpeed(self, piles, H):
        """
        :type piles: List[int]
        :type H: int
        :rtype: int
        """
        def possible(K):
            return sum((p - 1) / K + 1 for p in piles) <= H

        lo, hi = 1, max(piles)
        while lo < hi:
            mi = (lo + hi) / 2
            if not possible(mi):
                lo = mi + 1
            else:
                hi = mi
        return lo

class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)


if __name__ == '__main__':
    unittest.main()

Java = '''
# Thought: https://leetcode.com/problems/koko-eating-bananas/solution/
#
# Complexity Analysis
# Time Complexity: O(NlogW), where N is the number of piles, and W is the maximum size of a pile.
# Space Complexity: O(1).
#
#12ms 98.43%
class Solution {
    public int minEatingSpeed(int[] piles, int H) {
        int lo = 1;
        int hi = Integer.MAX_VALUE;
        while (lo < hi) {
            int mid = lo + (hi - lo) / 2;
            if (!possible(piles, H, mid)) {
                lo = mid + 1;
            } else {
                hi = mid;
            }
        }
        return lo;
    }

    private boolean possible(int[] piles, int H, int K) {
        int time = 0;
        for (int p : piles) time += (p - 1) / K + 1;
        return time <= H;
    }
}

# 6ms 100%
class Solution {
    public int minEatingSpeed(int[] piles, int H) {
        long ttl = 0;
        for (int pile : piles) ttl += pile;
        int minSpeed = (int)((ttl + H - 1) / H);
        while (true) {
            int hours = 0;
            for (int pile : piles) {
                hours += (pile + minSpeed - 1) / minSpeed;
            }
            if (hours > H) minSpeed++;
            else break;
        }
        return minSpeed;
    }
}
'''