# coding=utf-8
__source__ = 'https://leetcode.com/problems/implement-rand10-using-rand7/'
# Time:  O(1) average, but O(∞) worst case.
# Space: O(1)
#
# Description: Leetcode # 470. Implement Rand10() Using Rand7()
#
# Given a function rand7 which generates a uniform random integer in the range 1 to 7,
# write a function rand10 which generates a uniform random integer in the range 1 to 10.
#
# Do NOT use system's Math.random().
#
# Example 1:
#
# Input: 1
# Output: [7]
# Example 2:
#
# Input: 2
# Output: [8,4]
# Example 3:
#
# Input: 3
# Output: [8,1,10]
#
#
# Note:
#
# rand7 is predefined.
# Each testcase has one argument: n, the number of times that rand10 is called.
#
# Follow up:
#
# What is the expected value for the number of calls to rand7() function?
# Could you minimize the number of calls to rand7()?
#
import unittest


class Solution(object):
    pass  # your function here


class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)


if __name__ == '__main__':
    unittest.main()

Java = '''
# Thought: https://leetcode.com/problems/implement-rand10-using-rand7/solution/
# Approach 1: Rejection Sampling

# 5ms 99.55%
Complexity Analysis
Time Complexity: O(1) average, but O(∞) worst case.
Space Complexity: O(1)

/**
 * The rand7() API is already defined in the parent class SolBase.
 * public int rand7();
 * @return a random integer in the range 1 to 7
 */
class Solution extends SolBase {
    public int rand10() {
        int row, col, idx;
        do {
            row = rand7();
            col = rand7();
            idx = col + (row - 1) * 7;
        } while (idx > 40);
        return 1 + (idx - 1)  % 10;
    }
}

Approach 2: Utilizing out-of-range samples

class Solution extends SolBase {
    public int rand10() {
        int a, b, idx;
        while (true) {
            a = rand7();
            b = rand7();
            idx = b + (a - 1) * 7;
            if (idx <= 40) return 1 + (idx - 1) % 10;
            a = idx - 40;
            b = rand7();
            // get uniform dist from 1 - 63
            idx = b + (a - 1) * 7;
            if (idx <= 60) {
                return 1 + (idx - 1) % 10;
            }
            a = idx - 60;
            b = rand7();
            // get uniform dist from 1 - 21
            idx = b + (a - 1) * 7;
            if (idx <= 20) return 1 + (idx - 1) % 10;
        }
    }
}


#5ms 99.55%
/**
 * The rand7() API is already defined in the parent class SolBase.
 * public int rand7();
 * @return a random integer in the range 1 to 7
 */
class Solution extends SolBase {
    public int rand10() {
        int result = 40;
        while (result >= 40) {result = 7 * (rand7() - 1) + (rand7() - 1);}
        return result % 10 + 1;
    }
}


'''