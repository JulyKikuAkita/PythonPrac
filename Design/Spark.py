__source__ = 'https://www.bittiger.io/videos/vhPmQZzBsM8vv7Tnb/qtFZHdaf6JJQxyMCB'
# WHat is spark
#
#
FurtherReading = '''

'''
#
#
#
VideoLecture = '''
summary: https://www.bittiger.io/videos/vhPmQZzBsM8vv7Tnb/qtFZHdaf6JJQxyMCB

'''
# Description:
# Implement a (      )
#

#
# SNAKE concept:
# Scenario:case/interface
# Necessary:constrain/hypothesis
# Application:service/algorithm
# Kilobit:data
# Evolve:

Analysis_by_SNAKE = '''
# 1. Scenario:case/interface
Whats the usage scenario ?

2. Necessary:constrain/hypothesis
# DAU
# concurrent user = DAU / 86400(seconds) * (avg session length)
# peak concurrent user = 2 - 10 times (avg concurrent user)
# future peak concurrent user = 2 * peak concurrent user
# data usage: avg data download per user: 3Mbps
# memory requirement: avg user memory * peak user
# hard disk requirement : file size * file number
#
constraint of this scenario:
ex: 
DAU = 
- future DAU:
- concurrent user:
- peak concurrent user:
- future peak concurrent user:
- memory usage per user:
- hard disk usage:


# 3. Application:service/algorithm
- service diagram

- proposed algorithm (pros/ cons)
(i) the simplest one

(ii) the improved one

(iii) any better idea?


# 4. Kilobit:data
# Whats the data usage/ query load for your algo/serice?
(i) the simplest one

(ii) the improved one

(iii) any better idea?

# 5. Evolve:
# scalability
# improvement

'''
a ='''
NoSQL popularity winner:
1. Key->Val
Redis
Memcached
DynamoDB
Riak

2. Key->Doc
MongoDB
CouchDB
CouchBase
DynamoDB
MarkLogic

3. Column Family
Cassandra
HBase

4. Graph
Neo4j
OrietnDB
Titan
Giraph

5. Search
Solr
Elasticsearch
Splunk
'''
b = '''
有朋友可能会问内存、硬盘、SSD、网络在传输数据的时候到底差异多大呢？在这篇视频中给出了一份答案：
内存：10GB/s
硬盘：100MB/s
SSD：600MB/s
同机架网络传输：125MB/s
跨机架网络传输：12.5MB/s

'''