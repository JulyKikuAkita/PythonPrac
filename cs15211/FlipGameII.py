__source__ = 'https://leetcode.com/problems/flip-game-ii/'
# https://github.com/kamyu104/LeetCode/blob/master/Python/flip-game-ii.py
# Time:  O(n + c^2)
# Space: O(c)
#
# Description: Leetcode # 294. Flip Game II
#
# You are playing the following Flip Game with your friend: Given a string
# that contains only these two characters: + and -,
# you and your friend take turns to flip two consecutive "++" into "--".
# The game ends when a person can no longer make a move and therefore the other person will be the winner.
#
# Write a function to determine if the starting player can guarantee a win.
#
# For example, given s = "++++", return true.
# The starting player can guarantee a win by flipping the middle "++" to become "+--+".
#
# Follow up:
# Derive your algorithm's runtime complexity.
# Companies
# Google
# Related Topics
# Backtracking
# Similar Questions
# Nim Game Flip Game Guess Number Higher or Lower II Can I Win
#
#
# The best theory solution (DP, O(n + c^2)) could be seen here:
# https://leetcode.com/discuss/64344/theory-matters-from-backtracking-128ms-to-dp-0m

# The imap() function returns an iterator that calls a function on the values in the input iterators, and returns the results.
# It works like the built-in map(), except that it stops when any input iterator is exhausted
# (instead of inserting None values to completely consume all of the inputs).

# izip() returns an iterator that combines the elements of several iterators into tuples.
# It works like the built-in function zip(), except that it returns an iterator instead of a list.

import itertools
import re
import unittest
class Solution(object):
    def canWin(self, s):
        g, g_final = [0], 0
        for p in itertools.imap(len, re.split('-+', s)):
            while len(g) <= p:
                # Theorem 2: g[game] = g[subgame1]^g[subgame2]^g[subgame3]...;
                # and find first missing number.
                g += min(set(xrange(p)) - {x^y for x, y in itertools.izip(g[:len(g)/2], g[-2:-len(g)/2-2:-1])}),
            g_final ^= g[p]
        return g_final > 0  # Theorem 1: First player must win iff g(current_state) != 0


# Time:  O(n + c^3 * 2^c * logc), n is length of string, c is count of "++"
# Space: O(c * 2^c)
# hash solution.
# We have total O(2^c) game strings,
# and each hash key in hash table would cost O(c),
# each one has O(c) choices to the next one,
# and each one would cost O(clogc) to sort,
# so we get O((c * 2^c) * (c * clogc)) = O(c^3 * 2^c * logc) time.
# To cache the results of all combinations, thus O(c * 2^c) space.
class Solution2(object):
    def canWin(self, s):
        """
        :type s: str
        :rtype: bool
        """
        lookup = {}

        def canWinHelper(consecutives):                                         # O(2^c) time
            consecutives = tuple(sorted(c for c in consecutives if c >= 2))     # O(clogc) time
            if consecutives not in lookup:
                lookup[consecutives] = any(not canWinHelper(consecutives[:i] + (j, c-2-j) + consecutives[i+1:])  # O(c) time
                                           for i, c in enumerate(consecutives)  # O(c) time
                                           for j in xrange(c - 1))              # O(c) time
            return lookup[consecutives]                                         # O(c) time

        # re.findall: O(n) time, canWinHelper: O(c) in depth
        return canWinHelper(map(len, re.findall(r'\+\++', s)))

# Time:  O(c * n * c!), n is length of string, c is count of "++"
# Space: O(c * n), recursion would be called at most c in depth.
#                  Besides, it costs n space for modifying string at each depth.
class Solution3(object):
    def canWin(self, s):
        """
        :type s: str
        :rtype: bool
        """
        i, n = 0, len(s) - 1
        is_win = False
        while not is_win and i < n:                                     # O(n) time
            if s[i] == '+':
                while not is_win and i < n and s[i+1] == '+':           # O(c) time
                     # t(n, c) = c * (t(n, c-1) + n) + n = ...
                     # = c! * t(n, 0) + n * c! * (c + 1) * (1/0! + 1/1! + ... 1/c!)
                     # = n * c! + n * c! * (c + 1) * O(e) = O(c * n * c!)
                    is_win = not self.canWin(s[:i] + '--' + s[i+2:])    # O(n) space
                    i += 1
            i += 1
        return is_win

