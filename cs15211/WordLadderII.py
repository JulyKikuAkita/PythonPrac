__source__ = 'https://leetcode.com/problems/word-ladder-ii/description/'
# https://github.com/kamyu104/LeetCode/blob/master/Python/word-ladder-ii.py
# Time:  O(n * d), n is length of string, d is size of dictionary
# Space: O(d)
# Back_Track + BFS
#
# Description: Leetcode # 126. Word Ladder II
#
# Given two words (start and end), and a dictionary,
# find all shortest transformation sequence(s) from start to end, such that:
#
# Only one letter can be changed at a time
# Each intermediate word must exist in the dictionary
# For example,
#
# Given:
# start = "hit"
# end = "cog"
# dict = ["hot","dot","dog","lot","log"]
# Return
#   [
#     ["hit","hot","dot","dog","cog"],
#     ["hit","hot","lot","log","cog"]
#   ]
#
# Note:
# Return an empty list if there is no such transformation sequence.
# All words have the same length.
# All words contain only lowercase alphabetic characters.
# You may assume no duplicates in the word list.
# You may assume beginWord and endWord are non-empty and are not the same.
# UPDATE (2017/1/20):
# The wordList parameter had been changed to a list of strings (instead of a set of strings).
# Please reload the code definition to get the latest changes.
#
# Companies
# Amazon Yelp
# Related Topics
# Array Backtracking Breadth-first Search String
#
import unittest
# BFS
class Solution:
    # @param start, a string
    # @param end, a string
    # @param dict, a set of string
    # @return an integer
    def findLadders(self, start, end, dict):
        dict.add(start)
        dict.add(end)

        result, cur = [], [start]
        visited = set([start])
        found = False
        trace = {word : [] for word in dict}
        print trace

        while cur and not found:
            for word in cur:
                visited.add(word)
            next = set([])

            for word in cur:
                for i in xrange(len(word)):
                    for j in 'abcdefghijklmnopqrstuvwxyz':
                        candidate = word[:i] + j + word[i+1:]

                        if candidate not in visited and candidate in dict:
                            if candidate == end:
                                found = True
                            next.add(candidate)
                            trace[candidate].append(word)
            cur = next

        if found:
            self.backtrack(result, trace, [], end)

        return result

    def backtrack(self, result, trace, path, word):
        if not trace[word]:
            result.append([word] + path)
        else:
            for prev in trace[word]:
                self.backtrack(result, trace, [word] + path, prev)

# http://www.cnblogs.com/zuoyuan/p/3697045.html
class SolutionOther:
    # @param start, a string
    # @param end, a string
    # @param dict, a set of string
    # @return a list of lists of string
    def findLadders(self, start, end, dict):

        self.result = []
        self.prevMap = {}
        length = len(start)

        for i in dict:
            self.prevMap[i] = []
        candidates = [set(), set()]
        current = 0
        previous = 1
        candidates[current].add(start)

        print candidates, current, previous

        while True:
            current, previous = previous, current

            for i in candidates[previous]:
                try:
                    print dict, i
                    dict.remove(i)
                except ValueError:
                    pass
            candidates[current].clear()

            for word in candidates[previous]:
                for i in range(length):
                    part1 = word[:i]
                    part2 = word[i+1:]
                    for j in 'abcdefghijklmnopqrstuvwxyz':
                        if word[i] != j:
                            nextword = part1 + j +part2
                            if nextword in dict:
                                self.prevMap[nextword].append(word)
                                candidates[current].add(nextword)
                                #print self.prevMap, candidates

            if len(candidates[current]) == 0:
                #print self.result
                return self.result
            if end in candidates[current]:
                break

        self.buildpath([], end)

        return self.result

    def buildpath(self, path, word):
            if len(self.prevMap[word]) == 0:
                path.append(word)
                currPath = path[:]
                currPath.reverse()
                self.result.append(currPath)
                path.pop()
                return
            path.append(word)

            for iter in self.prevMap[word]:
                self.buildpath(path, iter)
            path.pop()

