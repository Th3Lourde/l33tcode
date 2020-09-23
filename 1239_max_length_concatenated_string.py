
'''

Given an array of strings,
we want to create a string s,
which is a concatentaion of a sub-sequence of
arr which have unique characters


Return the max possible length of s.

We have a list of strings, we want to build a bigger
string. This bigger string has unique characters.

For every element, we either have the option of
using it or not using it.

we don't have to pick the elements in order

What if we:
    - convert each element to a character set, "un" --> {'u', 'n'}

One idea I had was to sort by size and then go from there.

The question is:
    - Which one do we start with? How do we decide which way to go?
    if we have two strings of the same length, and we can't add them
    both, which one do we pick?

    I don't think that there is an answer here.



The solution that pops in my head is to try all permutations and see
which one results in the largest set.

It's brute-force, and it is the solution that comes to mind

Loop through options, add opts to chars (if the intersection == {})
if opts == {}, ans = max(ans, len(opts))
itr(chr, opts):
    ...


Run a 'clumping algo', where you group together all of the sets that
don't have any shared terms

Why does this fail?

This failed because our algorithm just tags and bags the first thing
that it has a null intersection for.

We don't want that. What do we want?

What if we instead created compound terms? Don't remove
the terms.

Well if we don't remove, we don't reduce our options, now do we?

hmm. Ok let's look at answer.

["ab","cd","cde","cdef","efg","fgh","abxyz"]

So I got the right answer, my mistake was just in using recursive
calls.

This is a brute force solution. I'm kinda confused on why this is included.

huh

So this is literally the same solution, just tighter and no recursion.

I would say that I got it right, but that I could use some work w.r.t. implementation.

Ok what's next?

Well I've done 20 backtracking problems. That's probably good for now.
Let's learn dp.

Time to burn some cash on educative.io


'''

class Solution:

    def maxLength(self, arr):
        ans = [set()]

        for a in arr:
            if len(a) < len(set(a)): continue

            a = set(a)

            for c in ans[:]:
                if a & c: continue

                ans.append(a | c)

        return max(len(a) for a in ans)









    def maxLength_1(self, arr):
        ans = [0]

        arr.sort(key=len, reverse=True)

        set_arr = []

        for e in arr:
            tmp = set()

            for chr in e:
                tmp.add(chr)

            if len(tmp) == len(e):
                set_arr.append(tmp)

        condensed_arr = []

        i = 0

        while i < len(set_arr):
            term = set_arr[i]

            j = i+1

            while j < len(set_arr):

                if term.intersection(set_arr[j]) == set():
                    term = term.union(set_arr[j])
                    set_arr.remove(set_arr[j])

                j += 1

            condensed_arr.append(term)

            i += 1


        def itr(chrs, opts, ans):

            ans[0] = max(ans[0], len(chrs))

            # check len(opts)
            for i in range(len(opts)):
                opt = opts[i]
                if chrs.intersection(opt) == set():
                    itr(chrs.union(opt), opts[:i]+opts[i+1:], ans)


        for i in range(len(condensed_arr)):
            itr(condensed_arr[i], condensed_arr[:i]+condensed_arr[i+1:], ans)

        return ans[0]


if __name__ == '__main__':
    s = Solution()

    print(s.maxLength(["un", "iq", "ue"]))

    print(s.maxLength(["cha","r","act","ers"]))

    print(s.maxLength(["abcdefghijklmnopqrstuvwxyz"]))

    print(s.maxLength(["yy","bkhwmpbiisbldzknpm"]))


    # ["yy","bkhwmpbiisbldzknpm"]


    # ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]



        # if len() == 1, return len of inputted string
