__source__ = 'https://leetcode.com/problems/course-schedule-ii/description/'
# https://github.com/kamyu104/LeetCode/blob/master/Python/course-schedule-ii.py
# Time:  O(|V| + |E|)
# Space: O(|E|)
#
# Description: Leetcode #  210. Course Schedule II
#
# There are a total of n courses you have to take, labeled from 0 to n - 1.
#
# Some courses may have prerequisites, for example to take course 0 you have to first take course 1,
# which is expressed as a pair: [0,1]
#
# Given the total number of courses and a list of prerequisite pairs, return the ordering of courses
# you should take to finish all courses.
#
# There may be multiple correct orders, you just need to return one of them. If it is impossible
# to finish all courses, return an empty array.
#
# For example:
#
# 2, [[1,0]]
# There are a total of 2 courses to take. To take course 1 you should have finished course 0.
# So the correct course order is [0,1]
#
# 4, [[1,0],[2,0],[3,1],[3,2]]
# There are a total of 4 courses to take. To take course 3 you should have finished both courses 1 and 2.
# Both courses 1 and 2 should be taken after you finished course 0. So one correct course order is [0,1,2,3].
# Another correct ordering is[0,2,1,3].
#
# Note:
# The input prerequisites is a graph represented by a list of edges, not adjacency matrices.
# Read more about how a graph is represented.
#
# Hints:
# This problem is equivalent to finding the topological order in a directed graph.
# If a cycle exists, no topological ordering exists and therefore it will be impossible to take all courses.
# Topological Sort via DFS - A great video tutorial (21 minutes) on Coursera explaining
# the basic concepts of Topological Sort.
# Topological sort could also be done via BFS.
#
# Companies
# Facebook Zenefits
# Related Topics
# Depth-first Search Breadth-first Search Graph Topological Sort
# Similar Questions
# Course Schedule Alien Dictionary Minimum Height Trees Sequence Reconstruction Course Schedule III
#
import unittest
import collections
class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        from collections import deque
        ind_cnt = [0] * numCourses
        ind = [ [] for _ in xrange(numCourses)]

        for p, q in prerequisites:
            ind_cnt[p] += 1
            ind[q].append(p)

        dq = deque()
        res = []
        for i in xrange(numCourses):
            if ind_cnt[i] == 0:
                dq.append(i)
        k = 0
        while dq:
            cur = dq.popleft()
            k += 1
            res.append(cur)
            for courses in ind[cur]:
                ind_cnt[courses] -= 1
                if ind_cnt[courses] == 0:
                    dq.append(courses)

        if k!= numCourses:
            return []

        return res

class Solution2(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        res = []
        cnt = [ 0 for x in xrange(numCourses)]
        map = [ [] for x in xrange(numCourses)]
        queue = []

        for p, q in prerequisites:
            if p not in map[q]:
                map[q].append(p)
                cnt[p] += 1

        for i in xrange(len(cnt)):
            if cnt[i] == 0:
                queue.append(i)

        while queue:
            cur = queue[0]
            queue.pop(0)
            res.append(cur)
            for item in map[cur]:
                cnt[item] -= 1
                if cnt[item] == 0:
                    queue.append(item)

        for i in xrange(len(cnt)):
            if cnt[i] > 0:
                return []
        return res

class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)

if __name__ == '__main__':
    unittest.main()

