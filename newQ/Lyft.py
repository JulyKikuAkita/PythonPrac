__source__ = ''
# Time:  O()
# Space: O()
#
# Description:
#http://www.geeksforgeeks.org/find-smallest-range-containing-elements-from-k-lists/
# 1. # You have k lists of sorted integers.
# Find the smallest range that includes at least one number from each of the k lists.
# For example,
# List 1: [4, 10, 15, 24,26]
# List 2: [0, 9, 12, 20] num = 9 index[1] = 1
# List 3: [5, 18, 22, 30]index[2] = 0 num = 5
# output = [20,24]]
# The idea is to use min heap. Below are the steps:
# Create a min heap of size k and insert first elements of all k lists into the heap.
# Maintain two variables min and max to store minimum and maximum values present in the heap at any point.
# Note min will always contain value of the root of the heap.
# Repeat following steps
# Get minimum element from heap (minimum is always at root) and compute the range.
# Replace heap root with next element of the list from which the min element is extracted.
# After replacing the root, heapify the tree.
# Update max if next element is greater. If the list doesn't have any more elements, break the loop.
# #
# Android:
# 电面： running length encoding， android experience， memory leak
# onsite:
# 1.print matrix in spiral order. codepad.io
# 2. 写一个简单的custom view  现场上机。
# 3. 设计一个司机和乘客的mapping 系统，一个m*n的二维数组，有很多司机和乘客（乘客远多于司机），
# int【x,y]代表所处的坐标，任务是给设计算法，保证每个司机都拉到一个乘客，并且所有的pickup话费的路程和最小
# 4.unit test 一个google distance api 的函数。上机
#
# 2)
# boolean allowDriverMode(shifts, current):
# shifts 就是一个的interval，按照顺时间顺序排好的，比如[[0-8], [10-12], [25,33]]
# current就是当前时间。
# 时间不是24小时制的,可以是任意大于0的数字，比如 40或100.
#
# 给一个shifts，给一个当前时间，求司机是否能进入驾驶模式。
# 在最近一次至少8小时休息后(必须是连续的休息时间)。
# 如果司机已经驾驶过12个小时，则不能进入驾驶模式。否则返回可以。
# function to determine whether the driver is allowed to enter driver mode
# * drivers are not allowed to drive a total of 12 hours without an 8 hour break
# the function inputs are:
# - a list of driver shifts as start/end integers, the integer is relative to lyft launch
# - the current time since lyft launch as integer
# def can_drive(history, current_time):
#
#     Returns true if the driver has driven less than 12 hours since their last 8 hour break
#     history: array - Shifts, e.g. [(0, 12), (13, 19)]
#     current_time:int - Current timestamp as hour since Lyft launch, e.g. 50
#     (i)can_drive = True example
#     # 9 hour break, 1 hour shift, 2 hour break, 10 hour shift
#     history = [(9, 10), (12, 22)]
#     current_time = 24
#
#     (ii)can_drive = False example:
#     history = [(0, 4), (5, 9), (10, 14), (15, 19), (20, 24)]
#     current_time = 24
#
#
# 4) print diagonal numbers
# // # Input:
# // # 1 2 3
# // # 4 5 6.
# // # 7 8 9.
#
# // # Print Output:
# // # 3
# // # 2 6
# // # 1 5 9
# // # 4 8
# // # 7
#
# # Phone screening
# 5). reverse integer leetcode #7
# 321 -> 123
# 8765 -> 5678
# bigO and what if negative number
#
# 6)
# Question1: Find second largest element in BST or leetcode 230
# http://www.geeksforgeeks.org/second-largest-element-in-binary-search-tree-bst/
#
# Question2: leetcode 238 Product of Array Except Self
# input:   [1, 2, 3, 4]
# output: [24, 12, 8, 6]
# The product of the all elements in the array except the current one
# (dp 2 array saving the cumulative product from beginning and from end)
#
# Quesion3: Find the most frequent element in a binary search tree
# left child <= root <= right child
# inorder, or use hashmap
#
# 1) Implement iterator for BST
# 2) Reverse words in a string (Leetcode 151)
#

Java = '''
Thought:








'''