__author__ = 'July'
# return all sub set of a set

class Solution:
    #recursion
    def getSubSets(self, bigset, index):
        allsubset = []
        if len(bigset) == index:
            allsubset.append([])
        else:
            allsubset = self.getSubSets(bigset, index + 1)
            item = bigset[index]
            clonedset = []
            for subset in allsubset:
                tmp = []
                tmp += (subset)
                tmp += ([item])
                clonedset.append(tmp)
            allsubset += clonedset
        return allsubset


class Solution2:
    #combination
    def getSubSets(self, bigset):
        result = []
        total = 1 << len(bigset)
        for i in xrange(total):
            subset = []
            k = i
            index = 0
            while k > 0 :
                if (k & 1) > 0: # if k is odd number
                    print k, bigset[index], index
                    subset.append(bigset[index])
                k >>= 1
                index += 1
            result.append(subset)
        return result


if __name__ == "__main__":
    setA = [1,2, 3]
    print Solution().getSubSets(setA, 0)
    print Solution2().getSubSets(setA)




