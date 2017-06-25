__source__ = 'https://www.bittiger.io/videos/DTGFfA5s3XdCTbGxG/TpxCSKrGpiKwuhP32'
# Implement a (      )
#
#
FurtherReading = '''

'''
#
#
#
VideoLecture = '''
summary: https://www.bittiger.io/videos/DTGFfA5s3XdCTbGxG/TpxCSKrGpiKwuhP32
面向对象是广为流传的设计思想，但是有太多的人沉迷于于此，甚至做出了过渡复杂的设计。在我看来，设计分三步：
第一步是还原世界。无论是设计停车场、还是设计21点扑克、还是设计成就系统，
核心是先了解现实世界的运作机制，然后围绕着现实世界去还原，这样才不会在一开始走过多的弯路。
第二步是探求合理。现实世界已有的机制不见得是最合理的，也不见得是符合我们具体需求的。
我们不要执着于还原，而是要进一步根据自己的具体问题进行分析和调整。
我们很多人崇拜“创业导师”的“创业课”，这不和我们当年迷信成功学、迷信佛教、迷信中医一个道理吗？
第三步是生长迭代。这告诉我们不要想一步吃个胖子，做出一个合理的系统设计就可以了，我们可以逐步优化。
同时也告诉现实世界是变化的，我们要不断的根据具体问题具体分析，不要迷恋一个“一劳永逸的解决方案”。
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