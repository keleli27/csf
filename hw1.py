# Name: Betsy Kelley
# Evergreen Login: keleli27
# Computer Science Foundations
# Programming as a Way of Life
# Homework 1

# You may do your work by editing this file, or by typing code at the
# command line and copying it into the appropriate part of this file when
# you are done.  When you are done, running this file should compute and
# print the answers to all the problems.

import math                     # makes the math.sqrt function available


###
### Problem 1
###

print "Problem 1 solution follows:"

a = 1
b = -5.86
c = 8.5408

xone = ((-b + math.sqrt(b**2 - (4 * a * c)) / (2 * a)))

xtwo = ((-b - math.sqrt(b**2 - (4 * a * c)) / (2 * a)))

print str(xone)
print str(xtwo)


###
### Problem 2
###

print "Problem 2 solution follows:"

import hw1_test

print str(hw1_test.a)
print str(hw1_test.b)
print str(hw1_test.c)
print str(hw1_test.d)
print str(hw1_test.e)
print str(hw1_test.f)


###
### Problem 3
###

print "Problem 3 solution follows:"



print str((hw1_test.a and hw1_test.b) or (not hw1_test.c) and not (hw1_test.d or hw1_test.e or hw1_test.f))




###
### Collaboration
###

# ... List your collaborators here, as a comment (on a line starting with "#").
###Partners in Python Crime
#Betsy Kelley
#DJ Porter
#Travis Malone

###Reflections

#This assignment took me roughly an hour and a half. (We completed the task at 
#4:39 PM.) The readings, tutorials and lecture were helpful, although there were 
#still a few sections where extra help (Google) was needed. I think at this time 
#we were expected to have a small base of knowledge, as well as some intuition
#that I do not neccessarily possess yet. It was also really quite terrifying submitting
#a task that I had no answers for...this seems to be something that I will just have
#to get used to at Evergreen.