# Test
class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)
        dict1 = [ "hot","dot","dog","lot","log" ]
        dict2 = ["a","b","c"]
        test = SolutionOther()
        #print test.findLadders("hit", "cog", dict1)
        #print test.findLadders("a", "b", dict2)
        print Solution().findLadders("hit", "cog", set(["hot","dot","dog","lot","log"]))

if __name__ == '__main__':
    unittest.main()

Java = '''
#Thought:

public class Solution {
    public List<List<String>> findLadders(String beginWord, String endWord, Set<String> wordList) {
        Set<String> unvisited = new HashSet<>(wordList);
        unvisited.add(endWord);
        unvisited.remove(beginWord);
        Set<String> roundVisited = new HashSet<>();
        Queue<String> queue = new LinkedList<>();
        queue.add(beginWord);
        Map<String, List<String>> nextMap = new HashMap<>();
        for (String str : unvisited) {
            nextMap.put(str, new ArrayList<>());
        }
        nextMap.put(beginWord, new ArrayList<>());
        Map<String, Integer> levelMap = new HashMap<>();
        levelMap.put(beginWord, 0);
        int prevLevel = 0;
        int minLevel = Integer.MAX_VALUE;
        while (!queue.isEmpty()) {
            String curr = queue.poll();
            int level = levelMap.get(curr);
            if (level > minLevel) {
                break;
            }
            if (prevLevel != level) {
                unvisited.removeAll(roundVisited);
                roundVisited.clear();
                prevLevel = level;
            }
            char[] arr = curr.toCharArray();
            for (int i = 0; i < arr.length; i++) {
                char originalChar = arr[i];
                boolean found = false;
                for (char newChar = 'a'; newChar <= 'z'; newChar++) {
                    if (newChar == originalChar) {
                        continue;
                    }
                    arr[i] = newChar;
                    String newString = new String(arr);
                    if (unvisited.contains(newString)) {
                        nextMap.get(curr).add(newString);
                        if (newString.equals(endWord)) {
                            found = true;
                            minLevel = Math.min(minLevel, level + 1);
                            break;
                        }
                        if (!roundVisited.contains(newString)) {
                            roundVisited.add(newString);
                            queue.add(newString);
                            levelMap.put(newString, level + 1);
                        }
                    }
                }
                if (found) {
                    break;
                }
                arr[i] = originalChar;
            }
        }
        List<List<String>> result = new ArrayList<>();
        if (minLevel == Integer.MAX_VALUE) {
            return result;
        }
        findPaths(endWord, beginWord, result, new ArrayList<>(), minLevel, nextMap);
        return result;
    }

    private void findPaths(String endWord, String currWord, List<List<String>> result, List<String> path,
                            int level, Map<String, List<String>> nextMap) {
        if (level < 0) {
            return;
        }
        level--;
        path.add(currWord);
        if (currWord.equals(endWord)) {
            result.add(new ArrayList<>(path));
        } else {
            for (String nextWord : nextMap.get(currWord)) {
                findPaths(endWord, nextWord, result, path, level, nextMap);
            }
        }
        path.remove(path.size() - 1);
    }
}

public class Solution {
    public List<List<String>> findLadders(String beginWord, String endWord, Set<String> wordList) {
        List<List<String>> result = new ArrayList<>();
        Set<String> unvisited = new HashSet<>();
        Map<String, List<String>> nextMap = new HashMap<>();
        Queue<LevelString> queue = new LinkedList<>();

        unvisited.addAll(wordList);
        unvisited.add(beginWord);
        unvisited.remove(endWord);
        for (String str : unvisited) {
            nextMap.put(str, new ArrayList<String>());
        }
        queue.add(new LevelString(endWord, 0));

        Set<String> visited = new HashSet<>();
        int currLevel = 0;
        int prevLevel = 0;
        int foundLevel = Integer.MAX_VALUE;
        while (!queue.isEmpty()) {
            LevelString currLevelString = queue.poll();
            String currString = currLevelString.string;
            currLevel = currLevelString.level;
            if (currLevel > foundLevel) {
                break;
            }
            if (currLevel > prevLevel) {
                unvisited.removeAll(visited);
            }
            prevLevel = currLevel;
            char[] currArr = currString.toCharArray();
            for (int i = 0; i < currArr.length; i++) {
                char originChar = currArr[i];
                boolean currFound = false;
                for (char newChar = 'a'; newChar <= 'z'; newChar++) {
                    currArr[i] = newChar;
                    String newString = new String(currArr);
                    if (newChar != originChar && unvisited.contains(newString)) {
                        nextMap.get(newString).add(currString);
                        if (beginWord.equals(newString)) {
                            currFound = true;
                            foundLevel = currLevel;
                            break;
                        }
                        if (!visited.contains(newString)) {
                            visited.add(newString);
                            queue.add(new LevelString(newString, currLevel + 1));
                        }
                    }
                }
                if (currFound) {
                    break;
                }
                currArr[i] = originChar;
            }
        }
        if (foundLevel != Integer.MAX_VALUE) {
            List<String> path = new ArrayList<>();
            path.add(beginWord);
            findResult(endWord, path, foundLevel + 1, nextMap, result);
        }
        return result;
    }

    private void findResult(String endWord, List<String> currPath, int level, Map<String, List<String>> nextMap, List<List<String>> result) {
        if (level < 0) {
            return;
        }
        String currWord = currPath.get(currPath.size() - 1);
        if (currWord.equals(endWord)) {
            result.add(new ArrayList<String>(currPath));
            return;
        }
        List<String> nextWords = nextMap.get(currWord);
        for (String nextWord : nextWords) {
            currPath.add(nextWord);
            findResult(endWord, currPath, level - 1, nextMap, result);
            currPath.remove(currPath.size() - 1);
        }
    }
}

class LevelString {
    String string;
    int level;
    public LevelString(String string, int level) {
        this.string = string;
        this.level = level;
    }
}

'''

