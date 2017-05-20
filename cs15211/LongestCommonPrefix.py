__author__ = 'July'
# https://github.com/kamyu104/LeetCode/blob/master/Python/longest-common-prefix.py
# Time:  O(n1 + n2 + ...)
# Space: O(1)
# String
#
# Write a function to find the longest common prefix string amongst an array of strings.
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


#java
js = '''
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

public class Solution {
    public String longestCommonPrefix(String[] strs) {
        if (strs.length == 0) {
            return "";
        }
        StringBuilder sb = new StringBuilder();
        int index = 0;
        while (true) {
            if (index == strs[0].length()) {
                return sb.toString();
            }
            char c = strs[0].charAt(index);
            for (int i = 1; i < strs.length; i++) {
                if (index == strs[i].length() || strs[i].charAt(index) != c) {
                    return sb.toString();
                }
            }
            sb.append(c);
            index++;
        }
    }
}
'''