__source__ = 'https://www.bittiger.io/classpage/qSDjkz44xh68E73xS'
# Implement a (    kafka  )
#
#
FurtherReading = '''

'''
#
#
#
VideoLecture = '''
https://www.bittiger.io/classpage/qSDjkz44xh68E73xS
summary:
这篇视频解读的是Confluent的Jay Kreps的经典讲座《I Heart Log: Real-time Data and Apache 》。
Jay为我们打开了一个新的视角来看所谓的数据集成、分布式系统、实时处理。我们的生命无非是一系列的log，
而我们世界的每一个当下也无非是log的一个快照。因此我们可以围绕log来重整我们的生活，让一切变得井然有序。
在这个思想的指导下，Kafka基于分布式的log实现了订阅模型的消息系统，让我们机器的世界更加美好。

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