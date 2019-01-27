__source__ = 'https://leetcode.com/problems/k-closest-points-to-origin/'
# Time:  O(NLogN ~ N)
# Space: O(N)
#
# Quick Select: K-problem
# Description: Leetcode # 973. K Closest Points to Origin
#
# We have a list of points on the plane.  Find the K closest points to the origin (0, 0).
#
# (Here, the distance between two points on a plane is the Euclidean distance.)
#
# You may return the answer in any order.
# The answer is guaranteed to be unique (except for the order that it is in.)
#
# Example 1:
#
# Input: points = [[1,3],[-2,2]], K = 1
# Output: [[-2,2]]
# Explanation:
# The distance between (1, 3) and the origin is sqrt(10).
# The distance between (-2, 2) and the origin is sqrt(8).
# Since sqrt(8) < sqrt(10), (-2, 2) is closer to the origin.
# We only want the closest K = 1 points from the origin, so the answer is just [[-2,2]].
# Example 2:
#
# Input: points = [[3,3],[5,-1],[-2,4]], K = 2
# Output: [[3,3],[-2,4]]
# (The answer [[-2,4],[3,3]] would also be accepted.)
#
#
# Note:
#
# 1 <= K <= points.length <= 10000
# -10000 < points[i][0] < 10000
# -10000 < points[i][1] < 10000
#
import unittest
import random

# 428ms 99.89%
class Solution(object):
    def kClosest(self, points, K):
        """
        :type points: List[List[int]]
        :type K: int
        :rtype: List[List[int]]
        """
        dist = lambda i: points[i][0]**2 + points[i][1]**2

        def work(i, j, K):
            if i >= j: return
            oi, oj = i, j
            pivot = dist(random.randint(i, j))
            while i < j:
                while i < j and dist(i) < pivot: i += 1
                while i < j and dist(j) > pivot: j -= 1
                points[i], points[j] = points[j], points[i]

            if K <= i - oi + 1:
                work(oi, i, K)
            else:
                work(i+1, oj, K - (i - oi + 1))

        work(0, len(points) - 1, K)
        return points[:K]

class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)


if __name__ == '__main__':
    unittest.main()

