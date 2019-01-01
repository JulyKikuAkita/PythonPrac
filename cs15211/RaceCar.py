# coding=utf-8
__source__ = 'https://leetcode.com/problems/race-car/'
# Time:  O()
# Space: O()
#
# Description: Leetcode # 818. Race Car
#
# Your car starts at position 0 and speed +1 on an infinite number line.  (Your car can go into negative positions.)
#
# Your car drives automatically according to a sequence of instructions A (accelerate) and R (reverse).
#
# When you get an instruction "A", your car does the following: position += speed, speed *= 2.
#
# When you get an instruction "R", your car does the following:
# if your speed is positive then speed = -1 , otherwise speed = 1.  (Your position stays the same.)
#
# For example, after commands "AAR", your car goes to positions 0->1->3->3, and your speed goes to 1->2->4->-1.
#
# Now for some target position, say the length of the shortest sequence of instructions to get there.
#
# Example 1:
# Input:
# target = 3
# Output: 2
# Explanation:
# The shortest instruction sequence is "AA".
# Your position goes from 0->1->3.
#
# Example 2:
# Input:
# target = 6
# Output: 5
# Explanation:
# The shortest instruction sequence is "AAARA".
# Your position goes from 0->1->3->7->7->6.
#
# Note:
#
#     1 <= target <= 10000.
#
import unittest

# 168ms 62.74%
class Solution(object):
    def racecar(self, target):
        """
        :type target: int
        :rtype: int
        """
        dp = [0, 1, 4] + [float('inf')] * target
        for t in xrange(3, target + 1):
            k = t.bit_length()
            if t == 2**k - 1:
                dp[t] = k
                continue
            for j in xrange(k - 1):
                dp[t] = min(dp[t], dp[t - 2**(k - 1) + 2**j] + k - 1 + j + 2)
            if 2**k - 1 - t < t:
                dp[t] = min(dp[t], dp[2**k - 1 - t] + k + 1)
        return dp[target]

class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)


if __name__ == '__main__':
    unittest.main()

