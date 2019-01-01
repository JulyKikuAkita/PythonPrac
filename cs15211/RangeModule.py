__source__ = 'https://leetcode.com/problems/range-module/'
# Time:  O(logK) to O(K)
# Space: O(A+R), the space used by ranges.
#
# Description: Leetcode # 715. Range Module
#
# A Range Module is a module that tracks ranges of numbers.
# Your task is to design and implement the following interfaces in an efficient manner.
#
# addRange(int left, int right) Adds the half-open interval [left, right),
# tracking every real number in that interval.
# Adding an interval that partially overlaps with currently tracked numbers
# should add any numbers in the interval [left, right) that are not already tracked.
#
# queryRange(int left, int right) Returns true if and only if every real number in the interval
# [left, right) is currently being tracked.
#
# removeRange(int left, int right) Stops tracking every real number currently being tracked
# in the interval [left, right).
#
# Example 1:
#
# addRange(10, 20): null
# removeRange(14, 16): null
# queryRange(10, 14): true (Every number in [10, 14) is being tracked)
# queryRange(13, 15): false (Numbers like 14, 14.03, 14.17 in [13, 15) are not being tracked)
# queryRange(16, 17): true (The number 16 in [16, 17) is still being tracked,
# despite the remove operation)
#
# Note:
# A half open interval [left, right) denotes all real numbers left <= x < right.
# 0 < left < right < 10^9 in all calls to addRange, queryRange, removeRange.
# The total number of calls to addRange in a single test case is at most 1000.
# The total number of calls to queryRange in a single test case is at most 5000.
# The total number of calls to removeRange in a single test case is at most 1000.
#
import unittest
import bisect
# 308ms 58.44%
class RangeModule(object):
    def __init__(self):
        self.ranges = []

    def _bounds(self, left, right):
        i, j = 0, len(self.ranges) - 1
        for d in (100, 10, 1):
            while i + d - 1 < len(self.ranges) and self.ranges[i+d-1][1] < left:
                i += d
            while j >= d - 1 and self.ranges[j-d+1][0] > right:
                j -= d
        return i, j

    def addRange(self, left, right):
        i, j = self._bounds(left, right)
        if i <= j:
            left = min(left, self.ranges[i][0])
            right = max(right, self.ranges[j][1])
        self.ranges[i:j+1] = [(left, right)]

    def queryRange(self, left, right):
        i = bisect.bisect_left(self.ranges, (left, float('inf')))
        if i: i -= 1
        return (bool(self.ranges) and
                self.ranges[i][0] <= left and
                right <= self.ranges[i][1])

    def removeRange(self, left, right):
        i, j = self._bounds(left, right)
        merge = []
        for k in xrange(i, j+1):
            if self.ranges[k][0] < left:
                merge.append((self.ranges[k][0], left))
            if right < self.ranges[k][1]:
                merge.append((right, self.ranges[k][1]))
        self.ranges[i:j+1] = merge

class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)


if __name__ == '__main__':
    unittest.main()

Java = '''
# Thought: https://leetcode.com/problems/range-module/solution/
#
Approach #1: Maintain Sorted Disjoint Intervals [Accepted]
Complexity Analysis
Time Complexity: Let K be the number of elements in ranges. 
addRange and removeRange operations have O(K) complexity
queryRange has O(logK) complexity 
Because addRange, removeRange adds at most 1 interval at a time, you can bound these further. 
For example, if there are A addRange, R removeRange, and Q queryRange number of operations respectively, 
we can express our complexity as O((A+R)^2 Qlog(A+R))
Space Complexity: O(A+R), the space used by ranges.

# 121ms 89.92%
class RangeModule {
    TreeSet<Interval> ranges;
    public RangeModule() {
        ranges = new TreeSet();
    }
    
    public void addRange(int left, int right) {
        Iterator<Interval> itr = ranges.tailSet(new Interval(0, left - 1)).iterator();
        while (itr.hasNext()) {
            Interval iv = itr.next();
            if (right < iv.left) break;
            left = Math.min(left, iv.left);
            right = Math.max(right, iv.right);
            itr.remove();
        }
        ranges.add(new Interval(left, right));
    }
    
    public boolean queryRange(int left, int right) {
        Interval iv = ranges.higher(new Interval(0, left));
        return (iv != null && iv.left <= left && right <= iv.right);
    }
    
    public void removeRange(int left, int right) {
        Iterator<Interval> itr = ranges.tailSet(new Interval(0, left)).iterator();
        ArrayList<Interval> todo = new ArrayList();
        while (itr.hasNext()) {
            Interval iv = itr.next();
            if (right < iv.left) break;
            if (iv.left < left) todo.add(new Interval(iv.left, left));
            if (right < iv.right) todo.add(new Interval(right, iv.right));
            itr.remove();
        }
        for (Interval iv: todo) ranges.add(iv);
    }
}

class Interval implements Comparable<Interval>{
    int left;
    int right;
    
    public Interval(int left, int right){
        this.left = left;
        this.right = right;
    }
    
    public int compareTo(Interval that){
        if (this.right == that.right) return this.left - that.left;
        return this.right - that.right;
    }
}

/**
 * Your RangeModule object will be instantiated and called as such:
 * RangeModule obj = new RangeModule();
 * obj.addRange(left,right);
 * boolean param_2 = obj.queryRange(left,right);
 * obj.removeRange(left,right);
 */

# 136ms 78.23%
class RangeModule {
    List<int[]> ranges = new ArrayList<int[]>();
    public RangeModule() {
        ranges.add(new int[]{-1, -1});
    }
    
    public void addRange(int left, int right) {
        int l = searchFloor(left);
        int r = searchFloor(right);
        int[] vl = ranges.get(l);
        int[] vr = ranges.get(r);
        if (vr[1] < left) {
            ranges.add(r + 1, new int[]{left, right});
        } else {
            for (int k = 0; k < r - l; k++) ranges.remove(l + 1);
            if (vl[1] < left) {
                ranges.add(l + 1, new int[]{left, Math.max(right, vr[1])});
            } else {
                ranges.remove(l);
                ranges.add(l, new int[] {vl[0], Math.max(right, vr[1])});
            }
        }
    }
    
    public boolean queryRange(int left, int right) {
        int l = searchFloor(left);
        int[] r = ranges.get(l);
        return (r[1] >= right);  
    }
    
    public void removeRange(int left, int right) {
        int l = searchFloor(left);
        int r = searchFloor(right);
        int[] vl = ranges.get(l);
        int[] vr = ranges.get(r);
        if (vr[1] <= left) return;
        for (int k = 0; k < r - l; k++) ranges.remove(l + 1);
        if (vr[1] > right) {
            ranges.add(l + 1, new int[]{right, vr[1]});
        }
        if (vl[1] > left) {
            ranges.remove(l);
            if (vl[0] < left) {
                ranges.add(l, new int[]{vl[0], left});
            }
        }
    }
    
    // search nearest internal starts at or before key and return the index
    private int searchFloor(int key) {
        int l = 0, h = ranges.size();
        while (l + 1 < h) {
            int m = l + (h - l) / 2;
            int v = ranges.get(m)[0];
            if (v < key) {
                l = m;
            } else if (v == key) {
                l = m;
                break;
            } else {
                h = m;
            }
        }
        return l;
    }
}

'''
