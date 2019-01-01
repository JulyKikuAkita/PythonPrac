__source__ = 'https://leetcode.com/problems/rabbits-in-forest/'
# Time:  O()
# Space: O()
#
# Description: Leetcode # 781. Rabbits in Forest
#
# In a forest, each rabbit has some color.
# Some subset of rabbits (possibly all of them) tell you how many other rabbits have the same color as them.
# Those answers are placed in an array.
#
# Return the minimum number of rabbits that could be in the forest.
#
# Examples:
# Input: answers = [1, 1, 2]
# Output: 5
# Explanation:
# The two rabbits that answered "1" could both be the same color, say red.
# The rabbit than answered "2" can't be red or the answers would be inconsistent.
# Say the rabbit that answered "2" was blue.
# Then there should be 2 other blue rabbits in the forest that didn't answer into the array.
# The smallest possible number of rabbits in the forest is therefore 5: 3 that answered plus 2 that didn't.
#
# Input: answers = [10, 10, 10]
# Output: 11
#
# Input: answers = []
# Output: 0
#
# Note:
# answers will have length at most 1000.
# Each answers[i] will be an integer in the range [0, 999].
#
import unittest
import collections
# 24ms 90.52%
class Solution(object):
    def numRabbits(self, answers):
        """
        :type answers: List[int]
        :rtype: int
        """
        count = collections.Counter(answers)
        return sum(-v % (k+1) + v for k, v in count.iteritems())

class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)

if __name__ == '__main__':
    unittest.main()

Java = '''
# Thought: https://leetcode.com/problems/rabbits-in-forest/solution/
#
Approach #1: Count [Accepted]
Complexity Analysis
Time Complexity: O(N), where N is the number of rabbits that answered.
In Java, our implementation using int[] instead of a Map would be O(N+W), 
where W is the number of possible different answers that rabbits could say.
Space Complexity: O(N). In Java, our implementation is O(W)

# 6ms 76.85%
class Solution {
    public int numRabbits(int[] answers) {
        int[] count = new int[1000];
        for (int x: answers) count[x]++;

        int ans = 0;
        for (int k = 0; k < 1000; k++) {
            ans += Math.floorMod(-count[k], k +1) + count[k];
        }
        return ans;
    }
}

# 3ms 98.39%
class Solution {
    public int numRabbits(int[] answers) {
        int[] count = new int[1000];
        for (int x: answers) count[x]++;
        int rabbits = 0;
        for (int i = 0; i < 1000; i++) {
            if (count[i] > 0) {
                rabbits += ((count[i] - 1) / (i + 1) + 1) * (i + 1);
            }
        }
        return rabbits;
    }
}
'''
