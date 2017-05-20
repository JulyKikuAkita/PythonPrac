__author__ = 'July'
'''
# https://github.com/kamyu104/LeetCode/blob/master/Python/zigzag-iterator.py
Given two 1d vectors, implement an iterator to return their elements alternately.

For example, given two 1d vectors:

v1 = [1, 2]
v2 = [3, 4, 5, 6]
By calling next repeatedly until hasNext returns false, the order of elements returned by next should be: [1, 3, 2, 4, 5, 6].

Follow up: What if you are given k 1d vectors? How well can your code be extended to such cases?

Clarification for the follow up question - Update (2015-09-18):
The "Zigzag" order is not clearly defined and is ambiguous for k > 2 cases. If "Zigzag" does not look right to you, replace "Zigzag" with "Cyclic". For example, given the following input:

[1,2,3]
[4,5,6,7]
[8,9]
It should return [1,4,8,2,5,9,3,6,7].
Hide Company Tags Google
'''

# Time:  O(n)
# Space: O(k)

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

# Your ZigzagIterator object will be instantiated and called as such:
# i, v = ZigzagIterator(v1, v2), []
# while i.hasNext(): v.append(i.next())
# java
js = '''
# http://blog.csdn.net/xudli/article/details/48749219

public class ZigzagIterator {
    List<Iterator<Integer> > iters = new ArrayList<Iterator<Integer> >();

    int count = 0;

    public ZigzagIterator(List<Integer> v1, List<Integer> v2) {
        if( !v1.isEmpty() ) iters.add(v1.iterator());
        if( !v2.isEmpty() ) iters.add(v2.iterator());
    }

    public int next() {
        int x = iters.get(count).next();
        if(!iters.get(count).hasNext()) iters.remove(count);
        else count++;

        if(iters.size()!=0) count %= iters.size();
        return x;
    }

    public boolean hasNext() {
        return !iters.isEmpty();
    }
}

public class ZigzagIterator {
    private List<Iterator<Integer>> iterators;
    private int index;

    public ZigzagIterator(List<Integer> v1, List<Integer> v2) {
        iterators = new ArrayList<>();
        if (!v1.isEmpty()) {
            iterators.add(v1.iterator());
        }
        if (!v2.isEmpty()) {
            iterators.add(v2.iterator());
        }
        index = 0;
    }

    public int next() {
        Iterator<Integer> iterator = iterators.get(index);
        int result = iterator.next();
        if (iterator.hasNext()) {
            index++;
        } else {
            iterators.remove(index);
        }
        if (iterators.size() > 0) {
            index %= iterators.size();
        }
        return result;
    }

    public boolean hasNext() {
        return !iterators.isEmpty();
    }
}

/**
 * Your ZigzagIterator object will be instantiated and called as such:
 * ZigzagIterator i = new ZigzagIterator(v1, v2);
 * while (i.hasNext()) v[f()] = i.next();
 */
'''