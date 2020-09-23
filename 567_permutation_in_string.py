
'''
Given two strings s1 and s2, write a function to return true
if s2 contains a permutation of s1,

which is to say that one of the first string's permutation is
the substring of the second string.

So when they mean permutation, they mean a substring of adjacent
characters.

There can be no missing characters, there can be no extra characters.

So this is obv a sliding window.

Create a window that is the size of s1, iterate through s2.

The 'tricky' part is to determine whether or not s2 is a permutation
of s1.

Initial solution is to create a dict (that we update as we itr, elementwise)
and then check to see if the elements or frequency of the elements are the
same.

Or, we just create all permutations of s1, throw them in a set, and then check
to see if our current sliding window element is in the set.

I like #2 better, however it would take much longer.

Let's see whether or not we can directly compare dict's

We can just directly compare, great.

Last thing is just to add/remove terms/keys from the dict as we itr.

remove, -= 1, if 0, del key

add, if not in dict, = 1, else += 1

- - -
- - - - -

'''

class Solution:
    def checkInclusion(self, s1, s2):

        if len(s1) > len(s2): return False

        d1 = {}

        for chr in s1:
            if chr not in d1:
                d1[chr] = 1

            else:
                d1[chr] += 1

        for i in range(len(s2)-len(s1)+1):

            if i == 0:
                # Make the dict
                d2 = {}

                for z in range(i, i+len(s1)):
                    chr = s2[z]
                    if chr not in d2:
                        d2[chr] = 1

                    else:
                        d2[chr] += 1

            else:
                # Remove
                if d2[s2[i-1]] == 1:
                    del d2[s2[i-1]]

                else:
                    d2[s2[i-1]] -= 1

                # Add
                if s2[i+len(s1)-1] in d2:
                    d2[s2[i+len(s1)-1]] += 1

                else:
                    d2[s2[i+len(s1)-1]] = 1


            if d1 == d2: return True

        return False

if __name__ == '__main__':
    s = Solution()

    print(s.checkInclusion("ab", "eidbaooo"))
    print(s.checkInclusion("ab", "eidboaoo"))
    print(s.checkInclusion("ab", "a"))
    print(s.checkInclusion("ab", "ba"))
    print(s.checkInclusion("ab", "aba"))
    print(s.checkInclusion("ab", "cba"))
    print(s.checkInclusion("ab", "cba"))
    print(s.checkInclusion("ab", "cbab"))
    print(s.checkInclusion("ab", "cbab"))
