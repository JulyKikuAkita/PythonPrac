__source__ = 'https://leetcode.com/problems/tag-validator/'
# Time:  O()
# Space: O()
# Link to check regex:
# http://regexr.com/
#
# Description: 591. Tag Validator
#
# Given a string representing a code snippet, you need to implement a tag validator to parse the code and
# return whether it is valid. A code snippet is valid if all the following rules hold:
#
# The code must be wrapped in a valid closed tag. Otherwise, the code is invalid.
# A closed tag (not necessarily valid) has exactly the following format : <TAG_NAME>TAG_CONTENT</TAG_NAME>.
#  Among them, <TAG_NAME> is the start tag, and </TAG_NAME> is the end tag.
# The TAG_NAME in start and end tags should be the same.
# A closed tag is valid if and only if the TAG_NAME and TAG_CONTENT are valid.
# A valid TAG_NAME only contain upper-case letters, and has length in range [1,9]. Otherwise, the TAG_NAME is invalid.
# A valid TAG_CONTENT may contain other valid closed tags, cdata and any characters (see note1)
# EXCEPT unmatched <, unmatched start and end tag, and unmatched or closed tags with invalid TAG_NAME.
# Otherwise, the TAG_CONTENT is invalid.
# A start tag is unmatched if no end tag exists with the same TAG_NAME, and vice versa.
# However, you also need to consider the issue of unbalanced when tags are nested.
# A < is unmatched if you cannot find a subsequent >. And when you find a < or </,
# all the subsequent characters until the next > should be parsed as TAG_NAME (not necessarily valid).
# The cdata has the following format : <![CDATA[CDATA_CONTENT]]>.
# The range of CDATA_CONTENT is defined as the characters between <![CDATA[ and the first subsequent ]]>.
# CDATA_CONTENT may contain any characters. The function of cdata is to forbid the validator to parse CDATA_CONTENT,
# so even it has some characters that can be parsed as tag (no matter valid or invalid),
# you should treat it as regular characters.

# Valid Code Examples:
# Input: "<DIV>This is the first line <![CDATA[<div>]]></DIV>"
#
# Output: True
#
# Explanation:
#
# The code is wrapped in a closed tag : <DIV> and </DIV>.
#
# The TAG_NAME is valid, the TAG_CONTENT consists of some characters and cdata.
#
# Although CDATA_CONTENT has unmatched start tag with invalid TAG_NAME, it should be considered as plain text, not parsed as tag.
#
# So TAG_CONTENT is valid, and then the code is valid. Thus return true.
#
#
# Input: "<DIV>>>  ![cdata[]] <![CDATA[<div>]>]]>]]>>]</DIV>"
#
# Output: True
#
# Explanation:
#
# We first separate the code into : start_tag|tag_content|end_tag.
#
# start_tag -> "<DIV>"
#
# end_tag -> "</DIV>"
#
# tag_content could also be separated into : text1|cdata|text2.
#
# text1 -> ">>  ![cdata[]] "
#
# cdata -> "<![CDATA[<div>]>]]>", where the CDATA_CONTENT is "<div>]>"
#
# text2 -> "]]>>]"
#
#
# The reason why start_tag is NOT "<DIV>>>" is because of the rule 6.
# The reason why cdata is NOT "<![CDATA[<div>]>]]>]]>" is because of the rule 7.
# Invalid Code Examples:
# Input: "<A>  <B> </A>   </B>"
# Output: False
# Explanation: Unbalanced. If "<A>" is closed, then "<B>" must be unmatched, and vice versa.
#
# Input: "<DIV>  div tag is not closed  <DIV>"
# Output: False
#
# Input: "<DIV>  unmatched <  </DIV>"
# Output: False
#
# Input: "<DIV> closed tags with invalid tag name  <b>123</b> </DIV>"
# Output: False
#
# Input: "<DIV> unmatched tags with invalid tag name  </1234567890> and <CDATA[[]]>  </DIV>"
# Output: False
#
# Input: "<DIV>  unmatched start tag <B>  and unmatched end tag </C>  </DIV>"
# Output: False
# Note:
# For simplicity, you could assume the input code (including the any characters mentioned above) only contain letters, digits, '<','>','/','!','[',']' and ' '.
# Show Company Tags
# Show Tags
# Show Similar Problems
# Note:
# For simplicity, you could assume the input code (including the any characters mentioned above)
# only contain letters, digits, '<','>','/','!','[',']' and ' '.
# Hide Company Tags Microsoft
# Hide Tags String Stack
# Hide Similar Problems (M) Add Bold Tag in String
#

# It does get accepted (in about 90 ms), though I'm not entirely sure it's correct
# because I didn't think it through because I don't find the description clear.
# Anyway... first I replace any CDATA with c.
# Then repeatedly replace any tags not containing < with t. I return whether I end up with 't'.
import unittest
import re
# 24ms 100%
class Solution(object):
    def isValid(self, code):
        """
        :type code: str
        :rtype: bool
        """
        code = re.sub(r'<!\[CDATA\[.*?\]\]>|t', '-', code)
        prev = None
        while code != prev:
            prev = code
            code = re.sub(r'<([A-Z]{1,9})>[^<]*</\1>', 't', code)
        return code == 't'

class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)


if __name__ == '__main__':
    unittest.main()

Java = '''
# Thought: https://leetcode.com/problems/tag-validator/solution/

https://discuss.leetcode.com/topic/91381/short-python-accepted-but-not-sure-if-correct
Inspired by @StefanPochmann 's idea in this post https://discuss.leetcode.com/topic/91381/short-python-accepted-but-not-sure-if-correct

Only change is in Java we need to use double \ to quote a special character.

Two brilliant points:

Use Non Greedy mode (.*?) when matching CDATA. Reference: https://stackoverflow.com/questions/3075130/what-is-the-difference-between-and-regular-expressions
Use Group (([A-Z]{1,9}) then \\1) when matching TAG_NAME. Reference: http://www.regular-expressions.info/refcapture.html

1. Stack
# 13ms 55.22%
class Solution {
    public boolean isValid(String code) {
        Stack<String> stack = new Stack<>();
        for(int i = 0; i < code.length();){
            if(i>0 && stack.isEmpty()) return false;
            if(code.startsWith("<![CDATA[", i)){
                int j = i+9;
                i = code.indexOf("]]>", j);
                if(i < 0) return false;
                i += 3;
            }else if(code.startsWith("</", i)){
                int j = i + 2;
                i = code.indexOf('>', j);
                if(i < 0 || i == j || i - j > 9) return false;
                for(int k = j; k < i; k++){
                    if(!Character.isUpperCase(code.charAt(k))) return false;
                }
                String s = code.substring(j, i++);
                if(stack.isEmpty() || !stack.pop().equals(s)) return false;
            }else if(code.startsWith("<", i)){
                int j = i + 1;
                i = code.indexOf('>', j);
                if(i < 0 || i == j || i - j > 9) return false;
                for(int k = j; k < i; k++){
                    if(!Character.isUpperCase(code.charAt(k))) return false;
                }
                String s = code.substring(j, i++);
                stack.push(s);
            }else{
                i++;
            }
        }
        return stack.isEmpty();
    }
}


2. Regex:
# 25ms 14.93%
class Solution {
    public boolean isValid(String code) {
        if (code.equals("t")) return false;
        code = code.replaceAll("<!\\[CDATA\\[.*?\\]\\]>", "c");

        String prev = "";
        while(!code.equals(prev)) {
            prev = code;
            code = code.replaceAll("<([A-Z]{1,9})>[^<]*</\\1>", "t");
        }
        return code.equals("t");
    }
}

'''