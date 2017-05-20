__author__ = 'July'
# https://github.com/kamyu104/LeetCode/blob/master/Python/super-ugly-number.py
# Time:  O(n * logk) ~ O(n * k)
# Space: O(n + k)

# Write a program to find the nth super ugly number.
#
# Super ugly numbers are positive numbers whose all
# prime factors are in the given prime list primes of size k.
# For example, [1, 2, 4, 7, 8, 13, 14, 16, 19, 26, 28, 32]
# is the sequence of the first 12 super ugly numbers given
# primes = [2, 7, 13, 19] of size 4.
#
# Note:
# (1) 1 is a super ugly number for any given primes.
# (2) The given numbers in primes are in ascending order.
# (3) 0 < k <= 100, 0 < n <= 106, 0 < primes[i] < 1000.
# Google
# Heap solution. (240ms)
import heapq
class Solution(object):
    def nthSuperUglyNumber(self, n, primes):
        """
        :type n: int
        :type primes: List[int]
        :rtype: int
        """

        heap, uglies, idx, ugly_by_last_prime = [], [0] * n , [0] * len(primes), [0] * n
        uglies[0] = 1

        for k, p in enumerate(primes):
            heapq.heappush(heap, (p,k))  # sort by first val

        for i in xrange(1,n):
            uglies[i], k = heapq.heappop(heap)
            ugly_by_last_prime[i] = k
            idx[k] += 1
            while ugly_by_last_prime[idx[k]] > k:
                idx[k] += 1
            heapq.heappush(heap, (primes[k] * uglies[idx[k]], k))
        return uglies[-1]


# Time:  O(n * k)
# Space: O(n + k)
# Hash solution. (360ms)
class Solution2(object):
    def nthSuperUglyNumber(self, n, primes):
        """
        :type n: int
        :type primes: List[int]
        :rtype: int
        """

        uglies, idx, heap, ugly_set = [0] * n , [0] * len(primes), [], set([1])
        uglies[0] = 1

        for k, p in enumerate(primes):
            heapq.heappush(heap, (p, k))  # sort by first val
            ugly_set.add(p)

        for i in xrange(1, n):
            uglies[i], k = heapq.heappop(heap)
            while (primes[k] * uglies[idx[k]]) in ugly_set:
                idx[k] += 1
            heapq.heappush(heap, (primes[k] * uglies[idx[k]], k))
            ugly_set.add(primes[k] * uglies[idx[k]])

        return uglies[-1]


# Time:  O(n * logk) ~ O(n * klogk)
# Space: O(n + k)
# 580ms
class Solution3(object):
    def nthSuperUglyNumber(self, n, primes):
        """
        :type n: int
        :type primes: List[int]
        :rtype: int
        """
        uglies, idx, heap = [1] , [0] * len(primes), []
        for k, p in enumerate(primes):
            heapq.heappush(heap, (p, k))  # sort by first val

        for i in xrange(1, n):
            min_val, k = heap[0]
            uglies += [min_val]

            while heap[0][0] == min_val: #worst time: O(klogk)
                min_val, k = heapq.heappop(heap)
                idx[k] += 1
                heapq.heappush(heap, (primes[k] * uglies[idx[k], k]))
        return uglies[-1]


# Time:  O(n * k)
# Space: O(n + k)
# TLE due to the last test case, but it passess and performs the best in C++.
class Solution4(object):
    def nthSuperUglyNumber(self, n, primes):
        """
        :type n: int
        :type primes: List[int]
        :rtype: int
        """
        uglies = [0] * n
        uglies[0] = 1
        ugly_by_prime = list(primes)
        idx = [0] * len(primes)

        for i in xrange(1, n):
            uglies[i] = min(ugly_by_prime)
            for k in xrange(len(primes)):
                if uglies[i] == ugly_by_prime[k]:
                    idx[k] += 1
                    ugly_by_prime[k] = primes[k] * uglies[idx[k]]
        return uglies[-1]

# Time:  O(n * logk) ~ O(n * klogk)
# Space: O(k^2)
# TLE due to the last test case, but it passess and performs well in C++.
class Solution5(object):
    def nthSuperUglyNumber(self, n, primes):
        """
        :type n: int
        :type primes: List[int]
        :rtype: int
        """
        ugly_number = 0

        heap = []
        heapq.heappush(heap, 1)

        for p in primes:
            heapq.heappush(heap, p)

        for _ in xrange(n):
            ugly_number = heapq.heappop(heap)
            for i in xrange(len(primes)):
                if ugly_number % primes[i] == 0:
                    for j in xrange(i + 1):
                        heapq.heappush(heap, ugly_number * primes[j])
                    break

        return ugly_number


#java
js = '''
public class Solution {
    public int nthSuperUglyNumber(int n, int[] primes) {
        if (n <= 0 || primes.length == 0) {
            return 0;
        }
        int[] dp = new int[n];
        dp[0] = 1;
        PriorityQueue<Integer> pq = new PriorityQueue<>();
        for (int prime : primes) {
            pq.add(prime);
        }
        int[] indices = new int[primes.length];
        int[] nums = new int[primes.length];
        for (int i = 0; i < nums.length; i++) {
            nums[i] = primes[i];
        }
        for (int i = 1; i < n; i++) {
            int cur = pq.poll();
            while (!pq.isEmpty() && pq.peek() == cur) {
                pq.poll();
            }
            dp[i] = cur;
            for (int j = 0; j < primes.length; j++) {
                if (nums[j] == cur) {
                    indices[j]++;
                    nums[j] = dp[indices[j]] * primes[j];
                    pq.add(nums[j]);
                }
            }
        }
        return dp[n - 1];
    }
}


Overflow
public class Solution {
    public int nthSuperUglyNumber(int n, int[] primes) {
        if( n <= 0 || primes.length == 0) return 0;
        PriorityQueue<Integer> pq = new PriorityQueue<>();
        pq.add(1);
        for(int i = 0 ; i < primes.length; i++){
            pq.add(primes[i]);
        }

        int cur = 1;
        for(int i = 1; i <= n; i++){
            cur = pq.poll();
            for(int j = 0; j < primes.length; j++){
                if (cur % primes[j] == 0){
                    for (int k = 0; k <= j; k++){
                        pq.add(cur * primes[k]);
                    }
                    break;
                }


            }
        }
        return cur;
    }
}


http://algobox.org/super-ugly-number/
The time complexity is O(n log k) with O(k) extra space.
the heap-based solution has a too high overhead to beat the array-based solution,
which has a time complexity of O(nk) with also O(k) extra space.
'''