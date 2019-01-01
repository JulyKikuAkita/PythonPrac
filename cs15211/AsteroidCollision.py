__source__ = 'https://leetcode.com/problems/asteroid-collision/'
# Time:  O(N)
# Space: O(N)
#
# Description: Leetcode # 735. Asteroid Collision
#
# We are given an array asteroids of integers representing asteroids in a row.
#
# For each asteroid, the absolute value represents its size,
# and the sign represents its direction (positive meaning right,
# negative meaning left). Each asteroid moves at the same speed.
#
# Find out the state of the asteroids after all collisions.
# If two asteroids meet, the smaller one will explode.
# If both are the same size, both will explode.
# Two asteroids moving in the same direction will never meet.
#
# Example 1:
# Input:
# asteroids = [5, 10, -5]
# Output: [5, 10]
# Explanation:
# The 10 and -5 collide resulting in 10.  The 5 and 10 never collide.
# Example 2:
# Input:
# asteroids = [8, -8]
# Output: []
# Explanation:
# The 8 and -8 collide exploding each other.
# Example 3:
# Input:
# asteroids = [10, 2, -5]
# Output: [10]
# Explanation:
# The 2 and -5 collide resulting in -5.  The 10 and -5 collide resulting in 10.
# Example 4:
# Input:
# asteroids = [-2, -1, 1, 2]
# Output: [-2, -1, 1, 2]
# Explanation:
# The -2 and -1 are moving left, while the 1 and 2 are moving right.
# Asteroids moving the same direction never meet, so no asteroids will meet each other.
# Note:
#
# The length of asteroids will be at most 10000.
# Each asteroid will be a non-zero integer in the range [-1000, 1000]..
#
import unittest

#40ms 80.99%
class Solution(object):
    def asteroidCollision(self, asteroids):
        """
        :type asteroids: List[int]
        :rtype: List[int]
        """
        ans = []
        for new in asteroids:
            while ans and new < 0 < ans[-1]:
                if ans[-1] < -new:
                    ans.pop()
                    continue
                elif ans[-1] == -new:
                    ans.pop()
                break
            else:
                ans.append(new)
        return ans

class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)


if __name__ == '__main__':
    unittest.main()

Java = '''
# Thought: https://leetcode.com/problems/asteroid-collision/solution/
# Approach #1: Stack [Accepted]
# Complexity Analysis
# Time Complexity: O(N), where N is the number of asteroids. Our stack pushes and pops each asteroid at most once.
# Space Complexity: O(N), the size of ans.
# 24ms 44.23%
class Solution {
    public int[] asteroidCollision(int[] asteroids) {
        Stack<Integer> s = new Stack<>();
        boolean doPush;
        for (int n : asteroids) {
            doPush = true;
            while (!s.isEmpty() && s.peek() > 0 && n < 0) {
                int cur = s.pop();
                if (cur > Math.abs(n)) n = cur;
                else if (cur == Math.abs(n)) {
                    doPush = false;
                    break;
                }
            } 
            if (doPush) s.push(n);
        }
        
        int[] ans = new int[s.size()];
        for (int i = s.size() - 1; i >= 0; i--) {
            ans[i] = s.pop();
        }
        return ans;
    }
}

# 10ms 99.72%
class Solution {
    public int[] asteroidCollision(int[] asteroids) {
        int l = -1, r = 0, n = asteroids.length;
        while (r < n) {
            //System.out.println("Entering while loop with l: " + l + ", r: " + r);
            if (l >= 0 && asteroids[l] > 0 && asteroids[r] < 0) {
                if (asteroids[l] > -asteroids[r]) r++;
                else if (asteroids[l] < -asteroids[r]) l--;
                else {
                    r++;
                    l--;
                }
               continue; //start from while loop
            }
            //System.out.println("l: " + l + ", r: " + r);
            asteroids[++l] = asteroids[r++];
        }
        return Arrays.copyOf(asteroids, l + 1);
    }
}

'''