Java = '''
# Thought: https://leetcode.com/problems/k-closest-points-to-origin/solution/
# Approach 1: Sort
# Complexity Analysis
# Time Complexity: O(NlogN), where N is the length of points.
# Space Complexity: O(N)

# 71ms 62.57%
class Solution {
    public int[][] kClosest(int[][] points, int K) {
        Arrays.sort(points, (int[] a, int[] b) -> (a[0] * a[0] + a[1] * a[1]) - (b[0]* b[0] + b[1]* b[1]));
        int[][] res = new int[K][];
        for (int i = 0; i < K; i++) {
            res[i] = points[i];
        }
        return res;
    }
}

# Approach 2: Divide and Conquer
# Complexity Analysis
# Time Complexity: O(N) in average case complexity, where N is the length of points.
# Space Complexity: O(N)

# 11ms 100%
import java.util.concurrent.ThreadLocalRandom;
class Solution {
    int[][] points;
    public int[][] kClosest(int[][] points, int K) {
        this.points = points;
        work(0, points.length - 1, K);
        return Arrays.copyOfRange(points, 0, K);
    }
    
    public void work(int i, int j, int K) {
        if (i >= j) return;
        int oi = i, oj = j;
        int pivot = dist(ThreadLocalRandom.current().nextInt(i, j));
        while (i < j) {
            while (i < j && dist(i) < pivot) i++;
            while (i < j && dist(j) > pivot) j--;
            swap(i, j);
        }
        
        if (K <= i - oi + 1) {
            work(oi, i, K);
        } else {
            work(i + 1, oj, K - (i - oi + 1));
        }
    }
    
    public int dist(int i) {
        return points[i][0] * points[i][0] + points[i][1] * points[i][1];
    }
    
    public void swap(int i, int j) {
        int t0 = points[i][0], t1 = points[i][1];
        points[i][0] = points[j][0];
        points[i][1] = points[j][1];
        points[j][0] = t0;
        points[j][1] = t1;
    }
}

# https://leetcode.com/problems/k-closest-points-to-origin/discuss/220235/Java-Three-solutions-to-this-classical-K-th-problem.
# This is a very classical problem, so-called K-th problem.
# Here I will share some summaries and some classical solutions to this kind of problem.
# 
# I. The very naive and simple solution is sorting the all points by their distance to the origin point directly, 
# then get the top k closest points. We can use the sort function and the code is very short.
# 
# Theoretically, the time complexity is O(NlogN), pratically, the real time it takes on leetcode is 104ms.
# 
# The advantages of this solution are short, intuitive and easy to implement.
# The disadvantages of this solution are not very efficient and have to know all of the points previously, 
# and it is unable to deal with real-time(online) case, it is an off-line solution.
# 
# The short code shows as follows:

# 72ms 61.85%
class Solution {
    public int[][] kClosest(int[][] points, int K) {
        Arrays.sort(points, (p1, p2) -> p1[0] * p1[0] + p1[1] * p1[1] - p2[0] * p2[0] - p2[1] * p2[1]);
        return Arrays.copyOfRange(points, 0, K);
    }
}

# II. The second solution is based on the first one. We don't have to sort all points.
# Instead, we can maintain a max-heap with size K. Then for each point, we add it to the heap. 
# Once the size of the heap is greater than K, 
# we are supposed to extract one from the max heap to ensure the size of the heap is always K. 
# Thus, the max heap is always maintain top K smallest elements from the first one to crruent one. 
# Once the size of the heap is over its maximum capacity, it will exclude the maximum element in it, 
# since it can not be the proper candidate anymore.
# 
# Theoretically, the time complexity is O(NlogK), but practically, the real time it takes on leetcode is 134ms.
# 
# The advantage of this solution is it can deal with real-time(online) stream data. 
# It does not have to know the size of the data previously.
# The disadvantage of this solution is it is not the most efficient solution.
# 
# The short code shows as follows:

# 79ms 56.66%
class Solution {
    public int[][] kClosest(int[][] points, int K) {
        PriorityQueue<int[]> pq 
        = new PriorityQueue<int[]>((p1, p2) -> p2[0] * p2[0] + p2[1] * p2[1] - p1[0] * p1[0] - p1[1] * p1[1]);
        for (int[] p : points) {
            pq.offer(p);
            if (pq.size() > K) {
                pq.poll();
            }
        }
        int[][] res = new int[K][2];
        while (K > 0) {
            res[--K] = pq.poll();
        }
        return res;
    }
}

# III. The last solution is based on quick sort, we can also call it quick select. 
# In the quick sort, we will always choose a pivot to compare with other elements. 
# After one iteration, we will get an array that all elements smaller than the pivot are on the left side of the pivot 
# and all elements greater than the pivot are on the right side of the pivot 
# (assuming we sort the array in ascending order). 
# So, inspired from this, each iteration, we choose a pivot and then find the position p the pivot should be. 
# Then we compare p with the K, if the p is smaller than the K, 
# meaning the all element on the left of the pivot are all proper candidates but it is not adequate, 
# we have to do the same thing on right side, and vice versa. 
# If the p is exactly equal to the K, meaning that we've found the K-th position. 
# Therefore, we just return the first K elements, since they are not greater than the pivot.
# 
# Theoretically, the average time complexity is O(N) , but just like quick sort, 
# in the worst case, this solution would be degenerated to O(N^2), and practically, 
# the real time it takes on leetcode is 15ms.
# 
# The advantage of this solution is it is very efficient.
# The disadvantage of this solution are it is neither an online solution nor a stable one. 
# And the K elements closest are not sorted in ascending order.
# 
# The short code shows as follows:
#
# 8ms 100%
class Solution {
    public int[][] kClosest(int[][] points, int K) {
        int len = points.length, l = 0, r = len - 1;
        while (l <= r) {
            int mid = helper(points, l, r);
            if (mid == K) break;
            if (mid < K) l = mid + 1;
            else {
                r = mid - 1;
            }
        }
        return Arrays.copyOfRange(points, 0, K);
    }
    
    private int helper(int[][] A, int l, int r) {
        int[] pivot = A[l];
        while (l < r) {
            while (l < r && compare(A[r], pivot) >= 0) r--;
            A[l] = A[r];
            while (l < r && compare(A[l], pivot) <= 0) l++;
            A[r] = A[l];
        }
        A[l] = pivot;
        return l;
    }
    
    private int compare(int[] p1, int[] p2) {
        return p1[0] * p1[0] + p1[1] * p1[1] - p2[0] * p2[0] - p2[1] * p2[1];
    }
}
'''
