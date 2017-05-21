__source__ = 'https://leetcode.com/problems/maximum-xor-of-two-numbers-in-an-array/#/description'
# Time:  O(n)
# Space: O(n)
#
# Description:
# Given a non-empty array of numbers, a0, a1, a2,...,an-1, where 0 <= ai < 2^31.
#
# Find the maximum result of ai XOR aj, where 0 <= i, j < n.
#
# Could you do this in O(n) runtime?
#
# Example:
#
# Input: [3, 10, 5, 25, 2, 8]
#
# Output: 28
#
# Explanation: The maximum result is 5 ^ 25 = 28.
# Hide Company Tags Google
# Hide Tags Bit Manipulation Trie
#
import unittest
# Build the answer bit by bit from left to right.
# Let's say we already know the largest first seven bits we can create.
# How to find the largest first eight bits we can create?
# Well it's that maximal seven-bits prefix followed by 0 or 1.
# Append 0 and then try to create the 1 one (i.e., answer ^ 1)
# from two eight-bits prefixes from nums. If we can, then change that 0 to 1.

class Solution(object):
    def findMaximumXOR(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        answer = 0
        for i in range(32)[::-1]:
            answer <<= 1
            prefixes = {num >> i for num in nums}
            answer += any(answer^1 ^ p in prefixes for p in prefixes)
        return answer

class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)


if __name__ == '__main__':
    unittest.main()

Java = '''
#Thought:
1. Java O(n) solution using bit manipulation and HashMap
public class Solution {
    public int findMaximumXOR(int[] nums) {
        int max = 0, mask = 0;
        for(int i = 31; i >= 0; i--){
            mask = mask | (1 << i);
            Set<Integer> set = new HashSet<>();
            for(int num : nums){
                set.add(num & mask);
            }
            int tmp = max | (1 << i);
            for(int prefix : set){
                if(set.contains(tmp ^ prefix)) {
                    max = tmp;
                    break;
                }
            }
        }
        return max;
    }
}

'''