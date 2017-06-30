__author__ = 'July'
# https://github.com/kamyu104/LeetCode/blob/master/Python/lexicographical-numbers.py
# Time:  O(n)
# Space: O(1)

# Given an integer n, return 1 - n in lexicographical order.
#
# For example, given 13, return: [1,10,11,12,13,2,3,4,5,6,7,8,9].
#
# Please optimize your algorithm to use less time and space.
# The input size may be as large as 5,000,000.
# Bloomberg

class Solution(object):
    def lexicalOrder(self, n):
        result = []

        i = 1
        while len(result) < n:
            k = 0
            while i * 10**k <= n:
                result.append(i * 10**k)
                k += 1

            num = result[-1] + 1
            while num <= n and num % 10:
                result.append(num)
                num += 1

            if not num % 10:
                num -= 1
            else:
                num /= 10

            while num % 10 == 9:
                num /= 10

            i = num+1

        return result

java = '''
The basic idea is to find the next number to add.
Take 45 for example: if the current number is 45, the next one will be 450 (450 == 45 * 10)(if 450 <= n),
or 46 (46 == 45 + 1) (if 46 <= n) or 5 (5 == 45 / 10 + 1)(5 is less than 45 so it is for sure less than n).
We should also consider n = 600, and the current number = 499, the next number is 5 because there are all "9"s
after "4" in "499" so we should divide 499 by 10 until the last digit is not "9".
It is like a tree, and we are easy to get a sibling, a left most child and the parent of any node.

public List<Integer> lexicalOrder(int n) {
        List<Integer> list = new ArrayList<>(n);
        int curr = 1;
        for (int i = 1; i <= n; i++) {
            list.add(curr);
            if (curr * 10 <= n) {
                curr *= 10;
            } else if (curr % 10 != 9 && curr + 1 <= n) {
                curr++;
            } else {
                while ((curr / 10) % 10 == 9) {
                    curr /= 10;
                }
                curr = curr / 10 + 1;
            }
        }
        return list;
    }

Simple Java DFS Solution
The idea is pretty simple. If we look at the order we can find out we just keep adding digit from 0 to 9 to every digit and make it a tree.
Then we visit every node in pre-order.
       1        2        3    ...
      /\        /\       /\
   10 ...19  20...29  30...39   ....

public class Solution {
    public List<Integer> lexicalOrder(int n) {
        List<Integer> res = new ArrayList<>();
        for (int i = 1; i < 10; i++) {
            dfs(i, n, res);
        }
        return res;
    }

    public void dfs( int cur, int n, List<Integer> res) {
        if ( cur > n) return;
        res.add(cur);
        for (int i = 0; i < 10; i++) {
            if (cur * 10 + i > n) return;
            dfs(cur * 10 + i, n ,res);
        }
    }
}
'''