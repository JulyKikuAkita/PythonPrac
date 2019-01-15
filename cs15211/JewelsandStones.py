__source__ = 'https://leetcode.com/problems/jewels-and-stones/description/'
# Time:  O()
# Space: O()
#
# Description: Leetcode # 771. Jewels and Stones
#
# You're given strings J representing the types of stones that are jewels,
# and S representing the stones you have.  Each character in S is a type of stone you have.
# You want to know how many of the stones you have are also jewels.
#
# The letters in J are guaranteed distinct, and all characters in J and S are letters.
# Letters are case sensitive, so "a" is considered a different type of stone from "A".
#
# Example 1:
#
# Input: J = "aA", S = "aAAbbbb"
# Output: 3
# Example 2:
#
# Input: J = "z", S = "ZZ"
# Output: 0
# Note:
#
# S and J will consist of letters and have length at most 50.
# The characters in J are distinct.
import unittest

class SolutionBruteForce(object):
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        return sum(s in J for s in S)

class SolutionHashSet(object):
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        Jset = set(J)
        return sum(s in J for s in S)

class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)


if __name__ == '__main__':
    unittest.main()

Java = '''
#Thought: https://leetcode.com/problems/jewels-and-stones/solution/
# Time Complexity: O(J.length+S.length)). The O(J.length) part comes from creating J.
# The O(S.length) part comes from searching S.
# Space Complexity: O(J.length).

class Solution {
    public int numJewelsInStones(String J, String S) {
        Set<Character> Jset = new HashSet<>();
        for (char j : J.toCharArray()) Jset.add(j);

        int ans = 0;
        for (char s: S.toCharArray()) {
            if (Jset.contains(s)) ans++;
        }
        return ans;
    }
}
'''