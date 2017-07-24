__source__ = 'https://leetcode.com/problems/clone-graph/description/'
# https://github.com/kamyu104/LeetCode/blob/master/Python/clone-graph.py
# Time:  O(n)
# Space: O(n)
# BFS
#
# Clone an undirected graph. Each node in the graph contains a label and a list of its neighbors.
#
#
# OJ's undirected graph serialization:
# Nodes are labeled uniquely.
#
# We use # as a separator for each node, and , as a separator for node label and each neighbor of the node.
# As an example, consider the serialized graph {0,1,2#1,2#2,2}.
#
# The graph has a total of three nodes, and therefore contains three parts as separated by #.
#
# First node is labeled as 0. Connect node 0 to both nodes 1 and 2.
# Second node is labeled as 1. Connect node 1 to node 2.
# Third node is labeled as 2. Connect node 2 to node 2 (itself), thus forming a self-cycle.
# Visually, the graph looks like the following:
#
#        1
#       / \
#      /   \
#     0 --- 2
#          / \
#          \_/
#
#
# Companies
# Pocket Gems Google Uber Facebook
# Related Topics
# Depth-first Search Breadth-first Search Graph
# Similar Questions
# Copy List with Random Pointer
#
# Definition for a undirected graph node
class UndirectedGraphNode:
     def __init__(self, x):
         self.label = x
         self.neighbors = []

class Solution:
    # @param node, a undirected graph node
    # @return a undirected graph node
    def cloneGraph(self, node):
        if node == None:
            return None
        cloned_node = UndirectedGraphNode(node.label)
        cloned, queue = {node: cloned_node}, [node]

        while queue:
            current = queue.pop()
            for neighbor in current.neighbors:
                if neighbor not in cloned:
                    queue.append(neighbor)
                    cloned_neighbor = UndirectedGraphNode(neighbor.label)
                    cloned[neighbor] = cloned_neighbor
                cloned[current].neighbors.append(cloned[neighbor])
        return cloned[node]



class SolutionOther:
    # @param node, a undirected graph node
    # @return a undirected graph node
    def cloneGraph(self, node):
        nodeMap = {}
        return self.dfs(node, nodeMap)

    def dfs(self, node, nodemap):
        if node == None:
            return None
        if node.label in nodemap:
            return nodemap[node.label]

        newNode = UndirectedGraphNode(node.label)
        nodemap[node.label] = newNode

        for neighbor in node.neighbors:
            newNode.neighbors.append(self.dfs(neighbor, nodemap))

        return newNode


    def cloneGraphUsingBFS(self, node):
        if node == None:
            return None
        queue = []
        map = {}
        head = UndirectedGraphNode(node.label)
        queue.append(node)
        map[node] = head

        while queue:
            curr = queue.pop()
            for neighbor in curr.neighbors:
                if neighbor not in map:
                    newNode = UndirectedGraphNode(neighbor.label)
                    map[curr].neighbors.append(newNode)
                    map[neighbor] = newNode
                    queue.append(neighbor)
                else:
                    # turn directed graph to undirected graph
                    map[curr].neighbors.append(map[neighbor])
        return head
#test

#Java
Java = '''
/**
 * Definition for undirected graph.
 * class UndirectedGraphNode {
 *     int label;
 *     List<UndirectedGraphNode> neighbors;
 *     UndirectedGraphNode(int x) { label = x; neighbors = new ArrayList<UndirectedGraphNode>(); }
 * };
 */
# DFS:
# 74.34% 5ms
public class Solution {
    public UndirectedGraphNode cloneGraph(UndirectedGraphNode node) {
        HashMap<Integer, UndirectedGraphNode> map = new HashMap<>();
        return clone(node, map);
    }

    private UndirectedGraphNode clone(UndirectedGraphNode node, Map<Integer, UndirectedGraphNode> map) {
        if (node == null) return null;
        if (map.containsKey(node.label)) return map.get(node.label);
        UndirectedGraphNode clone = new UndirectedGraphNode(node.label);
        map.put(clone.label, clone);

        for (UndirectedGraphNode neighbor: node.neighbors) {
            clone.neighbors.add(clone(neighbor, map));
        }
        return clone;
    }
}

# BFS:
# 45.32% 8ms
public class Solution {
    public UndirectedGraphNode cloneGraph(UndirectedGraphNode node) {
        if (node == null) {
            return null;
        }
        Stack<UndirectedGraphNode> stack = new Stack<>();
        stack.push(node);
        Map<UndirectedGraphNode, UndirectedGraphNode> newGraphMap = new HashMap<>();
        newGraphMap.put(node, new UndirectedGraphNode(node.label));
        while (!stack.isEmpty()) {
            UndirectedGraphNode oldCurr = stack.pop();
            UndirectedGraphNode newCurr = newGraphMap.get(oldCurr);
            for (UndirectedGraphNode oldNeighbor : oldCurr.neighbors) {
                UndirectedGraphNode newNeighbor = newGraphMap.get(oldNeighbor);
                if (newNeighbor == null) {
                    stack.push(oldNeighbor);
                    newNeighbor = new UndirectedGraphNode(oldNeighbor.label);
                    newGraphMap.put(oldNeighbor, newNeighbor);
                }
                newCurr.neighbors.add(newNeighbor);
            }
        }
        return newGraphMap.get(node);
    }
}

# 31.88% 9ms
public class Solution {
    public UndirectedGraphNode cloneGraph(UndirectedGraphNode node) {
        if (node == null) return null;
        UndirectedGraphNode clone = new UndirectedGraphNode(node.label);
        HashMap<Integer, UndirectedGraphNode> map = new HashMap(); //store visited nodes
        map.put(clone.label, clone); //add first node to HashMap

        LinkedList<UndirectedGraphNode> queue = new LinkedList(); //to store **original** nodes need to be visited
        queue.add(node); //add first **original** node to queue
        while(!queue.isEmpty()) {
            UndirectedGraphNode n = queue.pop();
            for(UndirectedGraphNode neighbor : n.neighbors) {
                if (!map.containsKey(neighbor.label)) {
                    map.put(neighbor.label, new UndirectedGraphNode(neighbor.label));
                    queue.add(neighbor);
                }
                map.get(n.label).neighbors.add(map.get(neighbor.label));
            }
        }
        return clone;
    }
}

'''