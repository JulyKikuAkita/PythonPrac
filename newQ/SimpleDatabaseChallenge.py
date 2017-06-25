__source__ = 'https://www.thumbtack.com/challenges/simple-database'
Material = '''
https://github.com/PramodhN/simple-database-challenge
'''
# Time:  O()
# Space: O()
#
# Description:
# Simple Database Challenge
# In the Simple Database problem, you'll implement an in-memory database similar to Redis.
# For simplicity's sake, instead of dealing with multiple clients and communicating over the network,
# your program will receive commands via standard input (stdin), and should write appropriate responses
# to standard output (stdout).
# Guidelines
#
# We recommend that you use a high-level language, like Python, Go, Haskell, Ruby, or Java.
# We're much more interested in seeing clean code and good algorithmic performance than raw throughput.
# It is very helpful to the engineers who grade these challenges if you reduce external dependencies,
# make compiling your code as simple as possible, and include instructions for compiling and/or running
# your code directly from the command line, without the use of an IDE.
# Your submission must comply with the input/output formats and performance requirements specified below.
# Data Commands
#
# Your database should accept the following commands:
# SET name value - Set the variable name to the value value. Neither variable names nor values will contain spaces.
# GET name - Print out the value of the variable name, or NULL if that variable is not set.
# UNSET name - Unset the variable name, making it just like that variable was never set.
# NUMEQUALTO value - Print out the number of variables that are currently set to value.
# If no variables equal that value, print 0.
# END - Exit the program. Your program will always receive this as its last command.
# Commands will be fed to your program one at a time, with each command on its own line.
# Any output that your program generates should end with a newline character.
# Here are some example command sequences:
# #

Java = '''
#Thought:

'''