__source__ = 'https://leetcode.com/problems/zigzag-iterator/'
# # https://github.com/kamyu104/LeetCode/blob/master/Python/zigzag-iterator.py
# Time:  O(n)
# Space: O(k)
#
# Description: Leetcode # 281. Zigzag Iterator
#
# Given two 1d vectors, implement an iterator to return their elements alternately.
#
# For example, given two 1d vectors:
#
# v1 = [1, 2]
# v2 = [3, 4, 5, 6]
# By calling next repeatedly until hasNext returns false,
# the order of elements returned by next should be: [1, 3, 2, 4, 5, 6].
#
# Follow up: What if you are given k 1d vectors? How well can your code be extended to such cases?
#
# Clarification for the follow up question - Update (2015-09-18):
# The "Zigzag" order is not clearly defined and is ambiguous for k > 2 cases.
# If "Zigzag" does not look right to you, replace "Zigzag" with "Cyclic". For example, given the following input:
#
# [1,2,3]
# [4,5,6,7]
# [8,9]
# It should return [1,4,8,2,5,9,3,6,7].
#
# Companies
# Google
# Related Topics
# Design
# Similar Questions
# Binary Search Tree Iterator Flatten 2D Vector Peeking Iterator Flatten Nested List Iterator
#
import unittest
import collections
class ZigzagIterator(object):

    def __init__(self, v1, v2):
        """
        Initialize your q structure here.
        :type v1: List[int]
        :type v2: List[int]
        """
        self.q = collections.deque([(len(v), iter(v)) for v in (v1, v2) if v])

    def next(self):
        """
        :rtype: int
        """
        len, iter = self.q.popleft()
        if len > 1:
            self.q.append((len-1, iter))
        return next(iter)

    def hasNext(self):
        """
        :rtype: bool
        """
        return bool(self.q)

class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)

if __name__ == '__main__':
    unittest.main()

# Your ZigzagIterator object will be instantiated and called as such:
# i, v = ZigzagIterator(v1, v2), []
# while i.hasNext(): v.append(i.next())

Java = '''
#Thought:
#98.61% 2ms
public class ZigzagIterator {
    LinkedList<Iterator> list;

    public ZigzagIterator(List<Integer> v1, List<Integer> v2) {
        list = new LinkedList<Iterator>();
        if( !v1.isEmpty()) list.add(v1.iterator());
        if( !v2.isEmpty()) list.add(v2.iterator());
    }

    public int next() {
        Iterator cur = list.remove();
        int result = (Integer) cur.next();
        if (cur.hasNext()) list.add(cur);
        return result;
    }

    public boolean hasNext() {
        return !list.isEmpty();
    }
}

#63.04% 3ms
public class ZigzagIterator {
    private Iterator<Integer> i, j, tmp;

    public ZigzagIterator(List<Integer> v1, List<Integer> v2) {
        i = v2.iterator();
        j = v1.iterator();
    }

    public int next() {
        if (j.hasNext()) { tmp = j; j = i; i = tmp; }
        return i.next();
    }

    public boolean hasNext() {
        return i.hasNext() || j.hasNext();
    }
}

#98.61% 2ms
public class ZigzagIterator {
    int c1 = 0;
    int c2 = 0;
    List<Integer> l1;
    List<Integer> l2;
    public ZigzagIterator(List<Integer> v1, List<Integer> v2) {
        l1 = v1;
        l2 = v2;
    }

    public int next() {
        if(c1 == l1.size()) return l2.get(c2++);
        else if(c2 == l2.size()) return l1.get(c1++);
        else if(c1 <= c2) return l1.get(c1++);
        else return l2.get(c2++);
    }

    public boolean hasNext() {
        return c1+c2 == l1.size() + l2.size() ? false : true;
    }
}
/**
 * Your ZigzagIterator object will be instantiated and called as such:
 * ZigzagIterator i = new ZigzagIterator(v1, v2);
 * while (i.hasNext()) v[f()] = i.next();
 */'''
