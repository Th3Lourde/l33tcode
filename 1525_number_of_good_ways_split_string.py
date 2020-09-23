'''
Given a string s, want to split it.
A split is called good if you can split
s into 2 non-empty strings p and q where

its concatentation == s

and the number of distinc letters in p and q are the same.

concatentation == s → p + q == s.

min len or p, q == 1.

Start on far left, have some kind of barrier.

Have two dictionaries. One represents the keys on the LHS,
other represents keys on the RHS.

As we shift the barrier from l--> update the keys

After every shift, check if split is good.

"aacaba"



"a|acaba"


1) l = {}, loop through string to get r (which represents the whole string)
2) for 1, len(s)-1:
    term = s[i] (term we are putting from RHS to LHS)

    add key to lhs, -= 1 from rhs, if d[term] == 0, del key
    We can even do better and keep a counter that goes up/down depending
    on if we are initializing a term or not.
        |--> This would help prevent us from having to get the keys constantly.


3) Test if split is good. If distL == distR, ans += 1






'''


class Solution:
    def numSplits(self, s):
        ans = 0
        dL = 0 # Distinct Left
        dR = 0 # Distinct Right
        l = {}
        r = {}

        for i in range(len(s)):
            if s[i] not in r:
                # new term for right
                dR += 1
                r[s[i]] = 1

            else:
                r[s[i]] += 1

        for i in range(0, len(s)-1):
            term = s[i]

            # subtract term from rhs
            r[term] -= 1

            # Re-balance distinct terms if applicable
            if r[term] == 0:
                dR -= 1

            # add term to lhs, distinct case
            if term not in l:
                dL += 1
                l[term] = 1

                # non-distinct case
            elif term in l:
                l[term] += 1

                # check if good split
            if dL == dR:
                ans += 1

        return ans


if __name__ == '__main__':
    s = Solution()

    print(s.numSplits("aacaba"))
    print(s.numSplits("abcd"))
    print(s.numSplits("aaaaa"))
    print(s.numSplits("acbadbaada"))

    print(s.numSplits("a"))
