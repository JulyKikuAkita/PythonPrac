__source__ = 'https://leetcode.com/problems/flatten-nested-list-iterator/'
# https://github.com/kamyu104/LeetCode/blob/master/Python/flatten-nested-list-iterator.py
# Time:  O(n), n is the number of the integers.
# Space: O(h), h is the depth of the nested lists.
#
# Description: Leetcode # 341. Flatten Nested List Iterator
#
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger(object):
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """
# Companies
# Google Facebook Twitter
# Related Topics
# Stack Design
# Similar Questions
# Flatten 2D Vector Zigzag Iterator Mini Parser Array Nesting
#
import unittest
class NestedIterator(object):

    def __init__(self, nestedList):
        """
        Initialize your data structure here.
        :type nestedList: List[NestedInteger]
        """
        self.__depth = [[nestedList, 0]]


    def next(self):
        """
        :rtype: int
        """
        nestedList, i = self.__depth[-1]
        self.__depth[-1][1] += 1
        return nestedList[i].getInteger()


    def hasNext(self):
        """
        :rtype: bool
        """
        while self.__depth:
            nestedList, i = self.__depth[-1]
            if i == len(nestedList):
                self.__depth.pop()
            elif nestedList[i].isInteger():
                    return True
            else:
                self.__depth[-1][1] += 1
                self.__depth.append([nestedList[i].getList(), 0])
        return False


# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())

class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)

if __name__ == '__main__':
    unittest.main()

Java = '''
# Thought:
/**
 * // This is the interface that allows for creating nested lists.
 * // You should not implement it, or speculate about its implementation
 * public interface NestedInteger {
 *
 *     // @return true if this NestedInteger holds a single integer, rather than a nested list.
 *     public boolean isInteger();
 *
 *     // @return the single integer that this NestedInteger holds, if it holds a single integer
 *     // Return null if this NestedInteger holds a nested list
 *     public Integer getInteger();
 *
 *     // @return the nested list that this NestedInteger holds, if it holds a nested list
 *     // Return null if this NestedInteger holds a single integer
 *     public List<NestedInteger> getList();
 * }
 */

# 3ms 94.48%
public class NestedIterator implements Iterator<Integer> {
    private Stack<Iterator<NestedInteger>> stack;
    Integer nextInteger;
    public NestedIterator(List<NestedInteger> nestedList) {
        stack = new Stack<>();
        if(nestedList != null){
            stack.push(nestedList.iterator());
        }
    }

    @Override
    public Integer next() {
        return nextInteger;
    }

    @Override
    public boolean hasNext() {
        while(!stack.isEmpty()){
            Iterator<NestedInteger> iter = stack.peek();
            if(!iter.hasNext()){
                stack.pop();
                continue;
            }
            NestedInteger nextVal = iter.next();
            if(nextVal.isInteger()){
                nextInteger = nextVal.getInteger();
                return true;
            }else{
                stack.push(nextVal.getList().iterator());
            }
        }
        return false;
    }
}

/**
 * Your NestedIterator object will be instantiated and called as such:
 * NestedIterator i = new NestedIterator(nestedList);
 * while (i.hasNext()) v[f()] = i.next();
 */

# 2ms 100%
class NestedIterator implements Iterator<Integer> {
    List<NestedInteger> nestedList;
    List<Integer> list = new ArrayList<Integer>();
    int index;
    private void help(List<NestedInteger> input){
       // List<Integer> res = new ArrayList<Integer>();
        for(NestedInteger item : input){
            if(item.isInteger()){
                list.add(item.getInteger());
            }else{
                help(item.getList());
            }
        }
     //   System.out.println(res.toString());
     //   return res;
    }

    public NestedIterator(List<NestedInteger> nestedList) {
        this.nestedList = nestedList;
        index = 0;
        help(nestedList);
    }

    @Override
    public Integer next() {
        return list.get(index++);
    }

    @Override
    public boolean hasNext() {
        if(index < list.size()){
            return true;
        }
        return false;
    }
}

'''