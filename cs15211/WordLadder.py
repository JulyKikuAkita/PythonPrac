__source__ = 'https://leetcode.com/problems/word-ladder/tabs/description'
# https://github.com/kamyu104/LeetCode/blob/master/Python/word-ladder.py
# Time:  O(n * d), n is length of string, d is size of dictionary
# Space: O(d)
# BFS
#
# Description: Leetcode # 127. Word Ladder
#
# Given two words (start and end), and a dictionary,
# find the length of shortest transformation sequence from start to end, such that:
#
# Only one letter can be changed at a time
# Each intermediate word must exist in the dictionary
# For example,
#
# Given:
# start = "hit"
# end = "cog"
# dict = ["hot","dot","dog","lot","log"]
# As one shortest transformation is "hit" -> "hot" -> "dot" -> "dog" -> "cog",
# return its length 5.
#
# Note:
# Return 0 if there is no such transformation sequence.
# All words have the same length.
# All words contain only lowercase alphabetic characters.
# You may assume no duplicates in the word list.
# You may assume beginWord and endWord are non-empty and are not the same.
# UPDATE (2017/1/20):
# The wordList parameter had been changed to a list of strings (instead of a set of strings).
# Please reload the code definition to get the latest changes.
#
# Companies
# Amazon LinkedIn Snapchat Facebook Yelp
#
import unittest
#DFS #OT # not a goodway as it is asking for shortest path
class SolutionDFS(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: Set[str]
        :rtype: int
        """
        if beginWord == endWord:
            return 1;

        cnt = float("INF")
        for i in xrange(len(beginWord)):
            for j in 'abcdefghijklmnopqrstuvwxyz':
                can = beginWord[:i]+j+beginWord[i+1:]
                if can == endWord:
                    return 2
                elif can in wordList:
                    wordList.remove(can)
                    cnt = min(cnt, 1 + self.ladderLength(can, endWord, wordList))
                    wordList.add(can)
        return cnt if cnt != float("INF") else 0

# below BFS
# 185 ms
class SolutionFatest(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: Set[str]
        :rtype: int
        """
        cnt = 2
        begin = [beginWord]
        end = [endWord]
        visited = set([beginWord])

        while begin and end:
            if len(begin) > len(end):
                begin , end = end, begin

            cur = []
            for word in begin:
                for i in xrange(len(word)):
                    for j in "abcdefghijklmnopqrstuvwxyz":
                        can = word[:i] + j + word[i+1:]
                        if can in end:
                            return cnt
                        elif can not in visited and can in wordList:
                            cur.append(can)
                            visited.add(can)
            begin = cur
            cnt += 1
        return 0

class Solution:
    # @param start, a string
    # @param end, a string
    # @param dict, a set of string
    # @return an integer
    def ladderLength(self, start, end, dict):
        distance, cur, visited = 0, [start], set([start])
        dict.add(end)

        while cur:
            next = []
            for word in cur:
                if word == end:
                    return distance + 1
                for i in xrange(len(word)):
                    for j in 'abcdefghijklmnopqrstuvwxyz':
                        candidate = word[:i] + j + word[i + 1:]
                        if candidate not in visited and candidate in dict:
                            next.append(candidate)
                            visited.add(candidate)
            distance += 1
            cur = next
        return 0

class Solution2(object):
    def ladderLength(self, beginWord, endWord, wordList):
        wordList.add(endWord)
        q= []
        q.append([beginWord, 1])
        while q:
            currword, currlen  = q.pop(0)
            if currword == endWord:
                return currlen
            for i in range(len(currword)):
                part1 = currword[:i]
                part2 = currword[i+1:]
                for j in 'abcdefghijklmnopqrstuvwxyz':
                    if currword[i] != j:
                        nextword = part1 + j + part2
                        if nextword in wordList:
                            q.append((nextword, currlen+1))
                            wordList.remove(nextword)
        return 0

#http://www.programcreek.com/2012/12/leetcode-word-ladder/
# when start = hit -> hot, need to start from i loop instead of continue i loop
class Naive: #wrong answer
    # @param start, a string
    # @param end, a string
    # @param dict, a set of string
    # @return an integer
    def ladderLength(self, start, end, dict):
        ans = 0
        dict.add(end)
        for i in xrange(len(start)):
            for j in 'abcdefghijklmnopqrstuvwxyz':
                if start[i] == j :
                    continue
                candidate = start[:i] + j + start[i+1:]
                if candidate in dict:
                    ans += 1
                    start = candidate
                    if candidate == end:
                        return ans
        return ans

#test
class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)
        test = Solution()
        dict1 = {"hot","dot","dog","lot","log"}
        #print test.ladderLength("hit", "cog", dict1)

        print Solution().ladderLength("hit", "cog", set(["hot","dot","dog","lot","log"]))
        print Solution2().ladderLength("hit", "cog", set(["hot","dot","dog","lot","log"]))
        print Naive().ladderLength("hit", "cog", set(["ait","dot","dog","lot","log"]))

