__author__ = 'July'

# https://github.com/kamyu104/LeetCode/blob/master/Python/rearrange-string-k-distance-apart.py
# Time:  O(n)
# Space: O(n)

'''
Given a non-empty string str and an integer k, rearrange the string such that the same characters are at least distance k from each other.

All input strings are given in lowercase letters. If it is not possible to rearrange the string, return an empty string "".

Example 1:
str = "aabbcc", k = 3

Result: "abcabc"

The same letters are at least distance 3 from each other.
Example 2:
str = "aaabc", k = 3

Answer: ""

It is not possible to rearrange the string.
Example 3:
str = "aaadbbcc", k = 2

Answer: "abacabcd"

Another possible answer is: "abcabcda"

The same letters are at least distance 2 from each other.
Credits:
Special thanks to @elmirap for adding this problem and creating all test cases.

Hide Company Tags Google
Hide Tags Hash Table Heap Greedy
'''


class Solution(object):
    def rearrangeString(self, str, k):
        """
        :type str: str
        :type k: int
        :rtype: str
        """
        cnts = [0] * 26;
        for c in str:
            cnts[ord(c) - ord('a')] += 1

        sorted_cnts = []
        for i in xrange(26):
            sorted_cnts.append((cnts[i], chr(i + ord('a'))))
        sorted_cnts.sort(reverse=True)

        max_cnt = sorted_cnts[0][0]
        blocks = [[] for _ in xrange(max_cnt)]
        i = 0
        for cnt in sorted_cnts:
            for _ in xrange(cnt[0]):
                blocks[i].append(cnt[1])
                i = (i + 1) % max(cnt[0], max_cnt - 1)

        for i in xrange(max_cnt-1):
            if len(blocks[i]) < k:
                return ""

        return "".join(map(lambda x : "".join(x), blocks))


# Time:  O(nlogc), c is the count of unique characters.
# Space: O(c)
from collections import defaultdict
from heapq import heappush, heappop
class Solution2(object):
    def rearrangeString(self, str, k):
        """
        :type str: str
        :type k: int
        :rtype: str
        """
        if k == 0:
            return str

        cnts = defaultdict(int)
        for c in str:
            cnts[c] += 1

        heap = []
        for c, cnt in cnts.iteritems():
            heappush(heap, [-cnt, c])

        result = []
        while heap:
            used_cnt_chars = []
            for _ in xrange(min(k, len(str) - len(result))):
                if not heap:
                    return ""
                cnt_char = heappop(heap)
                result.append(cnt_char[1])
                cnt_char[0] += 1
                if cnt_char[0] < 0:
                    used_cnt_chars.append(cnt_char)
            for cnt_char in used_cnt_chars:
                heappush(heap, cnt_char)

        return "".join(result)


# java
js = '''
1. 16 ms
import java.util.SortedMap;

public class Solution {
    public String rearrangeString(String str, int k) {
        if (str.length() < 2 || k <= 1) {
            return str;
        }
        StringBuilder sb = new StringBuilder();
        SortedMap<Integer, List<Character>> map = new TreeMap<>(Collections.reverseOrder());
        int[] lastIndex = new int[26];

        buildMap(map, str);
        Arrays.fill(lastIndex, -1);
        for (int i = 0; i < str.length(); i++) {
            boolean found = false;
            Set<Integer> keySet = map.keySet();
            Iterator<Integer> iter = keySet.iterator();
            while (iter.hasNext() && !found) {
                int key = iter.next();
                List<Character> list = map.get(key);
                for (char c : list) {
                    int index = c - 'a';
                    if (lastIndex[index] == -1 || lastIndex[index] <= i - k) {
                        sb.append(c);
                        list.remove(Character.valueOf(c));
                        if (list.isEmpty()) {
                            map.remove(key);
                        }
                        if (key > 1) {
                            if (!map.containsKey(key - 1)) {
                                map.put(key - 1, new ArrayList<>());
                            }
                            map.get(key - 1).add(c);
                        }
                        lastIndex[index] = i;
                        found = true;
                        break;
                    }
                }
            }
            if (!found) {
                return "";
            }
        }
        return sb.toString();
    }

    private void buildMap(SortedMap<Integer, List<Character>> map, String str) {
        int[] count = new int[26];
        for (int i = 0; i < str.length(); i++) {
            count[str.charAt(i) - 'a']++;
        }
        for (int i = 0; i < count.length; i++) {
            if (count[i] > 0) {
                if (!map.containsKey(count[i])) {
                    map.put(count[i], new ArrayList<>());
                }
                map.get(count[i]).add((char) (i + 'a'));
            }
        }
    }
}

2. 117 ms

import java.util.SortedMap;

public class Solution {
    public String rearrangeString(String str, int k) {
        if (str.length() < 2 || k <= 1) {
            return str;
        }
        StringBuilder sb = new StringBuilder();
        SortedMap<Integer, List<Character>> map = new TreeMap<>(Collections.reverseOrder());
        int[] lastIndex = new int[26];

        buildMap(map, str);
        Arrays.fill(lastIndex, -1);
        for (int i = 0; i < str.length(); i++) {
            boolean found = false;
            Set<Integer> keySet = map.keySet();
            Iterator<Integer> iter = keySet.iterator();
            while (iter.hasNext() && !found) {
                int key = iter.next();
                List<Character> list = map.get(key);
                for (char c : list) {
                    int index = c - 'a';
                    if (lastIndex[index] == -1 || lastIndex[index] <= i - k) {
                        sb.append(c);
                        list.remove(Character.valueOf(c));
                        if (list.isEmpty()) {
                            map.remove(key);
                        }
                        if (key > 1) {
                            if (!map.containsKey(key - 1)) {
                                map.put(key - 1, new ArrayList<>());
                            }
                            map.get(key - 1).add(c);
                        }
                        lastIndex[index] = i;
                        found = true;
                        break;
                    }
                }
            }
            if (!found) {
                return "";
            }
        }
        return sb.toString();
    }

    private void buildMap(SortedMap<Integer, List<Character>> map, String str) {
        int[] count = new int[26];
        for (int i = 0; i < str.length(); i++) {
            count[str.charAt(i) - 'a']++;
        }
        for (int i = 0; i < count.length; i++) {
            if (count[i] > 0) {
                if (!map.containsKey(count[i])) {
                    map.put(count[i], new ArrayList<>());
                }
                map.get(count[i]).add((char) (i + 'a'));
            }
        }
    }
}

'''