__source__ = 'https://leetcode.com/problems/reconstruct-itinerary/'
# https://github.com/kamyu104/LeetCode/blob/master/Python/reconstruct-itinerary.py
# Time:  O(t! / (n1! * n2! * ... nk!)), t is the total number of tickets,
#                                       ni is the number of the ticket which from is city i,
#                                       k is the total number of cities.
# Space: O(t)
#
# Description: Leetcode # 332. Reconstruct Itinerary
#
# Given a list of airline tickets represented by pairs of departure
# and arrival airports [from, to], reconstruct the itinerary in order.
# All of the tickets belong to a man who departs from JFK.
# Thus, the itinerary must begin with JFK.
#
# Note:
# If there are multiple valid itineraries, you should return the itinerary
# that has the smallest lexical order when read as a single string.
# For example, the itinerary ["JFK", "LGA"] has a smaller lexical
# order than ["JFK", "LGB"].
# All airports are represented by three capital letters (IATA code).
# You may assume all tickets may form at least one valid itinerary.
# Example 1:
# tickets = [["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]
# Return ["JFK", "MUC", "LHR", "SFO", "SJC"].
# Example 2:
# tickets = [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
# Return ["JFK","ATL","JFK","SFO","ATL","SFO"].
# Another possible reconstruction is ["JFK","SFO","ATL","JFK","ATL","SFO"].
# But it is larger in lexical order.
#
# Companies
# Google
# Related Topics
# Depth-first Search Graph
#
import collections
import unittest
class Solution(object):
    ans = ["JFK"]
    def findItinerary(self, tickets):
        """
        :type tickets: List[List[str]]
        :rtype: List[str]
        """
        graph = collections.defaultdict(list)
        for ticket in tickets:
            graph[ticket[0]].append([ticket[1], True])
        for k in graph.keys():
            graph[k].sort()

        self.dfs("JFK", len(tickets), graph, self.ans)
        return self.ans

    def dfs(self, origin, ticket_cnt, graph, ans):
            if ticket_cnt == 0:
                return True

            for i, (dest, valid)  in enumerate(graph[origin]):
                if valid:
                    graph[origin][i][1] = False
                    ans.append(dest)
                    if self.dfs(dest, ticket_cnt - 1, graph, ans):
                        return ans
                    ans.pop()
                    graph[origin][i][1] = True
            return False

class Solution2(object):
    def findItinerary(self, tickets):
        """
        :type tickets: List[List[str]]
        :rtype: List[str]
        """
        def route_helper(origin, ticket_cnt, graph, ans):
            if ticket_cnt == 0:
                return True

            for i, (dest, valid)  in enumerate(graph[origin]):
                if valid:
                    graph[origin][i][1] = False
                    ans.append(dest)
                    if route_helper(dest, ticket_cnt - 1, graph, ans):
                        return ans
                    ans.pop()
                    graph[origin][i][1] = True
            return False

        graph = collections.defaultdict(list)
        for ticket in tickets:
            graph[ticket[0]].append([ticket[1], True])
        for k in graph.keys():
            graph[k].sort()

        origin = "JFK"
        ans = [origin]
        route_helper(origin, len(tickets), graph, ans)
        return ans

#test
class TestMethods(unittest.TestCase):
    def test_Local(self):
        tick = [["MUC","LHR"],["JFK","MUC"],["SFO","SJC"],["LHR","SFO"]]
        t2 = [["LST","TBI"],["AXA","ELH"],["ASD","CBR"],["AUA","ELH"],["VIE","NAS"],["BAK","BIM"],["MHH","TCB"],["TIA","JFK"],["MHH","ASD"],["HBA","TIA"],["MHH","OOL"],["AUA","TIA"],["TIA","VIE"],["BNE","ADL"],["ASD","BIM"],["PER","GGT"],["MHH","SYD"],["ELH","MEL"],["EZE","OOL"],["TBI","PER"],["ANU","BNE"],["BAK","JFK"],["DAC","CBR"],["HBA","MHH"],["CBR","TIA"],["INN","TIA"],["DAC","MHH"],["CBR","BAK"],["TCB","PER"],["ASD","TIA"],["LST","TIA"],["VIE","TCB"],["OOL","TBI"],["AUA","PER"],["TIA","LST"],["BAK","TBI"],["MHH","LST"],["MEL","ASD"],["ASD","PER"],["BIM","ASD"],["BNE","BIM"],["BAK","INN"],["TCB","AUA"],["ADL","TIA"],["SYD","HBA"],["TIA","AUA"],["DAC","NAS"],["CBR","AXA"],["VIE","MHH"],["AXA","VIE"],["CBR","VIE"],["BIM","EZE"],["BIM","INN"],["TCB","MEL"],["TBI","CBR"],["FPO","LST"],["PER","INN"],["INN","VIE"],["NAS","OOL"],["MEL","HBA"],["TIA","CNS"],["NAS","ADL"],["DAC","LST"],["GGT","HBA"],["NAS","ASD"],["CBR","AXA"],["BAK","CBR"],["BNE","BAK"],["JFK","AXA"],["BIM","AUA"],["NAS","BNE"],["PER","INN"],["EZE","DAC"],["TBI","DAC"],["BNE","BIM"],["MHH","PER"],["TCB","OOL"],["CNS","TIA"],["BAK","TCB"],["ADL","BAK"],["LST","INN"],["ASD","TIA"],["PER","LST"],["HBA","BAK"],["CNS","TCB"],["BIM","AUA"],["OOL","SYD"],["VIE","BNE"],["VIE","TIA"],["ASD","DAC"],["BAH","BNE"],["PER","CBR"],["ANU","ASD"],["AXA","MHH"],["ELH","VIE"],["JFK","DAC"],["LST","BAK"],["BIM","ANU"],["AUA","BIM"],["BAK","ASD"],["TBI","TIA"],["MHH","PER"],["VIE","DAC"],["OOL","BNE"],["BAH","FPO"],["CNS","VIE"],["PER","NAS"],["TIA","BAH"],["OOL","DRW"],["CBR","GGT"],["DRW","AUA"],["SYD","CBR"],["AUA","ELH"],["ASD","GGT"],["DAC","HBA"],["VIE","AXA"],["TIA","LST"],["AXA","TCB"],["GGT","BAH"],["INN","BIM"],["TIA","ASD"],["PER","OOL"],["LST","ANU"],["TIA","BIM"],["INN","CBR"],["BNE","MHH"],["TCB","VIE"],["GGT","TBI"],["AXA","CNS"],["LST","EZE"],["BNE","CNS"],["SYD","BNE"],["CBR","SYD"],["CNS","BIM"],["JFK","CNS"],["BIM","BAK"],["HBA","MHH"],["ELH","BAK"],["INN","AXA"],["BIM","ANU"],["ANU","PER"],["TIA","MHH"],["TIA","NAS"]]
        print Solution2().findItinerary(t2)
        print Solution().findItinerary(t2)

