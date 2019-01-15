__source__ = 'https://leetcode.com/problems/random-flip-matrix/'
# Time:  O()
# Space: O()
#
# Description: Leetcode # 519. Random Flip Matrix
#
# You are given the number of rows n_rows and number of columns n_cols of a 2D binary matrix
# where all values are initially 0.
# Write a function flip which chooses a 0 value uniformly at random,
# changes it to 1, and then returns the position [row.id, col.id] of that value.
# Also, write a function reset which sets all values back to 0.
# Try to minimize the number of calls to system's Math.random()
# and optimize the time and space complexity.
#
# Note:
#
#     1 <= n_rows, n_cols <= 10000
#     0 <= row.id < n_rows and 0 <= col.id < n_cols
#     flip will not be called when the matrix has no 0 values left.
#     the total number of calls to flip and reset will not exceed 1000.
#
# Example 1:
#
# Input:
# ["Solution","flip","flip","flip","flip"]
# [[2,3],[],[],[],[]]
# Output: [null,[0,1],[1,2],[1,0],[1,1]]
#
# Example 2:
#
# Input:
# ["Solution","flip","flip","reset","flip"]
# [[1,2],[],[],[],[]]
# Output: [null,[0,0],[0,1],null,[0,0]]
#
# Explanation of Input Syntax:
#
# The input is two lists: the subroutines called and their arguments.
# Solution's constructor has two arguments, n_rows and n_cols.
# flip and reset have no arguments. Arguments are always wrapped with a list,
# even if there aren't any.
#
import unittest


class Solution:
    pass  # start coding


class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)


if __name__ == '__main__':
    unittest.main()

Java = '''
# Thought: https://leetcode.com/problems/random-flip-matrix/solution/
#
Approach 1: Virtual Array

# 87ms 79.13%
class Solution {
    Map<Integer, Integer> V = new HashMap<>();
    int nr, nc, rem;
    Random rand = new Random();

    public Solution(int n_rows, int n_cols) {
        nr = n_rows;
        nc = n_cols;
        rem = nr * nc;
    }
    
    public int[] flip() {
        int r = rand.nextInt(rem--);
        int x = V.getOrDefault(r, r);
        V.put(r, V.getOrDefault(rem, rem));
        return new int[]{x / nc, x % nc};
    }
    
    public void reset() {
        V.clear();
        rem = nr * nc;
    }
}

/**
 * Your Solution object will be instantiated and called as such:
 * Solution obj = new Solution(n_rows, n_cols);
 * int[] param_1 = obj.flip();
 * obj.reset();
 */

Approach 2: Square-Root Decomposition

# 188ms 3.04%
class Solution {
    int nr, nc, rem, b_size;
    List<Set<Integer>> buckets = new ArrayList<>();
    Random rand = new Random();
    
    public Solution(int n_rows, int n_cols) {
        nr = n_rows;
        nc = n_cols;
        rem = nr * nc;
        b_size = (int) Math.sqrt(nr * nc);
        for (int i = 0; i < nr * nc; i+= b_size)
            buckets.add(new HashSet<Integer>());
    }
    
    public int[] flip() {
        int c = 0;
        int c0 = 0;
        int k = rand.nextInt(rem);
        for (Set<Integer> b1 : buckets) {
            if (c0 + b_size - b1.size() > k) {
                while (true) {
                    if (!b1.contains(c)) {
                        if (c0 == k) {
                            b1.add(c);
                            rem--;
                            return new int[]{c / nc, c % nc};
                        }
                        c0++;
                    }
                    c++;
                }
            }
            c += b_size;
            c0 += b_size - b1.size();
        }
        return null;
    }
    
    public void reset() {
        for (Set<Integer> b1 : buckets)
            b1.clear();
        rem = nr * nc;
    }
}

'''
