# coding=utf-8
import collections

__source__ = 'https://leetcode.com/problems/x-of-a-kind-in-a-deck-of-cards/'
# Time:  O()
# Space: O()
#
# Description: Leetcode # 914. X of a Kind in a Deck of Cards
#
# In a deck of cards, each card has an integer written on it.
#
# Return true if and only if you can choose X >= 2 such that
# it is possible to split the entire deck into 1 or more groups of cards, where:
#
# Each group has exactly X cards.
# All the cards in each group have the same integer.
#
#
# Example 1:
#
# Input: [1,2,3,4,4,3,2,1]
# Output: true
# Explanation: Possible partition [1,1],[2,2],[3,3],[4,4]
# Example 2:
#
# Input: [1,1,1,2,2,2,3,3]
# Output: false
# Explanation: No possible partition.
# Example 3:
#
# Input: [1]
# Output: false
# Explanation: No possible partition.
# Example 4:
#
# Input: [1,1]
# Output: true
# Explanation: Possible partition [1,1]
# Example 5:
#
# Input: [1,1,2,2,2,2]
# Output: true
# Explanation: Possible partition [1,1],[2,2],[2,2]
#
# Note:
#
# 1 <= deck.length <= 10000
# 0 <= deck[i] < 10000
#
import unittest

#100% 28ms
class Solution(object):
    def hasGroupsSizeX(self, deck):
        """
        :type deck: List[int]
        :rtype: bool
        """

        dic = {}

        for d in deck:
            if d in dic:
                dic[d] += 1
            else:
                dic[d] = 1

        x = None
        for value in dic.values():
            if value > 1:
                a, b = value, x
                while b:
                    a, b = b, a % b
                if a > 1:
                    x = a
                else:
                    return False
            else:
                return False

        return True

class SolutionGCD(object):
    def hasGroupsSizeX(self, deck):
        """
        :type deck: List[int]
        :rtype: bool
        """
        from fractions import gcd
        vals = collections.Counter(deck).values()
        return reduce(gcd, vals) >= 2

class SolutionGCD2(object):
    def hasGroupsSizeX(self, deck):
        """
        :type deck: List[int]
        :rtype: bool
        """
        dict = {}
        for d in deck:
            if d in dict:
                dict[d] += 1
            else:
                dict[d] = 1

        x = None
        for value in dict.values():
            if value > 1:
                a, b = value, x
                while b:
                    a, b = b, a % b
                if a > 1:
                    x = a
                else:
                    return False
            else:
                return False
        return True


class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)


if __name__ == '__main__':
    unittest.main()

Java = '''
#Thought: https://leetcode.com/problems/x-of-a-kind-in-a-deck-of-cards/solution/

# Approach 1: Brute Force
# Complexity Analysis
#
# Time Complexity: O(N^2log(logN)), where N is the number of cards.
# It is outside the scope of this article to prove that the number of divisors of N is bounded by O(Nlog(logN)).
# Space Complexity: O(N).

#6ms 98.67%
class Solution {
    public boolean hasGroupsSizeX(int[] deck) {
        int[] count = new int[10000];
        for(int card : deck) {
            count[card]++;
        }
        List<Integer> numbers = new ArrayList<>();
        for(int c : count) {
            if(c!=0) {
                numbers.add(c);
            }
        }
        searchX: for(int x=2;x<=deck.length;x++){
            if(deck.length%x>0){
                continue;
            }
            for(int number : numbers){
                if(number%x>0){
                    continue searchX;
                }
            }
            return true;
        }
        return false;

    }
}

# Approach 2: Greatest Common Divisor
# Complexity Analysis
# Time Complexity: O(N(log^ 2 N)), where N is the number of votes. If there are C_i
# cards with number i, then each gcd operation is naively O(log^2 C_i).
# Better bounds exist, but are outside the scope of this article to develop.
# Space Complexity: O(N).

#5ms 99.65%
class Solution {
    public boolean hasGroupsSizeX(int[] deck) {
        int[] count = new int[10000];  // 0 <= deck[i] < 10000
        for (int card : deck) {
            count[card]++;
        }

        int cardNumEachGroup = -1;
        for (int i = 0; i < 10000; i++) {
            if (count[i] > 0) {
                if (cardNumEachGroup == -1) cardNumEachGroup = count[i];
                else {
                    cardNumEachGroup = gcd(cardNumEachGroup, count[i]);
                }
            }
        }
        return cardNumEachGroup >= 2;

    }

    public int gcd(int a, int b) {
        return b == 0 ? a : gcd(b, a % b);
    }
}
'''