import collections

__author__ = 'July'
# https://github.com/kamyu104/LeetCode/blob/master/Python/reconstruct-itinerary.py
# Time:  O(t! / (n1! * n2! * ... nk!)), t is the total number of tickets,
#                                       ni is the number of the ticket which from is city i,
#                                       k is the total number of cities.
# Space: O(t)

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
tick = [["MUC","LHR"],["JFK","MUC"],["SFO","SJC"],["LHR","SFO"]]
t2 = [["LST","TBI"],["AXA","ELH"],["ASD","CBR"],["AUA","ELH"],["VIE","NAS"],["BAK","BIM"],["MHH","TCB"],["TIA","JFK"],["MHH","ASD"],["HBA","TIA"],["MHH","OOL"],["AUA","TIA"],["TIA","VIE"],["BNE","ADL"],["ASD","BIM"],["PER","GGT"],["MHH","SYD"],["ELH","MEL"],["EZE","OOL"],["TBI","PER"],["ANU","BNE"],["BAK","JFK"],["DAC","CBR"],["HBA","MHH"],["CBR","TIA"],["INN","TIA"],["DAC","MHH"],["CBR","BAK"],["TCB","PER"],["ASD","TIA"],["LST","TIA"],["VIE","TCB"],["OOL","TBI"],["AUA","PER"],["TIA","LST"],["BAK","TBI"],["MHH","LST"],["MEL","ASD"],["ASD","PER"],["BIM","ASD"],["BNE","BIM"],["BAK","INN"],["TCB","AUA"],["ADL","TIA"],["SYD","HBA"],["TIA","AUA"],["DAC","NAS"],["CBR","AXA"],["VIE","MHH"],["AXA","VIE"],["CBR","VIE"],["BIM","EZE"],["BIM","INN"],["TCB","MEL"],["TBI","CBR"],["FPO","LST"],["PER","INN"],["INN","VIE"],["NAS","OOL"],["MEL","HBA"],["TIA","CNS"],["NAS","ADL"],["DAC","LST"],["GGT","HBA"],["NAS","ASD"],["CBR","AXA"],["BAK","CBR"],["BNE","BAK"],["JFK","AXA"],["BIM","AUA"],["NAS","BNE"],["PER","INN"],["EZE","DAC"],["TBI","DAC"],["BNE","BIM"],["MHH","PER"],["TCB","OOL"],["CNS","TIA"],["BAK","TCB"],["ADL","BAK"],["LST","INN"],["ASD","TIA"],["PER","LST"],["HBA","BAK"],["CNS","TCB"],["BIM","AUA"],["OOL","SYD"],["VIE","BNE"],["VIE","TIA"],["ASD","DAC"],["BAH","BNE"],["PER","CBR"],["ANU","ASD"],["AXA","MHH"],["ELH","VIE"],["JFK","DAC"],["LST","BAK"],["BIM","ANU"],["AUA","BIM"],["BAK","ASD"],["TBI","TIA"],["MHH","PER"],["VIE","DAC"],["OOL","BNE"],["BAH","FPO"],["CNS","VIE"],["PER","NAS"],["TIA","BAH"],["OOL","DRW"],["CBR","GGT"],["DRW","AUA"],["SYD","CBR"],["AUA","ELH"],["ASD","GGT"],["DAC","HBA"],["VIE","AXA"],["TIA","LST"],["AXA","TCB"],["GGT","BAH"],["INN","BIM"],["TIA","ASD"],["PER","OOL"],["LST","ANU"],["TIA","BIM"],["INN","CBR"],["BNE","MHH"],["TCB","VIE"],["GGT","TBI"],["AXA","CNS"],["LST","EZE"],["BNE","CNS"],["SYD","BNE"],["CBR","SYD"],["CNS","BIM"],["JFK","CNS"],["BIM","BAK"],["HBA","MHH"],["ELH","BAK"],["INN","AXA"],["BIM","ANU"],["ANU","PER"],["TIA","MHH"],["TIA","NAS"]]
if __name__ == "__main__":
    print Solution2().findItinerary(t2)
    print Solution().findItinerary(t2)