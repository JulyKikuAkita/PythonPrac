__author__ = 'July'
#https://github.com/kamyu104/LeetCode/blob/master/Python/reverse-words-in-a-string.py
# Time:  O(n)
# Space: O(n)
# String
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
#  Bloomberg

import unittest
class Solution:
    # @param s, a string
    # @return a string
    def reverseWords(self, s):
        #print s.split()[::-1] # return string list -> join to string
        return ' '.join(reversed(s.split())) #reversed have no return

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


#testobj.reverse2Words("the sky is blue")
#testobj.reverse2Words(" works, but  why it   fails ")

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
js1 = '''
public class Solution {
    public String reverseWords(String s) {
        if (s == null || s.length() == 0) {
            return s;
        }
        char[] arr = s.toCharArray();
        int start = 0;
        int end = 0;
        int realEnd = -1;
        while (start < arr.length) {
            while (start < arr.length && arr[start] == ' ') {
                start++;
            }
            if (start == arr.length) {
                break;
            }
            end = start + 1;
            while (end < arr.length && arr[end] != ' ') {
                end++;
            }
            reverse(arr, start, end - 1);
            if (realEnd >= 0) {
                arr[++realEnd] = ' ';
            }
            move(arr, start, end - 1, realEnd + 1);
            realEnd += end - start;
            start = end + 1;
        }
        if (realEnd < 0) {
            return "";
        }
        reverse(arr, 0, realEnd);
        return new String(arr, 0, realEnd + 1);
    }

    private void move(char[] arr, int start, int end, int toStart) {
        if (start == toStart) {
            return;
        }
        for (int i = start; i <= end; i++) {
            arr[toStart + i - start] = arr[i];
        }
    }

    private void reverse(char[] arr, int start, int end) {
        while (start < end) {
            char tmp = arr[start];
            arr[start] = arr[end];
            arr[end] = tmp;
            start++;
            end--;
        }
    }
}
'''
js2 = '''
public class Solution {
    public String reverseWords(String s) {
        s = s.replaceAll("\\s+", " ").trim();
        if (s.length() == 0) {
            return s;
        }
        String[] strs = s.split(" ");
        String ret = "";
        for (int i = strs.length - 1; i >= 0; i--) {
            ret += strs[i] + " ";
        }

        return ret.substring(0, ret.length() - 1);
    }
}
'''
#Differnet question but similar, so put it her
"!dlroW wolleH"

js3 = '''
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

#Sales Force:
# Write a function reverse the words in a string
# eg: "Today is Tuesday"
# returns : "yadoT si yadseuT"
'''
public String reverseString(String s){
    // corner case
    if(s == null || s.length() == 0){
        return null;
    }

    s = s.trim();
    String[] cur = s.split(" ");  // Today is Tuesday
    StringBuilder sb = new StringBuilder();
    for(int i = 0; i < cur.length; i++){
        String tmp = reverseWord(cur[i]);
        sb.append(tmp);
        sb.append(" ");
    }
    sb.deleteCharAt(sb.length()-1);
    return sb.toString();

}

private String reverseWord(String s){

    int start = 0;
    int end = s.length()-1;
    char[] chars = s.toCharArray();
    while(start < end){ // double check for out of index  //(start + end) / 2
        swap(chars, start, end);
        start++;
        end--;
    }
    return new String(chars);

}

private void swap(char[] chars, int start, int end){
    char tmp = chars[start];
    chars[start] = chars[end];
    chars[end] = tmp;
}


}
'''


