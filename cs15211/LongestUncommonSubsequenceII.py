__source__ = 'https://leetcode.com/problems/longest-uncommon-subsequence-ii/#/description'
# Time:  O(x * n^2) where nn is the number of strings and xx is the average length of the strings.
# Space: O(1) Constant space required.
#
# Description: Leetcode # 522. Longest Uncommon Subsequence II
#
# Given a list of strings, you need to find the longest uncommon subsequence among them.
# The longest uncommon subsequence is defined as the longest subsequence of one of these strings
# and this subsequence should not be any subsequence of the other strings.
#
# A subsequence is a sequence that can be derived from one sequence by deleting some characters
# without changing the order of the remaining elements. Trivially, any string is a subsequence
# of itself and an empty string is a subsequence of any string.
#
# The input will be a list of strings, and the output needs to be the length of the longest uncommon subsequence.
# If the longest uncommon subsequence doesn't exist, return -1.
#
# Example 1:
# Input: "aba", "cdc", "eae"
# Output: 3
# Note:
#
# All the given strings' lengths will not exceed 10.
# The length of the given list will be in the range of [2, 50].
# Hide Company Tags Google
# Hide Tags String
# Hide Similar Problems (E) Longest Uncommon Subsequence I

# Explanation:
# When we add a letter Y to our candidate longest uncommon subsequence answer of X,
# it only makes it strictly harder to find a common subsequence.
# Thus our candidate longest uncommon subsequences will be chosen from the group of words itself.
#
# Suppose we have some candidate X.
# We only need to check whether X is not a subsequence of any of the other words Y.
# To save some time, we could have quickly ruled out Y when len(Y) < len(X),
# either by adding "if len(w1) > len(w2): return False" or enumerating over A[:i]
# (and checking neighbors for equality.)
# However, the problem has such small input constraints that this is not required.
#
# We want the max length of all candidates with the desired property,
# so we check candidates in descending order of length.
# When we find a suitable one, we know it must be the best global answer.
#
# Companies
# Google
# Related Topics
# String
# Similar Questions
# Longest Uncommon Subsequence I
#
import unittest
# 52ms
class Solution(object):
    def findLUSlength(self, strs):
        """
        :type strs: List[str]
        :rtype: int
        """

        def subseq(w1, w2) :
            #True iff word1 is a subsequence of word2.
            i = 0
            for c in w2:
                if i < len (w1) and w1[i] == c:
                    i += 1
            return  i == len(w1)

        strs.sort(key = len, reverse = True)
        for i, word1 in enumerate(strs):
            if all (not subseq(word1, word2) for j, word2 in enumerate(strs) if i != j):
                return len(word1)
        return -1

    def findLUSlength2(self, strs):
        def issubsequence(s, t):
            t = iter(t)
            return all(c in t for c in s)
        for s in sorted(strs, key=len, reverse=True):
            if sum(issubsequence(s, t) for t in strs) == 1:
                return len(s)
        return -1


# your function here

class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)


if __name__ == '__main__':
    unittest.main()

Java = '''
#Thought: https://leetcode.com/articles/longest-uncommon-subsequence-ii/

Approach #1 Brute Force[Accepted]
1) We simply maintain a map of all subsequence frequencies and
get the subsequence with frequency 1 that has longest length.
Time complexity : O(n*2^x). where x is the average length of the strings and nn is the total number of given strings
Space complexity : O(n*2^x). Hashmap of size n*2^x  is used.

# 20.95% 154ms
public int findLUSlength(String[] strs) {
    Map<String, Integer> subseqFreq = new HashMap<>();
    for (String s : strs)
        for (String subSeq : getSubseqs(s))
            subseqFreq.put(subSeq, subseqFreq.getOrDefault(subSeq, 0) + 1);
    int longest = -1;
    for (Map.Entry<String, Integer> entry : subseqFreq.entrySet())
        if (entry.getValue() == 1) longest = Math.max(longest, entry.getKey().length());
    return longest;
}

public static Set<String> getSubseqs(String s) {
    Set<String> res = new HashSet<>();
    if (s.length() == 0) {
         res.add("");
         return res;
    }
    Set<String> subRes = getSubseqs(s.substring(1)); //index 1 to s.length()-1
    res.addAll(subRes);
    for (String seq : subRes) res.add(s.charAt(0) + seq);
    return res;
}

NOTE: This solution does not take advantage of the fact that the optimal length
subsequence (if it exists) is always going to be the length of some string in the array.
Thus, the time complexity of this solution is non-optimal.
See https://discuss.leetcode.com/topic/85044/python-simple-explanation for optimal solution.

2. Approach #2 Checking Subsequence [Accepted]
Time complexity : O(x*n^2). where nn is the number of strings and x is the average length of the strings.
Space complexity : O(1)O(1). Constant space required.
# 92.04 % 10ms
public class Solution {
    public boolean isSubsequence(String x, String y) {
        int j = 0;
        for (int i = 0; i < y.length() && j < x.length(); i++)
            if (x.charAt(j) == y.charAt(i))
                j++;
        return j == x.length();
    }
    public int findLUSlength(String[] strs) {
        int res = -1;
        for (int i = 0, j; i < strs.length; i++) {
            for (j = 0; j < strs.length; j++) {
                if (j == i)
                    continue;
                if (isSubsequence(strs[i], strs[j]))
                    break;
            }
            if (j == strs.length)
                res = Math.max(res, strs[i].length());
        }
        return res;
    }
}


Approach #3 Sorting and Checking Subsequence [Accepted]
#69.97% 12ms
public class Solution {
    public int findLUSlength(String[] strs) {
        int len = strs.length;
        // reverse sorting array with length
        Arrays.sort(strs, new Comparator<String>() {
            public int compare(String s1, String s2) {
                return s2.length() - s1.length();
            }
        });

        for(int i=0; i<len; i++){
            int missMatchCount = strs.length - 1;
            for(int j=0; j<len; j++){
                if(i != j && !isSubSequence(strs[i], strs[j])){
                    missMatchCount --;
                }
            }
            // strs[i] is not a sub sequence of any other entry
            if(missMatchCount == 0){
                return strs[i].length();
            }
        }

        return -1;
    }

    private boolean isSubSequence(String s1, String s2){
        int idx = 0;
        for(char ch : s2.toCharArray()){
            if(idx < s1.length() && ch == s1.charAt(idx)){
                idx++;
            }
        }
        return idx == s1.length();
    }
}

#toCharArray always very fast ...
#noted for the usage of label
# 98.18% 9ms
public class Solution {
    public int findLUSlength(String[] strs) {
        int ret = -1;
        label: for (int i = 0; i < strs.length; i ++) {
            if (strs[i].length() <= ret) continue;
            int j = 0;
            for ( ; j < strs.length; j ++) {
                if (j == i) continue;
                if (isSubseq(strs[i], strs[j])) continue label;
            }
            if (strs[i].length() > ret) ret = strs[i].length();
        }
        return ret;
    }
    public boolean isSubseq(String s1, String s2) {
        if (s1.length() > s2.length()) return false;
        if (s1.length() == s2.length()) return s1.equals(s2);
        char[] chars1 = s1.toCharArray(), chars2 = s2.toCharArray();
        int j = 0;
        for (int i = 0; i < chars2.length && j < chars1.length; i ++) {
            if (chars1[j] == chars2[i]) j ++;
        }
        return j == chars1.length;
    }
}
'''