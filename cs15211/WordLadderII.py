__author__ = 'July'

# Time:  O(n * d), n is length of string, d is size of dictionary
# Space: O(d)
# Back_Track + BFS
#
# Given two words (start and end), and a dictionary, find all shortest transformation sequence(s) from start to end, such that:
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
# Note:
# All words have the same length.
# All words contain only lowercase alphabetic characters.
#

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

if __name__ == "__main__":
    print Solution().findLadders("hit", "cog", set(["hot","dot","dog","lot","log"]))


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


#test
dict1 = [ "hot","dot","dog","lot","log" ]
dict2 = ["a","b","c"]
test = SolutionOther()
#print test.findLadders("hit", "cog", dict1)
#print test.findLadders("a", "b", dict2)

#Java
js = '''
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