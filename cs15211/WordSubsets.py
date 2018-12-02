__source__ = 'https://leetcode.com/problems/word-subsets/'
# Time:  O(A + B)
# Space: O(A + B)
#
# Description: Leetcode # 916. Word Subsets
#
# We are given two arrays A and B of words.  Each word is a string of lowercase letters.
#
# Now, say that word b is a subset of word a if every letter in b occurs in a, including multiplicity.
# For example, "wrr" is a subset of "warrior", but is not a subset of "world".
#
# Now say a word a from A is universal if for every b in B, b is a subset of a.
#
# Return a list of all universal words in A.  You can return the words in any order.
#
# Example 1:
#
# Input: A = ["amazon","apple","facebook","google","leetcode"], B = ["e","o"]
# Output: ["facebook","google","leetcode"]
# Example 2:
#
# Input: A = ["amazon","apple","facebook","google","leetcode"], B = ["l","e"]
# Output: ["apple","google","leetcode"]
# Example 3:
#
# Input: A = ["amazon","apple","facebook","google","leetcode"], B = ["e","oo"]
# Output: ["facebook","google"]
# Example 4:
#
# Input: A = ["amazon","apple","facebook","google","leetcode"], B = ["lo","eo"]
# Output: ["google","leetcode"]
# Example 5:
#
# Input: A = ["amazon","apple","facebook","google","leetcode"], B = ["ec","oc","ceo"]
# Output: ["facebook","leetcode"]
#
#
# Note:
#
# 1 <= A.length, B.length <= 10000
# 1 <= A[i].length, B[i].length <= 10
# A[i] and B[i] consist only of lowercase letters.
# All words in A[i] are unique: there isn't i != j with A[i] == A[j].
#
import unittest

#1164ms 52.24%
class Solution(object):
    def wordSubsets(self, A, B):
        """
        :type A: List[str]
        :type B: List[str]
        :rtype: List[str]
        """
        def count(word):
            ans = [0] * 26
            for letter in word:
                ans[ord(letter) - ord('a')] += 1
            return ans

        bmax = [0] * 26
        for b in B:
            for i, c in enumerate(count(b)):
                bmax[i] = max(bmax[i], c)

        ans = []
        for a in A:
            if all(x >= y for x, y in zip(count(a), bmax)):
                ans.append(a)
        return ans

class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)


if __name__ == '__main__':
    unittest.main()

Java = '''
#Thought: https://leetcode.com/problems/word-subsets/solution/
Approach 1: Reduce to Single Word in B
-> Reduce B to a single word bmax as described above,
then compare the counts of letters between words a in A, and bmax.

Complexity Analysis
Time Complexity: O(A+B), where A and B is the total amount of information in A and B respectively.
Space Complexity: O(A.length+B.length).

#28ms 74.91%
class Solution {
    public List<String> wordSubsets(String[] A, String[] B) {
        int[] bmax = count("");
        for (String b: B) {
            int[] bCount = count(b);
            for (int i = 0; i < 26; ++i)
                bmax[i] = Math.max(bmax[i], bCount[i]);
        }

        List<String> ans = new ArrayList();
        search: for (String a: A) {
            int[] aCount = count(a);
            for (int i = 0; i < 26; ++i)
                if (aCount[i] < bmax[i])
                    continue search;
            ans.add(a);
        }

        return ans;
    }

    public int[] count(String S) {
        int[] ans = new int[26];
        for (char c: S.toCharArray())
            ans[c - 'a']++;
        return ans;
    }
}

#32ms 62.54%
class Solution {
    public List<String> wordSubsets(String[] A, String[] B) {
        int[] bmax = count("");
        for (String b: B) {
            int[] bCount = count(b);
            for (int i = 0; i < 26; i++) {
                bmax[i] = Math.max(bmax[i], bCount[i]);
            }
        }

        List<String> ans = new ArrayList();
        for (String a : A) {
            int[] aCount = count(a);
            boolean found = true;
            for (int i = 0; i < 26; i++) {
                if (aCount[i] < bmax[i]) {
                    found = false;
                    break;
                }
            }
            if (found) ans.add(a);
        }
        return ans;
    }

    private int[] count(String S) {
        int[] ans = new int[26];
        for (char c : S.toCharArray()) {
            ans[c - 'a']++;
        }
        return ans;
    }
}

#45ms 34.39%
class Solution {
    public List<String> wordSubsets(String[] A, String[] B) {
        int[] bmax = count("");
        for (String b: B) {
            int[] bCount = count(b);
            for (int i = 0; i < 26; i++) {
                bmax[i] = Math.max(bmax[i], bCount[i]);
            }
        }

        List<String> ans = new ArrayList();
        for (String a : A) {
            int[] aCount = count(a);
            for (int i = 0; i < 26; i++) {
                if (aCount[i] < bmax[i]) break;
                if (i == 25) ans.add(a);
            }
        }
        return ans;
    }

    private int[] count(String S) {
        int[] ans = new int[26];
        for (char c : S.toCharArray()) {
            ans[c - 'a']++;
        }
        return ans;
    }
}

#20ms 94.94%
class Solution {
    private boolean isSubset(String str, int[] maxs, int len) {
        if (str.length() < len) {
            return false;
        }
        int[] temp = new int[26];
        for (char c : str.toCharArray()) {
            temp[c - 'a']++;
        }
        // System.out.println(Arrays.toString(maxs));
        // System.out.println(Arrays.toString(temp));
        for (int i = 0; i < 26; i++) {
            if (maxs[i] > temp[i]) {
                //System.out.println("tt");
                return false;
            }
        }
        return true;
    }

    private void getMaxs(String str, int[] maxs) {
        int[] temp = new int[26];
        for (char c : str.toCharArray()) {
            temp[c - 'a']++;
        }
        for (char c : str.toCharArray()) {
            maxs[c - 'a'] = Math.max(maxs[c - 'a'], temp[c - 'a']);
        }
    }
    public List<String> wordSubsets(String[] A, String[] B) {
        List<String> ans = new ArrayList<>();
        int[] maxs = new int[26];
        for (String str : B) {
            getMaxs(str, maxs);
        }

        int len = 0;
        for (int i : maxs) {
            len += i;
        }

        if (len > 10) {
            return ans;
        }
        for (String a : A) {
            if (isSubset(a, maxs, len)) {
                ans.add(a);
            }
        }
       return ans;
    }
}
'''