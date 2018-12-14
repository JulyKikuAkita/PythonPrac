__source__ = 'https://leetcode.com/problems/palindrome-partitioning/'
# https://github.com/kamyu104/LeetCode/blob/master/Python/palindrome-partitioning.py
# Time:  O(n^2 ~ 2^n)
# Space: O(n^2)
#
# Description: Leetcode # 131. Palindrome Partitioning
#
# Given a string s, partition s such that every substring of the partition is a palindrome.
#
# Return all possible palindrome partitioning of s.
#
# For example, given s = "aab",
# Return
#
#   [
#     ["aa","b"],
#     ["a","a","b"]
#   ]
#
# Companies
# Bloomberg
# Related Topics
# Backtracking
# Similar Questions
# Palindrome Partitioning II
#

import unittest
# Time:  O(n^2 ~ 2^n)
# Space: O(n^2)
# dynamic programming solution
class Solution:
    # @param s, a string
    # @return a list of lists of string
    def partition(self, s):
        n = len(s)
        is_palindrome = [[0 for j in xrange(n)] for i in xrange(n)]
        for i in reversed(xrange(0,n)):
            for j in xrange(i, n):
                is_palindrome[i][j] = s[i] == s[j] and((j - i < 2) or is_palindrome[i + 1][j - 1])

        sub_partition = [[] for i in xrange(n)]
        #print sub_partition
        for i in reversed(xrange(n)):
            for j in xrange(i, n):
                if is_palindrome[i][j]:
                    if j + 1 < n:
                        for p in sub_partition[ j + 1]:
                            sub_partition[i].append([s[i:j +1]] + p)
                           # print i, j, s[i:j +1], p
                    else:
                        sub_partition[i].append([s[i:j+1]])

        return sub_partition[0]

# Time:  O(2^n)
# Space: O(n)
# recursive solution
class Solution2:
    # @param s, a string
    # @return a list of lists of string
    def partition(self, s):
        result = []
        self.partitionRecu(result, [], s, 0)
        return result

    def partitionRecu(self, result, cur, s, i):
        if i == len(s):
            result.append(list(cur)) # Converts a tuple into list.
        else:
            for j in xrange(i, len(s)):
                #print i, j, s[i:j + 1], cur
                if self.isPalindrome(s[i:j + 1]):
                    cur.append(s[i: j + 1])
                    self.partitionRecu(result, cur, s, j + 1)
                    cur.pop()

    def isPalindrome(self, s):
        for i in xrange(len(s) / 2):
            if s[i] != s[-(i+1)]:
                return False
        return True

class SolutionOther:
    # @param s, a string
    # @return a list of lists of string
    def partition(self, s):
        Solution.res = []
        self.dfs(s, [])
        return Solution.res

    def isPalindrome(self, s):
        for i in range(len(s)):
            if s[i] != s[len(s) - 1 - i]:
                return False
        return True

    def dfs(self, s, stringlist):
        if len(s) == 0:
            Solution.res.append(stringlist)
        for i in range(1, len(s) +1):
            print i, s[:i],self.isPalindrome(s[:i]), stringlist ,s[i:]
            if self.isPalindrome(s[:i]):
                self.dfs(s[i:], stringlist+[s[:i]])

class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)
         #print Solution().partition("aab")
        print Solution2().partition("aab")
        #print DP().partition("aab")

if __name__ == '__main__':
    unittest.main()

Java = '''
# Thought:
#
# backtracking
# 84.45% 7ms
class Solution {
    public List<List<String>> partition(String s) {
       List<List<String>> list = new ArrayList<>();
       backtrack(list, new ArrayList<>(), s, 0);
       return list;
    }

    public void backtrack(List<List<String>> list, List<String> tempList, String s, int start){
       if(start == s.length())
          list.add(new ArrayList<>(tempList));
       else{
          for(int i = start; i < s.length(); i++){
             if(isPalindrome(s, start, i)){
                tempList.add(s.substring(start, i + 1));
                backtrack(list, tempList, s, i + 1);
                tempList.remove(tempList.size() - 1);
             }
          }
       }
    }

    private boolean isPalindrome(String s, int left, int right) {
        while (left < right) {
            if (s.charAt(left) != s.charAt(right)) return false;
            left ++;
            right--;
        }
        return true;
    }
}

# DP O(n^2)
# 8ms 41.73%
class Solution {
 	public static List<List<String>> partition(String s) {
		int len = s.length();
		List<List<String>>[] result = new List[len + 1];
		result[0] = new ArrayList<List<String>>();
		result[0].add(new ArrayList<String>());

		boolean[][] pair = new boolean[len][len];
		for (int i = 0; i < s.length(); i++) {
			result[i + 1] = new ArrayList<List<String>>();
			for (int left = 0; left <= i; left++) {
				if (s.charAt(left) == s.charAt(i) && (i-left <= 1 || pair[left + 1][i - 1])) {
					pair[left][i] = true;
					String str = s.substring(left, i + 1);
					for (List<String> r : result[left]) {
						List<String> ri = new ArrayList<String>(r);
						ri.add(str);
						result[i + 1].add(ri);
					}
				}
			}
		}
		return result[len];
	}
}

# 3ms 99.86%
class Solution {
    public List<List<String>> partition(String s) {
        List<List<String>> result = new ArrayList<List<String>>();
        if (s == null || s.length() == 0) {
            return result;
        }

        findPartition(s, result, new ArrayList<String>(), 0, 1);
        return result;
    }

    private boolean isPalindrome(String s, int i, int j) {
        if (s == null || i < 0 || j > s.length() || i > j) {
            return false;
        }

        j--;
        while (i < j) {
            if (s.charAt(i) != s.charAt(j)) {
                return false;
            }
            i++;
            j--;
        }

        return true;
    }

    private void findPartition(String s, List<List<String>> result, List<String> list, int start, int end) {
        if (start == s.length()) {
            result.add(new ArrayList<String>(list));
            return;
        }

        while (end <= s.length()) {
            if (isPalindrome(s, start, end)) {
                list.add(s.substring(start, end));
                findPartition(s, result, list, end, end + 1);
                list.remove(list.size() - 1);
            }
            end++;
        }
    }
}
'''