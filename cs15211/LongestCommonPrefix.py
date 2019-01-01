__source__ = 'https://leetcode.com/problems/longest-common-prefix/'
# https://github.com/kamyu104/LeetCode/blob/master/Python/longest-common-prefix.py
# Time:  O(n * k), k is the length of the common prefix
# Space: O(1)
#
# Description: Leetcode # 14. Longest Common Prefix
#
# Write a function to find the longest common prefix string
# amongst an array of strings.
#
# Companies
# Yelp
# Related Topics
# String
#
import unittest
class Solution:
    # @return a string
    def longestCommonPrefix(self, strs):
        if not strs:
            return ""
        longest = strs[0]
        for string in strs[1:]:
            i = 0
            while i < len(string) and i < len(longest) and string[i] == longest[i]:
                i += 1
            longest = longest[:i]
        return longest

class SolutionOther:
    # @return a string
    def longestCommonPrefix(self, strs):

        if len(strs) <=1:
            return strs[0] if len(strs) == 1 else ""
        end, minstrl =0, min([len(s) for s in strs])
        #print "minstrl =" ,minstrl ,strs, len(strs), strs[0]

        while end < minstrl:
            for i in range(1, len(strs)):
                #print i, end, "answer =" , strs[0][:end]
                if strs[i][end] != strs[i-1][end]:
                    return strs[0][:end]
            end = end +1

        return strs[0][:end]

    def longestCommonPrefix2(self, strs):
        len_strs = len(strs)
        if len_strs == 0:
            return ''
        if len_strs == 1:
            return strs[0]
        lengths = [len(i) for i in strs]
        common_prefix = ''
        for i in xrange(min(lengths)):
            tmp = strs[0][i]
            for j in xrange(1,len_strs):
                if strs[j][i] != tmp:
                    return common_prefix
            common_prefix += tmp
        return common_prefix

#test
class TestMethods(unittest.TestCase):
    def test_Local(self):
        test = SolutionOther()
        str = ['panda', 'panda', "giana"]
        str1 = ["aba","abc"]
        str2 = ["aba","a"]
        print  test.longestCommonPrefix(str1)
        print  test.longestCommonPrefix(str2)
        print Solution().longestCommonPrefix(["hello", "heaven", "heavy"])

if __name__ == '__main__':
    unittest.main()

Java = '''
# Thought: https://leetcode.com/problems/longest-common-prefix/solution/

# 3ms 100%
class Solution {
    public String longestCommonPrefix(String[] strs) {
        if (strs.length == 0) return "";
        String candidate = strs[0];
        for (int i = 1; i < strs.length; i++) {
            while (!strs[i].startsWith(candidate)) {
                candidate = candidate.substring(0, candidate.length() - 1);
            }
        }
        return candidate;
    }
}

Approach #1 (Horizontal scanning)
# 4ms 99.82%
class Solution {
    public String longestCommonPrefix(String[] strs) {
        if(strs == null || strs.length == 0)    return "";
        String pre = strs[0];
        int i = 1;
        while(i < strs.length){
            while(strs[i].indexOf(pre) != 0)
                pre = pre.substring(0,pre.length()-1);
            i++;
        }
        return pre;
    }
}

# 5ms 90.07%
class Solution {
    public String longestCommonPrefix(String[] strs) {
        if (strs == null || strs.length == 0 ) return "";
        int prefix = strs[0].length();
        String base = strs[0];
        int start = 1;
        int end = strs.length -1;
        while(start <= end){
            prefix = getPrefix(strs[start], base, prefix);
            start ++;
        }
        return base.substring( 0, prefix);
    }

    private int getPrefix(String base, String cur , int prefix){
        prefix = Math.min(prefix, Math.min(base.length(), cur.length()));
        for(int i = 0; i < prefix ; i++){
            if(base.charAt(i) != cur.charAt(i)){
                return i;
            }
        }
        return prefix;
    }
}

Approach #3 (Divide and conquer)
# 9ms 29.45%
class Solution {
    public String longestCommonPrefix(String[] strs) {
        if (strs == null || strs.length == 0) return "";
        return longestCommonPrefix(strs, 0 , strs.length - 1);
    }

    private String longestCommonPrefix(String[] strs, int l, int r) {
        if (l == r) {
            return strs[l];
        }
        else {
            int mid = (l + r)/2;
            String lcpLeft =   longestCommonPrefix(strs, l , mid);
            String lcpRight =  longestCommonPrefix(strs, mid + 1,r);
            return commonPrefix(lcpLeft, lcpRight);
       }
    }

    String commonPrefix(String left,String right) {
        int min = Math.min(left.length(), right.length());
        for (int i = 0; i < min; i++) {
            if ( left.charAt(i) != right.charAt(i) )
                return left.substring(0, i);
        }
        return left.substring(0, min);
    }

}

# Approach 4: Binary search
# 8ms 46.78%
class Solution {
    public String longestCommonPrefix(String[] strs) {
        if (strs == null || strs.length == 0)
            return "";
        int minLen = Integer.MAX_VALUE;
        for (String str : strs)
            minLen = Math.min(minLen, str.length());
        int low = 1;
        int high = minLen;
        while (low <= high) {
            int middle = (low + high) / 2;
            if (isCommonPrefix(strs, middle))
                low = middle + 1;
            else
                high = middle - 1;
        }
        return strs[0].substring(0, (low + high) / 2);
    }

    private boolean isCommonPrefix(String[] strs, int len){
        String str1 = strs[0].substring(0,len);
        for (int i = 1; i < strs.length; i++)
            if (!strs[i].startsWith(str1))
                return false;
        return true;
    }
}

# 4ms 99.82%
class Solution {
    public String longestCommonPrefix(String[] strs) {
        if (strs.length == 0) {
            return "";
        }
        int minLength = getMinLength(strs);
        for (int i = 0; i < minLength; i++) {
            char c = strs[0].charAt(i);
            for (int j = 1; j < strs.length; j++) {
                if (strs[j].charAt(i) != c) {
                    return strs[0].substring(0, i);
                }
            }
        }
        return strs[0].substring(0, minLength);
    }
    
    private int getMinLength(String[] strs) {
        int result = Integer.MAX_VALUE;
        for (int i = 0; i < strs.length; i++) {
            result = Math.min(result, strs[i].length());
        }
        return result;
    }
}
'''
