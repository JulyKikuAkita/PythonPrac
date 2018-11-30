import collections

__source__ = 'https://leetcode.com/problems/number-of-matching-subsequences/description/'
# Time:  O()
# Space: O()
#
# Description: Leetcode # 792. Number of Matching Subsequences
#
# Given string S and a dictionary of words words,
# find the number of words[i] that is a subsequence of S.
#
# Example :
# Input:
# S = "abcde"
# words = ["a", "bb", "acd", "ace"]
# Output: 3
# Explanation: There are three words in words that are a subsequence of S: "a", "acd", "ace".
# Note:
#
# All words in words and S will only consists of lowercase letters.
# The length of S will be in the range of [1, 50000].
# The length of words will be in the range of [1, 5000].
# The length of words[i] will be in the range of [1, 50].
#
import unittest

#188ms 99.32%
class Solution(object):
    def numMatchingSubseq(self, S, words):
        """
        :type S: str
        :type words: List[str]
        :rtype: int
        """
        count = 0
        contain = {}
        no_contain = {}
        for word in words:
            if word in contain:
                count += 1
                continue
            if word in no_contain:
                continue
            if self.isSubseq(S, word):
                #print(word)
                count += 1
                contain[word] = 1
            else:
                no_contain[word] = 1
        return count

    def isSubseq(self, S, word):
        index = -1
        for w in word:
            index = S.find(w, index+1)
            if index == -1:
                return False
        return True
# Detailed:
#  https://leetcode.com/problems/number-of-matching-subsequences/discuss/117634/Efficient-and-simple-go-through-words-in-parallel-with-explanation
class Solution2(object):
    def numMatchingSubseq(self, S, words):
        """
        :type S: str
        :type words: List[str]
        :rtype: int
        """
        waiting = collections.defaultdict(list)
        for it in map(iter, words):
            waiting[next(it)].append(it)
        for c in S:
            for it in waiting.pop(c, ()):
                waiting[next(it, None)].append(it)
        return len(waiting[None])

class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)


if __name__ == '__main__':
    unittest.main()

