__source__ = 'https://leetcode.com/problems/course-schedule/description/'
# https://github.com/kamyu104/LeetCode/blob/master/Python/course-schedule.py
# Time:  O(|V| + |E|)
# Space: O(|E|)
#
# Description: Leetcode # 207. Course Schedule
#
# There are a total of n courses you have to take, labeled from 0 to n - 1.
#
# Some courses may have prerequisites, for example to take course 0
# you have to first take course 1, which is expressed as a pair: [0,1]
#
# Given the total number of courses and a list of prerequisite pairs,
#  is it possible for you to finish all courses?
#
# For example:
#
# 2, [[1,0]]
# There are a total of 2 courses to take. To take course 1
# you should have finished course 0. So it is possible.
#
# 2, [[1,0],[0,1]]
# There are a total of 2 courses to take. To take course 1 you should have
# finished course 0, and to take course 0 you should also have finished course 1. So it is impossible.
#
# click to show more hints.
#
# Hints:
# This problem is equivalent to finding if a cycle exists in a directed graph.
# If a cycle exists, no topological ordering exists and therefore it will be impossible to take all courses.
# There are several ways to represent a graph. For example, the input prerequisites is a graph represented by
#  a list of edges. Is this graph representation appropriate?
# Topological Sort via DFS - A great video tutorial (21 minutes) on Coursera explaining the basic concepts
#  of Topological Sort.
# Topological sort could also be done via BFS.
#
# Companies
# Apple Yelp Zenefits
# Related Topics
# Depth-first Search Breadth-first Search Graph Topological Sort
# Similar Questions
# Course Schedule II Graph Valid Tree Minimum Height Trees Course Schedule III
#
import collections
import unittest
# http://algobox.org/course-schedule/
class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        from collections import deque
        n = numCourses

        ind = [ [] for _ in xrange(n)] #indegree
        ind_cnt = [0] * n #outdegree

        for p in prerequisites:
            ind_cnt[p[0]] += 1
            ind[p[1]].append(p[0])

        print ind, ind_cnt
        dq = deque()
        for i in xrange(n):
            if ind_cnt[i] == 0:
                dq.append(i)

        k = 0
        while dq:
            x = dq.popleft()
            k += 1
            for i in ind[x]:
                ind_cnt[i] -= 1
                if ind_cnt[i] == 0:
                    dq.append(i)
        return k == n

class Solution2(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        if not prerequisites or numCourses == 0:
            return True

        indegree = [ 0 for x in xrange(numCourses)]
        queue = []

        for p, q in prerequisites:
                indegree[p] += 1

        for i in xrange(len(indegree)):
            if indegree[i] == 0:
                queue.append(i)

        while queue:
            cur = queue[0]
            queue.pop(0)
            for p, q in prerequisites:
                if q == cur:
                    indegree[p] -= 1
                    if indegree[p] == 0:
                        queue.append(p)

        for i in xrange(len(indegree)):
             if indegree[i] > 0:
                 return False

        return True

class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)
        print Solution().canFinish(1, [])

if __name__ == '__main__':
    unittest.main()

