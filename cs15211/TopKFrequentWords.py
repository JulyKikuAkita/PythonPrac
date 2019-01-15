__source__ = 'https://leetcode.com/problems/top-k-frequent-words/'
# Time:  O()
# Space: O()
#
# Description: Leetcode # 692. Top K Frequent Words
#
# Given a non-empty list of words, return the k most frequent elements.
#
# Your answer should be sorted by frequency from highest to lowest.
# If two words have the same frequency, then the word with the lower alphabetical order comes first.
#
# Example 1:
# Input: ["i", "love", "leetcode", "i", "love", "coding"], k = 2
# Output: ["i", "love"]
# Explanation: "i" and "love" are the two most frequent words.
#     Note that "i" comes before "love" due to a lower alphabetical order.
# Example 2:
# Input: ["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"], k = 4
# Output: ["the", "is", "sunny", "day"]
# Explanation: "the", "is", "sunny" and "day" are the four most frequent words,
#     with the number of occurrence being 4, 3, 2 and 1 respectively.
# Note:
# You may assume k is always valid, 1 <= k <= number of unique elements.
# Input words contain only lowercase letters.
# Follow up:
# Try to solve it in O(n log k) time and O(n) extra space.
#
import heapq
import unittest
import collections
#
# Approach #1: Sorting [Accepted]
# Time Complexity: O(NlogN), where N is the length of words.
# We count the frequency of each word in O(N) time, then we sort the given words in O(NlogN) time.
#
# Space Complexity: O(N), the space used to store our candidates.

class Solution(object):
    def topKFrequent(self, words, k):
        """
        :type words: List[str]
        :type k: int
        :rtype: List[str]
        """
        count = collections.Counter(words)
        candidates = count.keys()
        candidates.sort(key = lambda w: (-count[w], w))
        return candidates[:k]

# In Python, we improve this to O(N+klogN): our heapq.heapify operation and counting operations are O(N),
# and each of kk heapq.heappop operations are O(logN).
# Space Complexity: O(N)O(N), the space used to store our count.

class Solution2(object):
    def topKFrequent(self, words, k):
        """
        :type words: List[str]
        :type k: int
        :rtype: List[str]
        """
        count = collections.Counter(words)
        heap = [(-freq, word) for word, freq in count.items()]
        heapq.heapify(heap)
        return [heapq.heappop(heap)[1] for _ in xrange(k)]

class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)


if __name__ == '__main__':
    unittest.main()

Java = '''
# Thought: https://leetcode.com/problems/top-k-frequent-words/solution/

# Approach #1: Sorting [Accepted]
# 68ms 11.37%
class Solution {
    public List<String> topKFrequent(String[] words, int k) {
        Map<String, Integer> count = new HashMap<>();
        for (String word: words) {
            count.put(word, count.getOrDefault(word, 0) + 1);
        }
        List<String> candidates = new ArrayList(count.keySet());
        Collections.sort(candidates, (w1, w2) -> count.get(w1).equals(count.get(w2))?
                        w1.compareTo(w2) : count.get(w2) - count.get(w1)); //if w1 - w2,
                        // sorting in increasing order, thus return least frequent words
        return candidates.subList(0, k);
    }
}

# Approach #2: Heap [Accepted] PQ
# 11ms 99.80%
# Time Complexity: O(Nlogk), where N is the length of words.
# We count the frequency of each word in O(N) time, then we add N words to the heap,
# each in O(logk) time. Finally, we pop from the heap up to k times. As k <= N, this is O(Nlogk) in total.

/*
Lambda expression
https://www.mkyong.com/java8/java-8-lambda-comparator-example/
*/
# 13ms 81.92%
class Solution {
    public List<String> topKFrequent(String[] words, int k) {
        List<String> res = new ArrayList<>();
        Map<String, Integer> map = new HashMap<>();
        for (String word: words) {
            map.put(word, map.getOrDefault(word, 0) + 1);
        }
        PriorityQueue<Map.Entry<String, Integer>> pq = new PriorityQueue<>(new Checker());
        for (Map.Entry<String, Integer> entry : map.entrySet()) {
            pq.offer(entry);
            if (pq.size() > k) pq.poll();
        }
        while (pq.size() != 0) {
            res.add(0, pq.poll().getKey());
        }
        return res;
    }
}

class Checker implements Comparator<Map.Entry<String, Integer>> {
    public int compare(Map.Entry<String, Integer> o1, Map.Entry<String, Integer> o2) {
        if (o1.getValue() == o2.getValue()) {
            return o2.getKey().compareTo(o1.getKey());
        } else {
            return o1.getValue() - o2.getValue();
        }
    }
}

# 10ms 99.34%
class Solution {
    private class Point implements Comparable<Point> {
        private String str;
        private int count;
        public Point(String str) {
            this.str = str;
            this.count = 1;
        }
        @Override
        public int hashCode() {
            return str.hashCode();
        }
        @Override
        public int compareTo(Point b) {
            if(count != b.count) {
                return b.count - count;
            }
            else {
                return str.compareTo(b.str);
            }
        }
        public void addCount() {
            count++;
        }
        public String getStr() {
            return str;
        }
    }
    public List<String> topKFrequent(String[] words, int k) {
        Map<String, Point> map = new HashMap<>();
        for(String word: words) {
            if(map.containsKey(word)) {
                map.get(word).addCount();
            }
            else map.put(word, new Point(word));
        }
        PriorityQueue<Point> pq = new PriorityQueue<>(map.values());

        int count = 0;
        List<String> res = new ArrayList<>();
        while(!pq.isEmpty() && count < k) {
            res.add(pq.poll().getStr());
            count++;
        }

        return res;
    }
}
'''