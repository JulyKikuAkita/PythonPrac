__source__ = 'https://leetcode.com/problems/reverse-words-in-a-string/#/description'
# https://github.com/kamyu104/LeetCode/blob/master/Python/reverse-words-in-a-string.py
# Time:  O(n)
# Space: O(n)
# String
#
# Description: Leetcode # 151. Reverse Words in a String
#
# Given an input string, reverse the string word by word.
#
# For example,
# Given s = "the sky is blue",
# return "blue is sky the".
#
# click to show clarification.
#
# Clarification:
# What constitutes a word?
# A sequence of non-space characters constitutes a word.
# Could the input string contain leading or trailing spaces?
# Yes. However, your reversed string should not contain leading or trailing spaces.
# How about multiple spaces between two words?
# Reduce them to a single space in the reversed string.
#
# Companies
# Microsoft Snapchat Apple Bloomberg Yelp
# Related Topics
# String
# Similar Questions
# Reverse Words in a String II
#
import unittest
class Solution:
    # @param s, a string
    # @return a string
    def reverseWords(self, s):
        #print s.split()[::-1] # return string list -> join to string
        return ' '.join(reversed(s.split())) #reversed have no return

#testobj.reverse2Words("the sky is blue")
#testobj.reverse2Words(" works, but  why it   fails ")
#test
class Test(unittest.TestCase):
    def test(self):
        s1 = " works, but  why it   fails "
        s2 = "abc ef"
        s3 = "the sky is blue"
        self.assertEqual(Solution().reverseWords(s3), "blue is sky the")
        self.assertEqual(Solution().reverseWords(s1), "fails it why but works,")
if __name__ == '__main__':
    print Solution().reverseWords("Hello World!")

# Write a function reverse the words in a string
# eg: "Today is Tuesday"
# returns : "yadoT si yadseuT"
class SalesForceTest(unittest.TestCase):
    def reverse(self, s):
        if not s:
            return None
        arr = s.split()
        tmp = []
        for w in arr:
            tmp.append(w[::-1])
        return " ".join(tmp)

    def test(self):
        t1 = "Today is Tuesday"
        t2 = "yadoT si yadseuT"
        self.assertEqual(self.reverse(t1), t2, "Test1")
        self.assertEqual(self.reverse(t2), t1, "Test2")

#Java
#inplace
Java = '''
Thought:

// use collections
# 44.03% 10ms
public class Solution {
    public String reverseWords(String s) {
        String[] parts = s.trim().split("\\s+");
        Collections.reverse(Arrays.asList(parts));
        return String.join(" ", parts);
    }
}

#99.64% 2ms
public class Solution {
    public String reverseWords(String s) {
        s = s.trim();
        if (s.length()==0) return s;
        String[] words = s.split(" ");
        StringBuilder sb = new StringBuilder();
        for(int i = words.length-1;i>=0;i--){
            if(words[i].length()>0){
                sb.append(words[i]);
                if(i!=0) sb.append(" ");
            }
        }
        return sb.toString();

    }
}

//First, reverse the whole string, then reverse each word.
# 11.18% 81ms
public class Solution {
    public String reverseWords(String s) {
        String[] parts = s.trim().split("\\s+");
        String out = "";
        for (int i = parts.length - 1; i > 0; i--) {
            out += parts[i] + " ";
        }
        return out + parts[0];
    }
}

// inplace
#83.03% 4ms
public class Solution {
    public String reverseWords(String s) {
        char[] arr = s.toCharArray();
        int newEnd = -1;
        int oldStart = 0;
        int oldEnd = 0;
        while (oldStart < arr.length) {
            while (oldStart < arr.length && arr[oldStart] == ' ') {
                oldStart++;
            }
            if (oldStart == arr.length) {
                break;
            }
            oldEnd = oldStart + 1;
            while (oldEnd < arr.length && arr[oldEnd] != ' ') {
                oldEnd++;
            }
            if (newEnd >= 0) {
                arr[++newEnd] = ' ';
            }
            int len = oldEnd - oldStart;
            copy(arr, oldStart, ++newEnd, len);
            reverse(arr, newEnd, newEnd + len - 1);
            newEnd += len - 1;
            oldStart = oldEnd;
        }
        reverse(arr, 0, newEnd);
        return new String(arr, 0, newEnd + 1);
    }

    private void copy(char[] arr, int srcStart, int targetStart, int len) {
        for (int i = 0; i < len; i++) {
            arr[targetStart + i] = arr[srcStart + i];
        }
    }

    private void reverse(char[] arr, int start, int end) {
        while (start < end) {
            char c = arr[start];
            arr[start++] = arr[end];
            arr[end--] = c;
        }
    }
}
'''
# Differnet question but similar, so put it here
# "!dlroW wolleH"
#
total_Rev= '''
import org.junit.*;
public class Solution {
    public String reverseWords(String s) {
        s = s.replaceAll("\\s+", " ").trim();
        if (s == null || s.length() == 0 ){
            return "";
        }

        int i = 0;
        int start = 0;
        int end = s.length() - 1;

        char[] words = s.toCharArray();
        reverse(words, 0, s.length() - 1);

        while (i <= end){
            int j = i;
            while(j <= end && words[j] != ' '){
                j++;
            }
            reverse(words, i, j-1);
            i = j + 1;
        }
        return new String(words);
    }

    private void reverse(char[] words, int start, int end){
        while(start < end){
            char w = words[start];
            words[start] = words[end];
            words[end] = w;
            start ++;
            end -- ;
        }

    }

    #or do this
    public String reverseWords(String s) {
        s = s.replaceAll("\\s+", " ").trim();
        if (s == null || s.length() == 0 ){
            return "";
        }
        String[] stmp = s.split(" ");
        List<String> list = new ArrayList<>();
        for(int i = stmp.length -1; i >= 0; i--){
            list.add(stmp[i]);
        }
        StringBuilder sb = new StringBuilder();
        for(String w :list){
            sb.append(w);
            sb.append(" ");
        }
        sb.deleteCharAt(sb.length()-1);

        return sb.toString();
    }
}

Assert.assertEquals("Expected", Solution().reverseWords(str));
'''