class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)

if __name__ == '__main__':
    unittest.main()

Java = '''
# Thought:
# backtracking solution O(n!!)
For the time complexity, let's say the length of the input string s is n,
there are at most n - 1 ways to replace "++" to "--" (imagine s is all "+++..."),
once we replace one "++", there are at most (n - 2) - 1 ways to do the replacement,
it's a little bit like solving the N-Queens problem, the time complexity is (n - 1) x (n - 3) x (n - 5) x ...,
so it's O(n!!), double factorial.

# 21ms 55.15%
class Solution {
    public boolean canWin(String s) {
        if(s == null || s.length() == 0 ) return false;
        char[] arr = s.toCharArray();
        return dfs(arr);
    }

    private boolean dfs(char[] arr){
        for(int i = 1 ; i < arr.length; i++){
            if(arr[i-1] == '+' && arr[i] == '+'){
                arr[i-1] = '-';
                arr[i] = '-';

                boolean win = !dfs(arr);

                arr[i-1] = '+';
                arr[i] = '+';

                if(win) return true;
            }
        }
        return false;
    }
}

# backtracking + memorization 68%
# 9ms 87.87%
class Solution {
    public boolean canWin(String s) {
        return canWin(s, new HashMap<>());
    }

    public boolean canWin(String s, Map<String, Boolean> cache) {
        if (cache.containsKey(s)) {
            return cache.get(s);
        }
        int index = -1;
        while ((index = s.indexOf("++", index + 1)) >= 0) {
            String next = new StringBuilder().append(s.substring(0, index)).append("--").append(s.substring(index + 2)).toString();
            if (!canWin(next, cache)) {
                cache.put(s, true);
                return true;
            }
        }
        cache.put(s, false);
        return false;
    }
}

# 10ms 86.21%
class Solution {
    HashMap<String, Boolean> map = new HashMap<>();

    public boolean canWin(String s) {
        if(map.containsKey(s))  return map.get(s);

        for (int start = 0; start < s.length();) {
            int index = s.indexOf("++", start);
            if (index < 0) break;
            String newS = s.substring(0, index) + "--" + s.substring(index + 2);
            if (!canWin(newS)) {
                map.put(s, true);
                return true;
            }
            start = index + 1;
        }
        map.put(s, false);
        return false;
    }
}

# 1ms 99.50%
class Solution {
    public boolean canWin(String s) {
        HashSet<Integer> set = new HashSet<Integer>();
        String[] segment = s.split("-");
        for(String str : segment) {
            int cur = str.length();
            if(cur != 0 && cur % 4 != 1) {
                if(cur % 2 == 1) {
                    cur--;
                }
                if(set.contains(cur)) {
                    set.remove(cur);
                } else {
                    set.add(cur);
                }
            }
        }
        if(set.size() == 0) {
            return false;
        }
        return true;
    }
}

# 0ms 100%
class Solution {
    public boolean canWin(String s) {
        // two pointers p1 p2 to count consecutive '+'
        // flips is total flips available
        // change is total opportunities to alter remaining flips between odd and even
        int flips = 0, change = 0;
        for (int p1 = 0, p2 = 0, n = s.length(); p2 < s.length(); p1 = p2) {
            p1 = s.indexOf('+', p1);
            if (p1 == -1) break;
            p2 = s.indexOf('-', p1);
            if (p2 == -1) p2 = n;
            if (p2 - p1 == 2)
                ++flips;
            else if (p2 - p1 == 4 || p2 - p1 == 6)
                ++change;
            flips += (p2 - p1 - 1) / 2;
        }
        return change % 2 != 0 || flips % 2 != 0;
    }
}
'''