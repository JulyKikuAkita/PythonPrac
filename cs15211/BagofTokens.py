import collections

__source__ = 'https://leetcode.com/problems/bag-of-tokens/'
# Time:  O()
# Space: O()
#
# Description: Leetcode # 948. Bag of Tokens
#
# You have an initial power P, an initial score of 0 points,
# and a bag of tokens.
#
# Each token can be used at most once, has a value token[i],
# and has potentially two ways to use it.
#
# If we have at least token[i] power, we may play the token face up,
# losing token[i] power, and gaining 1 point.
# If we have at least 1 point,
# we may play the token face down, gaining token[i] power,
# and losing 1 point.
# Return the largest number of points we can have after playing any number of tokens.
#
# Example 1:
#
# Input: tokens = [100], P = 50
# Output: 0
# Example 2:
#
# Input: tokens = [100,200], P = 150
# Output: 1
# Example 3:
#
# Input: tokens = [100,200,300,400], P = 200
# Output: 2
#
#
# Note:
#
# tokens.length <= 1000
# 0 <= tokens[i] < 10000
# 0 <= P < 10000
#
import unittest

#28ms 83.33%
class Solution(object):
    def bagOfTokensScore(self, tokens, P):
        """
        :type tokens: List[int]
        :type P: int
        :rtype: int
        """
        tokens.sort()
        deque = collections.deque(tokens)
        ans = bns = 0
        while deque and (P >= deque[0] or bns):
            while deque and P >= deque[0]:
                P -= deque.popleft()
                bns += 1
            ans = max(ans, bns)

            if deque and bns:
                P += deque.pop()
                bns -= 1
        return ans

class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)


if __name__ == '__main__':
    unittest.main()

Java = '''
# Thought: https://leetcode.com/problems/bag-of-tokens/solution/
Approach 1: Greedy
Complexity Analysis
Time Complexity: O(NlogN), where NN is the length of tokens.
Space Complexity: O(N).

#11ms 29.13%
class Solution {
    public int bagOfTokensScore(int[] tokens, int P) {
        Arrays.sort(tokens);
        int lo = 0, hi = tokens.length - 1;
        int points = 0, ans = 0;
        while (lo <= hi && (P >= tokens[lo] || points > 0)) {
            while (lo <= hi && P >= tokens[lo]) {
                P -= tokens[lo++];
                points++;
            }

            ans = Math.max(ans, points);
            if (lo <= hi && points > 0) {
                P += tokens[hi--];
                points--;
            }
        }
        return ans;
    }
}

#7ms 99.58%
class Solution {
    public int bagOfTokensScore(int[] tokens, int P) {
        int left = 0;
        int right = tokens.length -1 ;
        int tok = 0;
        Arrays.sort(tokens);
        while(left <= right){
          if(P >= tokens[left]){
              P -= tokens[left++];
              tok++;
          } else if (tok > 0 && left != right){
              P += tokens[right--];
              tok--;
          } else
              break;
          }
        return tok;
    }
}

'''