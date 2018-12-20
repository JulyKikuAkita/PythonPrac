__source__ = 'https://leetcode.com/problems/length-of-last-word/'
# https://github.com/kamyu104/LeetCode/blob/master/Python/length-of-last-word.py
# Time:  O(n)
# Space: O(1)
# String
#
# Description: Leetcode # 58. Length of Last Word
#
# Given a string s consists of upper/lower-case alphabets and empty space characters ' ',
# return the length of last word in the string.
#
# If the last word does not exist, return 0.
#
# Note: A word is defined as a character sequence consists of non-space characters only.
#
# For example,
# Given s = "Hello World",
# return 5.
# Related Topics
# String
#
import unittest
class Solution:
    # @param s, a string
    # @return an integer
    def lengthOfLastWord(self, s):
        length = 0
        for i in reversed(s):
            if i == ' ':
                if length:
                    break
            else:
                length += 1
        return length

# Time:  O(n)
# Space: O(n)
class Solution2:
    # @param s, a string
    # @return an integer
    def lengthOfLastWord(self, s):
        return len(s.strip().split(" ")[-1])


if __name__ == "__main__":
    print Solution().lengthOfLastWord("Hello World ")
    print Solution2().lengthOfLastWord("")

class SolutionOther:
    # @param s, a string
    # @return an integer
    def lengthOfLastWord(self, s):
        if s == "" or s == None or s.isspace():
            return 0

        lastword= s.split()[::-1][0]
        return len(lastword)

class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)
        t1=SolutionOther()
        #print t1.lengthOfLastWord("Hello World")
        #print t1.lengthOfLastWord("")
        #print t1.lengthOfLastWord("    ")

if __name__ == '__main__':
    unittest.main()

Java = '''
# Thought:

# 3ms 84.50%
class Solution {
    public int lengthOfLastWord(String s) {
        return s.trim().length()-s.trim().lastIndexOf(" ")-1;
    }
}


# 2ms 100%
class Solution {
    public int lengthOfLastWord(String s) {
        int start = 0;
        int end = s.length() - 1;
        while (end >= 0 && s.charAt(end) == ' ') {
            end--;
        }
        if (end < 0) {
            return 0;
        }
        start = end - 1;
        while (start >= 0 && s.charAt(start) != ' ') {
            start--;
        }
        return end - start;
    }
}

# 2ms 100%
class Solution {
    public int lengthOfLastWord(String s) {
        s=s.trim();
        if(s.length()==0)
            return 0;
        int r=0;
        for(int i=s.length()-1;i>=0;i--){
            if(s.charAt(i)==' ')
                break;
            r++;
            
        }
        
        return r;
    }
}
'''
