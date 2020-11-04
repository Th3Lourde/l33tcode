'''
A string is a valid paren
iff it consists of only ( )
and chars.

It can be an empty string
If can be written as AB, A, B, (A)

depth(S), S is a VPS:

depth("") ⟹ 0
depth(A + B) ⟹ max(depth(A), depth(B))
depth("(" + A + ")") ⟹ 1 + depth(A)

So we should probably write a function that
returns the depth of a given VPS.

So it sounds like we are to loop through the
inputted sequence. For

Ok this question sucks.


'''

class Solution:
    def maxDepthAfterSplit(self, seq):
        ans = [1 for i in range(len(seq))]

        a = b = 0

        for i in range(len(seq)):
            chr = seq[i]

            if chr == '(':
                if a <= b:
                    a += 1
                    ans[i] = 0

                else:
                    b += 1

            else:
                if a >= b:
                    a -= 1
                    ans[i] = 0

                else:
                    b -= 1

        return ans
