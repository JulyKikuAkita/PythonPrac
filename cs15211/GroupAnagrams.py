__source__ = 'https://leetcode.com/problems/group-anagrams/description/'
# https://github.com/kamyu104/LeetCode/blob/master/Python/anagrams.py
# Time:  O(n)
# Space: O(n)
# Hash table
#
# Given an array of strings, group anagrams together.
#
# For example, given: ["eat", "tea", "tan", "ate", "nat", "bat"],
# Return:
#
# [
#   ["ate", "eat","tea"],
#   ["nat","tan"],
#   ["bat"]
# ]
#
# Note: All inputs will be in lower-case.
#
#
# Companies
# Amazon Bloomberg Uber Facebook Yelp
# Related Topics
# Hash Table String
# Similar Questions
# Valid Anagram Group Shifted Strings
#
import collections
import unittest
class Solution:
    # @param strs, a list of strings
    # @return a list of strings
    def anagrams(self, strs):
        map = {}
        result = []
        for str in strs:
            # str is char array , use join to turn to str
            char = "".join(sorted(str))
            if map.has_key(char):
                map[char].append(str)
            else:
                map[char] = [str]
        for value in map.values():
            if len(value) > 1:
                result += value  # if use append, become [[value]]
        return result

class Solution2(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        if not strs:
            return []

        dict = collections.defaultdict(list)
        for str in strs:
            new_str = "".join(sorted(str))
            dict[new_str].append(str.lower())

        res= []
        for key in dict:
            res.append(sorted(dict[key]))

        return res

#test
class TestMethods(unittest.TestCase):
    def test_Local(self):
        test = Solution2()
        print test.anagrams(['abc','bac','acb', 'aaa', 'bbb','ccc'])
        result = Solution().anagrams(["cat", "dog", "act", "mac"])
        print result

if __name__ == '__main__':
    unittest.main()

Java = '''
#Thought: https://leetcode.com/problems/contains-duplicate/solution/
# http://www.programcreek.com/2014/04/leetcode-anagrams-java/

# If two strings are anagram to each other, their sorted sequence is the same.
# Therefore, this problem can be seen as a problem of finding duplicate elements.

# 38.72% 31ms
public class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        if (strs == null || strs.length == 0) return new ArrayList<List<String>>();
        Map<String, List<String>> map = new HashMap<String, List<String>>();
        for (String s : strs) {
            char[] ca = s.toCharArray();
            Arrays.sort(ca);
            String keyStr = String.valueOf(ca);
            if (!map.containsKey(keyStr)) map.put(keyStr, new ArrayList<String>());
            map.get(keyStr).add(s);
        }
        return new ArrayList<List<String>>(map.values());
    }
}

#45.85% 30ms
public class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        List<List<String>> result = new ArrayList<>();
        Map<String, List<String>> map = new HashMap<>();
        for (String str : strs) {
            String key = sort(str);
            if (!map.containsKey(key)) {
                map.put(key, new ArrayList<>());
            }
            map.get(key).add(str);
        }
        for (Map.Entry<String, List<String>> entry : map.entrySet()) {
            List<String> list = entry.getValue();
            Collections.sort(list);
            result.add(list);
        }
        return result;
    }

    private String sort(String str) {
        char[] arr = str.toCharArray();
        Arrays.sort(arr);
        return new String(arr);
    }
}

#94.05% 24ms
class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        int[] prime = {2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103};

        List<List<String>> list = new ArrayList<>();
        HashMap<Integer, Integer> map = new HashMap<>();

        for (String s : strs) {
            // generate hashcode
            int key = 1;
            for (char c : s.toCharArray())
                key *= prime[c-'a'];

            List<String> l = null;
            if (map.containsKey(key)) {
                l = list.get(map.get(key));
            } else {
                l = new ArrayList<>();
                list.add(l);
                map.put(key, list.size()-1);
            }
            l.add(s);
        }

        return list;
    }
}

'''