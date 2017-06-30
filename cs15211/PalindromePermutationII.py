# https://github.com/kamyu104/LeetCode/blob/master/Python/palindromePermutationii.py
# Time:  O(n * n!)
# Space: O(n)
#
# Given a string s, return all the palindromic permutations (without duplicates) of it.
# Return an empty list if no palindromic permutation could be form.
#
# For example:
#
# Given s = "aabb", return ["abba", "baab"].
#
# Given s = "abc", return [].
#
# Google Uber
# Hide Tags Backtracking
# Hide Similar Problems (M) Next Permutation (M) Permutations II (E) Palindrome Permutation
#

import collections
import itertools
class Solution(object):
    def generatePalindromes(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        cnt = collections.Counter(s)
        mid = ''.join(k for k, v in cnt.iteritems() if v % 2 )
        chars = ''.join(k * (v / 2) for k , v in cnt.iteritems())
        return self.permuteUnique(mid, chars) if len(mid) < 2 else []

    def permuteUnique(self, mid, nums):
        result = []
        used = [False] * len(nums)
        self.permuteUniqueRecu(mid, result, used, [], nums)
        return result

    def permuteUniqueRecu(self, mid, result, used, cur, nums):
        if len(cur) == len(nums):
            half_palindrome = ''.join(cur)
            result.append(half_palindrome + mid + half_palindrome[::-1])
            return
        for i in xrange(len(nums)):
            if not used[i] and not (i > 0 and nums[i - 1] == nums[i] and used[i - 1]):
                used[i] = True
                cur.append(nums[i])
                self.permuteUniqueRecu(mid, result, used, cur, nums)
                cur.pop()
                used[i] = False

class Solution2(object):
    def generatePalindromes(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        cnt = collections.Counter(s)
        mid = tuple(k for k, v  in cnt.iteritems() if v % 2)
        chars = ''.join(k * (v / 2) for k ,v in cnt.iteritems())

        return [''.join(half_palindrome + mid + half_palindrome[::-1]) \
                for half_palindrome in set(itertools.permutations(chars))] if len(mid) < 2 else []


class Solution(object):
    def __init__(self):
        self.res = []
    def generatePalindromes(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        if not s or len(s) == 0:
            return []
        elif len(s) == 1:
            return [s]

        dict = collections.defaultdict(int)
        can = ""
        single = ""
        for c in s:
            dict[c] += 1

        for key in dict:
            if dict[key] % 2 != 0:
                single += key
                if len(single) > 1:
                    return []

            num = dict[key] / 2
            for i in xrange(num):
                can += key

        if len(can) == 0 and len(single) == 1:
            return [single]


        for i in xrange(len(can)):
            if i > 0 and can[i] == can[i-1]:
                continue
            self.dfs(can[i], can[:i]+can[i+1:], len(can), single)
        return self.res

    def dfs(self, left, can, length, single):
        if len(left) == length:
            self.res.append(left + single+ left[::-1])
            return
        for i in xrange(len(can)):
            if i > 0 and can[i] == can[i-1]:
                continue
            self.dfs(left + can[i], can[:i]+can[i+1:], length, single)
        return self.res


#JAVA solution
java = '''
Basically, the idea is to perform permutation on half of the palindromic string and then form the full palindromic result.

public class Solution {
    public List<String> generatePalindromes(String s) {
        int odd = 0;
        String mid = "";
        List<String> res = new ArrayList<>();
        List<Character> list = new ArrayList<>();
        Map<Character, Integer> map = new HashMap<>();

        // step 1. build character count map and count odds
        for (int i = 0; i < s.length(); i++) {
            char c = s.charAt(i);
            map.put(c, map.getOrDefault(c, 0) + 1);
            odd += map.get(c) % 2 != 0 ? 1 : -1;
        }

        // cannot form any palindromic string
        if (odd > 1) return res;

        // step 2. add half count of each character to list
        for (Map.Entry<Character, Integer> entry : map.entrySet()) {
            char key = entry.getKey();
            int val = entry.getValue();

            if (val % 2 != 0) mid += key;
            for (int i = 0; i < val / 2; i++) {
                list.add(key);
            }
        }

        // step 3. generate all the permutations
        getPerm(res, new StringBuilder(), list, mid, new boolean[list.size()]);

        return res;
    }

    // generate all unique permutation from list
    public void getPerm(List<String> res, StringBuilder sb, List<Character> list, String mid, boolean[] used) {
        if (sb.length() == list.size()) {
            // form the palindromic string
            res.add(sb.toString() + mid + sb.reverse().toString());
            sb.reverse();
            return;
        }

        HashSet<Character> set = new HashSet<>();
        for (int i = 0; i < list.size(); i++) {
            // avoid duplication
            if (!set.contains(list.get(i)) && !used[i]) {
                sb.append(list.get(i));
                set.add(list.get(i));
                used[i] = true;
                getPerm(res, sb, list, mid, used);
                used[i] = false;
                sb.setLength(sb.length() - 1);
            }
        }
    }
}

91.7%
public class Solution {
    public List<String> generatePalindromes(String s) {
        List<String> result = new ArrayList<>();
        if (s.length() == 0) {
            return result;
        }
        int[] count = countChars(s);
        Character mid = null;
        for (int i = 0; i < 128; i++) {
            if ((count[i] & 1) == 1) {
                if (mid == null) {
                    mid = (char) i;
                    count[i]--;
                } else {
                    return result;
                }
            }
        }
        return generateFull(count, mid);
    }

    private List<String> generateFull(int[] count, Character mid) {
        List<String> result = new ArrayList<>();
        List<String> halves = generateHalves(count, 0);
        for (String half : halves) {
            StringBuilder sb = new StringBuilder();
            sb.append(half).reverse();
            if (mid != null) {
                sb.append(mid);
            }
            sb.append(half);
            result.add(sb.toString());
        }
        return result;
    }

    private List<String> generateHalves(int[] count, int countIndex) {
        List<String> result = new ArrayList<>();
        while (countIndex < count.length && count[countIndex] == 0) {
            countIndex++;
        }
        if (countIndex == count.length) {
            result.add("");
            return result;
        }
        count[countIndex] -= 2;
        for (String next : generateHalves(count, countIndex)) {
            for (int i = 0; i <= next.length(); i++) {
                result.add(new StringBuilder().append(next.substring(0, i)).append((char) countIndex).append(next.substring(i)).toString());
                if (i < next.length() && next.charAt(i) == countIndex) {
                    break;
                }
            }
        }
        return result;
    }

    private int[] countChars(String s) {
        int[] result = new int[128];
        for (int i = 0; i < s.length(); i++) {
            result[s.charAt(i)]++;
        }
        return result;
    }
}
'''