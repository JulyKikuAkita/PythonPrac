__source__ = 'https://tekmarathon.com/2013/05/14/algorithm-to-find-substring-in-a-string-kmp-algorithm/'
# http://www.geeksforgeeks.org/searching-for-patterns-set-2-kmp-algorithm/
# Time:  O(n)
# Space: O(n)
#
# Description: KMP implementation
#

import unittest
# Python program for KMP Algorithm
def KMPSearch(pat, txt):
    M = len(pat)
    N = len(txt)

    # create lps[] that will hold the longest prefix suffix
    # values for pattern
    lps = [0]*M
    j = 0 # index for pat[]

    # Preprocess the pattern (calculate lps[] array)
    computeLPSArray(pat, M, lps)

    i = 0 # index for txt[]
    while i < N:
        if pat[j] == txt[i]:
            i += 1
            j += 1

        if j == M:
            print "Found pattern at index " + str(i-j)
            j = lps[j-1]

        # mismatch after j matches
        elif i < N and pat[j] != txt[i]:
            # Do not match lps[0..lps[j-1]] characters,
            # they will match anyway
            if j != 0:
                j = lps[j-1]
            else:
                i += 1

def computeLPSArray(pat, M, lps):
    len = 0 # length of the previous longest prefix suffix

    lps[0] # lps[0] is always 0
    i = 1

    # the loop calculates lps[i] for i = 1 to M-1
    while i < M:
        if pat[i]==pat[len]:
            len += 1
            lps[i] = len
            i += 1
        else:
            # This is tricky. Consider the example.
            # AAACAAAA and i = 7. The idea is similar
            # to search step.
            if len != 0:
                len = lps[len-1]

                # Also, note that we do not increment i here
            else:
                lps[i] = 0
                i += 1

txt = "ABABDABACDABABCABAB"
pat = "ABABCABAB"
KMPSearch(pat, txt)

# This code is contributed by Bhavya Jain


class FooTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        pass

    @classmethod
    def tearDownClass(cls):
        pass

    def setupDown(self):
        pass

    def tearDown(self):
        pass

    def test_foo(self):
        self.assertEqual(1, 1)

class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)

if __name__ == '__main__':
    unittest.main()
    # run one test
    #unittest.main(defaultTest='FooTest.test_foo', warnings='ignore')

Java = '''
//https://tekmarathon.com/2013/05/14/algorithm-to-find-substring-in-a-string-kmp-algorithm/
/**
     * Based on the pre processed array, search for the pattern in the text
     *
     * @param text
     *            text over which search happens
     * @param ptrn
     *            pattern that is to be searched
     */
    public void searchSubString(char[] text, char[] ptrn) {
        int i = 0, j = 0;
        // pattern and text lengths
        int ptrnLen = ptrn.length;
        int txtLen = text.length;

        // initialize new array and preprocess the pattern
        int[] b = preProcessPattern(ptrn);

        while (i < txtLen) {
            while (j >= 0 && text[i] != ptrn[j]) {
                j = b[j];
            }
            i++;
            j++;

            // a match is found
            if (j == ptrnLen) {
                System.out.println("found substring at index:" + (i - ptrnLen));
                j = b[j];
            }
        }
    }

/**
 * Pre processes the pattern array based on proper prefixes and proper
 * suffixes at every position of the array
 *
 * @param ptrn
 *            word that is to be searched in the search string
 * @return partial match table which indicates
 */
public int[] preProcessPattern(char[] ptrn) {
    int i = 0, j = -1;
    int ptrnLen = ptrn.length;
    int[] b = new int[ptrnLen + 1];

    b[i] = j;
    while (i < ptrnLen) {
            while (j >= 0 && ptrn[i] != ptrn[j]) {
            // if there is mismatch consider the next widest border
            // The borders to be examined are obtained in decreasing order from
            //  the values b[i], b[b[i]] etc.
            j = b[j];
        }
        i++;
        j++;
        b[i] = j;
    }
    return b;
}

// JAVA program for implementation of KMP pattern
// searching algorithm

class KMP_String_Matching
{
    void KMPSearch(String pat, String txt)
    {
        int M = pat.length();
        int N = txt.length();

        // create lps[] that will hold the longest
        // prefix suffix values for pattern
        int lps[] = new int[M];
        int j = 0;  // index for pat[]

        // Preprocess the pattern (calculate lps[]
        // array)
        computeLPSArray(pat,M,lps);

        int i = 0;  // index for txt[]
        while (i < N)
        {
            if (pat.charAt(j) == txt.charAt(i))
            {
                j++;
                i++;
            }
            if (j == M)
            {
                System.out.println("Found pattern "+
                              "at index " + (i-j));
                j = lps[j-1];
            }

            // mismatch after j matches
            else if (i < N && pat.charAt(j) != txt.charAt(i))
            {
                // Do not match lps[0..lps[j-1]] characters,
                // they will match anyway
                if (j != 0)
                    j = lps[j-1];
                else
                    i = i+1;
            }
        }
    }

    void computeLPSArray(String pat, int M, int lps[])
    {
        // length of the previous longest prefix suffix
        int len = 0;
        int i = 1;
        lps[0] = 0;  // lps[0] is always 0

        // the loop calculates lps[i] for i = 1 to M-1
        while (i < M)
        {
            if (pat.charAt(i) == pat.charAt(len))
            {
                len++;
                lps[i] = len;
                i++;
            }
            else  // (pat[i] != pat[len])
            {
                // This is tricky. Consider the example.
                // AAACAAAA and i = 7. The idea is similar
                // to search step.
                if (len != 0)
                {
                    len = lps[len-1];

                    // Also, note that we do not increment
                    // i here
                }
                else  // if (len == 0)
                {
                    lps[i] = len;
                    i++;
                }
            }
        }
    }

    // Driver program to test above function
    public static void main(String args[])
    {
        String txt = "ABABDABACDABABCABAB";
        String pat = "ABABCABAB";
        new KMP_String_Matching().KMPSearch(pat,txt);
    }
}
'''