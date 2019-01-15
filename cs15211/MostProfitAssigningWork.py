__source__ = 'https://leetcode.com/problems/most-profit-assigning-work/'
# Time:  O(NLogN + QLogQ), where N is the number of jobs, and Q is the number of people.
# Space: O(N)
#
# Description: Leetcode # 826. Most Profit Assigning Work
#
# We have jobs: difficulty[i] is the difficulty of the ith job,
# and profit[i] is the profit of the ith job.
#
# Now we have some workers. worker[i] is the ability of the ith worker,
# which means that this worker can only complete a job with difficulty at most worker[i].
#
# Every worker can be assigned at most one job, but one job can be completed multiple times.
#
# For example, if 3 people attempt the same job that pays $1, then the total profit will be $3.
# If a worker cannot complete any job, his profit is $0.
#
# What is the most profit we can make?
#
# Example 1:
#
# Input: difficulty = [2,4,6,8,10], profit = [10,20,30,40,50], worker = [4,5,6,7]
# Output: 100
# Explanation: Workers are assigned jobs of difficulty [4,4,6,6]
# and they get profit of [20,20,30,30] seperately.
#
# Notes:
#
#     1 <= difficulty.length = profit.length <= 10000
#     1 <= worker.length <= 10000
#     difficulty[i], profit[i], worker[i]  are in range [1, 10^5]
#
import unittest
# 88ms 96.33%
class Solution(object):
    def maxProfitAssignment(self, difficulty, profit, worker):
        """
        :type difficulty: List[int]
        :type profit: List[int]
        :type worker: List[int]
        :rtype: int
        """
        jobs = zip(difficulty, profit)
        jobs.sort()
        ans = i = best = 0
        for skill in sorted(worker):
            while i < len(jobs) and skill >= jobs[i][0]:
                best = max(best, jobs[i][1])
                i += 1
            ans += best
        return ans

class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)


if __name__ == '__main__':
    unittest.main()

Java = '''
# Thought: https://leetcode.com/problems/most-profit-assigning-work/solution/
#
Approach #1: Sorting Events [Accepted]
Complexity Analysis
Time Complexity: O(NLogN + QLogQ), where N is the number of jobs, and Q is the number of people.
Space Complexity: O(N), the additional space used by jobs.

# 62ms 71.05%
import java.awt.Point;
class Solution {
    public int maxProfitAssignment(int[] difficulty, int[] profit, int[] worker) {
        int N = difficulty.length;
        Point[] jobs = new Point[N];
        for (int i = 0; i < N; ++i)
            jobs[i] = new Point(difficulty[i], profit[i]);
        Arrays.sort(jobs, (a, b) -> a.x - b.x);
        Arrays.sort(worker);
        int ans = 0, i = 0, best = 0;
        for (int skill : worker) {
            while (i < N && skill >= jobs[i].x) {
                best = Math.max(best, jobs[i++].y);
            }
            ans += best;
        }
        return ans;
    }
}

# 8ms 99.34%
class Solution {
    public int maxProfitAssignment(int[] difficulty, int[] profit, int[] worker) {
        int max = 0;
        for (int d : difficulty) {
            max = Math.max(max, d);
        }
        int[] map = new int[max + 1];
        for (int i = 0; i < difficulty.length; i++) {
            map[difficulty[i]] = Math.max(profit[i], map[difficulty[i]]);
        }
        
        for (int i = 1; i < map.length; i++) {
            map[i] = Math.max(map[i], map[i - 1]);
        }
        
        int sum = 0;
        for (int w : worker) {
            w = Math.min(max, w);
            sum += map[w];
        }
        return sum;
    }
}

'''
