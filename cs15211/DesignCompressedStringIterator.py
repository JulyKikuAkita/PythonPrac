__source__ = 'https://leetcode.com/problems/design-compressed-string-iterator/#/description'
# Time:  O(1)
# Space: O(1)
#
# Description: 604. Design Compressed String Iterator
#
# Design and implement a data structure for a compressed string iterator.
# It should support the following operations: next and hasNext.
#
# The given compressed string will be in the form of each letter followed
# by a positive integer representing the number of this letter existing in the original uncompressed string.
#
# next() - if the original string still has uncompressed characters, return the next letter;
# Otherwise return a white space.
# hasNext() - Judge whether there is any letter needs to be uncompressed.
#
# Note:
# Please remember to RESET your class variables declared in StringIterator,
# as static/class variables are persisted across multiple test cases. Please see here for more details.
#
# Example:
#
# StringIterator iterator = new StringIterator("L1e2t1C1o1d1e1");
#
# iterator.next(); // return 'L'
# iterator.next(); // return 'e'
# iterator.next(); // return 'e'
# iterator.next(); // return 't'
# iterator.next(); // return 'C'
# iterator.next(); // return 'o'
# iterator.next(); // return 'd'
# iterator.hasNext(); // return true
# iterator.next(); // return 'e'
# iterator.hasNext(); // return false
# iterator.next(); // return ' '
# Hide Company Tags Google
# Hide Tags Design
# Hide Similar Problems (H) LRU Cache

import unittest
import re

# 72ms 14.49%
class StringIterator(object):

    def __init__(self, compressedString):
        """
        :type compressedString: str
        """
        self.__data = re.findall(r"([a-zA-Z])(\d+)", compressedString)
        self.__index, self.__count = -1, 0

    def next(self):
        """
        :rtype: str
        """
        if self.hasNext():
            self.__count -= 1
            return self.__data[self.__index][0]
        else:
            return ' '

    def hasNext(self):
        """
        :rtype: bool
        """
        if self.__count == 0 and self.__index + 1 < len(self.__data):
            self.__index += 1
            self.__count = int(self.__data[self.__index][1])
        return self.__count > 0

# Your StringIterator object will be instantiated and called as such:
# obj = StringIterator(compressedString)
# param_1 = obj.next()
# param_2 = obj.hasNext()

class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)


if __name__ == '__main__':
    unittest.main()

Java = '''
# Thought: https://leetcode.com/problems/design-compressed-string-iterator/solution/

The time required to perform next() operation is O(1).
The time required for hasNext() operation is O(1).
Since no precomputations are done, and hasNext() requires only O(1)O(1) time,
this solution is advantageous if hasNext() operation is performed most of the times.

# 71ms 72.07%
class StringIterator {
    String res;
    int ptr = 0, num = 0;
    char ch = ' ';
    public StringIterator(String s) {
        res = s;
    }
    public char next() {
        if (!hasNext())
            return ' ';
        if (num == 0) {
            ch = res.charAt(ptr++);
            while (ptr < res.length() && Character.isDigit(res.charAt(ptr))) {
                num = num * 10 + res.charAt(ptr++) - '0';
            }
        }
        num--;
        return ch;
    }
    public boolean hasNext() {
        return ptr != res.length() || num != 0;
    }
}


1. Java8:
# 84ms 22.76%
class StringIterator {
    int i;
    String[] arr;
    int[] counts;

    public StringIterator(String compressedString) {
        arr = compressedString.split("\\d+");
        counts = Arrays.stream(compressedString.substring(1).split("[a-zA-Z]+")).mapToInt(Integer::parseInt).toArray();
        i = 0;
    }

    public char next() {
        if (!hasNext()) return ' ';
        char ch = arr[i].charAt(0);
        if (--counts[i] == 0) ++i;
        return ch;
    }

    public boolean hasNext() {
        if (i == arr.length) return false;
        return true;
    }
}

/**
 * Your StringIterator object will be instantiated and called as such:
 * StringIterator obj = new StringIterator(compressedString);
 * char param_1 = obj.next();
 * boolean param_2 = obj.hasNext();
 */

 2.
# 72ms 68.28%
class StringIterator {

    Queue<int[]> queue = new LinkedList<>();

    public StringIterator(String s) {
        int i = 0, n = s.length();
        while (i < n) {
            int j = i+1;
            while (j < n && s.charAt(j) - 'A' < 0) j++; //same as Character.isDigit(compressedString.charAt(j))
            queue.add(new int[]{s.charAt(i) - 'A',  Integer.parseInt(s.substring(i+1, j))});
            i = j;
        }
    }

    public char next() {
        if (queue.isEmpty()) return ' ';
        int[] top = queue.peek();
        if (--top[1] == 0) queue.poll();
        return (char) ('A' + top[0]);
    }

    public boolean hasNext() {
        return !queue.isEmpty();
    }
}

'''