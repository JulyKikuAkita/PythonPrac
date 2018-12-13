__source__ = 'https://leetcode.com/problems/falling-squares/description/'
# Time:  O(N*N^(1/2))
# Space: O(N)
# Segment Tree
#
# Description: Leetcode # 699. Falling Squares
#
# On an infinite number line (x-axis), we drop given squares in the order they are given.
#
# The i-th square dropped (positions[i] = (left, side_length)) is a square
# with the left-most point being positions[i][0] and sidelength positions[i][1].
#
# The square is dropped with the bottom edge parallel to the number line,
# and from a higher height than all currently landed squares.
# We wait for each square to stick before dropping the next.
#
# The squares are infinitely sticky on their bottom edge,
# and will remain fixed to any positive length surface they touch (either the number line or another square).
# Squares dropped adjacent to each other will not stick together prematurely.
#
# Return a list ans of heights. Each height ans[i] represents the current highest height of any square we have dropped,
# after dropping squares represented by positions[0], positions[1], ..., positions[i].
#
# Example 1:
# Input: [[1, 2], [2, 3], [6, 1]]
# Output: [2, 5, 5]
# Explanation:
#
# After the first drop of positions[0] = [1, 2]:
# _aa
# _aa
# -------
# The maximum height of any square is 2.
#
#
# After the second drop of positions[1] = [2, 3]:
# __aaa
# __aaa
# __aaa
# _aa__
# _aa__
# --------------
# The maximum height of any square is 5.
# The larger square stays on top of the smaller square despite where its center
# of gravity is, because squares are infinitely sticky on their bottom edge.
#
#
# After the third drop of positions[1] = [6, 1]:
# __aaa
# __aaa
# __aaa
# _aa
# _aa___a
# --------------
# The maximum height of any square is still 5.
#
# Thus, we return an answer of [2, 5, 5].
#
#
# Example 2:
# Input: [[100, 100], [200, 100]]
# Output: [100, 100]
# Explanation: Adjacent squares don't get stuck prematurely - only their bottom edge can stick to surfaces.
# Note:
#
# 1 <= positions.length <= 1000.
# 1 <= positions[i][0] <= 10^8.
# 1 <= positions[i][1] <= 10^6.

import unittest
import bisect
# Binary Search
# 89.04% 48ms
class Solution(object):
    def fallingSquares(self, positions):
        """
        :type positions: List[List[int]]
        :rtype: List[int]
        """
        axis = [0, float('inf')]
        heights = [0, 0]
        ans = [0]
        for left, length in positions:
            right = left + length;
            idl = bisect.bisect_right(axis, left)
            idr = bisect.bisect_left(axis, right)
            h = max(heights[idl - 1:idr]) + length

            axis[idl : idr] = [left, right]
            heights[idl:idr] = [h, heights[idr - 1]]
            ans.append(max(ans[-1], h))
        return ans[1:]

class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)


if __name__ == '__main__':
    unittest.main()

