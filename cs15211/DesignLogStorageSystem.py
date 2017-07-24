__source__ = 'https://leetcode.com/problems/design-log-storage-system/discuss/'
# Time:  O()
# Space: O()
#
# Description: Leetcode # 635. Design Log Storage System
#
# You are given several logs that each log contains a unique id and timestamp.
# Timestamp is a string that has the following format:
# Year:Month:Day:Hour:Minute:Second, for example,
# 2017:01:01:23:59:59.
# All domains are zero-padded decimal numbers.
#
# Design a log storage system to implement the following functions:
#
# void Put(int id, string timestamp): Given a log's unique id and timestamp, store the log in your storage system.
#
# int[] Retrieve(String start, String end, String granularity):
# Return the id of logs whose timestamps are within the range from start to end.
# Start and end all have the same format as timestamp.
# However, granularity means the time level for consideration.
# For example, start = "2017:01:01:23:59:59", end = "2017:01:02:23:59:59", granularity = "Day",
# it means that we need to find the logs within the range from Jan. 1st 2017 to Jan. 2nd 2017.
#
# Example 1:
# put(1, "2017:01:01:23:59:59");
# put(2, "2017:01:01:22:59:59");
# put(3, "2016:01:01:00:00:00");
# retrieve("2016:01:01:01:01:01","2017:01:01:23:00:00","Year"); // return [1,2,3],
# because you need to return all logs within 2016 and 2017.
# retrieve("2016:01:01:01:01:01","2017:01:01:23:00:00","Hour"); // return [1,2],
# because you need to return all logs start from 2016:01:01:01 to 2017:01:01:23, where log 3 is left outside the range.
# Note:
# There will be at most 300 operations of Put or Retrieve.
# Year ranges from [2000,2017]. Hour ranges from [00,23].
# Output for Retrieve has no order required.
#
# Companies
# Snapchat
# Related Topics
# Design String
# Similar Questions
# Design In-Memory File System
#

import unittest
# Because the number of operations is very small,
# we do not need a complicated structure to store the logs: a simple list will do.
# Let's focus on the retrieve function.
# For each granularity, we should consider all timestamps to be truncated to that granularity.
# For example, if the granularity is 'Day', we should truncate the timestamp '2017:07:02:08:30:12'
# to be '2017:07:02'. Now for each log, if the truncated timetuple cur is between start and end,
# then we should add the id of that log into our answer.

#62ms
class LogSystem(object):

    def __init__(self):
        self.logs = []

    def put(self, id, timestamp):
        """
        :type id: int
        :type timestamp: str
        :rtype: void
        """
        self.logs.append((id, timestamp))

    def retrieve(self, s, e, gra):
        """
        :type s: str
        :type e: str
        :type gra: str
        :rtype: List[int]
        """
        index = {'Year': 5, 'Month': 8, 'Day': 11,
                 'Hour': 14, 'Minute': 17, 'Second': 20}[gra]
        start = s[:index]
        end = e[:index]

        return sorted(id for id, timestamp in self.logs
                      if start <= timestamp[:index] <= end)


# Your LogSystem object will be instantiated and called as such:
# obj = LogSystem()
# obj.put(id,timestamp)
# param_2 = obj.retrieve(s,e,gra)

class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)


if __name__ == '__main__':
    unittest.main()

Java = '''
#Thought: https://leetcode.com/problems/design-log-storage-system/solution/

#80.36% 170ms
public class LogSystem {

    List<String[]> timestamps = new LinkedList<>();
    List<String> units = Arrays.asList("Year", "Month", "Day", "Hour", "Minute", "Second");
    int[] indices = new int[]{4,7,10,13,16,19};

    public void put(int id, String timestamp) { timestamps.add(new String[]{Integer.toString(id), timestamp}); }

    public List<Integer> retrieve(String s, String e, String gra) {
        List<Integer> res = new LinkedList<>();
        int idx = indices[units.indexOf(gra)];
        for (String[] timestamp : timestamps) {
            if (timestamp[1].substring(0, idx).compareTo(s.substring(0, idx)) >= 0 &&
               	timestamp[1].substring(0, idx).compareTo(e.substring(0, idx)) <= 0) res.add(Integer.parseInt(timestamp[0]));
        }
        return res;
    }
}

/**
 * Your LogSystem object will be instantiated and called as such:
 * LogSystem obj = new LogSystem();
 * obj.put(id,timestamp);
 * List<Integer> param_2 = obj.retrieve(s,e,gra);
 */


#71.62% 175ms
public class LogSystem {

    public LogSystem() {

    }

    public void put(int id, String timestamp) {
       timestamps.add(new String[]{Integer.toString(id), timestamp});
    }

    public List<Integer> retrieve(String s, String e, String gra) {
        List<Integer> results = new ArrayList<>();
        int index = indices[format.indexOf(gra)];
        for (String[] t : timestamps)
        {
            if (t[1].substring(0, index).compareTo(s.substring(0, index)) >= 0 &&
               t[1].substring(0, index).compareTo(e.substring(0, index)) <= 0)
                results.add(Integer.parseInt(t[0]));
        }
        return results;
    }

    private List<String[]> timestamps = new LinkedList<>();
    private List<String> format = Arrays.asList("Year", "Month", "Day", "Hour", "Minute", "Second");
    private int[] indices = new int[]{4, 7, 10, 13, 16, 19};
}

#32.02% 205ms
public class LogSystem {
    TreeMap < Long, Integer > map;
    public LogSystem() {
        map = new TreeMap < Long, Integer > ();
    }

    public void put(int id, String timestamp) {
        int[] st = Arrays.stream(timestamp.split(":")).mapToInt(Integer::parseInt).toArray();
        map.put(convert(st), id);
    }
    public long convert(int[] st) {
        st[1] = st[1] - (st[1] == 0 ? 0 : 1);
        st[2] = st[2] - (st[2] == 0 ? 0 : 1);
        return (st[0] - 1999L) * (31 * 12) * 24 * 60 * 60 + st[1] * 31 * 24 * 60 * 60 + st[2] * 24 * 60 * 60 + st[3] * 60 * 60 + st[4] * 60 + st[5];
    }
    public List < Integer > retrieve(String s, String e, String gra) {
        ArrayList < Integer > res = new ArrayList();
        long start = granularity(s, gra, false);
        long end = granularity(e, gra, true);
        for (long key: map.tailMap(start).keySet()) {
            if (key >= start && key < end)
                res.add(map.get(key));
        }
        return res;
    }

    public long granularity(String s, String gra, boolean end) {
        HashMap < String, Integer > h = new HashMap();
        h.put("Year", 0);
        h.put("Month", 1);
        h.put("Day", 2);
        h.put("Hour", 3);
        h.put("Minute", 4);
        h.put("Second", 5);
        String[] res = new String[] {"1999", "00", "00", "00", "00", "00"};
        String[] st = s.split(":");
        for (int i = 0; i <= h.get(gra); i++) {
            res[i] = st[i];
        }
        int[] t = Arrays.stream(res).mapToInt(Integer::parseInt).toArray();
        if (end)
            t[h.get(gra)]++;
        return convert(t);
    }
}
'''