if __name__ == '__main__':
    unittest.main()

Java = '''
#Thought:

# Java Solution using Dijkstra's algorithm, with explanation
# 82.77% 63ms
class Solution {
    public int ladderLength(String beginWord, String endWord, List<String> wordList) {
        if (!wordList.contains(endWord)) return 0;

        Set<String> reached = new HashSet<String>();
        Set<String> wordDict = new HashSet<String>(wordList);
        reached.add(beginWord);
        wordDict.add(endWord);
        int distance = 1;
        while (!reached.contains(endWord)) {
            Set<String> toAdd = new HashSet<String>();
            for (String each : reached) {
                for (int i = 0; i < each.length(); i++) {
                    char[] chars = each.toCharArray();
                    for (char ch = 'a'; ch <= 'z'; ch++) {
                        if (chars[i] == ch) continue;
                        chars[i] = ch;
                        String word = new String(chars);
                        if (wordDict.contains(word)) {
                            toAdd.add(word);
                            wordDict.remove(word);
                        }
                    }
                }
            }
            distance++;
            if (toAdd.size() == 0) return 0;
            reached = toAdd;
        }
        return distance;
    }
}

# 93.86 % 26ms
class Solution {
    public int ladderLength(String beginWord, String endWord, List<String> wordList) {
        Set<String> dict = new HashSet<>(wordList);
        if (!dict.contains(endWord)) return 0;
        Set<String> startSet = new HashSet<String>() {{ add(beginWord); }};
        Set<String> endSet = new HashSet<String>() {{ add(endWord); }};
        return helper(dict, startSet, endSet, 1);
    }

     private int helper(Set<String> dict, Set<String> startSet, Set<String> endSet, int level) {
        if (startSet.isEmpty()) return 0;

        if (startSet.size() > endSet.size()) return helper(dict, endSet, startSet, level);

        // remove words from both ends
        for (String word : startSet) { dict.remove(word); };
        for (String word : endSet) { dict.remove(word); };

        // the set for next level
        Set<String> set = new HashSet<>();

        // for each string in the current level
        for (String str: startSet) {
            for (int i = 0; i < str.length(); i++) {
                char[] chars = str.toCharArray();

                for (char ch = 'a'; ch <= 'z'; ch++) {
                    if (chars[i] == ch) continue;
                    chars[i] = ch;
                    String word = new String(chars);
                     // found the word in other end(set)
                    if (endSet.contains(word)) return level + 1;
                    // if not, add to the next level
                    if (dict.contains(word)) set.add(word);
                }
            }
        }
        return helper(dict, endSet, set, level + 1);
     }

}

#14ms 99.93%
class Solution {
    public int ladderLength(String beginWord, String endWord, List<String> wordList) {
        Set<String> wordset = new HashSet<String>(wordList);
        Set<String> start = new HashSet<String>();
        Set<String> end = new HashSet<String>();

        if(!wordset.contains(endWord)) {
            return 0;
        }
        start.add(beginWord);
        end.add(endWord);
        return helper(start, end, wordset, 1);
    }

    public int helper(Set<String> start, Set<String> end, Set<String> wordset, int level) {
        if(start.size() > end.size()) {
            return helper(end, start, wordset, level);
        }
        wordset.removeAll(start);
        wordset.removeAll(end);
        Set<String> next = new HashSet<String>();
        for(String s : start) {
            char[] arr = s.toCharArray();
            for(int i = 0; i< arr.length; i++){
                char temp = arr[i];
                for(char c = 'a'; c <= 'z';c++) {
                    if(c == arr[i]) {
                        continue;
                    }
                    arr[i] = c;
                    String newWord = new String(arr);
                    if(end.contains(newWord)) {
                        return level+1;
                    }
                    if(wordset.contains(newWord)) {
                        next.add(newWord);

                    }
                    arr[i] = temp;
                }
            }
        }
        if(next.isEmpty()) {
            return 0;
        }
        return helper(end, next, wordset, level+1);

    }
}
'''