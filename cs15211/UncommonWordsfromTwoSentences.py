__source__ = 'https://leetcode.com/problems/uncommon-words-from-two-sentences/'
# Time:  O(M + N)
# Space: O(M + N)
#
# Description: Leetcode # 884. Uncommon Words from Two Sentences
#
# We are given two sentences A and B.
#
# (A sentence is a string of space separated words.  Each word consists only of lowercase letters.)
#
# A word is uncommon if it appears exactly once in one of the sentences,
# and does not appear in the other sentence.
#
# Return a list of all uncommon words.
#
# You may return the list in any order.
#
# Example 1:
#
# Input: A = "this apple is sweet", B = "this apple is sour"
# Output: ["sweet","sour"]
# Example 2:
#
# Input: A = "apple apple", B = "banana"
# Output: ["banana"]
#
#
# Note:
#
# 0 <= A.length <= 200
# 0 <= B.length <= 200
# A and B both contain only spaces and lowercase letters.
#
import unittest

#20ms 100%
class Solution(object):
    def uncommonFromSentences(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: List[str]
        """
        count = {}
        for word in A.split():
            count[word] = count.get(word, 0) + 1
        for word in B.split():
            count[word] = count.get(word, 0) + 1

        #Alternatively:
        #count = collections.Counter(A.split())
        #count += collections.Counter(B.split())

        return [word for word in count if count[word] == 1]

class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)


if __name__ == '__main__':
    unittest.main()

Java = '''
#Thought:
Complexity Analysis
Time Complexity: O(M + N)), where M, N are the lengths of A and B respectively.
Space Complexity: O(M + N), the space used by count.

# 5ms 99.55%
class Solution {
    public String[] uncommonFromSentences(String A, String B) {
        Map<String, Integer> count = new HashMap();
        for (String word : A.split(" ")) {
            count.put(word, count.getOrDefault(word, 0) + 1);
        }

        for (String word : B.split(" ")) {
            count.put(word, count.getOrDefault(word, 0) + 1);
        }

        List<String> ans = new LinkedList();
        for (String word: count.keySet()) {
            if (count.get(word) == 1) ans.add(word);
        }
        return ans.toArray(new String[ans.size()]);
    }
}

# 5ms 99.55%
class Solution {
    public String[] uncommonFromSentences(String A, String B) {
        Map<String, Integer> count = new HashMap();
        String C = A + " " + B;
        for (String word : C.split(" ")) {
            count.put(word, count.getOrDefault(word, 0) + 1);
        }

        List<String> ans = new LinkedList();
        for (String word: count.keySet()) {
            if (count.get(word) == 1) ans.add(word);
        }
        return ans.toArray(new String[ans.size()]);
    }
}

'''