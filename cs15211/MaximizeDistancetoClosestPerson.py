__source__ = 'https://leetcode.com/problems/maximize-distance-to-closest-person/'
# Time:  O(N)
# Space: O(1)
#
# Description: Leetcode # 849. Maximize Distance to Closest Person
#
# In a row of seats, 1 represents a person sitting in that seat, and 0 represents that the seat is empty.
#
# There is at least one empty seat, and at least one person sitting.
#
# Alex wants to sit in the seat such that the distance between him and the closest person to him is maximized.
#
# Return that maximum distance to closest person.
#
# Example 1:
#
# Input: [1,0,0,0,1,0,1]
# Output: 2
# Explanation:
# If Alex sits in the second open seat (seats[2]), then the closest person has distance 2.
# If Alex sits in any other open seat, the closest person has distance 1.
# Thus, the maximum distance to the closest person is 2.
# Example 2:
#
# Input: [1,0,0,0]
# Output: 3
# Explanation:
# If Alex sits in the last seat, the closest person is 3 seats away.
# This is the maximum distance possible, so the answer is 3.
# Note:
#
# 1 <= seats.length <= 20000
# seats contains only 0s or 1s, at least one 0, and at least one 1.
#

import unittest

# 28ms 100%
class Solution(object):
    def maxDistToClosest(self, seats):
        """
        :type seats: List[int]
        :rtype: int
        """
        count = 0; max_count = 0; first = -1; last = -1

        for seat in seats:
            if seat == 0:
                count += 1
            else:
                if count > max_count : max_count = count
                if first == -1: first = count
                count = 0

        last = count

        if float(max_count) / 2 == float(max_count) // 2:
            return max(int(max_count / 2),first,last)
        else:
            return max(int(float(max_count) // 2) + 1, first, last)

class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)


if __name__ == '__main__':
    unittest.main()

Java = '''
#Thought: https://leetcode.com/problems/maximize-distance-to-closest-person/solution/
Approach #1: Next Array [Accepted]
Complexity Analysis
Time Complexity: O(N), where NN is the length of seats.
Space Complexity: O(N), the space used by left and right.
notice it is either left[i-1] + 1 if the seat is empty, or 0 if it is full.

#7ms 50.38%
class Solution {
    public int maxDistToClosest(int[] seats) {
        int N = seats.length;
        int[] left = new int[N], right = new int[N];
        Arrays.fill(left, N);
        Arrays.fill(right, N);

        for (int i = 0; i < N; i++) {
            if (seats[i] == 1) left[i] = 0;
            else if (i > 0) left[i] = left[i - 1] + 1;
        }

        for (int i = N - 1; i >= 0; i--) {
            if (seats[i] == 1) right[i] = 0;
            else if (i < N - 1) right[i] = right[i + 1] + 1;
        }

        int ans = 0;
        for (int i = 0; i < N; i++) {
            if (seats[i] == 0) ans = Math.max(ans, Math.min(left[i], right[i]));
        }
        return ans;
    }
}

Approach #2: Two Pointer [Accepted]
Complexity Analysis
Time Complexity: O(N), where NN is the length of seats.
Space Complexity: O(1).

# 6ms 78.66%
class Solution {
    public int maxDistToClosest(int[] seats) {
        int N = seats.length;
        int prev = -1, future = 0;
        int ans = 0;

        for (int i = 0; i < N; i++) {
            if (seats[i] == 1) {
                prev = i;
            } else {
                while (future < N && seats[future] == 0 || future < i) future++;

                int left = prev == -1 ? N : i - prev;
                int right = future == N ? N : future - i;
                ans = Math.max(ans, Math.min(left, right));
            }
        }
        return ans;
    }
}


Approach #3: Group by Zero [Accepted]
Complexity Analysis
Time Complexity: O(N), where NN is the length of seats.
Space Complexity: O(1). (In Python, seats[::-1] uses O(N)O(N) space, but this can be remedied.)
//In a group of K adjacent empty seats between two people, the answer is (K+1) / 2.

# 5ms 98.75%
class Solution {
    public int maxDistToClosest(int[] seats) {
        int N = seats.length;
        int K = 0; //current longest group of empty seats
        int ans = 0;

        for (int i = 0; i < N; i++) {
            if (seats[i] == 1) K = 0;
            else {
                K++;
                ans = Math.max(ans, ( K + 1) / 2);
            }
        }

        for (int i = 0; i < N; i++) {
            if (seats[i] == 1) {
                ans = Math.max( ans, i);
                break;
            }
        }

        for( int i = N - 1; i >= 0; i--) {
            if (seats[i] == 1) {
                ans = Math.max( ans, N - 1 - i);
                break;
            }
        }
        return ans;
    }
}

# 4ms 100%
class Solution {
    public int maxDistToClosest(int[] seats) {
        int n = seats.length;
        int max = 0;
        int i = 0;

        while (i < n){
            while (i < n && seats[i] == 1){
                i++;
            }

            int j = i;
            while (i < n && seats[i] == 0){
                i++;
            }

            if (j == 0 || i == n){
                max = Math.max(max, i - j);
            } else{
                max = Math.max(max, (i - j + 1) / 2) ;
            }
        }
        return max;
    }
}
'''