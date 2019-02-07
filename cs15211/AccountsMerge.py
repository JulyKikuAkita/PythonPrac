__source__ = ' https://leetcode.com/problems/accounts-merge/'
# Time:  O(AlogA), where A is the sum of all str length of accounts[i]
# Space: O(A), the space used by our DSU structure.
#
# Description: Leetcode # 721. Accounts Merge
#
# Given a list accounts, each element accounts[i] is a list of strings,
# where the first element accounts[i][0] is a name,
# and the rest of the elements are emails representing emails of the account.
#
# Now, we would like to merge these accounts.
# Two accounts definitely belong to the same person if there is some email that is common to both accounts.
# Note that even if two accounts have the same name,
# they may belong to different people as people could have the same name.
# A person can have any number of accounts initially,
# but all of their accounts definitely have the same name.
#
# After merging the accounts, return the accounts in the following format:
# the first element of each account is the name, and the rest of the elements are emails in sorted order.
# The accounts themselves can be returned in any order.
#
# Example 1:
# Input:
# accounts = [["John", "johnsmith@mail.com", "john00@mail.com"], ["John", "johnnybravo@mail.com"],
# ["John", "johnsmith@mail.com", "john_newyork@mail.com"], ["Mary", "mary@mail.com"]]
# Output: [["John", 'john00@mail.com', 'john_newyork@mail.com', 'johnsmith@mail.com'],
# ["John", "johnnybravo@mail.com"], ["Mary", "mary@mail.com"]]
# Explanation:
# The first and third John's are the same person as they have the common email "johnsmith@mail.com".
# The second John and Mary are different people as none of their email addresses are used by other accounts.
# We could return these lists in any order, for example the answer [['Mary', 'mary@mail.com'],
# ['John', 'johnnybravo@mail.com'],
# ['John', 'john00@mail.com', 'john_newyork@mail.com', 'johnsmith@mail.com']] would still be accepted.
# Note:
#
# The length of accounts will be in the range [1, 1000].
# The length of accounts[i] will be in the range [1, 10].
# The length of accounts[i][j] will be in the range [1, 30].
#
#
import unittest
import collections
class Solution(object):
    def accountsMerge(self, accounts):
        """
        :type accounts: List[List[str]]
        :rtype: List[List[str]]
        """
        em_to_name = {}
        graph = collections.defaultdict(set)
        for acc in accounts:
            name = acc[0]
            for email in acc[1:]:
                graph[acc[1]].add(email)
                graph[email].add(acc[1])
                em_to_name[email] = name

        seen = set()
        ans = []
        for email in graph:
            if email not in seen:
                seen.add(email)
                stack = [email]
                component = []
                while stack:
                    node = stack.pop()
                    component.append(node)
                    for nei in graph[node]:
                        if nei not in seen:
                            seen.add(nei)
                            stack.append(nei)
                ans.append([em_to_name[email]] + sorted(component))
        return ans

#Union find
class Solution2(object):
    def accountsMerge(self, accounts):
        """
        :type accounts: List[List[str]]
        :rtype: List[List[str]]
        """
        dsu = DSU()
        em_to_name = {}
        em_to_id = {}
        i = 0
        for acc in accounts:
            name = acc[0]
            for email in acc[1:]:
                em_to_name[email] = name
                if email not in em_to_id:
                    em_to_id[email] = i
                    i += 1
                dsu.union(em_to_id[acc[1]], em_to_id[email])

        ans = collections.defaultdict(list)
        for email in em_to_name:
            ans[dsu.find(em_to_id[email])].append(email)
        return [[em_to_name[v[0]]] + sorted(v) for v in ans.values() ]


class DSU:
    def __init__(self):
        self.p = range(10001)

    def find(self, x):
        if self.p[x] != x:
            self.p[x] = self.find(self.p[x])
        return self.p[x]

    def union(self, x, y):
        self.p[self.find(x)] = self.find(y)


class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)


if __name__ == '__main__':
    unittest.main()

