__source__ = 'https://leetcode.com/problems/subdomain-visit-count/'
# Time:  O(N)
# Space: O(N)
#
# Description: Leetcode # 811. Subdomain Visit Count
#
# A website domain like "discuss.leetcode.com" consists of various subdomains.
# At the top level, we have "com", at the next level, we have "leetcode.com",
# and at the lowest level, "discuss.leetcode.com".
# When we visit a domain like "discuss.leetcode.com",
# we will also visit the parent domains "leetcode.com" and "com" implicitly.
#
# Now, call a "count-paired domain" to be a count (representing the number of visits this domain received),
# followed by a space, followed by the address.
# An example of a count-paired domain might be "9001 discuss.leetcode.com".
#
# We are given a list cpdomains of count-paired domains. We would like a list of count-paired domains,
# (in the same format as the input, and in any order),
# that explicitly counts the number of visits to each subdomain.
#
# Example 1:
# Input:
# ["9001 discuss.leetcode.com"]
# Output:
# ["9001 discuss.leetcode.com", "9001 leetcode.com", "9001 com"]
# Explanation:
# We only have one website domain: "discuss.leetcode.com". As discussed above,
# the subdomain "leetcode.com" and "com" will also be visited.
# So they will all be visited 9001 times.
#
# Example 2:
# Input:
# ["900 google.mail.com", "50 yahoo.com", "1 intel.mail.com", "5 wiki.org"]
# Output:
# ["901 mail.com","50 yahoo.com","900 google.mail.com","5 wiki.org","5 org","1 intel.mail.com","951 com"]
# Explanation:
# We will visit "google.mail.com" 900 times, "yahoo.com" 50 times,
# "intel.mail.com" once and "wiki.org" 5 times. For the subdomains,
# we will visit "mail.com" 900 + 1 = 901 times, "com" 900 + 50 + 1 = 951 times, and "org" 5 times.
#
# Notes:
#
# The length of cpdomains will not exceed 100.
# The length of each domain name will not exceed 100.
# Each address will have either 1 or 2 "." characters.
# The input count in any count-paired domain will not exceed 10000.
# The answer output can be returned in any order.
#
import unittest

#52ms 96.20%
class Solution(object):
    def subdomainVisits(self, cpdomains):
        """
        :type cpdomains: List[str]
        :rtype: List[str]
        """
        dic = {}
        for s in cpdomains:
            pair = s.split()
            count, domain = int(pair[0]), pair[1]
            dic[domain] = dic.get(domain, 0) + count
            subs = domain.split('.')
            i, size = 1, len(subs)
            while i < size:
                subdomain = '.'.join(subs[i:])
                dic[subdomain] = dic.get(subdomain, 0) + count
                i += 1
        res = []
        for (d, c) in dic.iteritems():
            res.append(' '.join((str(c), d)))
        return res

class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)

if __name__ == '__main__':
    unittest.main()

Java = '''
#Thought:

# with substring: 31ms 39.01%
class Solution {
    public List<String> subdomainVisits(String[] cpdomains) {
        Map<String, Integer> counts = new HashMap();
        for (String domain : cpdomains ) {
            String[] cpinfo = domain.split("\\s+");
            String[] frags = cpinfo[1].split("\\.");
            int count = Integer.valueOf(cpinfo[0]);
            String cur = "";
            for (int i = frags.length - 1; i >= 0; i--) {
                cur = frags[i] + (i < frags.length - 1 ? "." : "") + cur;
                counts.put(cur, counts.getOrDefault(cur, 0) + count);
            }
        }
        List<String> ans = new ArrayList();
        for (String dom : counts.keySet()) {
            ans.add("" + counts.get(dom) + " " + dom);
        }
        return ans;
    }
}

#11ms 99.72%
class Solution {
    public List<String> subdomainVisits(String[] cpdomains) {
        Map<String, Integer> map = new HashMap<>();

        for (int i = 0; i < cpdomains.length; i++) {
            int index = cpdomains[i].indexOf(' ');
            int count = Integer.parseInt(cpdomains[i].substring(0, index));
            String s = cpdomains[i].substring(index + 1);

            while (s.indexOf('.') >= 0) {
                map.put(s, map.getOrDefault(s, 0)  + count);
                s = s.substring(s.indexOf('.') + 1);
            }
            map.put(s, map.getOrDefault(s, 0)  + count); //last part of domain name
        }

        List<String> ans = new ArrayList<>();
        for (String key : map.keySet()) {
            ans.add(map.get(key) + " " + key);
        }
        return ans;
    }
}
'''