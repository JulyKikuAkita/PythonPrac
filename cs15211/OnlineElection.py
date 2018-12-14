__source__ = 'https://leetcode.com/problems/online-election/'
# Time:  O(N+QlogN), where N is the number of votes, and Q is the number of queries.
# Space: O(N)
#
# Description: Leetcode # 911. Online Election
#
# In an election, the i-th vote was cast for persons[i] at time times[i].
#
# Now, we would like to implement the following query function:
# TopVotedCandidate.q(int t) will return the number of the person that was leading the election at time t.
#
# Votes cast at time t will count towards our query.
# In the case of a tie, the most recent vote (among tied candidates) wins.
#
# Example 1:
#
# Input: ["TopVotedCandidate","q","q","q","q","q","q"],
# [[[0,1,1,0,0,1,0],[0,5,10,15,20,25,30]],[3],[12],[25],[15],[24],[8]]
# Output: [null,0,1,1,0,0,1]
# Explanation:
# At time 3, the votes are [0], and 0 is leading.
# At time 12, the votes are [0,1,1], and 1 is leading.
# At time 25, the votes are [0,1,1,0,0,1], and 1 is leading (as ties go to the most recent vote.)
# This continues for 3 more queries at time 15, 24, and 8.
#
# Note:
#
# 1 <= persons.length = times.length <= 5000
# 0 <= persons[i] <= persons.length
# times is a strictly increasing array with all elements in [0, 10^9].
# TopVotedCandidate.q is called at most 10000 times per test case.
# TopVotedCandidate.q(int t) is always called with t >= times[0].
#
import unittest
import bisect
import collections
import itertools
# 364ms 66.96%
class TopVotedCandidate(object):
    def __init__(self, persons, times):
        self.A = []
        count = collections.Counter()
        leader, m = None, 0  # leader, num votes for leader

        for p, t in itertools.izip(persons, times):
            count[p] += 1
            c = count[p]
            if c >= m:
                if p != leader:  # lead change
                    leader = p
                    self.A.append((t, leader))

                if c > m:
                    m = c

    def q(self, t):
        i = bisect.bisect(self.A, (t, float('inf')), 1)
        return self.A[i-1][1]

class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)


if __name__ == '__main__':
    unittest.main()

Java = '''
# Thought: https://leetcode.com/problems/online-election/solution/
Approach 1: List of Lists + Binary Search
Complexity Analysis
Time Complexity: O(N+Qlog2 N), where N is the number of votes, and Q is the number of queries.
Space Complexity: O(N)

# 221ms 58.13%
class TopVotedCandidate {
    class Vote {
        int person, time;
        Vote(int p, int t) {
            person = p;
            time = t;
        }
    }

    List<List<Vote>> A;
    public TopVotedCandidate(int[] persons, int[] times) {
        A = new ArrayList();
        Map<Integer, Integer> count = new HashMap();
        for (int i = 0; i < persons.length; ++i) {
            int p = persons[i], t = times[i];
            int c = count.getOrDefault(p, 0) + 1;

            count.put(p, c);
            while (A.size() <= c) {
                A.add(new ArrayList<Vote>());
            }
            A.get(c).add(new Vote(p, t));
        }
    }

    public int q(int t) {
        // Binary search on A[i][0].time for smallest i
        // such that A[i][0].time > t
        int lo = 1, hi = A.size();
        while (lo < hi) {
            int mid = lo + (hi - lo) / 2;
            if (A.get(mid).get(0).time <= t) {
                lo = mid + 1;
            } else {
                hi = mid;
            }
        }
        int i = lo - 1;
        // Binary search on A[i][j].time for smallest j
        // such that A[i][j].time > t
        lo = 0; hi = A.get(i).size();
        while (lo < hi) {
            int mid = lo + (hi - lo) / 2;
            if (A.get(i).get(mid).time <= t) {
                lo = mid + 1;
            } else {
                hi = mid;
            }
        }
        int j = Math.max(lo-1, 0);
        return A.get(i).get(j).person;
    }
}

/**
 * Your TopVotedCandidate object will be instantiated and called as such:
 * TopVotedCandidate obj = new TopVotedCandidate(persons, times);
 * int param_1 = obj.q(t);
 */

Approach 2: Precomputed Answer + Binary Search
Complexity Analysis
Time Complexity: O(N+QlogN), where N is the number of votes, and Q is the number of queries.
Space Complexity: O(N)

# 191ms 87.24%
class TopVotedCandidate {
    List<Vote> A;
    class Vote {
        int person, time;
        Vote(int p, int t) {
            person = p;
            time = t;
        }
    }

    public TopVotedCandidate(int[] persons, int[] times) {
        A = new ArrayList();
        Map<Integer, Integer> count = new HashMap();
        int leader = -1;  // current leader
        int m = 0;  // current number of votes for leader
        for (int i = 0; i < persons.length; ++i) {
            int p = persons[i], t = times[i];
            int c = count.getOrDefault(p, 0) + 1;
            count.put(p, c);

            if (c >= m) {
                if (p != leader) {
                    leader = p;
                    A.add(new Vote(leader, t));
                }
                if (c > m) m = c;
            }
        }
    }

    public int q(int t) {
        int lo = 1, hi = A.size();
        while (lo < hi) {
            int mid = lo + (hi - lo) / 2;
            if (A.get(mid).time <= t)
                lo = mid + 1;
            else
                hi = mid;
        }
        return A.get(lo - 1).person;
    }
}

/**
 * Your TopVotedCandidate object will be instantiated and called as such:
 * TopVotedCandidate obj = new TopVotedCandidate(persons, times);
 * int param_1 = obj.q(t);
 */

# 180ms 93.86%
class TopVotedCandidate {
    int[] leading;
    int[] times;
    public TopVotedCandidate(int[] persons, int[] times) {
        this.times = times;
        int max = 0;
        int[] people = new int[persons.length + 1];
        leading = new int[persons.length];
        for (int i = 0; i < persons.length; i++) {
            int p = persons[i];
            max = Math.max(++people[p], max);
            leading[i] = people[p] == max ? p : leading[i-1];
        }
    }

    public int q(int t) {
        return leading[binarySearch(times, t, 0, times.length-1)];
    }

    private int binarySearch(int[] times, int target, int left, int right) {
        if (left > right) return right;
        int mid = (left + right) / 2;
        if (times[mid] > target) {
            return binarySearch(times, target, left, mid - 1);
        } else if (times[mid] < target) {
            return binarySearch(times, target, mid + 1, right);
        } else {
            return mid;
        }
    }
}

'''