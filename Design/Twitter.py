__source__ = 'https://www.bittiger.io/videos/tAkRctFLtgNuCj5ev/TpxCSKrGpiKwuhP32'
# Implement a ( twitter / feedstream     )
FurtherReading = '''
https://leetcode.com/problems/design-twitter/#/description
https://discuss.leetcode.com/topic/48100/java-oo-design-with-most-efficient-function-getnewsfeed

'''
SourceVideo = '''
1. https://www.bittiger.io/videos/tAkRctFLtgNuCj5ev/TpxCSKrGpiKwuhP32
面对Twitter每秒5K的写和300K的读，
我们分别使用推模式和拉模式来应对，
但这两个模式各自会遇到“Lady Gaga”和“Architect”的问题。
我们虽然可以通过简单结合的方式来应对，但在现实中，我们却往往选择一条路走到黑，
从而简化我们的架构。至于具体的架构如何，让我们在视频中一起探讨。

2. https://www.bittiger.io/videos/8d7E2LPPy2HcZNr7D/TpxCSKrGpiKwuhP32
我们书接上回，看看如何通过内存优化来提速，并把200T的内存优化至1T。
我们进而讨论了如何设计interface，以及如何实现硬盘的持久存储和快速检索。
我们最后还一起探讨了如何加入搜索功能。
'''

# Description:
# Implement a ( twitter     )
# component: feed list, social graph
# considering getTweet, cache, search
#
# Read tweet: QPS = 300k
# Write tweet: QPS = 5k
# Notify : 1 M follower with in 1s
# -> we can get
# concurrent user: 15 M (DAU / 24 *60 * 60) * session length
# Daily tweets: = 5 k * 86400  = 432 M
#
'''
# Push VS Pull
concept =

(i) Push:
Write O(n)
Read O(1)
                                social graph
                                     |
                                     V
client write tweet -> write API -> fanout - O(n) -> timeline lists  - O(1) - > timeline service -> user read tweet

                                                                       | --------- user read tweet --------|

-> Lady gaga dilemma, 1 to 46 million followers, bottleneck on fanout


(ii) Pull:
Write O(1)
Read O(n)

                                                        social graph
                                                            |
                                                            V
client write tweet -> write API -> feed list - O(1) -> timeline service  - O(n) - > timeline list



->The architect of Matrix dilemma : 1 to many followees

(iii) Push + Pull

                                social graph
                                     |
                                     V
                  (follower < 100M) fanout - O(n) -> timeline lists  - O(1) - > timeline service  -- |
                                                                                                     |
                                                                                                     |
                                                                                                     |
                                                                                                     | -> merge ->timeline list
client write tweet -> write API ->                                                                   |
                                                                                                     |
                  (follower > 100M) feed list - O(1) -> timeline service  - O(n)  ------------------ |



-> what if user fluctuate between 100M? set a range instead of a fixed value, instead of < 100M, set follower <= 90M
'''






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

DAU =
- future DAU:
- concurrent user:
- peak concurrent user:
- future peak concurrent user:
- memory usage per user:
- hard disk usage:


############################# CACHE ###################################
use SNAKE:

constraint of this scenario:
ex:
Assumption:
1B users
avg feed size: 50 tweets
avg timelines size: 1000 tweets
one tweet text size: 200 Bytes
avg followers: 30

Memory needed:
size of timelines limit = 1b * 1000 * 200 = 200TB
size of feed list = 1b * 50 * 200 = 10T
size of social graph = 1b * 30 * 2 * 8 = 480G
(assume 2 way follow, so 30 * 2, assume need to save additional state, so use 8 bytes)
-> total memory need = 212 TB (not realistic for now)

-> adding restraint
if only cache for users who is active within 1 week
if only cache the latest 800 tweets
Assumption:
weekly active users: 100 Million
avg feed size: 80
avg timelined size = 500
size of timelines limit = 100M * 500 * 200 = 10TB
size of feed list = 100M * 80 * 200 = 1.6T
size of social graph = 100M * 30 * 2 * 8 = 48G
->total memory need: 13T

-> what else can we improve?
if not save the whole tweet text but only tweet id?
Assumption new tweet size = 20Bytes = userID(8) + tweetId(8)+ indicator(4)
Memory needed:
size of timelines limit = 100M * 500 * 20 = 1TB -> which is doable at a distributed system

-> what's the evolve?
if we lost cache? how to rebuild active user state (use timeline builders, use persistent data to rebuild user state)


############################# CACHE ###################################



# 3. Application:service/algorithm
- service diagram

- proposed algorithm (pros/ cons)
(i) the simplest one

(ii) the improved one

(iii) any better idea?


# 4. Kilobit:data assume data block size 64 MB
# Whats the data usage/ query load for your algo/serice?
(i) the simplest one

(ii) the improved one

(iii) any better idea?

# 5. Evolve:
# scalability
# improvement

'''