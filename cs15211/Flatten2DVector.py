__source__ = 'https://leetcode.com/problems/flatten-2d-vector/'
# https://github.com/kamyu104/LeetCode/blob/master/Python/flatten-2d-vector.py
# Time:  O(1)
# Space: O(1)
#
# Description: Leetcode # 251. Flatten 2D Vector
#
# Implement an iterator to flatten a 2d vector.
#
# For example,
# Given 2d vector =
#
# [
#   [1,2],
#   [3],
#   [4,5,6]
# ]
#
# By calling next repeatedly until hasNext returns false,
# the order of elements returned by next should be: [1,2,3,4,5,6].
#
# Follow up:
# As an added challenge, try to code it using only iterators in C++ or iterators in Java.
#
# Companies
# Google Airbnb Twitter Zenefits
# Related Topics
# Design
# Similar Questions
# Binary Search Tree Iterator Zigzag Iterator Peeking Iterator Flatten Nested List Iterator
#

# 44ms 40.47%
import unittest
class Vector2D:
    x, y = 0, 0
    vec = None

    # Initialize your data structure here.
    # @param {integer[][]} vec2d
    def __init__(self, vec2d):
        self.vec = vec2d
        self.x = 0
        if self.x != len(self.vec):
            self.y = 0
            self.adjustNextIter()

    # @return {integer}
    def next(self):
        ret = self.vec[self.x][self.y]
        self.y += 1
        self.adjustNextIter()
        return ret

    # @return {boolean}
    def hasNext(self):
        return self.x != len(self.vec) and self.y != len(self.vec[self.x])

    def adjustNextIter(self):
        while self.x != len(self.vec) and self.y == len(self.vec[self.x]):
            self.x += 1
            if self.x != len(self.vec):
                self.y = 0

class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)

if __name__ == '__main__':
    unittest.main()

Java = '''
# Thought:

# 1ms 100%
public class Vector2D implements Iterator<Integer> {

    int row = 0;
    int col = 0;
    List<List<Integer>> list;
    public Vector2D(List<List<Integer>> vec2d) {
        list = vec2d;
    }

    @Override
    public Integer next() {
        return list.get(row).get(col++);
    }

    @Override
    public boolean hasNext() {
        if(row >= list.size()) return false;
        while(col >=list.get(row).size()){
            col = 0;
            row++;

            if(row >= list.size()) return false;
        }
        return true;
    }
}

# 1ms 100%
public class Vector2D implements Iterator<Integer> {
    private List<Iterator<Integer>> iterators;
    private int index;

    public Vector2D(List<List<Integer>> vec2d) {
        iterators = new ArrayList<>();
        for (List<Integer> list : vec2d) {
            if (!list.isEmpty()) {
                iterators.add(list.iterator());
            }
        }
    }

    @Override
    public Integer next() {
        Iterator<Integer> iter = iterators.get(index);
        Integer result = iter.next();
        if (!iter.hasNext()) {
            index++;
        }
        return result;
    }

    @Override
    public boolean hasNext() {
        return index < iterators.size();
    }
}

# 2ms 43.83%
public class Vector2D {

    Queue<Iterator<Integer>> queue;
    Iterator<Integer> current = null;

    public Vector2D(List<List<Integer>> vec2d) {
        queue = new LinkedList<Iterator<Integer>>();
        for (int i = 0; i < vec2d.size(); i++){
            queue.add(vec2d.get(i).iterator());
        }
        current = queue.poll(); // first
    }

    public int next() {
        if (!current.hasNext()) return -1;

        return current.next();
    }

    public boolean hasNext() {
        if (current == null) return false;

        while (!current.hasNext()) {
            if (!queue.isEmpty()) {
                current = queue.poll();
            } else return false;
        }

        return true;
    }
}

'''