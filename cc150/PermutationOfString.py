__author__ = 'July'
# write a method to compute all permutation of a string
# write a methof to compute all combinatino of a string
import re
class Solution:
    # no ordering
    def getPermutation(self, str):
        result = self.getPermutationRecu(str)
        for i in xrange(len(result)):
           result[i] = result[i].translate(None, '.')
        return result


    def getPermutationRecu(self, str):
        result = []
        if str == None:
            return
        elif len(str) == 0:  #base case
            result.append(".")  # if use "", result is null
            return result
        first_char = str[0]
        remain_char = str[1:]
        words = self.getPermutationRecu(remain_char)
        for word in words:
            for j in xrange(len(word)):
                result.append(self.insertCharAt(word, j, first_char))
        return result

    def insertCharAt(self, word, index, char):
        #print word
        first_half = str(word[:index])
        last_half = str(word[index:])
        return first_half + char + last_half


    def getCombinateion(self, str):
        result = []
        space = 1 << len(str)
        for i in xrange(space):
            k = i
            index = 0
            substr = []
            while k:
                if k & 1 > 0:
                    substr.append(str[index])
                k >>= 1
                index += 1
            result.append(substr)
        return result



if __name__ == "__main__":
    print Solution().getPermutation("ab")
    print Solution().getCombinateion("ab")