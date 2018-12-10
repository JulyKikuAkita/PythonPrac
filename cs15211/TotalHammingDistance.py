__source__ = 'https://leetcode.com/problems/total-hamming-distance/'
# https://github.com/kamyu104/LeetCode/blob/master/Python/total-hamming-distance.py
# Time:  O(n)
# Space: O(1)
#
# Description: Leetcode # 477. Total Hamming Distance
#
# The Hamming distance between two integers is the number of positions
# at which the corresponding bits are different.
#
# Now your job is to find the total Hamming distance between all pairs of the given numbers.
#
# Example:
# Input: 4, 14, 2
#
# Output: 6
#
# Explanation: In binary representation, the 4 is 0100, 14 is 1110, and 2 is 0010 (just
# showing the four bits relevant in this case). So the answer will be:
# HammingDistance(4, 14) + HammingDistance(4, 2) + HammingDistance(14, 2) = 2 + 2 + 2 = 6.
# Note:
# Elements of the given array are in the range of 0 to 10^9
# Length of the array will not exceed 10^4.
# brute force: O(n^2)
#
# Companies
# Facebook
# Related Topics
# Bit Manipulation
# Similar Questions
# Hamming Distance
#
import unittest
class Solution(object):
    #http://stackoverflow.com/questions/21388448/sum-of-xor-values-of-all-pairs
    '''
     You can separate the calculation to do one bit at a time.

      For example, look at the rightmost bit of all the numbers in the array.
      Suppose that a numbers have a rightmost 0-bit, and b numbers have a 1-bit.
      Then out of the pairs, a*b of them will have 1 in the rightmost bit of the XOR.
      This is because there are a*b ways to choose one number that has a 0-bit and one that has a 1-bit.
      These bits will therefore contribute a*b towards the total of all the XORs.
      say [1,2,3]
      0 0   1
      0 1   0
      1 0   0
            (two 0 and one 1 has 2 ways to form pairs, the ans is 2 for right most bit)
            so the ttl = 2 + 2 + 2
      In general, when looking at the nth bit (where the rightmost bit is the 0th), count how many numbers have 0
      (call this an) and how many have 1 (call this bn). The contribution towards the final sum will be an*bn*2n.
       You need to do this for each bit and sum all these contributions together.

       This can be done in O(kn) time, where k is the number of bits in the given values.
    '''
    # 280ms 63.10%
    def totalHammingDistance(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result = 0
        for i in xrange(32):
            counts = [0] * 2
            for num in nums:
                counts[(num >> i) & 1] += 1
            result += counts[0] * counts[1]
        return result

    def totalHammingDistance2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return sum(b.count('0') * b.count('1') for b in zip(*map('{:032b}'.format, nums)))

class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)

if __name__ == '__main__':
    unittest.main()

Java = '''
# Thought: https://leetcode.com/problems/total-hamming-distance/solution/

For each bit position 1-32 in a 32-bit integer,
we count the number of integers in the array which have that bit set.
Then, if there are n integers in the array and k of them have a particular bit set and (n-k) do not,
then that bit contributes k*(n-k) hamming distance to the total.

# 21ms 62.19%
class Solution {
    public int totalHammingDistance(int[] nums) {
        int res = 0;
        for (int i = 0; i < 32; i++) {
            int bitCount = 0;
            for (int j = 0; j < nums.length; j++) {
                bitCount += (nums[j]>>i) & 1;
            }
            res += (nums.length - bitCount) * bitCount;
        }
        return res;
    }
}
'''