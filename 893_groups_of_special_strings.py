'''
You are given an array A of strings.

A move onto S consists of swapping any two even indexed characters of S, or any two odd indexed characters of S.

Two strings S and T are special-equivalent if after any number of moves onto S, S == T.

For example, S = "zzxy" and T = "xyzz" are special-equivalent because we may make
the moves "zzxy" -> "xzzy" -> "xyzz" that swap S[0] and S[2], then S[1] and S[3].

Now, a group of special-equivalent strings from A is a non-empty subset of A such that:

Every pair of strings in the group are special equivalent, and;

The group is the largest size possible (ie., there isn't a string S not in the group such that S is special
equivalent to every string in the group)

Return the number of groups of special-equivalent strings from A.

--------------------------------------------------------------------------------------------------------------------

So we are given a list of strings.

We define something called a move onto S.

If we perform a move onto S, then we have swapped any two even indexed characters or any two odd indexed characters of S.

So that is what a move is.

If we have two strings: S and T, and we are able to perform moves on them s.t. they are the same, these two strings
are special-equivalent.

The final thing that exists is something called a group of special-equivalent strings.
A group is a set of strings s.t. : Every pair of strings in the group are special equivalent, and the set
is the largest size possible.

Given a list of strings: A, return the number of groups of special equivalent strings.

Ok so how can we do this?

One thing that is nice is that the intersection between groups should be the empty set.

What's one thing that we could do? One thing we could do is:

Create a set so we know whether or not we have a string in the set.

Create/use a UID for each group (via counter). Start at group one, grab the first
string, compute all possible special-equivalent strings, for each of these, check
to see if we have it in our set.

If we have all of the strings, throw them into a set of 'used'.
Even if we don't have all of them, since there is no overlap, once we know that a
string doesn't have a group, we can stop.

Also if we get a string that is a permutation of another string, and the string does not
have a group, we can ignore that string.

So given a string, how can we generate all of the strings that are special-equiv?

Well one thing we can do is reduce the string to a character map for even and odd,
and then generate all of the strings.

How else could we do this?
I am having trouble thinking of a faster way to do it.

Ok so given a string, how could we create the permutation?

throw all of the even chars in a list, all of the odd chars in a list

Have add even, add odd, when we have a full string, add it to our list

Ok so the biggest challenge now is to pass a list that doesn't have a
certain element in it.

tmp makes the copy of our elements


e = ['a', 'c', 'e']
o = ['b', 'd', 'f']

def permute(p, e, o):

    if not e and not o:
        group.append(p)
        return

        # if we are adding an even perm
    elif len(p) % 2 == 0:
        tmp = list(e)

        for i in range(len(tmp)):
            permute(p+c, tmp[:i]+tmp[i+1:], o)


        # if we are adding an odd perm
    else:
        tmp = list(o)

        for i in range(len(tmp)):
            permute(p+c, e, tmp[:i]+tmp[i+1:])


seen = set()

--------------------------------------------------------------------------------
Ok so I kinda made a mistake here.

It turns out, that we only need to group the elements that
represent the same group. In order for a group to count, we
don't actually need all elements of the group to be present,
just all elements in the group in our list.

All groups count.

So still add all perms to seen, however seen will now have
elements that we don't actually have. This still serves our
goal of avoiding double-counting groups.

--------------------------------------------------------------------------------
I probably also should have clarified with my interviewer to see how many elements
I should be expecting in a list. It looks like creating the permutation of all elements
is not a good move.

What could we do differently in order to tell if we have already seen an element?

Well we have that odd, even characteristic which is unique. What is unique is the
elements in them. Not the order.

So given e, o, []str, how can we turn this into something we can query?

two sets won't work, we could have two e, o from different groups that could
give us a false positive (saying we have the groups when we really don't)

We could have an e, o mapping to the group id

e : {set of ids} <-- if the intersection of the even, odd ids is not empty,
then we have already seen this before.

Ok cool.

See element
create e, o mapping for element
if e or o not in dicts, have found new group
if e and o in dicts, and the intersection of the values ≠ ∅:
    have found a new group

else:
    not a new group

if new group, add one to counter
add the e : counter, o : counter to the dicts

for the dicts, e, o are keys, the group # is the id.

+= 1 group number before insertion.

so the keys are lists. We can't hash lists. We can however,
sort the characters, join them, and use those as hashes.

We could also use binary search to insert in a way that results
in a sorted list.

----------------------------------------------------------------------------------------------------
    Ok so I like that I got it right

I don't like how I didn't do a lot of test cases.
I don't like how I initially mis-read the problem.
I like how I wrote out my thinking that that my code matched what I was trying to implement.




'''

class Solution:
    def numSpecialEquivGroups(self, A):
        cntr = 0

        even = {}
        odd = {}

        for a in A:

            e = []
            o = []

            for k in range(len(a)):
                if k % 2 == 0:
                    e.append(a[k])

                elif k % 2 != 0:
                    o.append(a[k])

            e.sort()
            o.sort()

            ek = "".join(e)
            ok = "".join(o)

            if ek not in even or ok not in odd:
                # have found new group
                cntr += 1

                if ek not in even:
                    even[ek] = set({cntr})

                elif ek in even:
                    even[ek].add(cntr)

                if ok not in odd:
                    odd[ok] = set({cntr})

                elif ok in odd:
                    odd[ok].add(cntr)

            elif ek in even and ok in odd:
                if len(even[ek].intersection(odd[ok])) == 0:
                    # have found new group
                    cntr += 1

                    even[ek].add(cntr)

                    odd[ok].add(cntr)

        return cntr


def permute(p, e, o):

    if not e and not o:
        group.add(p)
        return

        # if we are adding an even perm
    elif len(p) % 2 == 0:
        tmp = list(e)

        for i in range(len(tmp)):
            permute(p+tmp[i], tmp[:i]+tmp[i+1:], o)


        # if we are adding an odd perm
    else:
        tmp = list(o)

        for i in range(len(tmp)):
            permute(p+tmp[i], e, tmp[:i]+tmp[i+1:])

if __name__ == '__main__':
    s = Solution()

    # print(s.numSpecialEquivGroups(["abcd","cdab","cbad","xyzz","zzxy","zzyx"]))
    # print(s.numSpecialEquivGroups(["abc","acb","bac","bca","cab","cba"]))
    # print(s.numSpecialEquivGroups(["a","b","c"]))
    # print(s.numSpecialEquivGroups([]))
    # print(s.numSpecialEquivGroups(["a"]))

    '''
    ["fcrokswjnxglmjouwkht","shlgnfbgchiiytgxmamc","hynzlifgupwmwxbrbjdq","wkklgurjncmtfjoshxwo","kogsokwjnjrthlfxwcmu"]
    '''