Java = '''
#Thought: https://leetcode.com/problems/contains-duplicate/solution/

#BFS //aka traditional topological sort
#68.76% 12ms
public class Solution {
    public boolean canFinish(int numCourses, int[][] prerequisites) {
        Map<Integer, List<Integer>> graph = new HashMap<>();
        int[] degrees = new int[numCourses];
        Queue<Integer> queue = new LinkedList<>();
        int count = numCourses;
        for (int i = 0; i < numCourses; i++) {
            graph.put(i, new ArrayList<>());
        }
        for (int[] prerequisite : prerequisites) {
            graph.get(prerequisite[1]).add(prerequisite[0]);
            degrees[prerequisite[0]]++; //drgree 0 not 1 //degree++ preq
        }
        for (int i = 0; i < numCourses; i++) {
            if (degrees[i] == 0) {
                queue.add(i);
                count--; // or (i) count = 0
            }
        }
        while (!queue.isEmpty()) {
            int cur = queue.poll(); //and (ii) do count++ here, and last verify count == numCourses
            for (int next : graph.get(cur)) {
                degrees[next]--;
                if (degrees[next] == 0) {
                    queue.add(next);
                    count--;
                }
            }
        }
        return count == 0;
    }
}


#99.72%  2ms use arr
public class Solution {
    public boolean canFinish(int numCourses, int[][] prerequisites) {
        if(numCourses == 0 || prerequisites == null || prerequisites.length == 0) return true;
        int[] degree = new int[numCourses];
        int[] point = new int[numCourses];
        int[] next = new int[prerequisites.length + 1];

        for (int i = 0; i < prerequisites.length; i++) {
            next[i + 1] = point[prerequisites[i][1]];
            point[prerequisites[i][1]] = i + 1;
            degree[prerequisites[i][0]]++;
        }

        int head = 0, tail = 0;
        int[] q = new int[numCourses];
        for (int i =0 ; i < numCourses; i++) {
            if (degree[i] == 0) {
                q[tail] = i;
                tail++;
            }
        }
        if (tail == numCourses) return true;

        while (head < tail) {
            int l = point[q[head]];
            while (l != 0) {
                degree[prerequisites[l - 1][0]]--;
                if (degree[prerequisites[l - 1][0]]== 0) {
                    q[tail] = prerequisites[l-1][0];
                    tail++;
                    if (tail == numCourses) return true;
                }
                l = next[l];
            }
            head++;
        }
        return false;
    }
}

#Topological Sort //bother p[0], p[1] can be key but degree only adds at value noy key
ex:
for(int[] p : prerequisites){
            ind_cnt[p[1]] += 1;
            ind.get(p[0]).add(p[1]);
        }

for(int[] p : prerequisites){
            ind_cnt[p[0]] += 1;
            ind.get(p[1]).add(p[0]);
        }

#73.68% 10ms
public class Solution {
    public boolean canFinish(int numCourses, int[][] prerequisites) {
        //The ind_cnt[i] is the number of prereqs for course i
        //aka indegree count
        int[] ind_cnt = new int[numCourses];
        List<List<Integer>> ind = new ArrayList<>();
        for(int i = 0; i < numCourses ; i++){
            ind.add(new ArrayList<>());
        }

        for(int[] p : prerequisites){
            ind_cnt[p[0]] += 1;
            ind.get(p[1]).add(p[0]);
        }

        Queue<Integer> queue = new ArrayDeque<>();
        for(int i = 0; i < numCourses ; i++){
            if(ind_cnt[i] == 0){
                queue.offer(i);
            }
        }

        int k = 0;
        //for (;!queue.isEmpty();++k)
        //    for (int i : ind.get(queue.poll())) if (--oud[i] == 0) queue.offer(i);

        while(!queue.isEmpty()){
            int i = queue.poll();
            k += 1;
            for(int j : ind.get(i)){
                ind_cnt[j] -= 1;
                if(ind_cnt[j] == 0){
                    queue.offer(j);
                }
            }
        }
        return k == numCourses;

    }
}

# DFS //note, either p[0], p[1] can be key
#64.05% 14ms
public class Solution {
    public boolean canFinish(int numCourses, int[][] prerequisites) {
        if(numCourses == 0 || prerequisites == null || prerequisites.length == 0) return true;
        int[] visited = new int[numCourses];
        Map<Integer, List<Integer>> map = new HashMap<>();
        for(int[] p : prerequisites){
            if(! map.containsKey(p[1])){  //note, either p[0], p[1] can be key
                map.put(p[1], new ArrayList());
            }
            map.get(p[1]).add(p[0]);
        }
        for(int i = 0; i < numCourses ; i++){
            if(!dfs(visited, map, i)){
                return false;
            }
        }
        return true;
    }

    //During recursion, if we follow a back edge which points to a previous node which is being visited,
    // then we find a cycle. Return false
    private boolean dfs(int[] visited, Map<Integer, List<Integer>> map, int i ){
        if(visited[i] == -1){  //visited
            return false;
        }
        if(visited[i] == 1){  //not visit
            return true;
        }
        visited[i] = -1; // mark as visited
        if(map.containsKey(i)){
            for(int val: map.get(i)){
                if(!dfs(visited, map, val)){
                    return false;
                }
            }
        }
        visited[i] = 1;  //unmark visited
        return true;
    }
}
'''