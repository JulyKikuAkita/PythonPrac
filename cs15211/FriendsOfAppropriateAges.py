__source__ = 'https://leetcode.com/problems/friends-of-appropriate-ages/'
# Time:  O(A^2+N), where N is the number of people, and A is the number of ages.
# Space: O(A), the space used to store count
#
# Description: Leetcode # 825. Friends Of Appropriate Ages
#
# Some people will make friend requests.
# The list of their ages is given and ages[i] is the age of the ith person.
#
# Person A will NOT friend request person B (B != A) if any of the following conditions are true:
#
# age[B] <= 0.5 * age[A] + 7
# age[B] > age[A]
# age[B] > 100 && age[A] < 100
# Otherwise, A will friend request B.
#
# Note that if A requests B, B does not necessarily request A.
# Also, people will not friend request themselves.
#
# How many total friend requests are made?
#
# Example 1:
#
# Input: [16,16]
# Output: 2
# Explanation: 2 people friend request each other.
# Example 2:
#
# Input: [16,17,18]
# Output: 2
# Explanation: Friend requests are made 17 -> 16, 18 -> 17.
# Example 3:
#
# Input: [20,30,100,110,120]
# Output:
# Explanation: Friend requests are made 110 -> 100, 120 -> 110, 120 -> 100.
#
#
# Notes:
#
# 1 <= ages.length <= 20000.
# 1 <= ages[i] <= 120.

from bisect import bisect
import unittest

#sorted solution, 212ms, 36.15%
class Solution(object):
    def numFriendRequests(self, ages):
        """
        :type ages: List[int]
        :rtype: int
        """
        #sorted solution
        ages = sorted(ages)
        res = 0
        flag = 1

        for i in xrange(len(ages) - 1, -1, -1):
            lo = 0.5 * ages[i] + 7
            if ages[i] > lo and i < len(ages) - 1 and ages[i] == ages[i + 1]:
                res += flag
                flag += 1
            else:
                flag = 1
            index = bisect.bisect_right(ages, lo)
            res += max(i - index, 0)
        return res

#40ms 100%
import math
class Solution2(object):
    def numFriendRequests(self, ages):
        """
        :type ages: List[int]
        :rtype: int
        """
        data = [0] * 121
        rolling_sum = [0]*121
        for a in ages:
            data[a] += 1
        for i in range(1,len(rolling_sum)):
            rolling_sum[i] += data[i] + rolling_sum[i-1]
        count = 0
        for i in range(len(rolling_sum)):
            if i > i/2+7:
                count += (rolling_sum[i] - rolling_sum[i/2+7]) * (data[i])- data[i]
        return count


class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)


if __name__ == '__main__':
    unittest.main()

Java = '''
# Thought: https://leetcode.com/problems/friends-of-appropriate-ages/solution/

Approach #1: Counting [Accepted]
Intuition

Instead of processing all 20000 people, we can process pairs of (age, count) representing
how many people are that age. Since there are only 120 possible ages, this is a much faster loop.

Algorithm

For each pair (ageA, countA), (ageB, countB), if the conditions are satisfied with respect to age,
then countA * countB pairs of people made friend requests.

If ageA == ageB, then we overcounted: we should have countA * (countA - 1)
pairs of people making friend requests instead, as you cannot friend request yourself.

# 7ms, 68.59%
class Solution {
    public int numFriendRequests(int[] ages) {
        int[] count = new int[121];
        for (int age : ages) count[age]++;

        int ans = 0;
        for (int ageA = 0; ageA <= 120; ageA++) {
            int countA = count[ageA];
            for (int ageB = 0; ageB <= 120; ageB++) {
                int countB = count[ageB];
                if (ageA * 0.5 + 7 >= ageB) continue;
                if (ageA < ageB) continue;
                if (ageA < 100 && 100 < ageB) continue;
                ans += countA * countB;
                if (ageA == ageB) ans -= countA;
            }
        }
        return ans;
    }
}

# improve:
# 4ms, 100%
class Solution {
    public int numFriendRequests(int[] ages) {
        int[] ageCount = new int[121];
        int[] countSum = new int[121];
        for(int n : ages){
            ageCount[n]++;
        }

        for(int i = 1; i < countSum.length; i++){
            countSum[i] = ageCount[i] + countSum[i - 1];
        }

        int output = 0;
        for(int i = 15; i < countSum.length; i++){
            if(ageCount[i] == 0) continue;
            int count = countSum[i] - countSum[i / 2 + 7];
            output += ageCount[i] * (count - 1);
        }

        return output;
    }
}
'''