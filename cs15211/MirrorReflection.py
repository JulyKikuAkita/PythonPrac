__source__ = 'https://leetcode.com/problems/mirror-reflection/'
# Time:  O(logP)
# Space: O(1)
#
# Description: Leetcode # 858. Mirror Reflection
#
# There is a special square room with mirrors on each of the four walls.
# Except for the southwest corner, there are receptors on each of the remaining corners, numbered 0, 1, and 2.
#
# The square room has walls of length p,
# and a laser ray from the southwest corner first meets the east wall at a distance q from the 0th receptor.
#
# Return the number of the receptor that the ray meets first.
# (It is guaranteed that the ray will meet a receptor eventually.)
#
# Example 1:
#
# Input: p = 2, q = 1
# Output: 2
# Explanation: The ray meets receptor 2 the first time it gets reflected back to the left wall.
#
# Note:
#     1 <= p <= 1000
#     0 <= q <= p
#
import unittest
# 24ms 50%
class Solution(object):
    def mirrorReflection(self, p, q):
        """
        :type p: int
        :type q: int
        :rtype: int
        """
        from fractions import gcd
        g = gcd(p, q)
        p = (p / g) % 2
        q = (q / g) % 2

        return 1 if p and q else 0 if p else 2

class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)

if __name__ == '__main__':
    unittest.main()

Java = '''
# Thought: https://leetcode.com/problems/mirror-reflection/solution/
#
Approach 1: Simulation
Complexity Analysis
Time Complexity: O(p). We can prove (using Approach #2) that the number of bounces is bounded by this.
Space Complexity: O(1) 

# 6ms 11.06%
class Solution {
    double EPS = 1e-6;
    
    public int mirrorReflection(int p, int q) {
        double x = 0, y = 0;
        double rx = p, ry = q;    

        // While it hasn't reached a receptor,...
        while ( !(close(x, p) && (close(y, 0) || close(y, p)) || close(x, 0) && close(y, p))) {
            // Want smallest t so that some x + rx, y + ry is 0 or p
            // x + rxt = 0, then t = -x/rx etc.
            double t = 1e9;
            if ((-x / rx) > EPS) t = Math.min(t, -x / rx);
            if ((-y / ry) > EPS) t = Math.min(t, -y / ry);
            if (((p-x) / rx) > EPS) t = Math.min(t, (p-x) / rx);
            if (((p-y) / ry) > EPS) t = Math.min(t, (p-y) / ry);

            x += rx * t;
            y += ry * t;
            
            if (close(x, p) || close(x, 0)) rx *= -1;
            if (close(y, p) || close(y, 0)) ry *= -1;
        }
        if (close(x, p) && close(y, p)) return 1;
        return close(x, p) ? 0 : 2;
    }
    
    private boolean close(double x, double y) {
        return Math.abs(x - y) < EPS;
    }
}

Approach 2: Mathematical
Complexity Analysis
Time Complexity: O(logP), the complexity of the gcd operation.
Space Complexity: O(1)
The mathematical answer is k = p / gcd(p, q).

# 2ms 100%
class Solution {
    public int mirrorReflection(int p, int q) {
        int g = gcd(p, q);
        p /= g; p %= 2;
        q /= g; q %= 2;
        
        if (p == 1 && q == 1) return 1;
        return p == 1 ? 0 : 2;
    }
    
    private int gcd(int a, int b) {
        return a == 0 ? b : gcd(b % a, a);
    }
}

'''