Java = '''
# Thought:

Be aware of order of course when building map, that impact the result order

1) BFS, aka topological sort
This question asks for an order in which prerequisite courses must be taken first.
This prerequisite relationship reminds one of directed graphs.
Then, the problem reduces to find a topological sort order of the courses,
which would be a DAG if it has a valid order.
The first step is to transform it into a directed graph.
Since it is likely to be sparse,we use adjacency list graph data structure. 1 -> 2 means 1 must be taken before 2.
How can we obtain a topological sort order of a DAG?

We observe that if a node has incoming edges, it has prerequisites.
Therefore, the first few in the order must be those with no prerequisites,
i.e. no incoming edges. Any non-empty DAG must have at least one node without incoming links.
You can draw a small graph to convince yourself. If we visit these few and remove all edges attached to them,
we are left with a smaller DAG, which is the same problem. This will then give our BFS solution.

2) DFS: postorder
Another way to think about it is the last few in the order must be those which are not prerequisites of other courses.
Thinking it recursively means if one node has unvisited child node,
you should visit them first before you put this node down in the final order array.
This sounds like the post-order of a DFS. Since we are putting nodes down in the reverse order,
we should reverse it back to correct ordering or use a stack.

**
 * Solution with DFS.
 * Note that we need to use "post-order" traversal here,
 so that a course can be taken only after all its prerequisites (descendants) have been taken.
 * time complexity O(n + |E|) (13ms) where |E| is the number of edges and it is equal to prerequisites.length.
 It takes O(|E|) to arrange graph information and O(n) to do BFS.
 * space complexity O(n)
 */

# DFS
# 4ms 99.97%
class Solution {
    private int mIdx = 0;
    public int[] findOrder(int numCourses, int[][] prerequisites) {
        int[] result = new int[numCourses];
        List[] graph = new ArrayList[numCourses];
        for (int i = 0; i < numCourses; i++) graph[i] = new ArrayList<Integer>();
        for (int[] p : prerequisites) graph[p[0]].add(p[1]); //note, reversed with BFS or CourseSchedule1
        // dfs
        boolean[] visited = new boolean[numCourses];
        boolean[] currRoute = new boolean[numCourses];
        for (int u = 0; u < numCourses; u++) {
            if (!visited[u] && dfs(graph, visited, currRoute, u, result)) return new int[0];
        }
        return result;
    }

    private boolean dfs(List[] graph, boolean[] visited, boolean[] currRoute, int idx, int[] result) {
        if (visited[idx]) return false;
        currRoute[idx] = true;
        for (int i = graph[idx].size() - 1; i >= 0; i--) { // reverse iterated so that result in correct order
            int v = (int)graph[idx].get(i);
            if (currRoute[v] || dfs(graph, visited, currRoute, v, result)) return true;
        }
        currRoute[idx] = false;
        visited[idx] = true;
        result[mIdx++] = idx;
        return false;
    }
}

# DFS
# 4ms 99.97%
class Solution {
    private int mIdx = 0;
    public int[] findOrder(int numCourses, int[][] prerequisites) {
        //if(numCourses == 0 || prerequisites == null || prerequisites.length == 0) return new int[0]; //failed findOrder(1, [])
        int[] result = new int[numCourses];

        Map<Integer, List<Integer>> map = new HashMap<>();
        for(int[] p : prerequisites){
            if(! map.containsKey(p[0])){
                map.put(p[0], new ArrayList());
            }
            map.get(p[0]).add(p[1]); //note, p[0] needs to be key as order impacts result
        }

        // dfs
        int[] visited = new int[numCourses];
        for(int i = 0; i < numCourses ; i++) {
            if(!dfs(visited, map, i, result)) return new int[0];
        }
        return result;
    }

    private boolean dfs(int[] visited, Map<Integer, List<Integer>> map, int idx, int[] result ){
        if (visited[idx] == -1) return false;
        if (visited[idx] == 1) return true;
        visited[idx] = -1;
        if (map.containsKey(idx)) {
            for (int val: map.get(idx)) {
                if (!dfs(visited, map, val, result)) return false;
            }
        }
        visited[idx] = 1;
        result[mIdx++] = idx;
        return true;
    }
}


# Topological sort (BFS) with list
# 6ms 96.66%
class Solution {
    public int[] findOrder(int numCourses, int[][] prerequisites) {
        int[] result = new int[numCourses];
        int index = 0;
        List<List<Integer>> graph = new ArrayList<>();
        int[] degrees = new int[numCourses];
        Queue<Integer> queue = new LinkedList<>();

        buildGraph(numCourses, prerequisites, graph, degrees);
        for (int i = 0; i < numCourses; i++) {
            if (degrees[i] == 0) {
                queue.add(i);
            }
        }
        while (!queue.isEmpty()) {
            int cur = queue.poll();
            result[index++] = cur;
            for (int next : graph.get(cur)) {
                degrees[next]--;
                if (degrees[next] == 0) {
                    queue.add(next);
                }
            }
        }
        return index == numCourses ? result : new int[0];
    }

    private void buildGraph(int numCourses, int[][] prerequisites, List<List<Integer>> graph, int[] degrees) {
        for (int i = 0; i < numCourses; i++) {
            graph.add(new ArrayList<>());
        }
        for (int[] edge : prerequisites) {
            graph.get(edge[1]).add(edge[0]);
            degrees[edge[0]]++;
        }
    }
}

# Topological sort (BFS) with map
# 7ms 90.34%
class Solution {
    public int[] findOrder(int numCourses, int[][] prerequisites) {
        int[] result = new int[numCourses];
        int index = 0;
        int[] degree = new int[numCourses];

        //build graph and degree arr
        Map<Integer, List<Integer>> map = new HashMap<>();
        for (int i = 0; i < numCourses; i++) {
            map.put(i, new ArrayList<>());
        }
        for (int[] preq : prerequisites) {
            map.get(preq[1]).add(preq[0]);
            degree[preq[0]]++; //degree++ preq
        }

        Queue<Integer> q = new LinkedList<>();
        for (int i = 0; i < numCourses; i++) {
            if(degree[i] == 0) q.add(i);
        }

        while(!q.isEmpty()){
            int cur = q.poll();
            result[index++] = cur; //add cur to result
            for (int next : map.get(cur)) {
                degree[next]--;
                if (degree[next] == 0) q.add(next);
            }
        }
        return index == numCourses ? result : new int[0];
    }

}
'''