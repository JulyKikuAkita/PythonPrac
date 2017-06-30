# https://github.com/kamyu104/LeetCode/blob/master/Python/longest-substring-without-repeating-characters.py
# Time:  O(n)
# Space: O(1)
# Hash table
#
# Given a string, find the length of the longest substring without repeating characters.
# For example, the longest substring without repeating letters for "abcabcbb" is "abc", which the length is 3.
# For "bbbbb" the longest substring is "b", with the length of 1.
# Amazon Adobe Bloomberg Yelp
# Hide Tags Hash Table Two Pointers String
# Hide Similar Problems (H) Longest Substring with At Most Two Distinct Characters

class Solution:
    # Time:  O(2n)
    # @return an integer
    def lengthOfLongestSubstring(self, s):
        longest, start, visited = 0, 0, [False for _ in xrange(256)]
        for i, char in enumerate(s):
            #when repetition found, record the current max and proceed to next non-repeted char
            if visited[ord(char)]:  # Convert a string to ASCII values.
                while char != s[start]:
                    #print i, char, ord(char), longest, "start =", start, visited[ord(s[start])], s[start]
                    visited[ord(s[start])] = False
                    start += 1
                start += 1
            else:
                visited[ord(char)] = True
            longest = max(longest, i - start + 1)
            #print i, char, ord(char), longest, "start =", start
        return longest

    # for every repeating char, set start to last repeating position of that char
    # O(n) runtime, O(1)space, single iteration
    def lengthOfLongestSubstringif(self, s):
        dict = {}
        nextStart = 0
        candidate =  0
        for i in xrange(len(s)):
            if s[i] in dict and dict[s[i]] >= nextStart : # in case of bbcccccb, nextStart don't go back to s[1] when encounter the last b
                nextStart = dict[s[i]] + 1
            candidate = max(candidate, i - nextStart +1)
            dict[s[i]] = i
        return candidate


class SolutionOther:
    # @return an integer
    def lengthOfLongestSubstring(self, s):
        dict, ans, p1, p2 = {} , 0, 0, 0
        while p2 < len(s):
            #Return the value for key if key is in the dictionary, else default. If default is not given,
            # it defaults to None, so that this method never raises a KeyError.
            p = dict.get(s[p2], None)
            print p2, s[p2], "=> ", p , dict, p1
            if p == None:
                dict[s[p2]] = p2
                p2 += 1
                ans = max(ans,p2-p1)
            else:
                while p1 <= p:
                    dict.pop(s[p1])
                    p1 += 1
                p1 = p + 1

        return ans



    def lengthOfLongestSubstring2(self, s):
        lastRepeating = -1 # so that len for s[0] = 1,
        ans = 0
        positions = {}
        for i in range(len(s)):
            if s[i] in positions and lastRepeating < positions[s[i]]:
                lastRepeating = positions[s[i]]
            #if i - lastRepeating > ans:
            #    ans = i-lastRepeating
            ans = max(ans, i - lastRepeating)
            positions[s[i]] = i
        return ans

#test
test = SolutionOther()
#print test.lengthOfLongestSubstring("aab")
#print test.lengthOfLongestSubstring("abcabcbb")
#print test.lengthOfLongestSubstring2("abcabcbb")
#print test.lengthOfLongestSubstring("bbbbb")

if __name__ == "__main__":
    s1 = "dvdfghij"
    s2 = "abcabcbb"
    s3 = "bbbbb"
    s4 = "tmmzuxt"
    s5 = "qwert"
    print Solution().lengthOfLongestSubstring(s1)
    print Solution().lengthOfLongestSubstringif(s1)
    print SolutionOther().lengthOfLongestSubstring2(s1)
java = '''
# the basic idea is, keep a hashmap which stores the characters in string as keys and their positions as values,
and keep two pointers which define the max substring. move the right pointer to scan through the string ,
and meanwhile update the hashmap. If the character is already in the hashmap, then move the left pointer
to the right of the same character last found. Note that the two pointers can only move forward.

  public class Solution {
    public int lengthOfLongestSubstring(String s) {
        if (s.length() == 0) return 0;
        HashMap<Character, Integer> map = new HashMap<Character, Integer>();
        int max = 0;
        for (int i = 0, j =0; i < s.length(); ++i){
            if (map.containsKey(s.charAt(i))){
                j = Math.max(j, map.get(s.charAt(i)) + 1);
            }
            map.put(s.charAt(i), i);
            max = Math.max(max, i - j + 1);
        }
        return max;
    }
}

/**
 * Solution (DP, O(n)):
 *
 * Assume L[i] = s[m...i], denotes the longest substring without repeating
 * characters that ends up at s[i], and we keep a hashmap for every
 * characters between m ... i, while storing <character, index> in the
 * hashmap.
 * We know that each character will appear only once.
 * Then to find s[i+1]:
 * 1) if s[i+1] does not appear in hashmap
 *    we can just add s[i+1] to hash map. and L[i+1] = s[m...i+1]
 * 2) if s[i+1] exists in hashmap, and the hashmap value (the index) is k
 *    let m = max(m, k), then L[i+1] = s[m...i+1], we also need to update
 *    entry in hashmap to mark the latest occurency of s[i+1].
 *
 * Since we scan the string for only once, and the 'm' will also move from
 * beginning to end for at most once. Overall complexity is O(n).
 *
 * If characters are all in ASCII, we could use array to mimic hashmap.
 */

public class Solution {
    public int lengthOfLongestSubstring(String s) {
        if (s.length() == 0) return 0;
        // for ASCII char sequence, use this as a hashmap
        int[] idx = new int[256];
        //initaize arr to -1 inorder to correct calculate interval
        for(int i = 0 ; i < idx.length; i++) {
            idx[i] = -1;
        }
        int max = 0, m = 0;
        for (int i = 0; i < s.length(); i++){
            int ascii = (int) (s.charAt(i));
            m = Math.max(idx[ascii] + 1, m);
            idx[ascii] = i;
            max = Math.max(max, i - m + 1);
        }
        return max;
    }
}

The idea is use a hash set to track the longest substring without repeating characters so far,
use a fast pointer j to see if character j is in the hash set or not, if not, great, add it to the hash set,
move j forward and update the max length, otherwise, delete from the head by using a slow pointer i until
we can put character j to the hash set.

public int lengthOfLongestSubstring(String s) {
    int i = 0, j = 0, max = 0;
    Set<Character> set = new HashSet<>();

    while (j < s.length()) {
        if (!set.contains(s.charAt(j))) {
            set.add(s.charAt(j++));
            max = Math.max(max, set.size());
        } else {
            set.remove(s.charAt(i++));
        }
    }

    return max;
}
'''