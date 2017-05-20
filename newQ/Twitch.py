__author__ = 'July'

'''
第一题跟leetcode的merge interval很像，要求返回总区间去重后的累积长度
! j. t' Z& \2 s3 {. }5 I5 E3 n
第二题跟word break很像。要求写一个split函数如下$ o8 i& O$ H1 e, y  y
List<String> split(String s, List<String> deli);0 y3 b$ P7 N; p: Z
根据第二个参数去分割字符串. h1 j8 s$ N8 r0 [
eg 输入"abcdefg", ["c", "ef"]
返回 [''ab", "d", "g"]& B6

Interview Questions
Print a NxN matrix in clockwise spiral.
Answer Question
Function to check if a number is prime. Function to find the prime factors of a number.
Answer Question

For a given binary tree, assign the sibling pointer of each node. A sibling is always the node to its immediate right on the same level of the tree.
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