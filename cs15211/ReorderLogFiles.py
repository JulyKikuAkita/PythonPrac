__source__ = 'https://leetcode.com/problems/reorder-log-files/'
# Time:  O(AlogA)
# Space: O(A)
#
# Description: Leetcode # 937. Reorder Log Files
#
# You have an array of logs.  Each log is a space delimited string of words.
#
# For each log, the first word in each log is an alphanumeric identifier.  Then, either:
#
#     Each word after the identifier will consist only of lowercase letters, or;
#     Each word after the identifier will consist only of digits.
#
# We will call these two varieties of logs letter-logs and digit-logs.
# It is guaranteed that each log has at least one word after its identifier.
#
# Reorder the logs so that all of the letter-logs come before any digit-log.
# The letter-logs are ordered lexicographically ignoring identifier,
# with the identifier used in case of ties.
# The digit-logs should be put in their original order.
#
# Return the final order of the logs.
#
# Example 1:
#
# Input: ["a1 9 2 3 1","g1 act car","zo4 4 7","ab1 off key dog","a8 act zoo"]
# Output: ["g1 act car","a8 act zoo","ab1 off key dog","a1 9 2 3 1","zo4 4 7"]
#
# Note:
#
#     0 <= logs.length <= 100
#     3 <= logs[i].length <= 100
#     logs[i] is guaranteed to have an identifier, and a word after the identifier.
#
import unittest

# 28ms 100%
class Solution(object):
    def reorderLogFiles(self, logs):
        """
        :type logs: List[str]
        :rtype: List[str]
        """
        def f(log):
            id_, rest = log.split(" ", 1)
            return (0, rest, id_) if rest[0].isalpha() else (1,)
        return sorted(logs, key = f)

class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)

if __name__ == '__main__':
    unittest.main()

Java = '''
# Thought: https://leetcode.com/problems/reorder-log-files/solution/
#
Approach 1: Custom Sort
Complexity Analysis
Time Complexity: O(AlogA), where A is the total content of logs.
Space Complexity: O(A).

# 55ms 23.15%
class Solution {
    public String[] reorderLogFiles(String[] logs) {
        Arrays.sort(logs, (log1, log2) -> {
            String[] split1 = log1.split(" ", 2);
            String[] split2 = log2.split(" ", 2);
            boolean isDigit1 = Character.isDigit(split1[1].charAt(0));
            boolean isDigit2 = Character.isDigit(split2[1].charAt(0));
            if (!isDigit1 && !isDigit2) {
                 // int cmp = split1[1].compareTo(split2[1]); //also pass
                // if (cmp != 0) return cmp;
                return split1[0].compareTo(split2[0]);
            }
            return isDigit1 ? (isDigit2 ? 0 : 1) : -1;
        });
        return logs;
    }
}

# 5ms 99.54%
class Solution {
    public String[] reorderLogFiles(String[] logs) {
        String[] result = new String[logs.length];
        if (logs.length == 0)
            return result;
     
        int left = 0, right = logs.length - 1;
        for (int i = logs.length - 1; i >= 0; i --) {
            String s = logs[i];
            int index = s.indexOf(" ");
            char ch = s.charAt(index + 1);
            if (ch <= '9' && ch >= 0) {
                result[right] = s;
                right--;
            } else {
                result[left] = s;
                left++;
            }
        }        
        Comparator<String> newComparator = new Comparator<String>() {
            @Override
            public int compare(String a, String b) {
                return a.substring(a.indexOf(" ") + 1).compareTo(b.substring(b.indexOf(" ") + 1));
            }
        };
        Arrays.sort(result, 0, right + 1, newComparator);
        
        return result;
    }
}
'''
