__source__ = 'https://leetcode.com/problems/maximum-product-of-word-lengths/'
# https://github.com/kamyu104/LeetCode/blob/master/Python/maximum-product-of-word-lengths.py
# Time:  O(n) ~ O(n^2)
# Space: O(n)
#
# Description: Leetcode # 318. Maximum Product of Word Lengths
#
# Given a string array words, find the maximum value of
# length(word[i]) * length(word[j]) where the two words
# do not share common letters. You may assume that each
# word will contain only lower case letters. If no such
# two words exist, return 0.
#
# Example 1:
# Given ["abcw", "baz", "foo", "bar", "xtfn", "abcdef"]
# Return 16
# The two words can be "abcw", "xtfn".
#
# Example 2:
# Given ["a", "ab", "abc", "d", "cd", "bcd", "abcd"]
# Return 4
# The two words can be "ab", "cd".
#
# Example 3:
# Given ["a", "aa", "aaa", "aaaa"]
# Return 0
# No such pair of words.
#
# Follow up:
# Could you do better than O(n2), where n is the number of words?
#
# Companies
# Google
# Related Topics
# Bit Manipulation
#
import unittest
# Counting Sort + Pruning + Bit Manipulation
class Solution(object):
    def maxProduct(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        def counting_sort(words):
            k = 1000 # k is max length of words in the dictionary
            buckets = [ [] for _ in xrange(k)]
            for word in words:
                buckets[len(word)].append(word)
            res = []
            for i in reversed(xrange(k)):
                if buckets[i]:
                    res.extend(buckets[i])
            return res

        words = counting_sort(words)
        bits = [0] * len(words)
        for i, word in enumerate(words):
            for c in word:
                bits[i] |= (1 << (ord(c) - ord('a')))

        max_product = 0
        for i in xrange(len(words) - 1):
            if len(words[i]) ** 2 <= max_product:
                break
            for j in xrange(i + 1, len(words)):
                if len(words[i]) * len(words[j]) <= max_product:
                    break
                if not (bits[i] & bits[j]):
                    max_product = len(words[i]) * len(words[j])
        return max_product

# Time:  O(nlogn) ~ O(n^2)
# Space: O(n)
# Sorting + Pruning + Bit Manipulation
class Solution2(object):
    def maxProduct(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        words.sort(key = lambda x: len(x), reverse = True)
        bits = [0] * len(words)

        for i, word in enumerate(words):
            for c in word:
                bits[i] |= ( 1 << (ord(c) - ord('a')))

        max_product = 0
        for i in xrange(len(words) - 1):
            if len(words[i]) ** 2 <= max_product:  # ** power of
                break

            for j in xrange(i+1, len(words)):
                if len(words[i]) * len(words[j]) <= max_product:
                    break
                if not (bits[i] & bits[j]):
                    max_product = len(words[i]) * len(words[j])
        return max_product

class TestMethods(unittest.TestCase):
    def test_Local(self):
        words = ["a", "ab", "abc", "d", "cd", "bcd", "abcd"]
        print Solution2().maxProduct(words)

if __name__ == '__main__':
    unittest.main()

Java = '''
# Thought:

# 12ms 84.36%
class Solution {
    public int maxProduct(String[] words) {
        int len = words.length;
        int[] nums = new int[len];
        for (int i = 0; i < len; i++) {
            nums[i] = convertString(words[i]);
        }
        int result = 0;
        for (int i = 0; i < len; i++) {
            for (int j = i + 1; j < len; j++) {
                if ((nums[i] & nums[j]) == 0) {
                    result = Math.max(result, words[i].length() * words[j].length());
                }
            }
        }
        return result;
    }

    private int convertString(String word) {
        int result = 0;
        for (int i = 0; i < word.length(); i++) {
            result |= (1 << (word.charAt(i) - 'a'));
        }
        return result;
    }
}

# 12ms 84.36%
class Solution {
    public int maxProduct(String[] words) {
        int max = 0;
        int[] bytes = new int[words.length];
        for(int i=0;i<words.length;i++){
            int val = 0;
            for(int j=0;j<words[i].length();j++){
                val |= 1<<(words[i].charAt(j)-'a');
            }
            bytes[i] = val;
        }
        for(int i=0; i<bytes.length; i++){
            for(int j=i+1; j<bytes.length; j++){
                if((bytes[i] & bytes[j])==0)max = Math.max(max,words[i].length()*words[j].length());
            }
        }
        return max;
    }
}

'''
