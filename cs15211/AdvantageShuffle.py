__source__ = 'https://leetcode.com/problems/advantage-shuffle/'
# Time:  O(NlogN) sorting
# Space: O(N)
#
# Description: Leetcode # 870. Advantage Shuffle
#
# Given two arrays A and B of equal size,
# the advantage of A with respect to B is the number of indices i for which A[i] > B[i].
#
# Return any permutation of A that maximizes its advantage with respect to B.
#
# Example 1:
#
# Input: A = [2,7,11,15], B = [1,10,4,11]
# Output: [2,11,7,15]
# Example 2:
#
# Input: A = [12,24,8,32], B = [13,25,32,11]
# Output: [24,32,8,12]
#
#
# Note:
#
# 1 <= A.length = B.length <= 10000
# 0 <= A[i] <= 10^9
# 0 <= B[i] <= 10^9
#
import unittest

#220ms 98.46%
class Solution(object):
    def advantageCount(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: List[int]
        """
        sortedA = sorted(A)
        sortedB = sorted(B)

        # assigned[b] = list of a that are assigned to beat b
        # remaining = list of a that are not assigned to any b
        assigned = {b: [] for b in B}
        remaining = []

        # populate (assigned, remaining) appropriately
        # sortedB[j] is always the smallest unassigned element in B
        j = 0
        for a in sortedA:
            if a > sortedB[j]:
                assigned[sortedB[j]].append(a)
                j += 1
            else:
                remaining.append(a)

        # Reconstruct the answer from annotations (assigned, remaining)
        return [assigned[b].pop() if assigned[b] else remaining.pop()
                for b in B]

class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)


if __name__ == '__main__':
    unittest.main()

Java = '''
#Thought: https://leetcode.com/problems/advantage-shuffle/solution/
Approach 1: Greedy
Complexity Analysis
Time Complexity: O(NlogN), where N is the length of A and B.
Space Complexity: O(N).

#87ms 65.48%
class Solution {
    public int[] advantageCount(int[] A, int[] B) {
        int[] sortedA = A.clone();
        Arrays.sort(sortedA);
        int[] sortedB = B.clone();
        Arrays.sort(sortedB);

        // assigned[b] = list of a that are assigned to beat b
        Map<Integer, Deque<Integer>> assigned = new HashMap();
        for (int b: B) assigned.put(b, new LinkedList());

        // remaining = list of a that are not assigned to any b
        Deque<Integer> remaining = new LinkedList();

        // populate (assigned, remaining) appropriately
        // sortedB[j] is always the smallest unassigned element in B
        int j = 0;
        for (int a : sortedA) {
            if (a > sortedB[j]) {
                assigned.get(sortedB[j++]).add(a);
            } else {
                remaining.add(a);
            }
        }

        // Reconstruct the answer from annotations (assigned, remaining)
        int[] ans = new int[B.length];
        for (int i = 0; i < B.length; ++i) {
            // if there is some a assigned to b...
            if (assigned.get(B[i]).size() > 0) {
                ans[i] = assigned.get(B[i]).pop();
            } else {
                ans[i] = remaining.pop();
            }
        }
        return ans;
    }
}

#34ms 99.29% With binary search

'''