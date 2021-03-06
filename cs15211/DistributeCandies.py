__source__ = 'https://leetcode.com/problems/distribute-candies/'
# Time:  O(n)
# Space: O(n)
#
# Description: Leetcode # 575. Distribute Candies
#
# Given an integer array with even length,
# where different numbers in this array represent different kinds of candies.
# Each number means one candy of the corresponding kind.
# You need to distribute these candies equally in number to brother and sister.
# Return the maximum number of kinds of candies the sister could gain.
#
# Example 1:
# Input: candies = [1,1,2,2,3,3]
# Output: 3
#
# Explanation:
# There are three different kinds of candies (1, 2 and 3), and two candies for each kind.
# Optimal distribution: The sister has candies [1,2,3] and the brother has candies [1,2,3], too.
# The sister has three different kinds of candies.
#
# Example 2:
# Input: candies = [1,1,2,3]
# Output: 2
# Explanation: For example, the sister has candies [2,3] and the brother has candies [1,1].
# The sister has two different kinds of candies, the brother has only one kind of candies.
# Note:
#
# The length of the given array is in range [2, 10,000], and will be even.
# The number in given array is in range [-100,000, 100,000].
# Hide Company Tags LiveRamp
# Hide Tags Hash Table
#

# There are len(set(candies)) unique candies, and the sister picks only len(candies) / 2 of them,
# so she can't have more than this amount.
#
# For example, if there are 5 unique candies, then if she is picking 4 candies,
# she will take 4 unique ones. If she is picking 7 candies, then she will only take 5 unique ones.
#
# 104ms 68.21%
class Solution(object):
    def distributeCandies(self, candies):
        """
        :type candies: List[int]
        :rtype: int
        """
        return min(len(candies) / 2, len(set(candies)))

Java = '''
# Thought: https://leetcode.com/problems/distribute-candies/solution/

# 85ms 32.39%
class Solution {
    public int distributeCandies(int[] candies) {
        Set<Integer> set = new HashSet<>();
        for (int candy : candies) {
            set.add(candy);
        }
        return Math.min(set.size(), candies.length / 2);
    }
}

# 109ms 13.92%
class Solution {
    public int distributeCandies(int[] candies) {
        return Math.min(candies.length / 2, IntStream.of(candies).boxed().collect(Collectors.toSet()).size());
    }
}
'''
