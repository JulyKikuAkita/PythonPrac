__source__ = 'https://leetcode.com/problems/valid-palindrome/#/description'
# https://github.com/kamyu104/LeetCode/blob/master/Python/valid-palindrome.py
# Time:  O(n)
# Space: O(1)
# String
#
# Description: Leetcode # 125. Valid Palindrome
# Given a string, determine if it is a palindrome,
# considering only alphanumeric characters and ignoring cases.
#
# For example,
# "A man, a plan, a canal: Panama" is a palindrome.
# "race a car" is not a palindrome.
#
# Note:
# Have you consider that the string might be empty? This is a good question to ask during an interview.
#
# For the purpose of this problem, we define empty string as valid palindrome.
# Companies
# Microsoft Uber Facebook Zenefits
# Related Topics
# Two Pointers String
# Similar Questions
#
import unittest
class Solution:
    # @param s, a string
    # @return a boolean
    def isPalindrome(self, s):
        i, j = 0, len(s) - 1
        while i < j:
            while i < j and not (s[i].isalnum()):
                i += 1
            while i < j and not (s[j].isalnum()):
                j -= 1
            if s[i].lower() != s[j].lower():
                return False
            i, j = i+1, j-1
        return True

class SolutionOther:
    # @param s, a string
    # @return a boolean
    def isPalindrome(self, s):
        text = [x.lower() for x in s if x.isalpha() or x.isdigit()]
        revtext = text[::-1]
        num = len(text)
        #print revtext
        if num == 0:
            return True
        else:
            if num % 2 == 0:
                for i in range(num/2) :
                    if text[i] != revtext[i]:
                        return False
                else:
                    return True
            else:
                for i in range((num-1)/2) :
                    if text[i] != revtext[i]:
                        #print text[num-1-i]
                        return False
                else:
                    return True

# test
class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)
        t1 = Solution()
        #print t1.isPalindrome("A man, a plan, a canal: Panama")
        #print t1.isPalindrome("race a car")
        #print  t1.isPalindrome("a.")
        #print  t1.isPalindrome(".,")
        #print  t1.isPalindrome("......a.....")
        print  t1.isPalindrome("1a2")
        print Solution().isPalindrome("A man, a plan, a canal: Panama")

if __name__ == '__main__':
    unittest.main()

Java = '''
#Thought:
#11.24% 35ms
public class Solution {
    public boolean isPalindrome(String s) {
        String actual = s.replaceAll("[^A-Za-z0-9]", "").toLowerCase();
        String rev = new StringBuilder(actual).reverse().toString();
        return actual.equals(rev);
    }
}

#35.72% 12ms
public class Solution {
    public boolean isPalindrome(String s) {
        //if (s == null || s.length() == 0) return true;
        int start = 0, end = s.length() - 1;
        s = s.toLowerCase();
        while (start < end) {
            while (start < end && !Character.isLetterOrDigit(s.charAt(start))) start++;
            while (start < end && !Character.isLetterOrDigit(s.charAt(end))) end--;
            if (start < end && s.charAt(start) != s.charAt(end)) return false;
            start++;
            end--;
        }
        return true;
    }
}

#87.90% 7ms
public class Solution {
    public boolean isPalindrome(String s) {
        if (s.isEmpty()) {
        	return true;
        }
        int head = 0, tail = s.length() - 1;
        char cHead, cTail;
        while(head <= tail) {
        	cHead = s.charAt(head);
        	cTail = s.charAt(tail);
        	if (!Character.isLetterOrDigit(cHead)) {
        		head++;
        	} else if(!Character.isLetterOrDigit(cTail)) {
        		tail--;
        	} else {
        		if (Character.toLowerCase(cHead) != Character.toLowerCase(cTail)) {
        			return false;
        		}
        		head++;
        		tail--;
        	}
        }

        return true;
    }
}

#87.90% 7ms
public class Solution {
    public boolean isPalindrome(String s) {
        int i = 0;
        int j = s.length() - 1;
        while (i < j) {
            while (i < j && !isAlpha(s.charAt(i)) && !isNumeric(s.charAt(i))) {
                i++;
            }
            while (i < j && !isAlpha(s.charAt(j)) && !isNumeric(s.charAt(j))) {
                j--;
            }
            if (i < j && !isEqual(s.charAt(i), s.charAt(j))) {
                return false;
            }
            i++;
            j--;
        }
        return true;
    }

    private boolean isAlpha(char c) {
        return (c >= 'A' && c <= 'Z') || (c >= 'a' && c <= 'z');
    }

    private boolean isNumeric(char c) {
        return (c >= '0' && c <= '9');
    }

    private boolean isEqual(char a, char b) {
        if (isAlpha(a) && isAlpha(b)) {
            return toLowerCase(a) == toLowerCase(b);
        } else {
            return a == b;
        }
    }

    private char toLowerCase(char c) {
        if (c >= 'A' && c <= 'Z') {
            return (char) ('a' + (c - 'A'));
        } else {
            return c;
        }
    }
}

'''