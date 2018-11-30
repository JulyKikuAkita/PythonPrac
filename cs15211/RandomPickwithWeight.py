__source__ = 'https://leetcode.com/problems/random-pick-with-weight/description/'
# Time:  O()
# Space: O()
#
# Description: Leetcode # 528. Random Pick with Weight
#
# Given an array w of positive integers, where w[i] describes the weight of index i,
# write a function pickIndex which randomly picks an index in proportion to its weight.
#
# Note:
#
# 1 <= w.length <= 10000
# 1 <= w[i] <= 10^5
# pickIndex will be called at most 10000 times.
# Example 1:
#
# Input:
# ["Solution","pickIndex"]
# [[[1]],[]]
# Output: [null,0]
# Example 2:
#
# Input:
# ["Solution","pickIndex","pickIndex","pickIndex","pickIndex","pickIndex"]
# [[[1,3]],[],[],[],[],[]]
# Output: [null,0,1,1,1,0]
# Explanation of Input Syntax:
#
# The input is two lists: the subroutines called and their arguments.
# Solution's constructor has one argument, the array w. pickIndex has no arguments.
# Arguments are always wrapped with a list, even if there aren't any.
#
import unittest


class Solution(object):
    pass  # your function here


class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)


if __name__ == '__main__':
    unittest.main()

Java = '''
# Thought: https://leetcode.com/problems/random-pick-with-weight/solution/
# Time Complexity: O(N) preprocessing. O(log(N)) pickIndex.
# Space Complexity: O(N)
# Approach 1: Prefix Sum and Binary Search
# 84ms 99.91%
class Solution {
    List<Integer> psum = new ArrayList<>();
    int tot = 0;
    Random rand = new Random();

    public Solution(int[] w) {
        for (int x: w) {
            tot += x;
            psum.add(tot);
        }
    }

    public int pickIndex() {
        int targ = rand.nextInt(tot);
        int lo = 0;
        int hi = psum.size() - 1;
        while (lo != hi) {
            int mid = lo + (hi - lo) / 2;
            if (targ >= psum.get(mid)) lo = mid + 1;
            else hi = mid;
        }
        return lo;
    }
}

/**
 * Your Solution object will be instantiated and called as such:
 * Solution obj = new Solution(w);
 * int param_1 = obj.pickIndex();
 */
'''