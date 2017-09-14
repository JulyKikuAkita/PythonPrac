__source__ = 'https://leetcode.com/problems/evaluate-division/description/'
# https://github.com/kamyu104/LeetCode/blob/master/Python/evaluate-division.py
# Time:  O(e + q * |V|!), |V| is the number of variables
# Space: O(e)
#
# Description: Leetcode # 399. Evaluate Division
#
# Equations are given in the format A / B = k,
# where A and B are variables represented as strings,
# and k is a real number (floating point number).
# Given some queries, return the answers.
# If the answer does not exist, return -1.0.
#
# Example:
# Given a / b = 2.0, b / c = 3.0.
# queries are: a / c = ?, b / a = ?, a / e = ?, a / a = ?, x / x = ? .
# return [6.0, 0.5, -1.0, 1.0, -1.0 ].
#
# The input is:
# vector<pair<string, string>> euqations, vector<double>& values, vector<pair<string, string>> query .
#
# where equations.size() == values.size(),the values are positive.
# this represents the equations.return vector<double>. .
# The example above: equations = [ ["a", "b"], ["b", "c"] ].
# values = [2.0, 3.0]. queries = [ ["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"] ].
# return would be [6.00000,3.00000,-1.00000,1.00000,-1.00000]
# The input is always valid. You may assume that
# evaluating the queries will result in no division by zero and there is no contradiction.
#
# Companies
# Google
# Related Topics
# Graph
#
import unittest
import collections
import itertools
class Solution(object):
    def calcEquation(self, equations, values, query):
        """
        :type equations: List[List[str]]
        :type values: List[float]
        :type query: List[List[str]]
        :rtype: List[float]
        """
        def check(up, down, lookup, visited):
            if up in lookup and down in lookup[up]:
                return (True, lookup[up][down])
            for k, v in lookup[up].iteritems():
                if k not in visited:
                    visited.add(k)
                    tmp = check(k, down, lookup, visited)
                    if tmp[0]:
                        return (True, v * tmp[1])
            return (False, 0)

        lookup = collections.defaultdict(dict)
        for i, e in enumerate(equations):
            lookup[e[0]][e[1]] = values[i]
            if values[i]:
                lookup[e[1]][e[0]] = 1.0 / values[i]

        result = []
        for q in query:
            visited = set()
            tmp = check(q[0], q[1], lookup, visited)
            result.append(tmp[1] if tmp[0] else -1)
        return result

# A variation of Floyd-Warshall, computing quotients instead of shortest paths.
# An equation A/B=k is like a graph edge A->B, and (A/B)*(B/C)*(C/D)
# is like the path A->B->C->D. Submitted once, accepted in 35 ms.
def calcEquation(self, equations, values, queries):
    quot = collections.defaultdict(dict)
    for (num, den), val in zip(equations, values):
        quot[num][num] = quot[den][den] = 1.0
        quot[num][den] = val
        quot[den][num] = 1 / val
    for k, i, j in itertools.permutations(quot, 3):
        if k in quot[i] and j in quot[k]:
            quot[i][j] = quot[i][k] * quot[k][j]
    return [quot[num].get(den, -1.0) for num, den in queries]

class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)

if __name__ == '__main__':
    unittest.main()

Java = '''
#Thought:
graph
Image a/b = k as a link between node a and b, the weight from a to b is k,
the reverse link is 1/k. Query is to find a path between two nodes.

#62.73% 3ms
public class Solution {
    public double[] calcEquation(String[][] equations, double[] values, String[][] queries) {
        HashMap<String, ArrayList<String>> pairs = new HashMap<String, ArrayList<String>>();
        HashMap<String, ArrayList<Double>> valuesPair = new HashMap<String, ArrayList<Double>>();
        for (int i = 0; i < equations.length; i++) { //equations = [ ["a", "b"], ["b", "c"] ],
            String[] equation = equations[i];
            if (!pairs.containsKey(equation[0])) {
                pairs.put(equation[0], new ArrayList<String>());
                valuesPair.put(equation[0], new ArrayList<Double>());
            }

            if (!pairs.containsKey(equation[1])) {
                pairs.put(equation[1], new ArrayList<String>());
                valuesPair.put(equation[1], new ArrayList<Double>());
            }

            pairs.get(equation[0]).add(equation[1]);
            pairs.get(equation[1]).add(equation[0]);
            valuesPair.get(equation[0]).add(values[i]);
            valuesPair.get(equation[1]).add(1 / values[i]);
        }

        //queries = [ ["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"] ].
        double[] res = new double[queries.length];
        for (int i = 0; i < queries.length; i++) {
            String[] query = queries[i];
            res[i] = dfs(query[0], query[1], pairs, valuesPair, new HashSet<String>(), 1.0);
            if (res[i] == 0.0) res[i] = -1.0;
        }
        return res;
    }
    private double dfs(String start, String end, HashMap<String, ArrayList<String>> pairs, HashMap<String, ArrayList<Double>> values, HashSet<String> set, double value) {
        if (set.contains(start)) return 0.0;
        if (!pairs.containsKey(start)) return 0.0;
        if (start.equals(end)) return value;

        set.add(start);
        ArrayList<String> strList = pairs.get(start);
        ArrayList<Double> valueList = values.get(start);
        double tmp = 0.0;
        for (int i = 0; i < strList.size(); i++) {
            tmp = dfs(strList.get(i), end, pairs, values, set, value * valueList.get(i));
            if (tmp != 0.0) break;
        }

        set.remove(start);
        return tmp;
    }
}

#62.73% 3ms
class Solution {
    public double[] calcEquation(String[][] equations, double[] values, String[][] queries) {
        HashMap<String, HashMap<String, Double>> hm = initHashMap(equations, values);
        double[] res = new double[queries.length];

        for (int i = 0; i < queries.length; i++) {
            String f = queries[i][0];
            String s = queries[i][1];
            if (!hm.containsKey(f) || !hm.containsKey(s)) res[i] = -1.0d;
            else if (f.equals(s)) res[i] = 1.0d;
            else res[i] = calcHelper(hm, f, s, new HashSet<String> ());
        }

        return res;
    }

    public double calcHelper(HashMap<String, HashMap<String, Double>> hm, String f, String s, HashSet<String> visited) {

        if (hm.get(f).containsKey(s)) {
            return hm.get(f).get(s);
        } else {
            for (Map.Entry<String, Double> entry : hm.get(f).entrySet()) {
                if (visited.contains(entry.getKey())) continue;
                visited.add(entry.getKey());
                double res = calcHelper(hm, entry.getKey(), s, visited);
                if (res != -1.0d) {
                    return entry.getValue() * res;
                }
            }
            return -1.0d;
        }
    }

    public HashMap<String, HashMap<String, Double>> initHashMap(String[][] equations, double[] values) {
        HashMap<String, HashMap<String, Double>> hm = new HashMap<String, HashMap<String, Double>>();
        for (int i = 0; i < equations.length; i++) {
            String f = equations[i][0];
            String s = equations[i][1];
            putInHashMap(hm, f, s, values[i]);
            putInHashMap(hm, s, f, 1.0d / values[i]);
        }
        return hm;
    }

    public void putInHashMap(HashMap<String, HashMap<String, Double>> hm, String f, String s, double values) {
        if (hm.containsKey(f)) {
            hm.get(f).put(s, values);
        } else {
            HashMap<String, Double> newPairs = new HashMap<String, Double> ();
            newPairs.put(s, values);
            hm.put(f, newPairs);
        }
    }
}
'''