Java = '''
#Thought: https://leetcode.com/problems/accounts-merge/solution/
#
# Approach #1: Depth-First Search [Accepted]
# Intuition
#
# Draw an edge between two emails if they occur in the same account.
# The problem comes down to finding connected components of this graph.
#
# Algorithm
#
# For each account, draw the edge from the first email to all other emails.
# Additionally, we'll remember a map from emails to names on the side.
# After finding each connected component using a depth-first search,
# we'll add that to our answer.
#
# Time Complexity: O(\sum ai loga i), where a_ia  i is the length of accounts[i].
# Without the log factor, this is the complexity to build the graph and search for each component.
# The log factor is for sorting each component at the end.
# Space Complexity: O(\sum a_i), the space used by our graph and our search.
#
# 92ms 34.59%
class Solution {
    public List<List<String>> accountsMerge(List<List<String>> accounts) {
        Map<String, String> emailToName = new HashMap();
        Map<String, ArrayList<String>> graph = new HashMap();
        for (List<String> account : accounts) {
            String name = "";
            for (String email : account) {
                if (name == "") {
                    name = email;
                    continue;
                }
                graph.computeIfAbsent(email, x -> new ArrayList<String>()).add(account.get(1));
                graph.computeIfAbsent(account.get(1), x -> new ArrayList<String>()).add(email);
                emailToName.put(email, name);
            }
        }

        Set<String> seen = new HashSet();
        List<List<String>> ans = new ArrayList();
        for (String email: graph.keySet()) {
            if (!seen.contains(email)) {
                seen.add(email);
                Stack<String> stack = new Stack();
                stack.push(email);
                List<String> component = new ArrayList();
                while (!stack.empty()) {
                    String node = stack.pop();
                    component.add(node);
                    for (String nei : graph.get(node)) {
                        if (!seen.contains(nei)) {
                            seen.add(nei);
                            stack.push(nei);
                        }
                    }
                }
                Collections.sort(component);
                component.add(0, emailToName.get(email));
                ans.add(component);
            }
        }
        return ans;
    }
}

# Approach #2: Union-Find [Accepted]
# https://leetcode.com/articles/redundant-connection/ for knowing more about union find
# Intuition
# As in Approach #1, our problem comes down to finding the connected components of a graph.
# This is a natural fit for a Disjoint Set Union (DSU) structure.
#
# Time Complexity: O(Alog A), where A = \sum a i and a_i is the length of accounts[i].
# is the Inverse-Ackermann function.
# If we used union-by-rank, this complexity improves to O(A \alpha(A)), where \alpha
# Space Complexity: O(A), the space used by our DSU structure.
#
# 32ms 99.04%
class Solution {

    //union find
    class Node {
        String name;
        ArrayList<String> accounts;
        Node parent;
        public Node(String name) {
            this.name = name;
            accounts = new ArrayList();
            parent = this;
        }
    }

    Node findParent(Node node) {
        while (node.parent != node) {
            // path compression
            node.parent = node.parent.parent;
            node = node.parent;
        }
        return node;
    }

    public List<List<String>> accountsMerge(List<List<String>> accounts) {
        HashMap<String, Node> map = new HashMap();
        List<Node> all = new ArrayList();
        //group
        for (int i = 0; i < accounts.size(); i++) {
            List<String> cur = accounts.get(i);
            Node node = new Node(cur.get(0));
            for (int j = 1; j < cur.size(); j++) {
                String email = cur.get(j);
                if (!map.containsKey(email)) {
                    map.put(email, node);
                    node.accounts.add(email);
                } else { //group them to the same parent
                    Node node_p = findParent(node);
                    Node exist_p = findParent(map.get(email));
                    node_p.parent = exist_p;
                }
            }
            all.add(node);
        }
        // add account to parent
        for (Node node : all) {
            if (node.parent != node) {
                Node p = findParent(node);
                p.accounts.addAll(node.accounts);
            }
        }

        //get ans email list
        List<List<String>> res = new ArrayList();
        for (Node node : all) {
            if (node.parent == node) {
                List<String> tmp = new ArrayList();
                tmp.add(node.name);
                Collections.sort(node.accounts);
                tmp.addAll(node.accounts);
                res.add(tmp);
            }
        }
        return res;
    }
}

# Union find by id
# 84ms 41.71%
class Solution {
    public List<List<String>> accountsMerge(List<List<String>> accounts) {
        DSU dsu = new DSU();
        Map<String, String> emailToName = new HashMap();
        Map<String, Integer> emailToID = new HashMap();
        int id = 0;
        for (List<String> account: accounts) {
            String name = "";
            for (String email: account) {
                if (name == "") {
                    name = email;
                    continue;
                }
                emailToName.put(email, name);
                if (!emailToID.containsKey(email)) {
                    emailToID.put(email, id++);
                }
                dsu.union(emailToID.get(account.get(1)), emailToID.get(email));
            }
        }

        Map<Integer, List<String>> ans = new HashMap();
        for (String email: emailToName.keySet()) {
            int index = dsu.find(emailToID.get(email));
            ans.computeIfAbsent(index, x-> new ArrayList()).add(email);
        }
        for (List<String> component: ans.values()) {
            Collections.sort(component);
            component.add(0, emailToName.get(component.get(0)));
        }
        return new ArrayList(ans.values());
    }
}
class DSU {
    int[] parent;
    public DSU() {
        parent = new int[10001];
        for (int i = 0; i <= 10000; ++i)
            parent[i] = i;
    }
    public int find(int x) {
        if (parent[x] != x) parent[x] = find(parent[x]);
        return parent[x];
    }
    public void union(int x, int y) {
        parent[find(x)] = find(y);
    }
}

# https://leetcode.com/problems/accounts-merge/discuss/109157/JavaC%2B%2B-Union-Find
# union find for Strings good example
# 100ms 24.88%
class Solution {
    public List<List<String>> accountsMerge(List<List<String>> accounts) {
        Map<String, String> roots = new HashMap();
        Map<String, String> owner = new HashMap();
        Map<String, TreeSet<String>> unions = new HashMap();
        
        for (List<String> acc : accounts) {
            for (int i = 1; i < acc.size(); i++) {
                roots.put(acc.get(i), acc.get(i));
                owner.put(acc.get(i), acc.get(0));
            }
        }
        
        //union all emails in the same account list
        for (List<String> acc : accounts) {
            String x = find(acc.get(1), roots);
            for (int i = 2; i < acc.size(); i++) {
                roots.put(find(acc.get(i), roots), x);
            }
        }
        
        //union emails accros diff accounts
        for (List<String> acc : accounts) {
            String x = find(acc.get(1), roots);
            unions.computeIfAbsent(x, k-> new TreeSet<String>());
            for (int i = 1; i < acc.size(); i++) {
                unions.get(x).add(acc.get(i));
            }
        }
        
        List<List<String>> res = new ArrayList();
        for (String e : unions.keySet()) {
            List<String> emails = new ArrayList(unions.get(e));
            emails.add(0, owner.get(e));
            res.add(emails);
        }
        return res;
    }
    
    private String find(String x, Map<String, String> roots) {
        return roots.get(x).equals(x) ? x : find(roots.get(x), roots);
    }
}
'''