if __name__ == '__main__':
    unittest.main()

Java = '''
# Thought: 
# http://algobox.org/reconstruct-itinerary/
Just Eulerian path. Greedy DFS, building the route backwards when retreating.

All the airports are vertices and tickets are directed edges. 
Then all these tickets form a directed graph.

The graph must be Eulerian since we know that a Eulerian path exists.

Thus, start from "JFK", we can apply the Hierholzer's algorithm
to find a Eulerian path in the graph which is a valid reconstruction.

Since the problem asks for lexical order smallest solution,
we can put the neighbors in a min-heap. In this way, 
we always visit the smallest possible neighbor first in our trip.



# 7ms 75.17%
class Solution {
    public List<String> findItinerary(String[][] tickets) {
        HashMap<String, PriorityQueue<String>> map = new HashMap<String, PriorityQueue<String>>();
	    LinkedList<String> result = new LinkedList<String>();

        for (String[] tkt: tickets) {
            if (!map.containsKey(tkt[0])) {
                PriorityQueue<String> q = new PriorityQueue<>();
                map.put(tkt[0], q);
            }
            map.get(tkt[0]).offer(tkt[1]);
        }
        dfs("JFK", map, result);
        return result;
    }

    public void dfs(String s, HashMap<String, PriorityQueue<String>> map, LinkedList<String> result) {
        PriorityQueue<String> q = map.get(s);
        while(q != null && ! q.isEmpty()) dfs(q.poll(), map, result);
        result.addFirst(s);
    }
}


# BFS
# 77ms 3.33%
class Solution {
    public List<String> findItinerary(String[][] tickets) {
        Map<String, PriorityQueue<String>> targets = new HashMap<>();
        for (String[] ticket : tickets)
            targets.computeIfAbsent(ticket[0], k -> new PriorityQueue()).add(ticket[1]);
        List<String> route = new LinkedList();
        Stack<String> stack = new Stack<>();
        stack.push("JFK");
        while (!stack.empty()) {
            while (targets.containsKey(stack.peek()) && !targets.get(stack.peek()).isEmpty())
                stack.push(targets.get(stack.peek()).poll());
            route.add(0, stack.pop());
        }
        return route;
    }
}

# 7ms 75.17%
class Solution {
    public List<String> findItinerary(String[][] tickets) {
        String[] path = new String[tickets.length + 1];
        path[0] = "JFK";
        Map<String, List<String>> graph = buildGraph(tickets);
        if (dfs(path, 1, graph)) {
            return Arrays.asList(path);
        }
        return new ArrayList<>();
    }

    private Map<String, List<String>> buildGraph(String[][] tickets) {
        Map<String, List<String>> graph = new HashMap<>();
        for (String[] ticket : tickets) {
            if (!graph.containsKey(ticket[0])) {
                graph.put(ticket[0], new ArrayList<>());
            }
            graph.get(ticket[0]).add(ticket[1]);
        }
        for (Map.Entry<String, List<String>> entry : graph.entrySet()) {
            Collections.sort(entry.getValue());
        }
        return graph;
    }

    private boolean dfs(String[] path, int index, Map<String, List<String>> graph) {
        if (index == path.length) {
            return true;
        }
        List<String> nextCities = graph.get(path[index - 1]);
        if (nextCities == null) {
            return false;
        }
        for (int i = 0; i < nextCities.size(); i++) {
            String nextCity = nextCities.get(i);
            if (nextCity == null) {
                continue;
            }
            path[index] = nextCity;
            nextCities.set(i, null);
            if (dfs(path, index + 1, graph)) {
                return true;
            }
            nextCities.set(i, nextCity);
        }
        return false;
    }
}
'''
