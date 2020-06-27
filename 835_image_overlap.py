'''
Given two images (as matrices)
Matrices are square.

Given that you can perform any
translation that you wish on the
image, return the number of ones
that will be lined up.

e.g.
A = [
    [1,1,0],
    [0,1,0],
    [0,1,0],
    ]

B = [
    [0,0,0],
    [0,1,1],
    [0,0,1],
    ]

We translate A one right and one down
and get out match.

We could loop through every possible
translation and record the number of
ones that match up. Return the max.

So how would we simulate the translation?
Well, the first thing we'd probably do is
record all of the indices of the ones in the
first image, then iterate through all possible
translations and compute the matches.

Probably use a function to do this.

Found a good guide with a bunch of problems
on leetcode, going to do that instead of this.

This problem isn't fun.

'''



class Solution:
    def largestOverlap(self, A, B):
        ...
