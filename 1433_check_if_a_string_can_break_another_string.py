'''
Given strings s1, s2, where they are the same size,
Check if some permutation of s1 can break some perm
of s2, or vice versa.

A string x can break y, if x[i] >= y[i] ∀ 𝑖 ∈ ⟦ 0 , n-1 ⟧.

Sort both strings so they are in alphabetical order.

Then march through each string and check if x[i] >= y[i]
for all elements.

sort both in descending order.

Yea create two min heaps, appending ord("") of every
element. Then poll. Depending on which one is > than
the other initially will determine which one we are
checking.

Establish order on first poll. If the order is broken,
return False.

If the two initial elements are equal, we still haven't
decided

trend = None

for i in range(len(s1)):
    if trend == None:
        if ord(s1[i]) == ord(s2[i]):
            continue

        elif ord(s1[i]) > ord(s2[i]):
            trend = True

        elif ord(s1[i]) < ord(s2[i]):
            trend = False

    elif trend != None:
        if trend == True and ord(s1[i]) < ord(s2[i]):
            # s1[i] >= s2[i] is ok
            return False

        elif trend != True and ord(s2[i]) < ord(s1[i]):
            return False

return True

Oh lol we need to sort them first

Forgot to implement an idea, implemented it,
got it right.

Since we know that we are going through the letters
of the alphabet, we can just create a dict, and step
through the elements that way.

If the frequency of elements is the same, trend = None
If one has less frequency than the other, the one with
the lower frequency will be the string that breaks the
other string.

Come up with solution with
tc: 0(n)
sp: 0(n)

Might have to come up with a difference.
This sum won't work out. Solve the next problem.

'''

class Solution:

    def checkIfCanBreak(self, s1, s2):
        d1 = {}
        d2 = {}

        for i in range(len(s1)):
            if s1[i] in d1:
                d1[s1[i]] += 1

            elif s1[i] not in d1:
                d1[s1[i]] = 1

            if s2[i] in d2:
                d2[s2[i]] += 1

            elif s2[i] not in d2:
                d2[s2[i]] = 1


        alpha = "abcdefghijklmnopqrstuvwxyz"

        trend = None

        for char in alpha:
            if trend == None:
                if d1[char] == d2[char]:
                    continue

                elif d1[char] < d2[char]:
                    trend = True

                elif d1[char] > d2[char]:
                    trend = False

            elif trend != None:
                if d1[char] > d2[char]





    def checkIfCanBreak_1(self, s1, s2):
        s1 = list(s1)
        s2 = list(s2)
        s1.sort()
        s2.sort()

        trend = None

        for i in range(len(s1)):
            if trend == None:
                if ord(s1[i]) == ord(s2[i]):
                    continue

                elif ord(s1[i]) > ord(s2[i]):
                    trend = True

                elif ord(s1[i]) < ord(s2[i]):
                    trend = False

            elif trend != None:
                if trend == True and ord(s1[i]) < ord(s2[i]):
                    # s1[i] >= s2[i] is ok
                    return False

                elif trend != True and ord(s2[i]) < ord(s1[i]):
                    return False

        return True

if __name__ == '__main__':
    s = Solution()
    print(s.checkIfCanBreak("abc", "xya"))
    print(s.checkIfCanBreak("abc", "acd"))
    print(s.checkIfCanBreak("leetcodee", "interview"))

    print(s.checkIfCanBreak("abe", "acd"))
