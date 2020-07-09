'''
Given a string S.

We are allowed to vary the case of
each character.

Return a list of all possible strings
that we could create.

S = "a1b2"
["a1b2", "a1B2", "A1b2","A1B2"]

The number of answers that we have is equal
to the number of letters that we have in the
string.

This is fundamentally a permutation problem
where we are tasked with creating all perumations
of that which we can vary.

Let's say that we have an array.

ans = []

d = {}   <-- check to see if we already have the str

We have a function that calls itself (helper function)

def helper(s, i)

s represents the current permutation
i represents the current character (letter) that we are on.

"a1b2", i = 0

"A1b2", "a1b2" )-- For both, check to see if we have the str
                add to dict if we do not.

Find the next letter (if one exists), call function again
based upon that, where i is the index of the next letter

Given s


d = {}
ans = []

# find the next letter
i = nextIndex(s, 0)

if i == -1: return [s]

helper(s, i)

return ans

-------------------------

helper(perm, i)

if perm not in d:
    ans.append(perm)
    d[perm] = True

# Make sure that this works
newPerm = perm[:i] + perm[i].swapcase() + perm[i+1:]

if newPerm not in d:
    ans.append(newPerm)
    d[newPerm] = True

# Find next letter
while i < len(perm) and not perm[i].isalpha():
    i += 1

if i < len(perm):
    helper(perm, i)
    helper(newPerm, i)



'''




class Solution:
    def letterCasePerumtation(self, S):

        def nextIndex(perm, i):
            while i < len(perm) and not perm[i].isalpha():
                i += 1

            if i < len(perm):
                return i

            return -1

        def helper(perm, i):
            if perm not in d:
                ans.append(perm)
                d[perm] = True

            # Make sure that this works
            newPerm = perm[:i] + perm[i].swapcase() + perm[i+1:]

            if newPerm not in d:
                ans.append(newPerm)
                d[newPerm] = True

            i = nextIndex(perm, i+1)

            if i >= 0:
                helper(perm, i)
                helper(newPerm, i)

        d = {}
        ans = []

        # find the next letter
        i = nextIndex(S, 0)

        if i == -1: return [S]

        helper(S, i)

        return ans

if __name__ == '__main__':
    s = Solution()

    # print(s.letterCasePerumtation("a1b2"))
    # print(s.letterCasePerumtation("3z4"))
    print(s.letterCasePerumtation("A"))
