__author__ = 'July'
# https://github.com/kamyu104/LeetCode/blob/master/Python/word-ladder.py
# Time:  O(n * d), n is length of string, d is size of dictionary
# Space: O(d)
# BFS
#
# Given two words (start and end), and a dictionary, find the length of shortest transformation sequence from start to end, such that:
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
# Linkedln
#
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

#	185 ms
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
test = Solution()
dict1 = {"hot","dot","dog","lot","log"}
#print test.ladderLength("hit", "cog", dict1)

if __name__ == "__main__":
    print Solution().ladderLength("hit", "cog", set(["hot","dot","dog","lot","log"]))
    print Solution2().ladderLength("hit", "cog", set(["hot","dot","dog","lot","log"]))
    print Naive().ladderLength("hit", "cog", set(["ait","dot","dog","lot","log"]))

#java
#double ended BFS
js = '''
public class Solution {
    public int ladderLength(String beginWord, String endWord, Set<String> wordList) {
        Set<String> beginSet = new HashSet<>();
        Set<String> endSet = new HashSet<>();
        Set<String> visitedSet = new HashSet<>();
        int count = 2;
        int len = beginWord.length();
        beginSet.add(beginWord);
        endSet.add(endWord);
        visitedSet.add(beginWord);
        while (!beginSet.isEmpty() && !endSet.isEmpty()) {
            if (beginSet.size()  > endSet.size()) {
                Set<String> tmpSet = beginSet;
                beginSet = endSet;
                endSet = tmpSet;
            }
            Set<String> curSet = new HashSet<>();
            for (String word : beginSet) {
                char[] arr = word.toCharArray();
                for (int j = 0; j < len; j++) {
                    char c = arr[j];
                    for (char k = 'a'; k <= 'z'; k++) {
                        arr[j] = k;
                        String cur = new String(arr);
                        if (endSet.contains(cur)) {
                            return count;
                        } else if (wordList.contains(cur) && !visitedSet.contains(cur)) {
                            visitedSet.add(cur);
                            curSet.add(cur);
                        }
                    }
                    arr[j] = c;
                }
            }
            beginSet = curSet;
            count++;
        }
        return 0;
    }
}

# https://linchicoding.wordpress.com/2014/10/13/leetcode-word-ladder/
#DFS: #OT
public class SolutionDFS {
    public int ladderLength(String start, String end, Set<String> dict) {
        if(start.equals(end)) return 1;
        char[] arr = start.toCharArray();
        int min = Integer.MAX_VALUE;
        for(int i = 0; i <start.length(); i++){
            char temp = arr[i];
            for(char ch = 'a'; ch <='z'; ch++){
                if(ch != temp){
                    arr[i] = ch;
                    String nxt = new String(arr);
                    if(end.equals(nxt))
                        return 2;
                    else if(dict.contains(nxt)){
                        dict.remove(nxt);
                        min = Math.min(min, 1+ ladderLength(nxt, end, dict));
                        dict.add(nxt);
                    }
                }
            }
            arr[i] = temp;
        }
        return min==Integer.MAX_VALUE ? 0:min;
    }

}
'''