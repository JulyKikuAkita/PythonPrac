__source__ = 'https://leetcode.com/problems/text-justification/#/description'
# https://github.com/kamyu104/LeetCode/blob/master/Python/text-justification.py
# Time:  O(n)
# Space: O(1)
# String
#
# Given an array of words and a length L, format the text such that each line has exactly L characters
# and is fully (left and right) justified.
#
# You should pack your words in a greedy approach; that is, pack as many words as you can in each line.
# Pad extra spaces ' '
# when necessary so that each line has exactly L characters.
#
# Extra spaces between words should be distributed as evenly as possible.
# If the number of spaces on a line do not divide evenly between words, the empty slots on the left
# will be assigned more spaces than the slots on the right.
#
# For the last line of text, it should be left justified and no extra space is inserted between words.
#
# For example,
# words: ["This", "is", "an", "example", "of", "text", "justification."]
# L: 16.
#
# Return the formatted lines as:
# [
#    "This    is    an",
#    "example  of text",
#    "justification.  "
# ]
# Note: Each word is guaranteed not to exceed L in length.
# Companies
# LinkedIn Airbnb Facebook
# Related Topics
# String
#

class Solution:
    # @param words, a list of strings
    # @param L, an integer
    # @return a list of strings
    def fullJustify(self, words, L):
        result = []
        i = 0
        while i < len(words):
            size, begin = 0, i
            print "i = ", i, size, begin
            while i < len(words):
                if size == 0:
                    newsize = len(words[i])
                else:
                    #set default gap = 1
                    newsize = size + len(words[i]) + 1

                if newsize <= L:
                    size = newsize
                else:
                    break
                i += 1


            spaceCount = L - size
            # i - begin - 1 = # of gaps in one line
            if i - begin - 1 > 0 and i < len(words): #  i < len(words): meaning don't padding everycount at last line
                everyCount = spaceCount / ( i - begin - 1) + 1 #everyCount at least 1
                spaceCount %= i - begin - 1
            else:
                everyCount = 1
            print size, newsize, i, begin,  "every_count:", everyCount , "spaceCount:", spaceCount


            j = begin
            while j < i:
                if j == begin:
                    s = words[j]
                else:
                    s += ' ' * everyCount
                    if spaceCount > 0 and i < len(words): #  i < len(words): meaning don't padding everycount at last line
                        s += ' '
                        spaceCount -= 1
                    s += words[j]
                j += 1
            s += ' ' * spaceCount
            print s
            result.append(s)
        return result

if __name__ == "__main__":
    #print Solution().fullJustify(["This", "is", "an", "example", "of", "text", "justification."], 16)
    #print Solution().fullJustify(["What","must","be","shall","be."], 12)
    print Solution().fullJustify(["What","must","be","shall","be."], 12)
    #print Solution().fullJustify(['012','34','56','7890'] , 6)



# http://www.cnblogs.com/zuoyuan/p/3782107.html
class SolutionOther:
    # @param words, a list of strings
    # @param L, an integer
    # @return a list of strings
    def fullJustify(self, words, L):
        res = []
        i = 0
        while i < len(words):
            size = 0
            begin = i
            while i < len(words):
                newsize = len(words[i]) if size == 0 else size + len(words[i])+1
                if newsize <= L : size = newsize
                else: break
                i += 1
            spaceCount = L - size
            if i - begin - 1 > 0 and i < len(words):
                everyCount = spaceCount/(i-begin-1)
                spaceCount %= i-begin-1
            else:
                everyCount = 0

            j = begin
            while j < i:
                if j == begin:
                    s = words[j]
                else:
                    s += ' '*(everyCount+1)
                    if spaceCount > 0 and i < len(words):
                        s += ' '
                        spaceCount -= 1
                    s += words[j]
                j += 1

            s += ' '*spaceCount
            res.append(s)
        return res

#test
test = SolutionOther()
words = ["This", "is", "an", "example", "of", "text", "justification."]
#print test.fullJustify(words, 16)

#java
Java = '''
public class Solution {
    public List<String> fullJustify(String[] words, int maxWidth) {
        List<String> res = new ArrayList<>();
        int start = 0, end = 0, wc = words.length;
        while (start < wc) {
            int len = 0; //len for each word
            while (end < wc && words[end].length() + len <= maxWidth) {
                len = words[end].length() + len + 1;
                end++;
            } //note: [start, end)
            StringBuilder sb = new StringBuilder();
            if (start == end) { //word > maxWidth
                throw new IllegalArgumentException(String.format("%s > maxWidth == %s", words[start], maxWidth));
            } else if (end - start == 1) { //only add one word
                sb.append(words[start]);
                addSpace(sb, maxWidth - words[start].length());
            } else if (end == wc){ //add last word
                for (int i = start; i < end - 1; i++) {
                    sb.append(words[i]).append(' ');
                }
                sb.append(words[end - 1]);
                addSpace(sb, maxWidth - len + 1);
            } else { //justified space between words
                int allSpace = maxWidth - len + 1;
                int holes = end - start - 1;
                int avg_padding = allSpace / holes;
                for (int i = start; i < end - 1; i++) {
                    sb.append(words[i]);
                    int offset = 0;
                    if (allSpace % holes > i - start) offset = 1;
                    addSpace(sb, avg_padding + 1 + offset);
                }
                sb.append(words[end - 1]);
            }
            start = end;
            res.add(sb.toString());
        }
        return res;
    }

    public void addSpace(StringBuilder sb, int num) {
        for (int i = 0; i < num ; i++) {
            sb.append(' ');
        }
    }

}


public class Solution {
    public List<String> fullJustify(String[] words, int maxWidth) {
        List<String> res = new ArrayList<>();
        int start = 0;
        int len = 0;

        for(int i = 0; i < words.length ;i++){
            if( i == start){
                len = words[i].length();
            }else{
                len = len + 1 + words[i].length();

                if(len > maxWidth){
                    String line = dfs(words, start, i - 1, maxWidth);
                    res.add(line);

                    start = i;
                    len = 0;
                    i--;
                }
            }
        }

        //generate last line
        StringBuilder sb = new StringBuilder();
        for(int i =start; i < words.length;i++){
            if ( i == start){
                sb.append(words[i]);
            }else{
                sb.append(" ");
                sb.append(words[i]);
            }
        }

        int a = sb.length();
        for(int i = a; i < maxWidth; i++){
            sb.append(" ");
        }

        res.add(sb.toString());
        return res;
    }

    private String dfs(String[] words, int start, int end, int maxLen){
        StringBuilder sb = new StringBuilder();
        int countOfSpace = maxLen;
        for(int i = start; i <= end; i++){
            countOfSpace -= words[i].length();
        }
        sb.append(words[start]);

        for(int i = start +1; i<= end; i++){
            int cnt = countOfSpace /(end - i + 1);
            if( countOfSpace % (end -i + 1) != 0){
                cnt++;
            }
            for(int j = 0; j < cnt; j++){
                sb.append(" ");
            }
            countOfSpace -= cnt;
            sb.append(words[i]);
        }

        int a = sb.length();
        for(int i = a; i < maxLen; i++){
            sb.append(" ");
        }
        return sb.toString();

    }
}
'''