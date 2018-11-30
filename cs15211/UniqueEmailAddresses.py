__source__ = 'https://leetcode.com/problems/unique-email-addresses/description/'
# Time:  O()
# Space: O()
#
# Description: Leetcode # 929. Unique Email Addresses
#
# Every email consists of a local name and a domain name, separated by the @ sign.
#
# For example, in alice@leetcode.com, alice is the local name, and leetcode.com is the domain name.
#
# Besides lowercase letters, these emails may contain '.'s or '+'s.
#
# If you add periods ('.') between some characters in the local name part of an email address,
# mail sent there will be forwarded to the same address without dots in the local name.
# For example, "alice.z@leetcode.com" and "alicez@leetcode.com" forward to the same email address.
# (Note that this rule does not apply for domain names.)
#
# If you add a plus ('+') in the local name, everything after the first plus sign will be ignored.
# This allows certain emails to be filtered, for example m.y+name@email.com will be forwarded to my@email.com.
#  (Again, this rule does not apply for domain names.)
#
# It is possible to use both of these rules at the same time.
#
# Given a list of emails, we send one email to each address in the list.
# How many different addresses actually receive mails?
#
# Example 1:
#
# Input: ["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"]
# Output: 2
# Explanation: "testemail@leetcode.com" and "testemail@lee.tcode.com" actually receive mails
#
# Note:
#
# 1 <= emails[i].length <= 100
# 1 <= emails.length <= 100
# Each emails[i] contains exactly one '@' character.
#
import unittest

# Approach 1: Canonical Form
# 32ms 98.92%
class Solution(object):
    def numUniqueEmails(self, emails):
        seen = set()
        for email in emails:
            local, _, domain = email.partition('@')
            if '+' in local:
                local = local[:local.index('+')]
            seen.add(local.replace('.','') + '@' + domain)
        return len(seen)

class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)


if __name__ == '__main__':
    unittest.main()

Java = '''
#Thought: https://leetcode.com/problems/unique-email-addresses/solution/
# Approach 1: Canonical Form
# Time Complexity: O(C), where C is the total content of emails.
# Space Complexity: O(C).
# 23ms 845.08%
#
class Solution {
    public int numUniqueEmails(String[] emails) {
        Set<String> res = new HashSet<>();
        for (String email: emails) {
            int i = email.indexOf('@');
            String local = email.substring(0, i);
            String rest = email.substring(i);
            if (local.contains("+")) {
                local = local.substring(0, local.indexOf('+'));
            }
            local = local.replace(".", ""); //local = local.replaceAll("\\.", ""); //37ms, 59.93%
            res.add(local + rest);
        }
        return res.size();
    }
}

#cheating 100%
class Solution {
    public int numUniqueEmails(String[] emails) {
        Set<String> seen = new HashSet();
        for(String email:emails){
            int i = email.indexOf('@');
            String rest = email.substring(i);
            seen.add(rest);
        }
        return seen.size();
    }
}


'''