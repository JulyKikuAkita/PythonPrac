__source__ = 'https://leetcode.com/problems/longest-common-prefix/description/'
# https://github.com/kamyu104/LeetCode/blob/master/Python/longest-common-prefix.py
# Time:  O(n * k), k is the length of the common prefix
# Space: O(1)
# Description: 14. Longest Common Prefix
# Write a function to find the longest common prefix string
# amongst an array of strings.
#
# Companies
# Yelp
# Related Topics
# String
#
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


if __name__ == "__main__":
    print Solution().longestCommonPrefix(["hello", "heaven", "heavy"])


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
test = SolutionOther()
str = ['panda', 'panda', "giana"]
str1 = ["aba","abc"]
str2 = ["aba","a"]

print  test.longestCommonPrefix(str1)
print  test.longestCommonPrefix(str2)


#Java
Java = '''
Thought: https://leetcode.com/problems/longest-common-prefix/solution/
Approach #1 (Horizontal scanning)
# 89.41% 9ms
public class Solution {
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

# 43.13% 12ms
public class Solution {
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

#59.86% 11ms
public class Solution {
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
# 29.70%  13ms
public class Solution {
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
'''