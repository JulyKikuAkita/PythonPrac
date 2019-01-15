__source__ = 'https://leetcode.com/problems/boats-to-save-people/'
# Time:  O(NlogN)
# Space: O(N)
#
# Greedy
#
# Description: Leetcode # 881. Boats to Save People
#
# The i-th person has weight people[i], and each boat can carry a maximum weight of limit.
#
# Each boat carries at most 2 people at the same time,
# provided the sum of the weight of those people is at most limit.
#
# Return the minimum number of boats to carry every given person.
# (It is guaranteed each person can be carried by a boat.)
#
#
#
# Example 1:
#
# Input: people = [1,2], limit = 3
# Output: 1
# Explanation: 1 boat (1, 2)
# Example 2:
#
# Input: people = [3,2,2,1], limit = 3
# Output: 3
# Explanation: 3 boats (1, 2), (2) and (3)
# Example 3:
#
# Input: people = [3,5,3,4], limit = 5
# Output: 4
# Explanation: 4 boats (3), (3), (4), (5)
# Note:
#
# 1 <= people.length <= 50000
# 1 <= people[i] <= limit <= 30000
#

import unittest

#120ms 86.10%
class Solution(object):
    def numRescueBoats(self, people, limit):
        """
        :type people: List[int]
        :type limit: int
        :rtype: int
        """
        people.sort()
        i, j = 0, len(people) - 1
        ans = 0
        while i <= j:
            ans += 1
            if people[i] + people[j] <= limit:
                i += 1
            j -= 1
        return ans

class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)


if __name__ == '__main__':
    unittest.main()

Java = '''
# Thought: https://leetcode.com/problems/boats-to-save-people/solution/
Approach 1: Greedy (Two Pointer)
Complexity Analysis
Time Complexity: O(NlogN), where N is the length of people.
Space Complexity: O(N)

# 36ms 39.25#
class Solution {
    public int numRescueBoats(int[] people, int limit) {
        Arrays.sort(people);
        int i = 0, j = people.length - 1;
        int counts = 0;
        while (i <= j) {
            counts++;
            if (people[i] + people[j] <= limit) {
                i++;
            }
            j--;
        }
        return counts;
    }
}
// Bucket sort for O(n)
# 6ms 100%
class Solution {
    public int numRescueBoats(int[] people, int limit) {
        int[] buckets = new int[limit+1];
        for(int p: people) buckets[p]++;
        int start = 0;
        int end = buckets.length - 1;
        int solution = 0;
        while(start <= end) {
            while(start <= end && buckets[start] <= 0) start++;
            while(start <= end && buckets[end] <= 0) end--;
            if(buckets[start] <= 0 && buckets[end] <= 0) break;
            solution++;
            if(start + end <= limit) buckets[start]--;
            buckets[end]--;
        }
        return solution;
    }
}

'''