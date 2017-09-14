__source__ = 'https://github.com/kamyu104/LeetCode/blob/master/Python/mini-parser.py'
# https://github.com/kamyu104/LeetCode/blob/master/Python/mini-parser.py
# Time:  O(n)
# Space: O(h)
#
# Description: Leetcode # 385. Mini Parser
#
# Given a nested list of integers represented as a string, implement a parser to deserialize it.
#
# Each element is either an integer, or a list -- whose elements may also be integers or other lists.
#
# Note: You may assume that the string is well-formed:
#
# String is non-empty.
# String does not contain white spaces.
# String contains only digits 0-9, [, - ,, ].
# Example 1:
#
# Given s = "324",
#
# You should return a NestedInteger object which contains a single integer 324.
# Example 2:
#
# Given s = "[123,[456,[789]]]",
#
# Return a NestedInteger object containing a nested list with 2 elements:
#
# 1. An integer containing value 123.
# 2. A nested list containing two elements:
#     i.  An integer containing value 456.
#     ii. A nested list with one element:
#          a. An integer containing value 789.
#
# Companies
# Airbnb
# Related Topics
# String Stack
# Similar Questions
# Flatten Nested List Iterator Ternary Expression Parser
#
# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#
class NestedInteger(object):
   def __init__(self, value=None):
       """
       If value is not specified, initializes an empty list.
       Otherwise initializes a single integer equal to value.
       """

   def isInteger(self):
       """
       @return True if this NestedInteger holds a single integer, rather than a nested list.
       :rtype bool
       """

   def add(self, elem):
       """
       Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
       :rtype void
       """

   def setInteger(self, value):
       """
       Set this NestedInteger to hold a single integer equal to value.
       :rtype void
       """

   def getInteger(self):
       """
       @return the single integer that this NestedInteger holds, if it holds a single integer
       Return None if this NestedInteger holds a nested list
       :rtype int
       """

   def getList(self):
       """
       @return the nested list that this NestedInteger holds, if it holds a nested list
       Return None if this NestedInteger holds a single integer
       :rtype List[NestedInteger]
       """


import unittest
class Solution(object):
    def deserialize(self, s):
        if not s:
            return NestedInteger()

        if s[0] != '[':
            return NestedInteger(int(s))

        stk = []

        i = 0
        for j in xrange(len(s)):
            if s[j] == '[':
                stk += NestedInteger(),
                i = j+1
            elif s[j] in ',]':
                if s[j-1].isdigit():
                    stk[-1].add(NestedInteger(int(s[i:j])))
                if s[j] == ']' and len(stk) > 1:
                    cur = stk[-1]
                    stk.pop();
                    stk[-1].add(cur)
                i = j+1

        return stk[-1]

class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)

if __name__ == '__main__':
    unittest.main()

Java = '''
#Thought:
This approach will just iterate through every char in the string (no recursion).

If encounters '[', push current NestedInteger to stack and start a new one.
If encounters ']', end current NestedInteger and pop a NestedInteger from stack to continue.
If encounters ',', append a new number to curr NestedInteger, if this comma is not right after a brackets.
Update index l and r, where l shall point to the start of a integer substring, while r shall points to the end+1 of substring.

/**
 * // This is the interface that allows for creating nested lists.
 * // You should not implement it, or speculate about its implementation
 * public interface NestedInteger {
 *     // Constructor initializes an empty nested list.
 *     public NestedInteger();
 *
 *     // Constructor initializes a single integer.
 *     public NestedInteger(int value);
 *
 *     // @return true if this NestedInteger holds a single integer, rather than a nested list.
 *     public boolean isInteger();
 *
 *     // @return the single integer that this NestedInteger holds, if it holds a single integer
 *     // Return null if this NestedInteger holds a nested list
 *     public Integer getInteger();
 *
 *     // Set this NestedInteger to hold a single integer.
 *     public void setInteger(int value);
 *
 *     // Set this NestedInteger to hold a nested list and adds a nested integer to it.
 *     public void add(NestedInteger ni);
 *
 *     // @return the nested list that this NestedInteger holds, if it holds a nested list
 *     // Return null if this NestedInteger holds a single integer
 *     public List<NestedInteger> getList();
 * }
 */
#17.11% 28ms
public class Solution {
    public NestedInteger deserialize(String s) {
        if (s == null || s.length() == 0) return null;
        if (s.charAt(0) != '[') { // ERROR: special case
            return new NestedInteger(Integer.valueOf(s));
        }

        Stack<NestedInteger> stack = new Stack<>();
        NestedInteger curr = null;
        int l = 0; // l shall point to the start of a number substring;
               // r shall point to the end+1 of a number substring
        for (int r = 0; r < s.length(); r++) {
            char ch = s.charAt(r);
            if (ch == '[') {
                if (curr != null) {
                    stack.push(curr);
                }
                curr = new NestedInteger();
                l = r+1;
            } else if (ch == ']') {
                String num = s.substring(l ,r);
                if (!num.isEmpty()){
                    curr.add(new NestedInteger(Integer.valueOf(num)));
                }
                if (!stack.isEmpty()) {
                    NestedInteger pop = stack.pop();
                    pop.add(curr);
                    curr = pop;
                }
                l = r + 1;
            } else if (ch == ',') {
                if (s.charAt(r - 1) != ']') {
                    String num = s.substring(l, r);
                    curr.add( new NestedInteger(Integer.valueOf(num)));
                }
                l = r + 1;
            }
        }
        return curr;
    }
}
#if need full-implementation:
https://discuss.leetcode.com/topic/54268/straightforward-java-solution-with-explanation-and-a-simple-implementation-of-nestedinteger-for-your-ease-of-testing

#99.47% 10ms
class Solution {
    private int parse(char[] chars, int idx, NestedInteger root) {
        int num = 0;
        boolean neg = false;
        boolean hasNum = false;
        while (idx < chars.length) {
            char c = chars[idx++];
            if (c == '[' || c == ']') {
                if (hasNum) {
                    root.add(neg ? new NestedInteger(-num) : new NestedInteger(num));
                    hasNum = false;
                    neg = false;
                    num = 0;
                }
                if (c == ']') return idx;
                NestedInteger next = new NestedInteger();
                root.add(next);
                idx = parse(chars, idx, next);
            } else if (c == '-') neg = true;
            else if (c == ',') {
                if (hasNum) {
                    root.add(neg ? new NestedInteger(-num) : new NestedInteger(num));
                    num = 0;
                    neg = false;
                    hasNum = false;
                }
            } else {
                num *= 10;
                num += c - '0';
                hasNum = true;
            }
        }
        if (hasNum) root.add(neg ? new NestedInteger(-num) : new NestedInteger(num));
        return chars.length;
    }
    public NestedInteger deserialize(String s) {
        NestedInteger root = new NestedInteger();
        if (s.length() == 0) return root;
        char[] c = s.toCharArray();
        parse(c, 0, root);
        return root.getList().get(0);
    }
}

'''