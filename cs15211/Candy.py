__source__ = 'https://leetcode.com/problems/candy/description/'
# https://github.com/kamyu104/LeetCode/blob/master/Python/candy.py
# Time:  O(n)
# Space: O(n)
# Greedy
#
# Description: Leetcode # 135. Candy
#
# There are N children standing in a line. Each child is assigned a rating value.
#
# You are giving candies to these children subjected to the following requirements:
#
# Each child must have at least one candy.
# Children with a higher rating get more candies than their neighbors.
# What is the minimum candies you must give?
#
# Related Topics
# Greedy
#
import operator
import unittest
class Solution:
    # @param ratings, a list of integer
    # @return an integer
    def candy(self, ratings):
        candies = [1 for _ in xrange(len(ratings))]
        for i in xrange(1, len(ratings)):
            if ratings[i] > ratings[i - 1]:
                candies[i] = candies[i - 1] + 1

        for i in reversed(xrange(1, len(ratings))):
            if ratings[i - 1] > ratings[i] and candies[i - 1] <= candies[i]:
                candies[i - 1] = candies[i] + 1
        return reduce(operator.add, candies) # return sum of all elements in candies list
        # example of reduce is here: http://www.lleess.com/2013/07/python-built-in-function-map-reduce-zip.html#.VO1rJlPF9MY

# http://www.programcreek.com/2014/03/leetcode-candy-java/
'''
We can always assign a neighbor with 1 more if the neighbor has higher a rating value.
However, to get the minimum total number, we should always start adding 1s in the ascending order.
We can solve this problem by scanning the array from both sides. First, scan the array from left to right, a
nd assign values for all the ascending pairs. Then scan from right to left and assign values to descending pairs.
'''
class SolutionJava:
    # @param ratings, a list of integer
    # @return an integer
    def candy(self, ratings):
        if not ratings or len(ratings) == 0:
            return 0
        candies = [1 for i in xrange(len(ratings))]

        # from let to right
        for i in xrange(1, len(ratings)):
            if ratings[i] > ratings[i-1]:
                candies[i] = candies[i-1] + 1
        result = candies[len(ratings) - 1]

        # from right to left
        for i in reversed(xrange(len(ratings) - 1)):
            if ratings[i] > ratings[i+1] and candies[i] <= candies[i+1]:
                candies[i] = candies[i+1] + 1
        return sum(candies)

class Solution2:
    # @param ratings, a list of integer
    # @return an integer
    def candy(self, ratings):
        candynum = [1 for i in range(len(ratings))]
        for i in range(1, len(ratings)):
            if ratings[i] > ratings[i-1]:
                candynum[i] = candynum[i-1] + 1
        print "round 1 : ", i, candynum
        for i in range(len(ratings)-2, -1, -1):
            if ratings[i+1] < ratings[i] and candynum[i+1] >= candynum[i]:
                candynum[i] = candynum[i+1] +1
            print "round 2 : ", i, candynum,  sum(candynum)
        return sum(candynum)

#Test
class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)
        candies = [1, 2, 3, 2, 3, 5, 2, 5]
        candies1 = [3, 2, 1]
        print  Solution().candy(candies1)
        print SolutionJava().candy(candies1)

if __name__ == '__main__':
    unittest.main()

Java = '''
#Thought: https://leetcode.com/problems/candy/solution/

We take ratings array as [5, 6, 2, 2, 4, 8, 9, 5, 4, 0, 5, 1]
In the given problem each student will have at least 1 candy. So distribute 1 candy to each.

ratings:     [5, 6, 2, 2, 4, 8, 9, 5, 4, 0, 5, 1]
candies:     [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
Now traverse the array from left to right. If the rating of (n+1) child is greater than (n) child
then set the candy of (n+1) child as one candy more than the (n) child candies.

ratings:     [5, 6, 2, 2, 4, 8, 9, 5, 4, 0, 5, 1]
candies:     [1, 2, 1, 1, 2, 3, 4, 1, 1, 1, 2, 1]
Now traverse the array from right to left. If the (n) child rating is more than (n+1) child
and (n) child candies is less than one more than (n+1) child candies
then update the candies of (n) child as 1+ (n+1) candies.

ratings:     [5, 6, 2, 2, 4, 8, 9, 5, 4, 0, 5, 1]
candies:     [1, 2, 1, 1, 2, 3, 4, 3, 2, 1, 2, 1]
Total minimum candies: 23

#69.63% 4ms
public class Solution {
    public int candy(int[] ratings) {
        if (ratings == null) return 0;
        int n = ratings.length;
        if (n <= 1) return n;
        int[] counts = new int[n];
        for (int i = 0; i < n; i++) {
            counts[i] = 1;
        }
        for (int i = 1; i < n; i++) {
            if (ratings[i] > ratings[i - 1]) counts[i] = counts[i - 1] + 1;
        }
        int sum = 0;
        for (int i = n - 1; i >= 1; i--) {
            sum += counts[i];
            if (ratings[i - 1] > ratings[i] && counts[i - 1] <= counts[i]) counts[i - 1] = counts[i] + 1;
        }
        sum += counts[0];
        return sum;
    }
}

#29.40% 5ms
class Solution {
    public int candy(int[] ratings) {
        int candies[] = new int[ratings.length];
        Arrays.fill(candies, 1);// Give each child 1 candy

        for (int i = 1; i < candies.length; i++){// Scan from left to right, to make sure right higher rated child gets 1 more candy than left lower rated child
            if (ratings[i] > ratings[i - 1]) candies[i] = (candies[i - 1] + 1);
        }

        for (int i = candies.length - 2; i >= 0; i--) {// Scan from right to left, to make sure left higher rated child gets 1 more candy than right lower rated child
            if (ratings[i] > ratings[i + 1]) candies[i] = Math.max(candies[i], (candies[i + 1] + 1));
        }

        int sum = 0;
        for (int candy : candies)
            sum += candy;
        return sum;
    }
}

# DP
# 111ms 0.28%
public class Solution {
    public int candy(int[] ratings) {
        if(ratings == null || ratings.length == 0) return 0;
        int len = ratings.length;

        int[] dp = new int[len];
        Arrays.fill(dp, 1);

        for(int i = 1; i < len ;i++){
            if(ratings[i] > ratings[i - 1]){
                dp[i] = dp[i - 1] + 1;
            }
        }

        for(int i = len - 2; i >= 0; i--){
            if(ratings[i] > ratings[i+1] && dp[i] <= dp[i+1]){
                dp[i] = dp[i+1] + 1;
            }
        }\
        return Arrays.stream(dp).sum();
    }
}

'''