# below is for 2017 version
Leecode2017 = '''
#29ms 94.81%
public class Solution {
        boolean isConnected = false;
        public List<List<String>> findLadders(String beginWord, String endWord, List<String> wordList){
            List<List<String>> result = new ArrayList<List<String>>();
            Set<String> dict = new HashSet<>(wordList);
            if(!dict.contains(endWord)){
                return result;
            }
            Set<String> fwd = new HashSet<String>();
            fwd.add(beginWord);
            Set<String> bwd = new HashSet<String>();
            bwd.add(endWord);

            Map<String, List<String>> hs = new HashMap<String, List<String>>();
            BFS(fwd, bwd, dict, false, hs);

            if (!isConnected) return result;

            List<String> temp = new ArrayList<String>();
            temp.add(beginWord);

            DFS(result, temp, beginWord, endWord, hs);

            return result;
        }

    public void BFS (Set<String> forward, Set<String> backward, Set<String> dict, boolean swap, Map<String, List<String>> hs){
        if (forward.isEmpty() || backward.isEmpty()){
            return;
        }
        if (forward.size() > backward.size()){
            BFS(backward, forward, dict, !swap, hs);
            return;
        }
        dict.removeAll(forward);
        dict.removeAll(backward);

        Set<String> set3 = new HashSet<String>();

        for (String str : forward){
            for (int i = 0; i < str.length(); i++){
                char[] ary = str.toCharArray();
                for (char j = 'a'; j <= 'z'; j++){
                    ary[i] = j;
                    String temp = new String(ary);
                    if(!backward.contains(temp) && !dict.contains(temp)){
                        continue;
                    }

                    String key = !swap ? str : temp;
                    String val = !swap ? temp : str;

                    if (!hs.containsKey(key)) hs.put(key, new ArrayList<String>());
                    if (backward.contains(temp)){
                        hs.get(key).add(val);
                        isConnected = true;
                    }
                    if (!isConnected && dict.contains(temp)){
                        hs.get(key).add(val);
                        set3.add(temp);
                    }
                }
            }
        }
        if (!isConnected){
            BFS(set3, backward, dict, swap, hs);
        }
    }

    public void DFS (List<List<String>> result, List<String> temp, String start, String end, Map<String, List<String>> hs){
        if(start.equals(end)){
            result.add(new ArrayList<String>(temp));
            return;
        }
        if (!hs.containsKey(start)) return;

        for (String s : hs.get(start)){
            temp.add(s);
            DFS(result, temp, s, end, hs);
            temp.remove(temp.size() - 1);
        }
    }
}
'''