Java = '''
#Thought: https://leetcode.com/problems/number-of-matching-subsequences/solution/
Approach #1: Brute Force [Time Limit Exceeded]

Approach #2: Next Letter Pointers [Accepted]
# Since the length of S is large, let's think about ways to iterate through S only once,
# instead of many times as in the brute force solution.
#
# We can put words into buckets by starting character.
# If for example we have words = ['dog', 'cat', 'cop'],
# then we can group them 'c' : ('cat', 'cop'), 'd' : ('dog',).
# This groups words by what letter they are currently waiting for.
# Then, while iterating through letters of S, we will move our words through different buckets.
#

# Complexity Analysis
#
# Time Complexity: O(S.length + \sum_i{words[i].length})
# Space Complexity: O(words.length).
# (In Java, our additional space complexity is O(\sum_i {words[i].length})),
# but can be made to be O(words.length) with a pointer based implementation.)

#79.8% 78ms
class Solution {
    public int numMatchingSubseq(String S, String[] words) {
        int ans = 0;
        ArrayList<Node>[] heads = new ArrayList[26];
        for (int i = 0; i < 26; i++) {
            heads[i] = new ArrayList<Node>();
        }

        for (String word: words) {
            heads[word.charAt(0) - 'a'].add(new Node(word, 0));
        }

        for (char c: S.toCharArray()) {
            ArrayList<Node> old_bucket = heads[c  - 'a'];
            heads[c - 'a'] = new ArrayList<Node>();

            for (Node node : old_bucket) {
                node.index++;
                if (node.index == node.word.length()) ans++;
                else {
                    heads[node.word.charAt(node.index) - 'a'].add(node);
                }
            }
            old_bucket.clear();
        }
        return ans;
    }
}

class Node {
    String word;
    int index;
    public Node(String w, int i) {
        word = w;
        index = i;
    }
}

# same idea with array
public int numMatchingSubseq(String S, String[] words) {
    List<Integer[]>[] waiting = new List[128];
    for (int c = 0; c <= 'z'; c++)
        waiting[c] = new ArrayList();
    for (int i = 0; i < words.length; i++)
        waiting[words[i].charAt(0)].add(new Integer[]{i, 1});
    for (char c : S.toCharArray()) {
        List<Integer[]> advance = new ArrayList(waiting[c]);
        waiting[c].clear();
        for (Integer[] a : advance)
            waiting[a[1] < words[a[0]].length() ? words[a[0]].charAt(a[1]++) : 0].add(a);
    }
    return waiting[0].size();
}


# Same idea with java StringCharacterIterator

#90.84% 58ms
import java.text.StringCharacterIterator;
class Solution {
    public int numMatchingSubseq(String S, String[] words) {
        List<StringCharacterIterator>[] waiting = new List[128];
        for (int c = 0; c <= 'z'; c++)
            waiting[c] = new ArrayList();
        for (String w : words)
            waiting[w.charAt(0)].add(new StringCharacterIterator(w));
        for (char c : S.toCharArray()) {
            List<StringCharacterIterator> advance = waiting[c];
            waiting[c] = new ArrayList();
            for (StringCharacterIterator it : advance)
                waiting[it.next() % it.DONE].add(it);
        }
        return waiting[0].size();
    }
}

# Explanation:
# I go through S once, and while I'm doing that, I move through all words accordingly.
That is, I keep track of how much of each word I've already seen,
and with each letter of S, I advance the words waiting for that letter.
To quickly find the words waiting for a certain letter,
I store each word (and its progress) in a list of words waiting for that letter.
Then for each of the lucky words whose current letter just occurred in S,
I update their progress and store them in the list for their next letter.
#
# Let's go through the given example:
#
# S = "abcde"
# words = ["a", "bb", "acd", "ace"]
# I store that "a", "acd" and "ace" are waiting for an 'a' and "bb" is waiting for a 'b'
# (using parentheses to show how far I am in each word):
#
# 'a':  ["(a)", "(a)cd", "(a)ce"]
# 'b':  ["(b)b"]
# Then I go through S. First I see 'a',
# so I take the list of words waiting for 'a' and store them as waiting under their next letter:
#
# 'b':  ["(b)b"]
# 'c':  ["a(c)d", "a(c)e"]
# None: ["a"]
# You see "a" is already waiting for nothing anymore,
# see 'b' and update accordingly:
#
# 'b':  ["b(b)"]
# 'c':  ["a(c)d", "a(c)e"]
# None: ["a"]
# Then 'c':
#
# 'b':  ["b(b)"]
# 'd':  ["ac(d)"]
# 'e':  ["ac(e)"]
# None: ["a"]
# Then 'd':
#
# 'b':  ["b(b)"]
# 'e':  ["ac(e)"]
# None: ["a", "acd"]
# Then 'e':
#
# 'b':  ["b(b)"]
# None: ["a", "acd", "ace"]
# And now I just return how many words aren't waiting for anything anymore.
#

#73.04% 85ms
class Solution {
    public int numMatchingSubseq(String S, String[] words) {
        Map<Character, Deque<String>> map = new HashMap<>();
        for (char c = 'a'; c <= 'z'; c++) {
            map.putIfAbsent(c, new LinkedList<String>());
        }
        for (String word : words) {
            map.get(word.charAt(0)).addLast(word);
        }

        int count = 0;
        for (char c : S.toCharArray()) {
            Deque<String> queue = map.get(c);
            int size = queue.size();
            for (int i = 0; i < size; i++) {
                String word = queue.removeFirst();
                if (word.length() == 1) {
                    count++;
                } else {
                    map.get(word.charAt(1)).addLast(word.substring(1)); //substring() is time consuming  -> use an array as a map to further improve this solution.
                }
            }
        }
        return count;
    }
}

# HashSet
# 100% 23ms
class Solution {
    public int numMatchingSubseq(String S, String[] words) {
        int sum = 0;
        HashSet<String> sub = new HashSet();
        HashSet<String> nonsub = new HashSet();
        for (String word: words) {
            if (sub.contains(word)) {
                sum++;
                continue;
            }
            if (nonsub.contains(word)) continue;
            if (isSub(S, word)) {
                sub.add(word);
                sum++;
            } else {
                nonsub.add(word);
            }
        }
        return sum;
    }

    private boolean isSub(String S, String word) {
        int index = -1;
        for (char c: word.toCharArray()) {
            index = S.indexOf(c, index + 1);
            if (index == -1) return false;
        }
        return true;
    }
}
'''