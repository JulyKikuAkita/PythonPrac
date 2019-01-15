__source__ = 'https://leetcode.com/problems/partition-to-k-equal-sum-subsets/'
# Time:  O()
# Space: O()
#
# Description: Leetcode # 698. Partition to K Equal Sum Subsets
#
# Given an array of integers nums and a positive integer k,
# find whether it's possible to divide this array into k non-empty subsets whose sums are all equal.
#
# Example 1:
# Input: nums = [4, 3, 2, 3, 5, 2, 1], k = 4
# Output: True
# Explanation: It's possible to divide it into 4 subsets (5), (1, 4), (2,3), (2,3) with equal sums.
# Note:
#
# 1 <= k <= len(nums) <= 16.
# 0 < nums[i] < 10000.
#
import unittest

# 28ms 88.55%
class Solution(object):
    def canPartitionKSubsets(self, nums, k):
        target, rem = divmod(sum(nums), k)
        if rem: return False

        def search(groups):
            if not nums: return True
            v = nums.pop()
            for i, group in enumerate(groups):
                if group + v <= target:
                    groups[i] += v
                    if search(groups): return True
                    groups[i] -= v
                if not group: break
            nums.append(v)
            return False

        nums.sort()
        if nums[-1] > target: return False
        while nums and nums[-1] == target:
            nums.pop()
            k -= 1
        return search([0] * k)

# 99.27% 24ms
class Solution2(object):
    def canPartitionKSubsets(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        n = len(nums)
        # k*target = sum(nums)
        total = sum(nums)
        if total % k: return False

        target = total / k
        seen = [0] * n
        # speeds things up, as larger numbers are tried first if its not possible
        # to get k subsets we will know sooner
        nums.sort(reverse = True)

        def dfs(k, index, current_sum):
            # trivial, one group
            if k == 1: return True
            # found one group, need more k-1 groups
            if current_sum == target:
                return dfs(k-1, 0, 0)
            # group can start with any number
            for i in range(index, n):
                # if we have not tried it before, and adding it
                # to current sum does not exceed target then
                if not seen[i] and current_sum+nums[i] <= target:
                    # we have seen it
                    seen[i] = 1
                    # recursively build group from i+1
                    if dfs(k, i+1, current_sum+nums[i]):
                        return True
                    seen[i] = 0
            return False

        return dfs(k,0,0)

class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)


if __name__ == '__main__':
    unittest.main()

Java = '''
# Thought: https://leetcode.com/problems/partition-to-k-equal-sum-subsets/solution/
Approach #1: Search by Constructing Subset Sums [Accepted]

Complexity Analysis
Time Complexity: O(k^{N-k} k!), where N is the length of nums, and k is as given.
As we skip additional zeroes in groups, naively we will make O(k!) calls to search,
then an additional O(k^{N-k}) calls after every element of groups is nonzero.
Space Complexity: O(N), the space used by recursive calls to search in our call stack.
# 48ms 29.09%
class Solution {
    public boolean canPartitionKSubsets(int[] nums, int k) {
        int sum = Arrays.stream(nums).sum();
        if (sum % k  > 0) return false;
        int target = sum / k;

        Arrays.sort(nums);
        int row = nums.length - 1;
        if (nums[row] > target) return false;
        while (row >= 0 && nums[row] == target) {
            row--;
            k--;
        }
        return search(new int[k], row, nums, target);
    }

    private boolean search(int[] groups, int row, int[] nums, int target) {
        if (row < 0) return true;
        int v = nums[row--];
        for (int i = 0; i < groups.length; i++) {
            if (groups[i] + v <= target) {
                groups[i] += v;
                if (search(groups, row, nums, target)) return true;
                groups[i] -= v;
            }
            if (groups[i] == 0) break;
        }
        return false;
    }
}


Approach #2: Dynamic Programming on Subsets of Input [Accepted]

Complexity Analysis
Time Complexity: O(N * 2^N), where N is the length of nums. There are 2^N states of
used (or state in our bottom-up variant), and each state performs O(N) work searching through nums.
Space Complexity: O(2^N), the space used by memo (or dp, total in our bottom-up variant).

# Top-down DP
enum Result { TRUE, FALSE }
# 50ms 28%
class Solution {
    public boolean canPartitionKSubsets(int[] nums, int k) {
        int sum = Arrays.stream(nums).sum();
        if (sum % k > 0) return false;

        Result[] memo = new Result[1 << nums.length];
        memo[ (1 << nums.length) - 1] = Result.TRUE;
        return search(0, sum ,memo, nums, sum / k);
    }

    private boolean search(int used, int todo, Result[] memo, int[] nums, int target) {
        if (memo[used] == null) {
            memo[used] = Result.FALSE;
            int targ = (todo - 1) % target + 1;
            for (int i = 0; i < nums.length; i++) {
                if ((((used >> i) & 1) == 0) && nums[i] <= targ) {
                    if (search(used | (1 << i), todo - nums[i], memo, nums, target)) {
                        memo[used] = Result.TRUE;
                        break;
                    }
                }
            }
        }
        return memo[used] == Result.TRUE;
    }
}

# Bottom-Up DP Variation
# 79ms 17.01%
class Solution {
    public boolean canPartitionKSubsets(int[] nums, int k) {
        int N = nums.length;
        Arrays.sort(nums);
        int sum = Arrays.stream(nums).sum();
        int target = sum / k;
        if (sum % k > 0 || nums[N - 1] > target) return false;

        boolean[] dp = new boolean[1 << N];
        dp[0] = true;
        int[] total = new int[1 << N];

        for (int state = 0; state < (1 << N); state++) {
            if (!dp[state]) continue;
            for (int i = 0; i < N; i++) {
                int future = state | ( 1 << i);
                if (state != future && !dp[future]) {
                    if (nums[i] <= target - (total[state] % target)) {
                        dp[future] = true;
                         total[future] = total[state] + nums[i];
                    } else {
                        break;
                    }
                }
            }
        }
        return dp[(1 << N) - 1];
    }
}

# 6ms, 94.62%
class Solution {
    public boolean canPartitionKSubsets(int[] nums, int k) {
        if (nums == null || nums.length == 0 || nums.length < k) return false;
        if (k == 1) return true;
        //int sum = Arrays.stream(nums).sum(); //48ms 29.09%
        int sum = 0;
        for (int i = 0; i < nums.length; i++ ) sum += nums[i]; //6ms, 94.62%
        if (sum < k || sum % k != 0) return false;

        int t = sum / k;
        int len = nums.length;
        boolean[] visited = new boolean[len];
        Arrays.sort(nums);
        if (nums[len - 1] > t) return false;

        for (int i = 0; i < k; i++) {
            if (!dfs(nums, t, visited)) return false;
        }
        return true;
    }

    private boolean dfs(int[] nums, int target, boolean[] visited) {
        if (target == 0) return true;
        for (int i = nums.length - 1; i >= 0; i--) {
            if (!visited[i] && nums[i] <= target) {
                visited[i] = true;
                if (dfs(nums, target - nums[i], visited)) return true;
                visited[i] = false;
            }
        }
        return false;
    }
}
'''