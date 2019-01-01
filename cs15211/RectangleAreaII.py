__source__ = 'https://leetcode.com/problems/rectangle-area-ii/'
# Time:  O()
# Space: O()
#
# Description: Leetcode # 850. Rectangle Area II
#
# We are given a list of (axis-aligned) rectangles.
# Each rectangle[i] = [x1, y1, x2, y2] ,
# where (x1, y1) are the coordinates of the bottom-left corner,
# and (x2, y2) are the coordinates of the top-right corner of the ith rectangle.
#
# Find the total area covered by all rectangles in the plane.
# Since the answer may be too large, return it modulo 10^9 + 7.
#
# Example 1:
#
# Input: [[0,0,2,2],[1,0,2,3],[1,0,3,1]]
# Output: 6
# Explanation: As illustrated in the picture.
#
# Example 2:
#
# Input: [[0,0,1000000000,1000000000]]
# Output: 49
# Explanation: The answer is 10^18 modulo (10^9 + 7), which is (10^9)^2 = (-7)^2 = 49.
#
# Note:
#
# 1 <= rectangles.length <= 200
# rectanges[i].length = 4
# 0 <= rectangles[i][j] <= 10^9
# The total area covered by all rectangles will never exceed 2^63 - 1
# and thus will fit in a 64-bit signed integer.
#
import unittest

# 52ms 49.44%
class Solution(object):
    def rectangleArea(self, rectangles):
        # Populate events
        OPEN, CLOSE = 0, 1
        events = []
        for x1, y1, x2, y2 in rectangles:
            events.append((y1, OPEN, x1, x2))
            events.append((y2, CLOSE, x1, x2))
        events.sort()

        def query():
            ans = 0
            cur = -1
            for x1, x2 in active:
                cur = max(cur, x1)
                ans += max(0, x2 - cur)
                cur = max(cur, x2)
            return ans

        active = []
        cur_y = events[0][0]
        ans = 0
        for y, typ, x1, x2 in events:
            # For all vertical ground covered, update answer
            ans += query() * (y - cur_y)

            # Update active intervals
            if typ is OPEN:
                active.append((x1, x2))
                active.sort()
            else:
                active.remove((x1, x2))

            cur_y = y

        return ans % (10**9 + 7)

class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)


if __name__ == '__main__':
    unittest.main()

