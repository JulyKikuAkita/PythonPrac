__source__ = 'https://github.com/kamyu104/LeetCode/blob/master/Python/sequence-reconstruction.py'
# Time:  O(n * s), n is the size of org, s is the size of seqs
# Space: O(n)
#
# Description:
# Check whether the original sequence org can be uniquely reconstructed from the sequences in seqs.
# The org sequence is a permutation of the integers from 1 to n, with 1 <= n <= 104.
# Reconstruction means building a shortest common supersequence of the sequences i
# n seqs (i.e., a shortest sequence so that all sequences in seqs are subsequences of it).
# Determine whether there is only one sequence that can be reconstructed from seqs and
# it is the org sequence.
#
# Example 1:
#
# Input:
# org: [1,2,3], seqs: [[1,2],[1,3]]
#
# Output:
# false
#
# Explanation:
# [1,2,3] is not the only one sequence that can be reconstructed,
# because [1,3,2] is also a valid sequence that can be reconstructed.
# Example 2:
#
# Input:
# org: [1,2,3], seqs: [[1,2]]
#
# Output:
# false
#
# Explanation:
# The reconstructed sequence can only be [1,2].
# Example 3:
#
# Input:
# org: [1,2,3], seqs: [[1,2],[1,3],[2,3]]
#
# Output:
# true
#
# Explanation:
# The sequences [1,2], [1,3], and [2,3] can uniquely reconstruct the original sequence [1,2,3].
# Example 4:
#
# Input:
# org: [4,1,5,2,6,3], seqs: [[5,2,6,3],[4,1,5,2]]
#
# Output:
# true
# UPDATE (2017/1/8):
# The seqs parameter had been changed to a list of list of strings (instead of a 2d array of strings).
# Please reload the code definition to get the latest changes.
#
# Hide Company Tags Google
# Hide Tags Graph Topological Sort
# Hide Similar Problems (M) Course Schedule II

import unittest
import collections
# Thoughts:
# For org to be uniquely reconstructible from seqs we need to satisfy 2 conditions:
#
# Every sequence in seqs should be a subsequence in org. This part is obvious.
# Every 2 consecutive elements in org should be consecutive elements in some sequence from seqs.
# Why is that? Well, suppose condition 1 is satisfied.
# Then for 2 any consecutive elements x and y in org we have 2 options.
# We have both xand y in some sequence from seqs. Then (as condition 1 is satisfied)
# they must be consequtive elements in this sequence.
# There is no sequence in seqs that contains both x and y.
# In this case we cannot uniquely reconstruct org from seqs as sequence with x and y switched
# would also be a valid original sequence for seqs.
# So this are 2 necessary criterions. It is pretty easy to see that this are also sufficient
# criterions for org to be uniquely reconstructible (there is only 1 way to reconstruct
# sequence when we know that condition 2 is satisfied).
#
# To implement this idea I have idxs hash that maps item to its index in org sequence to check
# condition 1. And I have pairs set that holds all consequitive element pairs for sequences from
# seqs to check condition 2 (I also consider first elements to be paired with previous undefined
# elements, it is necessary to check this).

# Time:  O(|V| + |E|)
# Space: O(|E|)
class Solution(object):
    def sequenceReconstruction(self, org, seqs):
        """
        :type org: List[int]
        :type seqs: List[List[int]]
        :rtype: bool
        """
        graph = collections.defaultdict(set)
        indegree = collections.defaultdict(int)
        integer_set = set()
        for seq in seqs:
            for i in seq:
                integer_set.add(i)
            if len(seq) == 1:
                if seq[0] not in indegree:
                    indegree[seq[0]] = 0
                continue
            for i in xrange(len(seq)-1):
                if seq[i] not in indegree:
                    indegree[seq[i]] = 0
                if seq[i+1] not in graph[seq[i]]:
                    graph[seq[i]].add(seq[i+1])
                    indegree[seq[i+1]] += 1

        cnt_of_zero_indegree = 0
        res = []
        q = []
        for i in indegree:
            if indegree[i] == 0:
                cnt_of_zero_indegree += 1
                if cnt_of_zero_indegree > 1:
                    return False
                q.append(i)

        while q:
            i = q.pop()
            res.append(i)
            cnt_of_zero_indegree = 0
            for j in graph[i]:
                indegree[j] -= 1
                if indegree[j] == 0:
                    cnt_of_zero_indegree += 1
                    if cnt_of_zero_indegree > 1:
                        return False
                    q.append(j)
        return res == org and len(org) == len(integer_set)

class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)


if __name__ == '__main__':
    unittest.main()

Java = '''
#Thought:
Java Solution using BFS Topological Sort 30.77%
public class Solution {
    public boolean sequenceReconstruction(int[] org, List<List<Integer>> seqs) {
        Map<Integer, Set<Integer>> map = new HashMap<>();
        Map<Integer, Integer> indegree = new HashMap<>();

        for(List<Integer> seq: seqs) {
            if(seq.size() == 1) {
                if(!map.containsKey(seq.get(0))) {
                    map.put(seq.get(0), new HashSet<>());
                    indegree.put(seq.get(0), 0);
                }
            } else {
                for(int i = 0; i < seq.size() - 1; i++) {
                    if(!map.containsKey(seq.get(i))) {
                        map.put(seq.get(i), new HashSet<>());
                        indegree.put(seq.get(i), 0);
                    }

                    if(!map.containsKey(seq.get(i + 1))) {
                        map.put(seq.get(i + 1), new HashSet<>());
                        indegree.put(seq.get(i + 1), 0);
                    }

                    if(map.get(seq.get(i)).add(seq.get(i + 1))) {
                        indegree.put(seq.get(i + 1), indegree.get(seq.get(i + 1)) + 1);
                    }
                }
            }
        }

        Queue<Integer> queue = new LinkedList<>();
        for(Map.Entry<Integer, Integer> entry: indegree.entrySet()) {
            if(entry.getValue() == 0) queue.offer(entry.getKey());
        }

        int index = 0;
        while(!queue.isEmpty()) {
            int size = queue.size();
            if(size > 1) return false;
            int curr = queue.poll();
            if(index == org.length || curr != org[index++]) return false;
            for(int next: map.get(curr)) {
                indegree.put(next, indegree.get(next) - 1);
                if(indegree.get(next) == 0) queue.offer(next);
            }
        }
        return index == org.length && index == map.size();
    }
}

2. 90%
Java O(n) time,O(n) space AC solution 14ms like count sort
The basic idea is to count how many numbers are smaller(self include) than the current number.
We then compare this count to the org.
It is pretty like the idea of count sort.

        int len = org.length;
        int[] map = new int[len + 1];//map number to its index
        Arrays.fill(map, -1);
        int[] memo = new int[org.length];//count how many numbers are smaller(on the right)
        for (int i = 0; i < len; i++) {
            map[org[i]] = i;
        }
        for (List<Integer> seq : seqs) {
            if (seq.size() == 0) continue;
            int prev = seq.get(0);
            if (prev <= 0 || prev > len || map[prev] == -1) return false;
            for (int i = 1; i < seq.size(); i++) {
                int curr = seq.get(i);
                if (curr <= 0 || curr > len || map[curr] == -1) return false;
                memo[map[prev]] = Math.max(memo[map[prev]], len - map[curr] + 1);
                prev = curr;
            }
            memo[map[prev]] = Math.max(memo[map[prev]], 1);
        }
        for (int i = 0; i < memo.length; i++) {
            if (memo[i] != len - i) return false;
        }
        return true;
    }
}
'''