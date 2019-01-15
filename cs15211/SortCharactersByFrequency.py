__source__ = 'https://leetcode.com/problems/sort-characters-by-frequency/'
# https://github.com/kamyu104/LeetCode/blob/master/Python/sort-characters-by-frequency.py
# Time:  O(n)
# Space: O(n)
#
# Description: Leetcode # 451. Sort Characters By Frequency
#
# Input:
# "tree"
#
# Output:
# "eert"
#
# Explanation:
# 'e' appears twice while 'r' and 't' both appear once.
# So 'e' must appear before both 'r' and 't'. Therefore "eetr" is also a valid answer.
# Example 2:
#
# Input:
# "cccaaa"
#
# Output:
# "cccaaa"
#
# Explanation:
# Both 'c' and 'a' appear three times, so "aaaccc" is also a valid answer.
# Note that "cacaca" is incorrect, as the same characters must be together.
# Example 3:
#
# Input:
# "Aabb"
#
# Output:
# "bbAa"
#
# Explanation:
# "bbaA" is also a valid answer, but "Aabb" is incorrect.
# Note that 'A' and 'a' are treated as two different characters.
import collections
import unittest

# 68ms 37.55%
class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        freq = collections.defaultdict(int)
        for c in s:
            freq[c] += 1

        counts = [""] * (len(s)+1)
        for c in freq:
            counts[freq[c]] += c

        result = ""
        for count in reversed(xrange(len(counts))):
            for c in counts[count]:
                result += c * count

        return result

class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)

if __name__ == '__main__':
    unittest.main()

Java = '''
# Thought:
Super simple O(n) Bucket Sort based Java solution (11 ms). No fancy Data structure needed. Beats 96%.
Could not find a simpler way to do this. I see people are using HashMap/TreeMap which are not at all required.
If you know bucket sort then following solution will be easy to understand!

# 28ms 64.93%
class Solution {
    public String frequencySort(String s) {
        Map<Character, Integer> map = new HashMap<>();
        for (char c : s.toCharArray()) {
            if (map.containsKey(c)) {
                map.put(c, map.get(c) + 1);
            } else {
                map.put(c, 1);
            }
        }
        
        PriorityQueue<Map.Entry<Character, Integer>> pq = new PriorityQueue<>(
            new Comparator<Map.Entry<Character, Integer>>(){
                @Override
                public int compare(Map.Entry<Character, Integer> a, Map.Entry<Character, Integer> b) {
                    return b.getValue() - a.getValue();
                }
            }
        );
        
        pq.addAll(map.entrySet());
        StringBuilder sb = new StringBuilder();
        while(!pq.isEmpty()) {
            Map.Entry e = pq.poll();
            for (int i = 0; i < (int) e.getValue(); i++) {
                sb.append(e.getKey());
            }
        }
        return sb.toString();
    }
}

Java O(n) Bucket Sort Solution / O(nlogn) PriorityQueue Solution, easy to understand
The logic is very similar to NO.347 and here we just use a map a count and according to the frequency
to put it into the right bucket.
Then we go through the bucket to get the most frequently character and append that to the final stringbuilder.

# 21ms 80.80%
class Solution {
    public String frequencySort(String s) {
        Map<Character, Integer> map = new HashMap<>();
        for (char c : s.toCharArray()) {
            if (map.containsKey(c)) {
                map.put(c, map.get(c) + 1);
            } else {
                map.put(c, 1);
            }
        }
        List<Character> [] bucket = new List[s.length() + 1];
        for (char key : map.keySet()) {
            int frequency = map.get(key);
            if (bucket[frequency] == null) {
                bucket[frequency] = new ArrayList<>();
            }
            bucket[frequency].add(key);
        }
        StringBuilder sb = new StringBuilder();
        for (int pos = bucket.length - 1; pos >=0; pos--) {
            if (bucket[pos] != null) {
                for (char num : bucket[pos]) {
                    for (int i = 0; i < map.get(num); i++) {
                        sb.append(num);
                    }
                }
            }
        }
        return sb.toString();
    }
}

And we have normal way using PriorityQueue as follows:

# 27ms 67.26%
class Solution {
    public String frequencySort(String s) {
        Map<Character, Integer> map = new HashMap<>();
        for (char c : s.toCharArray()) {
            if (map.containsKey(c)) {
                map.put(c, map.get(c) + 1);
            } else {
                map.put(c, 1);
            }
        }
        PriorityQueue<Map.Entry<Character, Integer>> pq = new PriorityQueue<>(
            new Comparator<Map.Entry<Character, Integer>>() {
                @Override
                public int compare(Map.Entry<Character, Integer> a, Map.Entry<Character, Integer> b) {
                    return b.getValue() - a.getValue();
                }
            }
        );
        pq.addAll(map.entrySet());
        StringBuilder sb = new StringBuilder();
        while (!pq.isEmpty()) {
            Map.Entry e = pq.poll();
            for (int i = 0; i < (int)e.getValue(); i++) {
                sb.append(e.getKey());
            }
        }
        return sb.toString();
    }
}

'''
