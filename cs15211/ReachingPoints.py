__source__ = 'https://leetcode.com/problems/reaching-points/'
# Time:  O()
# Space: O()
#
# Description: Leetcode # 780. Reaching Points
#
# A move consists of taking a point (x, y) and transforming it to either (x, x+y) or (x+y, y).
#
# Given a starting point (sx, sy) and a target point (tx, ty),
# return True if and only if a sequence of moves exists to transform the point (sx, sy) to (tx, ty).
# Otherwise, return False.
#
# Examples:
# Input: sx = 1, sy = 1, tx = 3, ty = 5
# Output: True
# Explanation:
# One series of moves that transforms the starting point to the target is:
# (1, 1) -> (1, 2)
# (1, 2) -> (3, 2)
# (3, 2) -> (3, 5)
#
# Input: sx = 1, sy = 1, tx = 2, ty = 2
# Output: False
#
# Input: sx = 1, sy = 1, tx = 1, ty = 1
# Output: True
#
# Note:
# sx, sy, tx, ty will all be integers in the range [1, 10^9].
#
import unittest

# 20ms 100%
class Solution(object):
    def reachingPoints(self, sx, sy, tx, ty):
        """
        :type sx: int
        :type sy: int
        :type tx: int
        :type ty: int
        :rtype: bool
        """
        while tx >= sx and ty >= sy:
            if tx == ty:
                break
            elif tx > ty:
                if ty > sy:
                    tx %= ty
                else:
                    return (tx - sx) % ty == 0
            else:
                if tx > sx:
                    ty %= tx
                else:
                    return (ty - sy) % tx == 0
        return tx == sx and ty == sy

class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)


if __name__ == '__main__':
    unittest.main()

Java = '''
# Thought: https://leetcode.com/problems/reaching-points/solution/
#
Approach #1: Exhaustive Search [Time Limit Exceeded]
Complexity Analysis
Time Complexity: O(2^(tx + ty)), a loose bound found by considering every move 
as (x, y) -> (x+1, y) or (x, y) -> (x, y+1) instead.
Space Complexity: O(tx * ty), the size of the implicit call stack

# TLE
class Solution {
    public boolean reachingPoints(int sx, int sy, int tx, int ty) {
        if (sx > tx || sy > ty) return false;
        if (sx == tx && sy == ty) return true;
        return reachingPoints(sx+sy, sy, tx, ty) || reachingPoints(sx, sx+sy, tx, ty);
    }
}

Approach #2: Dynamic Programming [Time Limit Exceeded]
Complexity Analysis
Time Complexity: O(tx * ty), as at most tx * ty points are searched once per point.
Space Complexity: O(tx * ty), the size of the implicit call stack.

# TLE
import java.awt.Point;
class Solution {
    Set<Point> seen;
    int tx, ty;

    public boolean reachingPoints(int sx, int sy, int tx, int ty) {
        seen = new HashSet();
        this.tx = tx;
        this.ty = ty;
        search(new Point(sx, sy));
        return seen.contains(new Point(tx, ty));
    }

    public void search(Point P) {
        if (seen.contains(P)) return;
        if (P.x > tx || P.y > ty) return;
        seen.add(P);
        search(new Point(P.x + P.y, P.y));
        search(new Point(P.x, P.x + P.y));
    }
}

Approach #3: Work Backwards (Naive Variant) [Time Limit Exceeded]
Complexity Analysis
Time Complexity: O(max(tx,ty)). If say ty = 1, we could be subtracting tx times.
Space Complexity: O(1)
# trying to transform the target point to the starting point via applying the parent operation 
(x, y) -> (x-y, y) or (x, y-x) [depending on which one doesn't have negative coordinates.]
# TLE
class Solution {
    public boolean reachingPoints(int sx, int sy, int tx, int ty) {
        while (tx >= sx && ty >= sy) {
            if (sx == tx && sy == ty)
                return true;
            if (tx > ty) tx -= ty;
            else ty -= tx;
        }
        return false;
    }
}

Approach #4: Work Backwards (Modulo Variant) [Accepted]
Complexity Analysis
Time Complexity: O(log(max(tx,ty))). The analysis is similar to the analysis of the Euclidean algorithm, 
and we assume that the modulo operation can be done in O(1) time.
Space Complexity: O(1)

Say tx > ty. 
We know that the next parent operations will be to subtract ty from tx, 
until such time that tx = tx % ty. 
When both tx > ty and ty > sy, we can perform all these parent operations in one step, 
replacing while tx > ty: tx -= ty with tx %= ty.

# 5ms 100%
class Solution {
    public boolean reachingPoints(int sx, int sy, int tx, int ty) {
        while (tx >= sx && ty >= sy) {
            if (tx == ty) break;
            if (tx > ty) {
                if (ty > sy) tx %= ty;
                else return (tx - sx) % ty == 0;
            } else {
                if (tx > sx) ty %= tx;
                else return (ty - sy) % tx == 0;
            }
        }
        return (tx == sx && ty == sy);
    }
}

'''
