'''
S and T are strings that contain lowercase letters.

S is composed of unique chrs.

S is sorted. Sort the characters in T that are in S.
If there are characters in T not in S, they can be
put anywhere in the resulting permutation.

Idea: go through all elements of T, put them in a dictionary.
We will want to keep track of the elements that we haven't used
and append them later.

Get the keys of the dict.

Step through S. If c ∈ S is in T, append all instances of that
character to our new permutation. Also delete that character from
our dictionary.

When we have seen all elements in S, step through the remaining
elements and add them to our permutation.

"acdbf"
"aaabbbcccdddeeeefff" <-- Some random permutation.
{"a":3, "b":3, "c":3, "d":3, "e":4, "f":3}
keys = [a,b,c,d,e,f]

stepping through S
a, is a ∈ keys?
yes, ans = "aaa"
keys = [b,c,d,e,f]

c, is c ∈ keys?
yes, ans = "aaaccc"
keys = [b,d,e,f]

d, is d ∈ keys?
yes, ans = "aaacccddd"
keys = [b,e,f]

b, is b ∈ keys?
yes, ans = "aaacccdddbbb"
keys = [e,f]

f, is f ∈ keys?
yes, ans = "aaacccdddbbbfff"

keys = [e]

Step through e, append to ans.
ans = "aaacccdddbbbfffeeee"

Test cases: Vary # in S, T, overlap.

Had s,t at zero, not zero, varied
amount of overlap, looks good, let's run it.

'''

class Solution:
    def customSortString(self, S, T):
        d = {}

        for c in T:
            if c in d:
                d[c] += 1

            else:
                d[c] = 1

        ans = ""
        keys = list(d.keys())

        for c in S:
            if c in d:
                keys.remove(c)
                ans = ans + "{}".format(c)*d[c]

        for c in keys:
            ans = ans + "{}".format(c)*d[c]

        return ans

if __name__ == '__main__':
    s = Solution()

    # print(s.customSortString("cba", "aaaabalaadfahdflakjdvdcd"))

    print(s.customSortString("", "aaaabalaadfahdflakjdvdcd"))
    print(s.customSortString("cba", ""))

    print(s.customSortString("bzadc", "aaaababbdbdbdbdbdlaadfahdflakjdvdcd"))
