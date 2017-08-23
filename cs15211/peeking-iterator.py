__source__ = 'https://leetcode.com/problems/peeking-iterator/description/'
# https://github.com/kamyu104/LeetCode/blob/master/Python/peeking-iterator.py
# Time:  O(1) per peek(), next(), hasNext()
# Space: O(1)
#
# Description: Leetcode # 284. Peeking Iterator
#
# Given an Iterator class interface with methods: next() and hasNext(),
# design and implement a PeekingIterator that support the peek() operation --
# it essentially peek() at the element that will be returned by the next call to next().
#
# Here is an example. Assume that the iterator is initialized to the beginning of
# the list: [1, 2, 3].
#
# Call next() gets you 1, the first element in the list.
#
# Now you call peek() and it returns 2, the next element. Calling next() after that
# still return 2.
#
# You call next() the final time and it returns 3, the last element. Calling hasNext()
# after that should return false.
#
# Follow up: How would you extend your design to be generic and work with all types, not just integer?
#
# Companies
# Google Apple Yahoo
# Related Topics
# Design
# Similar Questions
# Binary Search Tree Iterator Flatten 2D Vector Zigzag Iterator
#
# Below is the interface for Iterator, which is already defined for you.
#
# class Iterator(object):
#     def __init__(self, nums):
#         """
#         Initializes an iterator object to the beginning of a list.
#         :type nums: List[int]
#         """
#
#     def hasNext(self):
#         """
#         Returns true if the iteration has more elements.
#         :rtype: bool
#         """
#
#     def next(self):
#         """
#         Returns the next element in the iteration.
#         :rtype: int
#         """
import unittest
class PeekingIterator(object):
    def __init__(self, iterator):
        """
        Initialize your data structure here.
        :type iterator: Iterator
        """

        self.iterator = iterator
        self.val = None
        self.has_next_ = iterator.hasNext()
        self.has_peeked_ = False

    def peek(self):
        """
        Returns the next element in the iteration without advancing the iterator.
        :rtype: int
        """

        if not self.has_peeked_():
            self.has_peeked_ = True
            self.val = self.iterator.hasNext()
        return self.val;

    def next(self):
        """
        :rtype: int
        """
        self.val = self.peek()
        self.has_peeked_ = False
        self.has_next_ = self.iterator.hasNext()
        return self.val_;

    def hasNext(self):
        """
        :rtype: bool
        """
        return self.has_next_

# Your PeekingIterator object will be instantiated and called as such:
# iter = PeekingIterator(Iterator(nums))
# while iter.hasNext():
#     val = iter.peek()   # Get the next element but not advance the iterator.
#     iter.next()         # Should return the same value as [val].

class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)

if __name__ == '__main__':
    unittest.main()

Java = '''
#Thought:
# 51.70% 101ms
// Java Iterator interface reference:
// https://docs.oracle.com/javase/8/docs/api/java/util/Iterator.html
class PeekingIterator implements Iterator<Integer> {
    Iterator<Integer> iterator;
    Integer next;

	public PeekingIterator(Iterator<Integer> iterator) {
	    // initialize any member here.
	    this.iterator = iterator;
	    if (this.iterator.hasNext()) {
	        next = iterator.next();
	    }
	}

    // Returns the next element in the iteration without advancing the iterator.
	public Integer peek() {
        return next;
	}

	// hasNext() and next() should behave the same as in the Iterator interface.
	// Override them if needed.
	@Override
	public Integer next() {
	    Integer result = next;
	    if (iterator.hasNext()) {
	        next = iterator.next();
	    } else {
	        next = null;
	    }
	    return result;
	}

	@Override
	public boolean hasNext() {
	    return next != null;
	}
}

#24.39% 111ms
class PeekingIterator implements Iterator<Integer> {
    Iterator<Integer> iter;
    Integer value = null;
	public PeekingIterator(Iterator<Integer> iterator) {
	    // initialize any member here.
	    iter = iterator;
        if (iter != null) value = iter.next();
	}

    // Returns the next element in the iteration without advancing the iterator.
	public Integer peek() {
        return value;
	}

	// hasNext() and next() should behave the same as in the Iterator interface.
	// Override them if needed.
	@Override
	public Integer next() {
	    Integer result = value;
        if (iter.hasNext()) value = iter.next();
        else value = null;
        return result;
	}

	@Override
	public boolean hasNext() {
	    return (value != null);
	}
}
'''
