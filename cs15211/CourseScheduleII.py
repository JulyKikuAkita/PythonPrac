import sets
import collections

__author__ = 'July'
# https://github.com/kamyu104/LeetCode/blob/master/Python/course-schedule-ii.py
# Time:  O(|V| + |E|)
# Space: O(|E|)

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
# Facebook Zenefits


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


# java
js = '''
#DFS
public class Solution {
    private int idx = 0;
    public int[] findOrder(int numCourses, int[][] prerequisites) {
        //DFS
        if(numCourses == 0 || prerequisites == null || prerequisites.length == 0) return new int[0];
        idx = numCourses -1;
        int[] visited = new int[numCourses];
        Map<Integer, List<Integer>> map = new HashMap<>();
        int[] res = new int[numCourses];

        for(int[] p : prerequisites){
            if(! map.containsKey(p[1])){
                map.put(p[1], new ArrayList());
            }
            map.get(p[1]).add(p[0]);
        }
        for(int i = 0; i < numCourses ; i++){
            if(!dfs(visited, map, i, res)){
                return new int[0];
            }
        }
        return res;

    }

    //During recursion, if we follow a back edge which points to a previous node which is being visited,
    // then we find a cycle. Return false
    private boolean dfs(int[] visited, Map<Integer, List<Integer>> map, int i , int[] res){
        if(visited[i] == -1){  //visited
            return false;
        }
        if(visited[i] == 1){  //not visit
            return true;
        }
        visited[i] = -1; // mark as visited
        if(map.containsKey(i)){
            for(int val: map.get(i)){
                if(!dfs(visited, map, val, res)){
                    return false;
                }
            }
        }
        res[idx--] = i;
        visited[i] = 1;  //unmark visited
        return true;
    }
}
#BFS
public class Solution {
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
'''