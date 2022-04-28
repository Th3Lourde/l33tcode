'''
Given a string s, return true if a permutation
of the string could result in a palindrome

here's what we could do:
create a dict of the chr --> count

We can have one odd count, everything else must be
even.



carerac
      ^

chrToCount : {
    c:2
    a:2
    r:2
    e:1

}
'''

class Solution:
    def canPermutePalindrome(self, s):
        chrToCount = {}
        seenOdd = False

        for chr in s:
            if chr not in chrToCount:
                chrToCount[chr] = 1
            else:
                chrToCount[chr] += 1

        for chr in chrToCount:
            if chrToCount[chr] % 2 == 1:
                if seenOdd == False:
                    seenOdd = True
                else:
                    return False

        return True
