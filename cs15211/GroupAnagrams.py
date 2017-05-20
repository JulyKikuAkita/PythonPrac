__author__ = 'July'
# https://github.com/kamyu104/LeetCode/blob/master/Python/anagrams.py
# Time:  O(n)
# Space: O(n)
# Hash table
#
# Given an array of strings, return all groups of strings that are anagrams.
#
# Note: All inputs will be in lower-case.
#

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


if __name__ == "__main__":
    result = Solution().anagrams(["cat", "dog", "act", "mac"])
    print result

import collections
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
# Java
# http://www.programcreek.com/2014/04/leetcode-anagrams-java/

# If two strings are anagram to each other, their sorted sequence is the same.
# Therefore, this problem can be seen as a problem of finding duplicate elements.

#test
test = SolutionOther()
print test.anagrams(['abc','bac','acb', 'aaa', 'bbb','ccc'])

#java
js = '''
public class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
         List<List<String>> res = new ArrayList<List<String>>();
         if(strs == null || strs.length == 0){
             return res;
         }

         Map<String, List<String>> map = new HashMap<>();

         for(String str : strs){
             String key = getSorted(str);
             if(!map.containsKey(key)){
                 map.put(key, new ArrayList<>());
             }
             map.get(key).add(str);
         }

         // java 8
         /*
         map.forEach((k,v) -> Collections.sort(v)) ;
         map.forEach((k,v) -> res.add(v)) ;
         */

         //KeySet
         /*
         for(String k : map.keySet()){
             List<String> val = map.get(k);
             Collections.sort(val);
             res.add(val);
         }
         */

         //Values
         /*
         for(List<String> val : map.values()){
             Collections.sort(val);
             res.add(val);
         }
         */

         //EntrySet
         for(Map.Entry<String, List<String>> entry : map.entrySet()){
             List<String> val = entry.getValue();
             Collections.sort(val);
             res.add(val);
         }
        return res;
    }
    private String getSorted(String str){
        char[] chars = str.toCharArray();
        Arrays.sort(chars);
        return new String(chars);
    }

}
'''