Java = '''
# Thought: https://leetcode.com/problems/falling-squares/solution/
#
# Approach #2: Brute Force with Coordinate Compression [Accepted]
# O(N^2)
# 92ms 13.60%
# https://leetcode.com/problems/falling-squares/discuss/108766/Easy-Understood-O(n2)-Solution-with-explanation
# The idea is quite simple, we use intervals to represent the square.
# the initial height we set to the square cur is pos[1].
# That means we assume that all the square will fall down to the land.
# we iterate the previous squares, check is there any square i beneath my cur square.
# If we found that we have squares i intersect with us,
# which means my current square will go above to that square i.
# My target is to find the highest square and put square cur onto square i,
# and set the height of the square cur as
#
# cur.height = cur.height + previousMaxHeight;

# 90ms 12.62%
class Solution {
    private class Interval {
        int start, end, height;
        public Interval(int start, int end, int height) {
            this.start = start;
            this.end = end;
            this.height = height;
        }
    }
    public List<Integer> fallingSquares(int[][] positions) {
        List<Interval> intervals = new ArrayList<>();
        List<Integer> res = new ArrayList<>();
        int h = 0;
        for (int[] pos : positions) {
            Interval cur = new Interval(pos[0], pos[0] + pos[1] - 1, pos[1]);
            h = Math.max(h, getHeight(intervals, cur));
            res.add(h);
        }
        return res;
    }
    private int getHeight(List<Interval> intervals, Interval cur) {
        int preMaxHeight = 0;
        for (Interval i : intervals) {
            // Interval i does not intersect with cur
            if (i.end < cur.start) continue;
            if (i.start > cur.end) continue;
            // find the max height beneath cur
            preMaxHeight = Math.max(preMaxHeight, i.height);
        }
        cur.height += preMaxHeight;
        intervals.add(cur);
        return cur.height;
    }
}

Approach #4: Segment Tree with Lazy Propagation [Accepted]
# Complexity Analysis
# Time Complexity: O(N\sqrt{N}), where N is the length of positions.
# Each query and update has complexity O(\sqrt{N})
# Space Complexity: O(N), the space used by heights.

# 41.08% 42ms
# implementation of Segment Tree
class Solution {
    public static class SegmentTree {
        TreeNode root;
        public SegmentTree() {
            root = new TreeNode(0, Integer.MAX_VALUE, 0);
        }

        public int getMax() {
            return root.max;
        }

        public TreeNode update(int l, int r, int val) {
            return update(root, l, r, val);
        }

        public TreeNode update (TreeNode node, int l, int r, int val) {
            if (node.lazy != 0) {
                node.max = node.lazy;
                if (node.leftBound != node.rightBound) {
                    node.getLeft().lazy = node.lazy;
                    node.getRight().lazy = node.lazy;
                }
                node.lazy = 0;
            }
            if (node.rightBound < node.leftBound || r < node.leftBound || l > node.rightBound) return node;
            if (node.leftBound >= l && node.rightBound <= r) {
                node.max = val;
                if (node.leftBound != node.rightBound) {
                    node.getLeft().lazy = val;
                    node.getRight().lazy = val;
                }
                return node;
            }
            node.left = update(node.getLeft(), l ,r, val);
            node.right = update(node.getRight(), l, r, val);
            node.max = Math.max(node.left.max, node.right.max);
            return node;
        }

        public int query(int l, int r) {
            return query(root, l, r);
        }

        public int query(TreeNode node, int l, int r) {
            if (node.rightBound < node.leftBound || r < node.leftBound || l > node.rightBound) return 0;
            if (node.lazy != 0) {
                node.max = node.lazy;
                if (node.leftBound  != node.rightBound) {
                    node.getLeft().lazy = node.lazy;
                    node.getRight().lazy = node.lazy;
                }
                node.lazy = 0;
            }
            if (node.leftBound >= l && node.rightBound <= r) return node.max;
            int q1 = query(node.getLeft(), l, r);
            int q2 = query(node.getRight(), l, r);
            return Math.max(q1, q2);
        }

        public class TreeNode {
            TreeNode left;
            TreeNode right;
            int leftBound;
            int rightBound;
            int lazy;
            int max;
            public TreeNode(int l, int r, int m) {
                leftBound = l;
                rightBound = r;
                lazy = 0;
                max = m;
            }

            public int getMid() {
                return leftBound + (rightBound - leftBound) / 2;
            }

            public TreeNode getLeft() {
                if (left == null) left = new TreeNode(leftBound, getMid(), 0);
                return left;
            }

            public TreeNode getRight() {
                if (right == null) right = new TreeNode(getMid() + 1, rightBound, 0);
                return right;
            }
        }
    }

    public List<Integer> fallingSquares(int[][] positions) {
        List<Integer> res = new ArrayList();
        SegmentTree segmentTree = new SegmentTree();
        for (int[] p : positions) {
            int h = segmentTree.query(p[0], p[0] + p[1] - 1);
            segmentTree.update(p[0], p[0] + p[1] - 1, h + p[1]);
            res.add(segmentTree.getMax());
        }
        return res;
    }
}

# 86.12% 25ms
class Solution {
    public List<Integer> fallingSquares(int[][] positions) {
        Set<Integer> set = new HashSet<>();
        for (int[] pos : positions) {
            set.add(pos[0]);
            set.add(pos[0] + pos[1] - 1);
        }

        List<Integer> list = new ArrayList(set);
        Collections.sort(list);
        Map<Integer, Integer> mapX = new HashMap();
        for (int i = 0; i< list.size(); i++) {
            mapX.put(list.get(i), i);
        }

        int i = 0;
        int[] treeNode = new int[list.size() * 4];
        int[] lazy = new int[list.size() * 4];
        List<Integer> res = new ArrayList();
        int max = 0;
        for (int[] pos :positions) {
            int left = mapX.get(pos[0]);
            int right = mapX.get(pos[0] + pos[1] - 1);
            int pre_max = query(treeNode, lazy, 1, 0, list.size() -1, left, right);
            update(treeNode, lazy, 1, 0, list.size() - 1, left, right, pre_max + pos[1]);
            max = Math.max(max, pre_max + pos[1]);
            res.add(max);
        }
        return res;
    }

    public int query(int[] treeNode, int[] lazy, int index, int start, int end, int left, int right) {
        if (lazy[index] != 0) {
            treeNode[index] = lazy[index];
            if (start < end) {
                lazy[2 * index] = lazy[index];
                lazy[2 * index + 1] = lazy[index];
            }
            lazy[index] = 0;
        }
        if (start > end || right < start || left > end) return 0;
        if (left <= start && end <= right) return treeNode[index];
        int mid = (start + end) >>> 1;
        int left_max = query(treeNode, lazy, index * 2, start, mid, left, right);
        int right_max = query(treeNode, lazy, 2 * index + 1, mid + 1, end, left, right);
        return Math.max(left_max, right_max);
    }

    public void update(int[] treeNode, int[] lazy, int index, int start, int end, int left, int right, int val) {
        if (lazy[index] != 0) {
            treeNode[index] = lazy[index];
            if (start < end) {
                lazy[2 * index] = lazy[index];
                lazy[2 * index + 1] = lazy[index];
            }
            lazy[index] = 0;
        }
        if (start > end || left > end || right < start) return ;
        if (left <= start && end <= right) {
            treeNode[index] = val;
            if (start < end) {
                lazy[index * 2] = val;
                lazy[index * 2 + 1] = val;
            }
            return;
        }
        int mid = (start + end) >>> 1;
        update(treeNode, lazy, index * 2, start, mid, left, right, val);
        update(treeNode, lazy, index * 2 + 1, mid + 1, end, left, right, val);
        treeNode[index] = Math.max(treeNode[2*index], treeNode[2 * index + 1]);
    }
}

# Binary Search
# 98.02% 10ms
class Solution {
    public List<Integer> fallingSquares(int[][] positions) {
        int[] pos = new int[positions.length*2];
        for (int i = 0; i < positions.length; i++) {
            pos[i*2] = positions[i][0];
            pos[i*2+1] = positions[i][0] + positions[i][1];
        }
        Arrays.sort(pos);
        List<Integer> res = new LinkedList<>();
        int[] heights = new int[pos.length];
        int best = 0;
        for (int[] p : positions) {
            int start = p[0], end = p[0] + p[1];
            int index = Arrays.binarySearch(pos, start);
            int max = 0;
            for (int i = index; pos[i] < end; i++)
                max = Math.max(max, heights[i]);
            best = Math.max(best, max + p[1]);
            res.add(best);
            for (int i = index; pos[i] < end; i++)
                heights[i] = max + p[1];
        }
        return res;
    }
}

# TreeMap
The squares divide the number line into many segments with different heights.
Therefore we can use a TreeMap to store the number line.
The key is the starting point of each segment and the value is the height of the segment.
For every new falling square (s, l), we update those segments between s and s + l

# O(n^2)
# 63.46% 31ms
class Solution {
    public List<Integer> fallingSquares(int[][] positions) {
        List<Integer> list = new ArrayList<>();
        TreeMap<Integer, Integer> map = new TreeMap<>();

        // at first, there is only one segment starting from 0 with height 0
        map.put(0, 0);

        // The global max height is 0
        int max = 0;

        for(int[] position : positions) {

            // the new segment
            int start = position[0], end = start + position[1];

            // find the height among this range
            Integer key = map.floorKey(start); //Returns the greatest key less than or equal to the given key,
                                               // or null if there is no such key.
            int h = map.get(key);
            key = map.higherKey(key);
            while(key != null && key < end) {
                h = Math.max(h, map.get(key));
                key = map.higherKey(key); //Returns the least key strictly greater than the given key,
                                          // or null if there is no such key.
            }
            h += position[1];

            // update global max height
            max = Math.max(max, h);
            list.add(max);

            // update new segment and delete previous segments among the range
            int tail = map.floorEntry(end).getValue(); // Returns a key-value mapping associated with the greatest key
                                                       // less than or equal to the given key,
                                                       //or null if there is no such key.
            map.put(start, h);
            map.put(end, tail);
            key = map.higherKey(start);
            while(key != null && key < end) {
                map.remove(key);
                key = map.higherKey(key);
            }
        }
        return list;
    }
}
'''