__source__ = 'https://leetcode.com/problems/random-pick-with-blacklist/'
# Time:  O(B)
# Space: O(1)
#
# Description: Leetcode # 710. Random Pick with Blacklist
#
# Given a blacklist B containing unique integers from [0, N),
# write a function to return a uniform random integer from [0, N) which is NOT in B.
#
# Optimize it such that it minimizes the call to system’s Math.random().
#
# Note:
#
#     1 <= N <= 1000000000
#     0 <= B.length < min(100000, N)
#     [0, N) does NOT include N. See interval notation.
#
# Example 1:
#
# Input:
# ["Solution","pick","pick","pick"]
# [[1,[]],[],[],[]]
# Output: [null,0,0,0]
#
# Example 2:
#
# Input:
# ["Solution","pick","pick","pick"]
# [[2,[]],[],[],[]]
# Output: [null,1,1,1]
#
# Example 3:
#
# Input:
# ["Solution","pick","pick","pick"]
# [[3,[1]],[],[],[]]
# Output: [null,0,0,2]
#
# Example 4:
#
# Input:
# ["Solution","pick","pick","pick"]
# [[4,[2]],[],[],[]]
# Output: [null,1,3,1]
#
# Explanation of Input Syntax:
#
# The input is two lists: the subroutines called and their arguments.
# Solution's constructor has two arguments, N and the blacklist B. pick has no arguments.
# Arguments are always wrapped with a list, even if there aren't any.
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
# Thought: https://leetcode.com/problems/random-pick-with-blacklist/solution/
#
Approach 1: Whitelist
Complexity Analysis
Time Complexity: O(N) preprocessing. O(1)O(1)O(1) pick. 
Preprocessing is too slow to pass the time limit.
Space Complexity: O(N). MLE (Memory Limit Exceeded) will occur.

# TLE
class Solution {
    List<Integer> w;
    Random r;
    public Solution(int n, int[] b) {
        w = new ArrayList<>();
        r = new Random();
        Set<Integer> W = new HashSet<>();
        for (int i = 0; i < n; i++) W.add(i);
        for (int x : b) W.remove(x);
        for (int x : W) w.add(x);
    }

    public int pick() {
        return w.get(r.nextInt(w.size()));
    }
}

Approach 2: Binary Search over Blacklist
Complexity Analysis
Time Complexity: O(BlogB) preprocessing. O(logB) pick.
Space Complexity: O(B) Or O(1) if in-place sort is used and input array is not considered extra space.

# 140ms 59.87%
class Solution {
    int n;
    int[] b;
    Random r;

    public Solution(int N, int[] blacklist) {
        n = N;
        Arrays.sort(blacklist);
        b = blacklist;
        r = new Random();
    }

    public int pick() {
        int k = r.nextInt(n - b.length);
        int lo = 0;
		int hi = b.length - 1;

		while (lo < hi) {
			int i = (lo + hi + 1) / 2;
			if (b[i] - i > k) hi = i - 1;
			else lo = i;
		}
		return lo == hi && b[lo] - lo <= k ? k + lo + 1 : k;
    }
}

Approach 3: Virtual Whitelist
Complexity Analysis
Time Complexity: O(B) preprocessing. O(1) pick.
Space Complexity: O(B) O(A+R), the space used by ranges.

# 121ms 91.97%
class Solution {
    Map<Integer, Integer> m;
    Random r;
    int wlen;

    public Solution(int n, int[] b) {
        m = new HashMap<>();
        r = new Random();
        wlen = n - b.length;
        Set<Integer> w = new HashSet<>();
        for (int i = wlen; i < n; i++) w.add(i);
        for (int x : b) w.remove(x);
        Iterator<Integer> wi = w.iterator();
        for (int x : b)
            if (x < wlen)
                m.put(x, wi.next());
    }

    public int pick() {
        int k = r.nextInt(wlen);
        return m.getOrDefault(k, k);
    }
}

# 114ms 98.66%
class Solution {   
    ArrayList<Integer> arr;
    Set<Integer> set;
    Random rand;
    boolean enabled;
    int N;

    public Solution(int N, int[] blacklist) {
        arr = new ArrayList<>();
        set = new HashSet<>();
        enabled = blacklist.length >= N / 3;
        for (int num : blacklist) set.add(num);
        if (enabled) {
            for (int i = 0; i < N; i++) {
                if (set.contains(i)) continue;
                arr.add(i);
            }
        }
        rand = new Random();
        this.N = N;
    }
    
    public int pick() {
        if (enabled) return arr.get(rand.nextInt(arr.size()));
        int r = -1;
        while (r < 0 || set.contains(r)) r = rand.nextInt(N);
        return r;
    }
}

'''
