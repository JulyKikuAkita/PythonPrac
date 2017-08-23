__source__ = 'https://leetcode.com/problems/group-shifted-strings/description/'
# https://github.com/kamyu104/LeetCode/blob/master/Python/group-shifted-strings.py
# Time:  O(nlogn)
# Space: O(n)
#
# Description: Leetcode # 249. Group Shifted Strings
#
# Given a string, we can "shift" each of its letter to its successive letter, for example: "abc" -> "bcd".
# We can keep "shifting" which forms the sequence:
#
# "abc" -> "bcd" -> ... -> "xyz"
# Given a list of strings which contains only lowercase alphabets,
# group all strings that belong to the same shifting sequence.
#
# For example, given: ["abc", "bcd", "acef", "xyz", "az", "ba", "a", "z"],
# Return:
#
# [
#   ["abc","bcd","xyz"],
#   ["az","ba"],
#   ["acef"],
#   ["a","z"]
# ]
# Note: For the return value, each inner list's elements must follow the lexicographic order.
#
# Companies
# Google Uber
# Related Topics
# Hash Table String
# Similar Questions
# Group Anagrams
#
import unittest
import collections
class Solution:
    # @param {string[]} strings
    # @return {string[][]}
    def groupStrings(self, strings):
        groups = {};
        for s in strings: #Grouping
            if self.hashStr(s) not in groups:
                groups[self.hashStr(s)] = [s]
            else:
                groups[self.hashStr(s)].append(s)
        result = []
        for key, val in groups.iteritems():
            result.append(sorted(val))
        return result

    def hashStr(self, s):
        base = ord(s[0])
        hashcode = ""
        for i in xrange(len(s)):
            #if ord(s[i]) - base >= 0:
            #    hashcode += unichr(ord('a') + ord(s[i]) - base)
            #else:
            hashcode += unichr(ord('a') + ((ord(s[i]) - base + 26) % 26))
        return hashcode

class Solution2(object):
    def groupStrings(self, strings):
        """
        :type strings: List[str]
        :rtype: List[List[str]]
        """
        d = collections.defaultdict(list)
        for s in strings:
            shift = tuple([(ord(c) - ord(s[0])) % 26 for c in s])
            d[shift].append(s)

        return map(sorted, d.values())

# TEST
class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)
        in1 = \
        ["abc", "txb", "def" , "i", \
        "d", "nw", "e", "g", "h"]
        print Solution().groupStrings(in1)

if __name__ == '__main__':
    unittest.main()

Java = '''
#Thought:
The basic idea is to set a key for each group:
the sum of the difference between the adjacent chars in one string.
Then we can easily group the strings belonging to the same shifting sequence with the same key.

#1.06% 101ms
public class Solution {
    public List<List<String>> groupStrings(String[] strings) {
        return new ArrayList(Stream.of(strings).collect(Collectors.groupingBy(
            s -> s.chars().mapToObj(c -> (c - s.charAt(0) + 26) % 26)
                  .collect(Collectors.toList())
        )).values());
    }
}

#4.49% 72ms
class Solution {
    public List<List<String>> groupStrings(String[] strs) {
        HashMap<String, ArrayList<String>> map = new HashMap<String, ArrayList<String>>();
        Arrays.sort(strs);
        for (String s : strs) {
            String key = "";
            for (int i = 1; i < s.length(); i++)
                key += String.format("%2d", (s.charAt(i) - s.charAt(i-1) + 26) % 26);//Difference from the previous char.
            if (!map.containsKey(key)) map.put(key, new ArrayList<String>());
            map.get(key).add(s);
        }
        return new ArrayList<List<String>>(map.values());
    }
}

# 98.42%
class Solution {
    public List<List<String>> groupStrings(String[] strings) {
        List<List<String>> result = new ArrayList<>();
        Map<String, List<String>> map = new HashMap<>();

        for (int j = 0; j < strings.length; j++) {
            char[] arr = strings[j].toCharArray();
            int difference = arr[0] - 'a';
            arr[0] = 'a';

            for (int i = 1; i < arr.length; i++) {
                if (arr[i] - difference - 'a' > 0) {
                    arr[i] = (char)(arr[i] - difference);
                } else {
                    int diff = arr[i] - difference - 'a' + 1;
                    arr[i] = (char)('z' + diff);
                }
            }

            String normalized = new String(arr);

            if (map.containsKey(normalized)) {
                map.get(normalized).add(strings[j]);
            } else {
                List<String> list = new ArrayList<>();
                list.add(strings[j]);
                result.add(list);
                map.put(normalized, list);
            }
        }

        return result;
    }
}
'''