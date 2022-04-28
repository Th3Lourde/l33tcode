'''
Given two encoded strings: s1, s2,
return true if there exists an original string that could
be decoded as both s1 and s2, else return false

How strings can be encoded:
- original string can be split arbitrarily into different substrings of different sizes
- replace any of the substrings with their length
- Put the string back together

So the trick here is how to interpret the numbers in the different strings

niave implementation would be to have a backtracking call for each number
and evaluate the possibility of the different interpretations

01234567890123456789
internationalization
  ^

0123
i18n
 ^

b(0,0)
    b(1,1)
b(1,18)

evaluate current values
find new value for idxs
rec call with new values

rules:
- base case -
|--> if one idx is out of bounds but the other isn't, return false
|--> if they are equal, and out of bounds, return true
|--> if they are not equal, and out of bounds, return false

Eval:
    If both chrs:
    - if both idx map to characters (a-z), and those characters match, idx +=1 for both (no recursive call)
    - if both idx map to chr, and don't match, return false

    If one chr, other int:
    - move the chr pointer int to the right, if out of bounds, false

    If both int:
    - subtract the smaller int from the larger int. Find the next value for any zero values
    |--> for the non zero val, make a call with a new difference

    - If ints are equal

If both int:
- have some for-loop to capture all combinations of interpretations
- if both interpretations are equal, += 1 to the idx

We would be comparing valA and valB

One check if we should keep going
Another chunk of code to generate the next


b(idxA, idxB, valA, valB)

compare the values, find the next values based off of the current indices, call again

01234567890123456789
internationalization
          ^

0123
i18n
   ^

b(-1, "", -1, "")
    b(1, "n", 1, "1")
        b(2, "t", 2, "8")
            b(10, "n", 3, "n")
    b(1, "n", 2, "18")

'''

class Solution:
    def possiblyEquals(self, s1, s2):
        ...
        def backtrack(idxA, valA, idxB, valB):
            # if idxA is out of bounds or idxB is out of bounds
            # return false. They must both be in bounds or both
            # be out of bounds

            # 1 function
