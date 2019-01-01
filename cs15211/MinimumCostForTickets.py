__source__ = 'https://leetcode.com/problems/minimum-cost-for-tickets/'
# Time:  O()
# Space: O()
#
# Description: Leetcode # 983. Minimum Cost For Tickets
#
# In a country popular for train travel, you have planned some train travelling one year in advance.
# The days of the year that you will travel is given as an array days.
# Each day is an integer from 1 to 365.
#
# Train tickets are sold in 3 different ways:
#
# a 1-day pass is sold for costs[0] dollars;
# a 7-day pass is sold for costs[1] dollars;
# a 30-day pass is sold for costs[2] dollars.
# The passes allow that many days of consecutive travel.
# For example, if we get a 7-day pass on day 2, then we can travel for 7 days: day 2, 3, 4, 5, 6, 7, and 8.
#
# Return the minimum number of dollars you need to travel every day in the given list of days.
#
# Example 1:
#
# Input: days = [1,4,6,7,8,20], costs = [2,7,15]
# Output: 11
# Explanation:
# For example, here is one way to buy passes that lets you travel your travel plan:
# On day 1, you bought a 1-day pass for costs[0] = $2, which covered day 1.
# On day 3, you bought a 7-day pass for costs[1] = $7, which covered days 3, 4, ..., 9.
# On day 20, you bought a 1-day pass for costs[0] = $2, which covered day 20.
# In total you spent $11 and covered all the days of your travel.
# Example 2:
#
# Input: days = [1,2,3,4,5,6,7,8,9,10,30,31], costs = [2,7,15]
# Output: 17
# Explanation:
# For example, here is one way to buy passes that lets you travel your travel plan:
# On day 1, you bought a 30-day pass for costs[2] = $15 which covered days 1, 2, ..., 30.
# On day 31, you bought a 1-day pass for costs[0] = $2 which covered day 31.
# In total you spent $17 and covered all the days of your travel.
#
#
# Note:
#
# 1 <= days.length <= 365
# 1 <= days[i] <= 365
# days is in strictly increasing order.
# costs.length == 3
# 1 <= costs[i] <= 1000
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
# Thought: https://leetcode.com/problems/minimum-cost-for-tickets/solution/
Approach 1: Dynamic Programming (Day Variant)
Complexity Analysis
Time Complexity: O(W), where W = 365 is the maximum numbered day in your travel plan.
Space Complexity: O(W). 
# 7ms 29.10%
class Solution {
    int[] costs;
    Integer[] memo;
    Set<Integer> dayset;
    
    public int mincostTickets(int[] days, int[] costs) {
        this.costs = costs;
        memo = new Integer[366];
        dayset = new HashSet();
        for (int d: days) dayset.add(d);

        return dp(1);
    }
    
    public int dp(int i) {
        if (i > 365) return 0;
        if (memo[i] != null) return memo[i];
        int ans = 0;
        if (dayset.contains(i)) {
            ans = Math.min(dp(i + 1) + costs[0], 
                          dp(i + 7) + costs[1]);
            ans = Math.min(ans, dp(i+30) + costs[2]);
        } else {
            ans = dp(i + 1);
        }
        memo[i] = ans;
        return ans;
    }
}

Approach 2: Dynamic Programming (Window Variant)
Complexity Analysis
Time Complexity: O(N), where N is the number of unique days in your travel plan.
Space Complexity: O(N). 
# 6ms 39.49%
class Solution {
    int[] days, costs;
    Integer[] memo;
    int[] durations = new int[]{1, 7, 30};
    
    public int mincostTickets(int[] days, int[] costs) {
        this.days = days;
        this.costs = costs;
        memo = new Integer[days.length];

        return dp(0);
    }
    
    public int dp(int i) {
        if (i >= days.length) return 0;
        if (memo[i] != null) return memo[i];
        int ans = Integer.MAX_VALUE;
        int j = i;
        for (int k = 0; k < 3; ++k) {
            while (j < days.length && days[j] < days[i] + durations[k]) j++;
            ans = Math.min(ans, dp(j) + costs[k]);
        }
        memo[i] = ans;
        return ans;
    }
}

# https://leetcode.com/problems/minimum-cost-for-tickets/discuss/227412/Java-solution-DFS-with-memory-and-DP-solution
# DFS
# 6ms 39.49%
class Solution {
    Map<Integer, Integer> cache = new HashMap<>();

    public int mincostTickets(int[] days, int[] costs) {
        return dfs(-1, 0, days, costs);        
    }
    
    public int dfs(int endDay, int idx, int[] days, int[] costs) {
        if (idx == days.length) return 0;
        if (endDay >= days[idx]) return dfs(endDay, idx + 1, days, costs);
        if (cache.containsKey(days[idx])) return cache.get(days[idx]);
        
        for (int i = idx; i < days.length && days[i] >= endDay; i++) {
            int cost0 = costs[0] + dfs(days[i] + 0, i + 1, days, costs);
            int cost1 = costs[1] + dfs(days[i] + 6, i + 1, days, costs);
            int cost2 = costs[2] + dfs(days[i] + 29, i + 1, days, costs);
            
            int minCost = Math.min(cost0, Math.min(cost1, cost2));
            cache.put(days[idx], minCost);
            return minCost;
        }
        return cache.get(days[idx]);
    }
}

# DP
# 5ms 58.85%
class Solution {
    public int mincostTickets(int[] days, int[] costs) {
        if (days == null || days.length == 0) return 0;
        int n = days.length;
        int[][] dp = new int[n][3];
        for (int i = 0; i < 3; i++) {
            dp[0][i] = costs[i];
        }
        
        for (int i = 1; i < n; i++) {
            int today = days[i];
            int cost0 = dp[i - 1][0] + costs[0];
            for (int j = i - 1; j >= 0 && days[j] + 30 > today; j--) {
                cost0 = Math.min(cost0, dp[j][2]);
            }
            for (int j = i - 1; j >= 0 && days[j] + 7 > today; j--) {
                cost0 = Math.min(cost0, dp[j][1]);
            }
            dp[i][0] = cost0;
            dp[i][1] = dp[i - 1][0] + costs[1];
            dp[i][2] = dp[i - 1][0] + costs[2];
        }
        return dp[n - 1][0];
    }
}
'''