Java = '''
# Thought: https://leetcode.com/problems/rectangle-area-ii/solution/
#
Approach #1: Principle of Inclusion-Exclusion
Complexity Analysis
Time Complexity: O(N*2^N), where N is the number of rectangles.
Space Complexity: O(N)
# TLE
class Solution {
    public int rectangleArea(int[][] rectangles) {
        int N = rectangles.length;

        long ans = 0;
        for (int subset = 1; subset < (1<<N); ++subset) {
            int[] rec = new int[]{0, 0, 1_000_000_000, 1_000_000_000};
            int parity = -1;
            for (int bit = 0; bit < N; ++bit)
                if (((subset >> bit) & 1) != 0) {
                    rec = intersect(rec, rectangles[bit]);
                    parity *= -1;
                }
            ans += parity * area(rec);
        }

        long MOD = 1_000_000_007;
        ans %= MOD;
        if (ans < 0) ans += MOD;
        return (int) ans;
    }

    public long area(int[] rec) {
        long dx = Math.max(0, rec[2] - rec[0]);
        long dy = Math.max(0, rec[3] - rec[1]);
        return dx * dy;
    }

    public int[] intersect(int[] rec1, int[] rec2) {
        return new int[]{
            Math.max(rec1[0], rec2[0]),
            Math.max(rec1[1], rec2[1]),
            Math.min(rec1[2], rec2[2]),
            Math.min(rec1[3], rec2[3]),
        };
    }
}



Approach #2: Coordinate Compression
Complexity Analysis
Time Complexity: O(N^3), where N is the number of rectangles.
Space Complexity: O(N^2)
# 40ms 78.85%
class Solution {
    public int rectangleArea(int[][] rectangles) {
        int N = rectangles.length;
        Set<Integer> Xvals = new HashSet();
        Set<Integer> Yvals = new HashSet();

        for (int[] rec: rectangles) {
            Xvals.add(rec[0]);
            Xvals.add(rec[2]);
            Yvals.add(rec[1]);
            Yvals.add(rec[3]);
        }

        Integer[] imapx = Xvals.toArray(new Integer[0]);
        Arrays.sort(imapx);
        Integer[] imapy = Yvals.toArray(new Integer[0]);
        Arrays.sort(imapy);

        Map<Integer, Integer> mapx = new HashMap();
        Map<Integer, Integer> mapy = new HashMap();
        for (int i = 0; i < imapx.length; ++i)
            mapx.put(imapx[i], i);
        for (int i = 0; i < imapy.length; ++i)
            mapy.put(imapy[i], i);

        boolean[][] grid = new boolean[imapx.length][imapy.length];
        for (int[] rec: rectangles)
            for (int x = mapx.get(rec[0]); x < mapx.get(rec[2]); ++x)
                for (int y = mapy.get(rec[1]); y < mapy.get(rec[3]); ++y)
                    grid[x][y] = true;

        long ans = 0;
        for (int x = 0; x < grid.length; ++x)
            for (int y = 0; y < grid[0].length; ++y)
                if (grid[x][y])
                    ans += (long) (imapx[x+1] - imapx[x]) * (imapy[y+1] - imapy[y]);

        ans %= 1_000_000_007;
        return (int) ans;
    }
}

Approach #3: Line Sweep
Complexity Analysis
Time Complexity: O(N^2Log N), where N is the number of rectangles.
Space Complexity: O(N). 
# 45ms 76.65%
class Solution {
    public int rectangleArea(int[][] rectangles) {
        int OPEN = 0, CLOSE = 1;
        int[][] events = new int[rectangles.length * 2][];
        int t = 0;
        for (int[] rec: rectangles) {
            events[t++] = new int[]{rec[1], OPEN, rec[0], rec[2]};
            events[t++] = new int[]{rec[3], CLOSE, rec[0], rec[2]};
        }

        Arrays.sort(events, (a, b) -> Integer.compare(a[0], b[0]));

        List<int[]> active = new ArrayList();
        int cur_y = events[0][0];
        long ans = 0;
        for (int[] event: events) {
            int y = event[0], typ = event[1], x1 = event[2], x2 = event[3];

            // Calculate query
            long query = 0;
            int cur = -1;
            for (int[] xs: active) {
                cur = Math.max(cur, xs[0]);
                query += Math.max(xs[1] - cur, 0);
                cur = Math.max(cur, xs[1]);
            }

            ans += query * (y - cur_y);

            if (typ == OPEN) {
                active.add(new int[]{x1, x2});
                Collections.sort(active, (a, b) -> Integer.compare(a[0], b[0]));
            } else {
                for (int i = 0; i < active.size(); ++i)
                    if (active.get(i)[0] == x1 && active.get(i)[1] == x2) {
                        active.remove(i);
                        break;
                    }
            }

            cur_y = y;
        }

        ans %= 1_000_000_007;
        return (int) ans;
    }
}

Approach #4: Segment Tree
Complexity Analysis
Time Complexity: O(NLogN), where N is the number of rectangles.
Space Complexity: O(N)

# 48ms 73.63%
class Solution {
    public int rectangleArea(int[][] rectangles) {
        int OPEN = 1, CLOSE = -1;
        int[][] events = new int[rectangles.length * 2][];
        Set<Integer> Xvals = new HashSet();
        int t = 0;
        for (int[] rec: rectangles) {
            events[t++] = new int[]{rec[1], OPEN, rec[0], rec[2]};
            events[t++] = new int[]{rec[3], CLOSE, rec[0], rec[2]};
            Xvals.add(rec[0]);
            Xvals.add(rec[2]);
        }

        Arrays.sort(events, (a, b) -> Integer.compare(a[0], b[0]));

        Integer[] X = Xvals.toArray(new Integer[0]);
        Arrays.sort(X);
        Map<Integer, Integer> Xi = new HashMap();
        for (int i = 0; i < X.length; ++i)
            Xi.put(X[i], i);

        Node active = new Node(0, X.length - 1, X);
        long ans = 0;
        long cur_x_sum = 0;
        int cur_y = events[0][0];

        for (int[] event: events) {
            int y = event[0], typ = event[1], x1 = event[2], x2 = event[3];
            ans += cur_x_sum * (y - cur_y);
            cur_x_sum = active.update(Xi.get(x1), Xi.get(x2), typ);
            cur_y = y;

        }

        ans %= 1_000_000_007;
        return (int) ans;
    }
}

class Node {
    int start, end;
    Integer[] X;
    Node left, right;
    int count;
    long total;

    public Node(int start, int end, Integer[] X) {
        this.start = start;
        this.end = end;
        this.X = X;
        left = null;
        right = null;
        count = 0;
        total = 0;
    }

    public int getRangeMid() {
        return start + (end - start) / 2;
    }

    public Node getLeft() {
        if (left == null) left = new Node(start, getRangeMid(), X);
        return left;
    }

    public Node getRight() {
        if (right == null) right = new Node(getRangeMid(), end, X);
        return right;
    }

    public long update(int i, int j, int val) {
        if (i >= j) return 0;
        if (start == i && end == j) {
            count += val;
        } else {
            getLeft().update(i, Math.min(getRangeMid(), j), val);
            getRight().update(Math.max(getRangeMid(), i), j, val);
        }

        if (count > 0) total = X[end] - X[start];
        else total = getLeft().total + getRight().total;

        return total;
    }
}

# 7ms 97.51%
class Solution {
    private static long M = (long)1e9+7;
    
    public int rectangleArea(int[][] rectangles) {
        if (rectangles == null || rectangles.length == 0) return 0;
        long area = 0;
        for (int[] r : rectangles) {
            area = (area + areaOf(r[0], r[1], r[2], r[3])) % M;
        }
        
        for (int i = 0; i < rectangles.length; i++) {
            area = (area - overlap(rectangles, rectangles[i], i + 1) + M) % M;
        }
        return (int) area;
            
    }
    
    private long overlap(int[][] rectangles, int[] a, int idx) {
        if (idx == rectangles.length) return 0L;
        int[] b = rectangles[idx++];
        //if no overlap, return 
        if (Math.max(a[0], b[0]) >= Math.min(a[2], b[2]) || Math.max(a[1], b[1]) >= Math.min(a[3], b[3])) {
            return overlap(rectangles, a, idx);
        }
        
        //if there is overlap
        long area = areaOf(Math.max(a[0], b[0]), Math.max(a[1], b[1]), Math.min(a[2], b[2]), Math.min(a[3], b[3]));
        //find the overlap area between (a - b) and next b
        if (a[0] < b[0]) {
            int[] next = new int[] {a[0], a[1], b[0], a[3]};
            area = (area + overlap(rectangles, next, idx)) % M;
        }
        if (a[2] > b[2]) {
            int[] next = new int[] {b[2], a[1], a[2], a[3]};
            area = (area + overlap(rectangles, next, idx)) % M;
        }
        
        if (a[1] < b[1]) {
            int[] next = new int[]{Math.max(a[0], b[0]), a[1], Math.min(a[2], b[2]), b[1]};
            area = (area + overlap(rectangles, next, idx)) % M;
        }
        if (a[3] > b[3]) {
            int[] next = new int[] {Math.max(a[0], b[0]), b[3], Math.min(a[2], b[2]), a[3]};
            area = (area + overlap(rectangles, next, idx)) % M;
        }
        return area % M;
    }
    
    private long areaOf(int x1, int y1, int x2, int y2) {
        return (long) (x2 - x1) * (y2 - y1);
    }
}
'''
