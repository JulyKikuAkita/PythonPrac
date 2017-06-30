__author__ = 'July'

q = '''
第一题跟leetcode的merge interval很像，要求返回总区间去重后的累积长度 leetcode 56,57

第二题跟word break很像。要求写一个split函数如下
List<String> split(String s, List<String>)
根据第二个参数去分割字符串.
eg 输入"abcdefg", ["c", "ef"]
返回 [''ab", "d", "g"]

然后问的是偏System design，high level描述一个系统，有前端网页dashboard，
每次用户登陆的时候都要选一个系统里的问题叫everyday question来回答，问题不可以重复。
假设全世界只有一台电脑处理每个工作日上午八点7，000，000个用户的每日一问。问怎么设计后台数据库，
怎么写post handling，应该怎样选择每个用户的每日一问。怎么handle traffic

LZ貌似都答上来了。至于问题选择，我说如果要求随机就用hash function计算每个用户下一个问题id，
如果不随机那就直接index ＋ 1，然后问了他问题问完了咋办，他说假设一年之内用不完问题库的问题。
被用户数量吓了下，不过后面一想，好想不难啊，这台电脑就每天早上八点会遇到很多用户登陆，
那剩余的23个小时内让电脑去把明天用户的每日一问就算好不就对了。

'''
q2 = '''
Interview Questions
Print a NxN matrix in clockwise spiral. leeetcode 54, 59
Function to check if a number is prime. Function to find the prime factors of a number. leetcode 204

For a given binary tree, assign the sibling pointer of each node.
A sibling is always the node to its immediate right on the same level of the tree. leetcode 116, 117

leetcode 413 https://leetcode.com/problems/arithmetic-slices/#/description
public class Solution {
    public int numberOfArithmeticSlices(int[] A) {
    int curr = 0, sum = 0;
    for (int i=2; i<A.length; i++)
        if (A[i]-A[i-1] == A[i-1]-A[i-2]) {
            curr += 1;
            sum += curr;
        } else {
            curr = 0;
        }
    return sum;
    }
}

find the longest zigzag length starts at the root of a binary tree.
The longest zig-zag path is the longest LRLRLR... or RLRLRL... in a tree where 'L' and 'R' stands for left and right children.
Also, note that the longest zig-zag path doesn't necessarily starts from the root
http://puddleofriddles.blogspot.com/2012/01/find-maximum-zig-zag-path-in-binary.html
public class Solution {
    public int maxZigZag(TreeNode root) {
        int lcount = 0, rcount = 0, max = 0;
        if (root == null) return 0;
        while (true) {
            if (root.left != null) {
                root = root.left;
                lcount++;
            }else {
                break;
            }
            if (root.right != null) {
                root = root.right;
                lcount++;
            }else {
                break;
            }
        }

        while (true) {
            if (root.right != null) {
                root = root.right;
                rcount++;
            }else {
                break;
            }
            if (root.left != null) {
                root = root.left;
                rcount++;
            }else {
                break;
            }
        }

        max = Math.max(lcount, rcount);
        max = Math.max(max, maxZigZag(root.left));
        max = Math.max(max, maxZigZag(root.right));
        return max;
}   }


Twitch onsite 06/23/2017:
- leetcode 200 number of islands - return island with max area
- leetcode 206 reverse linked list
- leetcode 230 Kth Smallest Element in a BST
- 25 horses, 5 rack, how many time to get top 3
- design temperate tracker, with O(1) to get min, max, avg,
provide insert func, get freq, what if need to provide celsius and fahrenheit
- design public String getBOX(String input), return a string of a box assigned
ex:
getBOX("BOX1") -> return h01e_box1 (any random string)
getDBBOX("DBBOX2") -> return adsk_box2
decommion("BOX1") -> return true; // cleanup space for BOX1
getBOX("BOX1") -> return h01q_box1 (assign the available BOX1 space)



'''
class Twitch:
    def split(self, s, deli):
        # s: string
        # deli: a list of string as deliminator

        res = []
        cur = ""
        for d in deli:
            cur += s.split(d)[0]
            cur += " "
            s = s.split(d)[1]
            print cur, s
        if s:
            cur += s
        res.append("".join(cur))
        return res

if __name__ == "__main__":
    s = "abcdefg"
    deli = ["c", "ef"]
    cur = Twitch()
    print cur.split(s, deli)

    #playGround().printS()
    #print chr(ord('1')+ 1)