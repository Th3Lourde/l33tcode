'''
The gray code is a binary numeral system where two successive
values differ in only one bit.

Given a non-negative integer n,
n represents the total number of bits in the code,
print the sequence of gray code.

A gray code must begin with 0

So n is the number of bits

We start with all zeroes?

So each subsequent term differs from the current term by only
one bit.

Start with zeroes,

000

100

110

111

011

001

Start with zeroes,

For phase 1, loop through the different
binary representations and swap a bit,
then start from the beginning and end at the end

Then do a final pass and get the integers (maybe do this earlier, ignore for now)

Yea store this as a list of strings

Ok so I took the wrong approach. Out of time, come back and revise tomorrow.

Good exec, wrong assumptions.

Next time, test your assumptions in the testcase portion before going through
full implementation.

L,E.

Ok so we care about where each subsequent value only differs by one bit.
Let's do some examples to make sure that we understand what they are talking
about:

n = 0 → [0]

n = 2:

00
10
11
01

n = 3

000
100
110
111
011
001

Missing:

010
001

ans:
[0,1,3,2,6,7,5,4]

So what if we keep changing the value that we
reset at so it keeps going up by one?

000
100
110
111
011
001
010
001

I like it better if we instead vary the number of
1's in the string

Ok so this can't happen because each element must
only differ by one bit.

3: ['000', '001', '011', '010', '110', '111', '101', '100']

000
001
011
010
110
111
101
100



4:
['0000', '0001', '0011', '0010', '0110', '0111', '0101', '0100', '1100', '1101',
'1111', '1110', '1010', '1011', '1001', '1000']

0000
0001
0011
0010
0110
0111
0101
0100
1100
1101
1111
1110
1010
1011
1001
1000

Ok so that should be good enough to figure out the pattern (I hope)
The issue isn't getting all of the codes, but rather putting them in
an order that fits the use-case.

We could just brute force the solutions, then match them together in
a way that works. Tbh I'm having trouble figuring out how to match that
pattern with code.

Let's look at the solution and move on to the next backtracking problem.

Yea most of these use bit-manipulation of dynamic programming. Good call
to skip it.

I'm very ok with the fact that I didn't get this.

It just happens to be that the stack works.

Let's implement it from scratch to see if we get it.

So make changes 1 bit at a time.

pop element from stack, if not in set, turn to num and add
to ans


'''

def intListToBin(nums):
    for i in range(len(nums)):
        nums[i] = str(bin(nums[i]))[2:]

    return nums

# print(intListToBin([0,1,3,2,6,7,5,4]))
# print(intListToBin([0,1,3,2,6,7,5,4,12,13,15,14,10,11,9,8]))


class Solution:
    def grayCode(self, n):
        if n == 0:
            return [0]

        elif n == 1:
            return [0,1]

        initial = '0'*n
        resp = []
        seen = set()

        stk = [initial]

        while stk:
            node = stk.pop()

            if node not in seen:
                # Add it to answer
                seen.add(node)
                resp.append(int(node,2))

                # Problem states that answer
                # size = 2ⁿ
            if len(resp) == 2**n:
                break

                # We toggle the value
            for i in range(n):
                adj = "1" if node[i] == "0" else "0"
                nwVal = node[:i] + adj + node[i+1:]

                if nwVal not in seen:
                    stk.append(nwVal)

        return resp

if __name__ == '__main__':
    s = Solution()

    print(s.grayCode(4))
