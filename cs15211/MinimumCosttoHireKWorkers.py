__source__ = 'https://leetcode.com/problems/minimum-cost-to-hire-k-workers/'
# Time:  O(NlogN) sorting, PQ
# Space: O(N)
#
# Description: Leetcode # 857. Minimum Cost to Hire K Workers
#
# There are N workers.  The i-th worker has a quality[i] and a minimum wage expectation wage[i].
# Now we want to hire exactly K workers to form a paid group.
# When hiring a group of K workers, we must pay them according to the following rules:
#
# Every worker in the paid group should be paid in the ratio of their quality
# compared to other workers in the paid group.
# Every worker in the paid group must be paid at least their minimum wage expectation.
# Return the least amount of money needed to form a paid group satisfying the above conditions.
#
# Example 1:
#
# Input: quality = [10,20,5], wage = [70,50,30], K = 2
# Output: 105.00000
# Explanation: We pay 70 to 0-th worker and 35 to 2-th worker.
# Example 2:
#
# Input: quality = [3,1,10,10,1], wage = [4,8,2,2,7], K = 3
# Output: 30.66667
# Explanation: We pay 4 to 0-th worker, 13.33333 to 2-th and 3-th workers seperately.
#
#
# Note:
#
# 1 <= K <= N <= 10000, where N = quality.length = wage.length
# 1 <= quality[i] <= 10000
# 1 <= wage[i] <= 10000
# Answers within 10^-5 of the correct answer will be considered correct.
#
import unittest
import heapq
#100 ms 99.8%
class Solution(object):
    def mincostToHireWorkers(self, quality, wage, K):
        """
        :type quality: List[int]
        :type wage: List[int]
        :type K: int
        :rtype: float
        """
        i = 0
        ratio = []
        for q, w in zip(quality, wage):
            ratio.append([-1.0 * w / q, q])
            i += 1

        ratio.sort(key = lambda r: r[1])
        #print ratio
        total_qual = 0
        heap = ratio[:K]
        heapq.heapify(heap)

        for r, q in heap:
            total_qual += q

        res = -heap[0][0] * total_qual

        for r, q in ratio[K:]:
            if r > heap[0][0]:
                top_r, top_q = heapq.heappushpop(heap, [r, q])
                total_qual += q - top_q
                res = min(res, - heap[0][0] * total_qual)
        return res

#192ms 35.29%
class Solution2(object):
    def mincostToHireWorkers(self, quality, wage, K):
        """
        :type quality: List[int]
        :type wage: List[int]
        :type K: int
        :rtype: float
        """
        workers = sorted([float(w) / q, q] for w,q  in zip(wage, quality))
        res = float('inf')
        qsum = 0
        heap = []
        for r, q in workers:
            heapq.heappush(heap, -q)
            qsum += q
            if len(heap) > K: qsum += heapq.heappop(heap)
            if len(heap) == K: res = min(res, qsum * r)
        return res

class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)


if __name__ == '__main__':
    unittest.main()

Java = '''
# Thought: https://leetcode.com/problems/minimum-cost-to-hire-k-workers/solution/

Approach 1: Greedy:TLE
Complexity Analysis
Time Complexity: O(N^2 log N), where N is the number of workers.
Space Complexity: O(N)


Approach 2: Heap
Complexity Analysis
Time Complexity: O(NlogN), where N is the number of workers.
Space Complexity: O(N)

# https://leetcode.com/problems/minimum-cost-to-hire-k-workers/discuss/141768/Detailed-explanation-O(NlogN)

# 62.62% 71ms
class Solution {
    public double mincostToHireWorkers(int[] quality, int[] wage, int K) {
        double[][] workers = new double[quality.length][2];
        for(int i = 0; i < quality.length; ++i) {
            workers[i] = new double[]{(double)(wage[i]) / quality[i], (double) quality[i]};
        }
        Arrays.sort(workers, (a, b) -> Double.compare(a[0], b[0]));
        double res = Double.MAX_VALUE, qsum = 0;
        PriorityQueue<Double> pq = new PriorityQueue<>();
        for (double[] worker : workers) {
            qsum += worker[1];
            pq.add(-worker[1]);
            if (pq.size() > K) qsum += pq.poll();
            if (pq.size() == K) res = Math.min(res, qsum * worker[0]);
        }
        return res;
    }
}

#(comparator class faster than lambda expression ?)
# 28ms 99.85% 
class Solution {
    public double mincostToHireWorkers(int[] quality, int[] wage, int k) {
        if (k == 0) return 0;
        if (quality.length == 0) return 0;
        Worker[] workers = new Worker[quality.length];
        for (int i = 0 ; i < quality.length ; i++) {
            workers[i] = new Worker(quality[i], wage[i]);
        }

        Arrays.sort(workers, new Comparator<Worker>(){
            public int compare(Worker w1, Worker w2) {
                if (w1.ratio == w2.ratio) return 0;
                else if (w1.ratio > w2.ratio) return 1;
                else return -1;
            }
        });

        Queue<Worker> maxHeap = new PriorityQueue<>(11, new Comparator<Worker>(){
            public int compare(Worker w1, Worker w2) {
                return w2.quality - w1.quality;
            }
        });

        int sumOfHeap = 0;
        double res = Double.MAX_VALUE;
        for (Worker w : workers) {
            if (maxHeap.size() < k) {
                maxHeap.offer(w);
                sumOfHeap += w.quality;
            } else {
                sumOfHeap -= maxHeap.poll().quality;
                sumOfHeap += w.quality;
                maxHeap.offer(w);
            }
            if (maxHeap.size() == k) {
                res = Math.min(res, sumOfHeap * 1.0 * w.ratio);
            }
        }
        return res;
    }

    private class Worker {
        int quality;
        int wage;
        double ratio;
        public Worker(int quality, int wage) {
            this.quality = quality;
            this.wage = wage;
            this.ratio = wage * 1.0 / quality;
        }
    }
}
'''
