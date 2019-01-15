__source__ = ''
# Time:  O()
# Space: O()
#
# Description:
# 1. What's your approach to test google map point a -> point b direction is correct?
# (cannot use any of the third party benchmark map)
#
# 2. Leetcode 28
# Write a function of indexOf(String main, String search) and throw exception if no search found
# write test cases for (i) found (ii) not found
#
Java = '''
#Thought:
Please use this Google doc to code during your interview. To free your hands for coding,
we recommend that you use a headset or a phone with speaker option.
(1)
<Black box> functional testing- positive/negative scenario
    API -test -> load testing
    validate data format ex: Json or etc
    validate data itself is correct (assume not verify through a benchmark data)

    simplified the map to a matrix, and A and B are points on the matrix
    ->  if it's longitude/latitude -> verify data format/ range
    ->  drive direction -> how do I verify if it is valid?
    if it is a valid path -> checking loop/path on obstacles
    -> the idea is to simplified this to a valid path question from point A to point B
<white box >
<End to end>

(2)
questions =
Find all occurrences of substring in a string.  Determine complexity in big(O) notation.
Write two unit tests: 1. search string exists 2. search string doesn't exist

String main = "It's fun having a baby until baby wants to go to sleep"
String search = "baby"

KMP, -> O(n) but forget about the process
O(m*n)

private int[] search(String main, String search){
	if (main == null || search == null || both.length() == 0)  throw new illegalArgumentException("no string");

	int i = 0, j = 0;
    while (i < main.length()) {
        int start = i;
            while (i < main.length() &&j < search.length() && main.charAt(i) == search.charAt(j)) {
            i++;
            j++;
        }
        if ( j == search.length()){
            return new int[]{start, start + j};
        } else {
            i = start + j;
            j = 0;
        }
    }
    // not found // throw self-defined exception
    throw new illegalArgumentException("no match found");
    }

"babybabybay" "baby" ->(0,3)

    @Test
    public void testSearchFound() throw illegalArgumentException( {
        String s1 = "babybabybay";
        String s2 = 'baby;
        try{
            assertTrue(search(s1,s2)[0] == 0);
            assertTrue(search(s1,s2)[1] == 3);
        } catch(illegalArgumentException ile) {
            log.e(ile.toString());
            throw ile;
        }
    }

    /**
    create a func similar to assertException in py
    */
    public void searchNotFoundException(){

        String s1 = "babybabybay";
        String s2 = 'baby;
        try{
            search(s1,s2)[0] == 0;
                return false;
            } catch(illegalArgumentException ile) {
                log.i(ile.toString());
                return true;
        }
    }

    @Test
    public void testSearchNotFoundException(){
        String s1 = "babybabybay";
        String s2 = 'baby;
        try{
            assertFail(searchNotFoundException(s1,s2));
        } catch(illegalArgumentException ile) {
            log.e(ile.toString());
        }
    }
'''