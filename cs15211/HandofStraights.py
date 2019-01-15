__source__ = 'https://leetcode.com/problems/hand-of-straights/'
# Time:  O(N * (N/W))
# Space: O(N)
#
# Description: Leetcode # 846. Hand of Straights
#
# Alice has a hand of cards, given as an array of integers.
#
# Now she wants to rearrange the cards into groups so that each group is size W,
# and consists of W consecutive cards.
#
# Return true if and only if she can.
#
# Example 1:
#
# Input: hand = [1,2,3,6,2,3,4,7,8], W = 3
# Output: true
# Explanation: Alice's hand can be rearranged as [1,2,3],[2,3,4],[6,7,8].
# Example 2:
#
# Input: hand = [1,2,3,4,5], W = 4
# Output: false
# Explanation: Alice's hand can't be rearranged into groups of 4.
#
#
# Note:
#
# 1 <= hand.length <= 10000
# 0 <= hand[i] <= 10^9
# 1 <= W <= hand.length
#
import unittest
import collections

# 784ms 15.47%
class Solution(object):
    def isNStraightHand(self, hand, W):
        """
        :type hand: List[int]
        :type W: int
        :rtype: bool
        """
        count = collections.Counter(hand)
        while count:
            m = min(count)
            for k in xrange(m, m+W):
                v = count[k]
                if not v: return False
                if v == 1:
                    del count[k]
                else:
                    count[k] = v - 1
        return True

class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)


if __name__ == '__main__':
    unittest.main()

Java = '''
# Thought: https://leetcode.com/problems/hand-of-straights/solution/

Approach #1: Brute Force [Accepted]
Complexity Analysis
Time Complexity: O(N * (N/W)), where N is the length of hand.
The (N / W) factor comes from min(count).
In Java, the (N / W) factor becomes logN due to the complexity of TreeMap.
Space Complexity: O(N)

# 61ms 52.04%
class Solution {
    public boolean isNStraightHand(int[] hand, int W) {
        TreeMap<Integer, Integer> count = new TreeMap();
        for (int card : hand) {
            if (!count.containsKey(card)) {
                count.put(card, 1);
            } else {
                count.replace(card, count.get(card) + 1);
            }
        }

        while (count.size() > 0) {
            int first = count.firstKey();
            for (int card = first; card < first + W; ++card) {
                if (!count.containsKey(card)) return false;
                int c = count.get(card);
                if (c == 1) count.remove(card);
                else count.replace(card, c - 1);
            }
        }
        return true;
    }
}

# 6ms 97.71%
class Solution {
    public boolean isNStraightHand(int[] hand, int W) {
        int n = hand.length;
        if (n < W || n % W != 0) return false;
        int[] arr = new int[W];
        for (int i = 0; i < n; i++) {
            arr[hand[i] % W]++;
        }

        for (int i = 0; i < W - 1; i++) {
            if (arr[i] != arr[i + 1]) return false;
        }
        return true;
    }
}
'''