Java = '''
# Thought: https://leetcode.com/problems/race-car/solution/
#
Approach #1: Dijkstra's [Accepted]
Complexity Analysis
Time Complexity: O(TlogT). There are O(T) nodes, we process each one using O(logT) work 
(both popping from the heap and adding the edges).
Space Complexity: O(T)

# 188ms 41.28%
class Solution {
    public int racecar(int target) {
        int K = 33 - Integer.numberOfLeadingZeros(target - 1);
        int barrier = 1 << K;
        int[] dist = new int[2 * barrier + 1];
        Arrays.fill(dist, Integer.MAX_VALUE);
        dist[target] = 0;

        PriorityQueue<Node> pq = new PriorityQueue<Node>(
            (a, b) -> a.steps - b.steps);
        pq.offer(new Node(0, target));

        while (!pq.isEmpty()) {
            Node node = pq.poll();
            int steps = node.steps, targ1 = node.target;
            if (dist[Math.floorMod(targ1, dist.length)] > steps) continue;

            for (int k = 0; k <= K; ++k) {
                int walk = (1 << k) - 1;
                int targ2 = walk - targ1;
                int steps2 = steps + k + (targ2 != 0 ? 1 : 0);

                if (Math.abs(targ2) <= barrier && steps2 < dist[Math.floorMod(targ2, dist.length)]) {
                    pq.offer(new Node(steps2, targ2));
                    dist[Math.floorMod(targ2, dist.length)] = steps2;
                }
            }
        }

        return dist[0];
    }
}

class Node {
    int steps, target;
    Node(int s, int t) {
        steps = s;
        target = t;
    }
}


Approach #2: Dynamic Programming [Accepted]
Complexity Analysis
Time Complexity:O(TlogT). Each node i does logi work.
Space Complexity: O(T)

# 13ms 62.98%
class Solution {
    public int racecar(int target) {
        int[] dp = new int[target + 3];
        Arrays.fill(dp, Integer.MAX_VALUE);
        dp[0] = 0; dp[1] = 1; dp[2] = 4;

        for (int t = 3; t <= target; ++t) {
            int k = 32 - Integer.numberOfLeadingZeros(t);
            if (t == (1<<k) - 1) {
                dp[t] = k;
                continue;
            }
            for (int j = 0; j < k-1; ++j)
                dp[t] = Math.min(dp[t], dp[t - (1<<(k-1)) + (1<<j)] + k-1 + j + 2);
            if ((1<<k) - 1 - t < t)
                dp[t] = Math.min(dp[t], dp[(1<<k) - 1 - t] + k + 1);
        }

        return dp[target];  
    }
}

# 2ms 100%
class Solution { //bfs is slow;
     int[] dp = new int[10001];
    public int racecar(int t) {
        if (dp[t] > 0) return dp[t];
        int n = (int)(Math.log(t) / Math.log(2)) + 1;
        if (1 << n == t + 1) dp[t] = n;
        else {
            dp[t] = racecar((1 << n) - 1 - t) + n + 1;
            for (int m = 0; m < n - 1; ++m)
                dp[t] = Math.min(dp[t], racecar(t - (1 << (n - 1)) + (1 << m)) + n + m + 1);
        }
        return dp[t];
    }
}


# comments
class Solution {
    public int racecar(int target) {
        // target是position，或者为了好理解，target表示lane number。
        // 因为题目要求position是从0开始算起，所以在这道题里，target要当做index来看待。
        // dp[i]表示到达position i需要的最少步数。
        int[] dp = new int[target+1];
        return helper(dp, target);
    }
    
    private int helper(int[] dp, int target) {
        if (dp[target] > 0) {
            return dp[target];
        }
        /**
            x = log2(n) (log以2为底n)，该等式意思是：2的x次方等于n (即Math.pow(2, x) == n)。
            loga(b) == logc(b) / logc(a)：log以a为底的b = log以c为底的b / log以c为底的a。
            
            java里Math.log(n)表示：log以e为底的n，意思是e的多少次方等于n。
        */

        // n表示从0开始，一直向右加速('A')，第一次到达或超过当前position target，需要多少步 (即从0开始要连续多少个'A'才能到达或超过target)。
        // 因为target相当于index，所以要加1后再计算。

        // 举例：
        // 如果target = 4，则0 --> 1 --> 3 --> 7，需要三个'A'。
        // (int) Math.ceil(Math.log(4) / Math.log(2)) = 2；
        // (int) Math.ceil(Math.log(4 + 1) / Math.log(2)) = 3。
        int n = (int) Math.ceil(Math.log(target + 1) / Math.log(2));
        if ((1 << n) == target + 1) { // 如果连续加速n步后等于position i，而并没有超过它，这是最好情形。
            dp[target] = n;
        } else { // 否则我们要考虑两种情况，步数少的就是dp[target]的值：
                 //     1. 超过position target，到达紧挨着target右边的加速点后，再掉头返回到target的总步数。
                 //     2. 没到position target，到达紧挨着target左边的加速点后，掉头返回加速走i步，再掉头加速走到position target的总步数。
            
            // 第一种情况：
            // (1 << n) - (target + 1)是连续加速走n步后比position target超过的长度。
            // 长度 - 长度 = index。
            // n表示从0开始连续加速n步，1表示掉头操作。
            dp[target] = helper(dp, (1 << n) - (target + 1)) + n + 1;
            
            // 第二种情况：
            // i是到达紧挨着target左边的加速点后 (此时走了n - 1步)，再掉头返回走i步 (i的取值范围是[0, n - 1)，0表示掉头再掉头，把速度降为1。n - 1表示往回最多可以走小于n - 1步，因为刚刚只加速走了n - 1步，如果往回走n - 1步等于回到原点，没意义。)。
            // target - (1 << (n - 1)) + (1 << i)表示从往回走i步后停下来的position到position target的长度。
            for (int i = 0; i < n - 1; i++) {
                // n - 1是向右加速走n - 1步，1是掉头准备向左走，i是向左加速走i步，1是掉头准备向右走。
                dp[target] = Math.min(dp[target], helper(dp, target - (1 << (n - 1)) + (1 << i)) + (n - 1) + 1 + i + 1);
            }
        }
        return dp[target];
    }
}

'''
