# coding=utf-8
__source__ = 'https://github.com/kamyu104/LeetCode/blob/master/Python/poor-pigs.py'
# Time:  O(1)
# Space: O(1)
#
# Description:
# There are 1000 buckets, one and only one of them contains poison,
# the rest are filled with water. They all look the same.
# If a pig drinks that poison it will die within 15 minutes.
# What is the minimum amount of pigs you need to figure out
# which bucket contains the poison within one hour.
#
# Answer this question, and write an algorithm for the follow-up general case.
#
# Follow-up:
#
# If there are n buckets and a pig drinking poison will die within m minutes,
# how many pigs (x) you need to figure out the "poison" bucket within p minutes?
# There is exact one bucket with poison.
#
import math
import unittest
class Solution(object):
    def poorPigs(self, buckets, minutesToDie, minutesToTest):
        """
        :type buckets: int
        :type minutesToDie: int
        :type minutesToTest: int
        :rtype: int
        """
        return int(math.ceil(math.log(buckets) / math.log(minutesToTest / minutesToDie + 1)))

class Solution2(object):
    def poorPigs(self, buckets, minutesToDie, minutesToTest):
        """
        :type buckets: int
        :type minutesToDie: int
        :type minutesToTest: int
        :rtype: int
        """
        bucket_one = minutesToTest / minutesToDie + 1
        result = 0
        while pow(bucket_one, result) < buckets:
            result += 1
        return result

class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)


if __name__ == '__main__':
    unittest.main()

java = '''
Thought: https://leetcode.com/problems/poor-pigs/discuss/94266/Another-explanation-and-solution

With 2 pigs, poison killing in 15 minutes, and having 60 minutes,
we can find the poison in up to 25 buckets in the following way.
Arrange the buckets in a 5×5 square:

 1  2  3  4  5
 6  7  8  9 10
11 12 13 14 15
16 17 18 19 20
21 22 23 24 25

Now use one pig to find the row (make it drink from buckets 1, 2, 3, 4, 5, wait 15 minutes,
make it drink from buckets 6, 7, 8, 9, 10, wait 15 minutes, etc).
Use the second pig to find the column (make it drink 1, 6, 11, 16, 21, then 2, 7, 12, 17, 22, etc).

Having 60 minutes and tests taking 15 minutes means we can run four tests.
If the row pig dies in the third test, the poison is in the third row.
If the column pig doesn't die at all, the poison is in the fifth column
(this is why we can cover five rows/columns even though we can only run four tests).

With 3 pigs, we can similarly use a 5×5×5 cube instead of a 5×5 square
and again use one pig to determine the coordinate of one dimension
(one pig drinks layers from top to bottom, one drinks layers from left to right,
 one drinks layers from front to back). So 3 pigs can solve up to 125 buckets.

In general, we can solve up to (⌊minutesToTest / minutesToDie⌋ + 1)pigs buckets this way,
so just find the smallest sufficient number of pigs for example like this:

class Solution {
    public int poorPigs(int buckets, int minutesToDie, int minutesToTest) {
        int pigs = 0;
        while (Math.pow((minutesToTest / minutesToDie + 1), pigs) < buckets) {
            pigs += 1;
        }
        return pigs;
    }
}

# https://leetcode.com/problems/poor-pigs/discuss/94305/1-line-solution-with-detailed-problem-clarification-and-math-proof-(please-read-if-you-really-want-to-know-what-this-problem-means)
Clarifications:

A pig can be allowed to drink simultaneously on as many buckets as one would like,
and the feeding takes no time (!).
After a pig has instantly finished drinking buckets,
there has to be a "cool down" time of minutesToDie minutes.
During this time, only observation is allowed and no feedings at all.
Actually, this is a derived hint from the problem instead of an assumption.
Because after feeding on poison bucket, it is stated that a pig will die within minutesToDie minutes
instead of exact minutes.
This means that if you feed a pig more than once in a time frame less that minutesToDie minutes,
there is no way to tell which feeding contains poison if the pig happens to die eventually

With the two key points above, I think the problem picked a "bad" story.
Instead, it could be re-translated into a better story such as:

Given N sources with exactly one of them sending bad signal.
You are given x receivers to detect which source is sending bad signal.
A receiver can be configured to pick up signals from any number of specified sources.
The bad signal will permanently damage a receiver within minutesToDie minutes after received.
Find the minimum x if given minutesToTest minutes to test.
Solution:

    int poorPigs(int buckets, int minutesToDie, int minutesToTest) {
      return ceil(log(buckets)/log(minutesToTest/minutesToDie+1));  // log_{T+1}(N)
    }

Proof: For given minutesToDie and minutesToTest, with the clarification above,
the only thing that matters here is the number of tests allowed
T = (int)(minutesToTest/minutesToDie) because of the "cool down" restriction.
Then the problem is translated equivalently to:

How many states can we generate with x pigs and T tests to cover N scenarios?
The number of states is exactly (T+1)^x and here is why.
For each pig during T tests, it has exactly T+1 states: dies at some test#i (1<=i<=T) or still alive eventually.
For x pigs, obviously the maximum possible number of states we could have is (T+1)^x
since each pig's well-being solely depends on whether it ever fed on poison bucket and nothing to do with other pigs.
So all we need to do is to

find minimum x such that (T+1)^x >= N, which means x = ceil(logN/log(T+1)).
Now we have the optimal candidate, but can we actually implement a feeding solution to achieve that optimum solution?
Sure, here it is:

Label buckets as a (T+1)-based number represented as x-dimensional vector v = (v[1], v[2], ...,v[x])
consecutively ascending from (0,0,...0). (each 0<=v[j]<=T)
For each Test#i (1<=i<=T), if all pigs are dead by now, process is finished.
Otherwise, for each pigj alive, feed it on all buckets with v[j] = i simultaneously,
and record its death time D[j] = i if it dies after this test.
Default D[j] = 0 if pigj is still alive after all T tests.
Then we claim that: bucket with label (D[1],D[2],...,D[x]) must be the poison one.

Because for each pigj, by design of Step 2, it is guaranteed to be alive before feeding on bucket
(D[1],D[2],...,D[x]) and all those pigs which have ever fed on this bucket died right after that test.

'''