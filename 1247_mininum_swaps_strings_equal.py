'''
So we are given two strings: s1, s2:

We want to make s1 and s2 the same string.

We can do this by taking an element in s1 and another in s2
and switching them.

This switch is called a swap. Given two strings, how many
swaps do we need to do in order for them to be equal?

if they can't be equal, return -1

Ok so create a dictionary for both,
key : character
value : index?

If the values of each respective key doesn't match, no can do.

s1 = "xx", s2 = "yy"

d1 = {"x": [0, 1]}
d2 = {"y": [0, 1]}

Attempt to make s1 look like s2.

xx
^

yy
^

x != y

is there an extra y in s2 whose index > ^?
yes <-- perform binary search on the second ^,
look right.

swap the elements.

d1 = {"x": [1], "y": [0]}
d2 = {"y": [0], "x": [1]}

really what we want, is to have the length
of every key to be equal in both dictionaries

Figure out the elements that s1 needs
Figure out the elements that s2 needs

if the elements don't exist, return -1

The number of elements needed should be equal.
return num s1 or num s2 needs.

s1N is the number of elements in s2 that we
want to take and put into s1.

s2N is the number of elements in s1 that we
want to take and put into s2.

d1 = {"x": [0, 1]}
d2 = {"y": [0, 1]}

# Figure out how many elements s1 needs

loop through the keys of d2,

number of "y"s that we need = (d1["y"] - d2["y"])/2

s1N = 0

for k in keys: <-- of d2

    have = 0

    if k in d1:
        have = d1[k]

    terms = max( (d2[k] - have)/2, 0 )

    if int(terms) != terms:
        return -1 # happens when odd # of elements


    s1N += (d2[k] - have)/2

# Do the same thing for other dict


if s1N != s2N:
    return -1

return s1N



d1 = {"x": [0, 1]}



d2 = {"y": [0, 1]}

y not in d1, s1N = 1
x not in d2, s2N = 1

y == x
return 1

Ok so this won't work b/c order matters

Or, maybe we do this first (to figure out)
how many are needed, then we can figure out
how many swaps we need for them to be equal?

I'm not really sure how we can bridge this second gap.

Ok I actually do know how to bridge the gap.

Instead of going through the keys, what if we cycle
through the elements?

This would allow us to know what elements are in vs. out of
place.

This problem is a bloody mess (right now).

Switch tasks, take a break. Eat. Come back.

Ok let's finish this problem then write out routines and such.

I think that it is safe to assume that we are only going to be
switching characters that are not the same.

Create a list of characters that represent what is different for
each string.

wowwww. I completely misread it. The string contains x and y only.


"xxyyxyxyxx"

"xyyxyxxxyx"

x x y y x y x y x x

x y y x y x x x y x

-------------------
Removing characters that are the same

x y x y y x

y x y x x y

Problem goes like this:
split both strings into lists
step through them, if the characters
match, keep going.

If the characters don't match:
Find the character in the second string
that we need, flip it.

x x y y x y x y x x
^
x y y x y x x x y x
^

x x y y x y x y x x
  ^
x y y x y x x x y x
  ^     '
Not equal, find something in s2 that
does not have a match in s1, swap.

s = 1

x y y y x y x y x x
  ^
x y y x x x x x y x
  ^

s = 1

x y y y x y x y x x
      ^
x y y x x x x x y x
      ^   '

s = 2

x y y x x y x y x x
      ^
x y y x x y x x y x
      ^

s = 2

x y y x x y x y x x
              ^
x y y x x y x x y x
              ^ '

s = 3

x y y x x y x y x x
              ^
x y y x x y x x y x
              ^ '

In that case, count the number of times
each side has a mis-match. If the number
of times is equal, return times/2.

Ok so we have run into a situation where
we don't have something ideal but we still
need to make a swap.

So that means that we have three situations
that can occur:
 1) We find the character at a mis-match
 2) We can only find the character at a match
 3) We can't find the character

So loop through until we find case 1) or until
we run out of room

If we run out of room, and we have case 2, use
case 2 (record the first-instance of case 2).

If we are at case 3, return False

So there is a different case 3, just swapping the
elements. So case three, switch them.

Have a boolean that tells us whether or not we have
already done this once.


Let's model the swap for our purposes. I'm sure
that there are times when we won't actually need to.

"xy"
"yx" <-- Case three

"yy"
"xx"

"xy"
"xy"

So what is currently wrong is our target. Our target could be two
things.

Come back to this tomorrow.

Ok so I looked at the LC discussion, very helpful. Here is how someone
solved it:

There are two cases that we worry about: even mismatches, odd
mismatches. Odd mismatches look like the following:

x
y

or

y
x

we see, xy, put it in our set.
we see yx, check to see if it is in our set, if it is, add one
to counter.

The other sequences are "evens"

e.g.

xy
   ⟹  (x,y), (y,x)
yx

These sequences take two swaps in order to be resolved.
It follows that we try to resolve even sequences after
we have already resolved odd sequences.

Since we know an even sequence is even when if is not odd.
We know the sequence can be resolved if it occurs twice in
our set ← although they occur in a different order.

It is also worth noting that there exists a bound on the number
of even sequences that we can have.

The sequence below gives us trouble because ∄ a y in the bottom
row that can switch with the x. However if we were to increase
the frequency of any of the two sequences, we would create an odd
sequnce that could be resolved.

xy
yx

Thus is an even sequence can be resolved the element that can resolve
it occurs at most once.

How to handle odd sequences

sequences = set()
swaps = 0

for c1, c2 in zip(s1, s2):
    if c1 != c2: # not a match
        if (c1, c2) in sequences:
            sequences.remove((c1, c2))
            swaps += 1

        else: sequences.add((c1, c2))

# if we have anything left in sequences,
# we either have proof that we cannot make
# the strings equal, or we have an even
# sequence that needs to get resolved.

visited = set()

for seq in sequences:
    if (seq[1], seq[0]) not in sequences:
        return -1

    if (seq[1], seq[0]) not in visited:
        swaps += 2
        visited.add(seq)


return swaps



Sick got it, yea that is a pretty kick-ass solution.




'''

class Solution:

    def minimumSwap(self, s1, s2):
        sequences = set()
        swaps = 0

        for c1, c2 in zip(s1, s2):
            if c1 != c2: # not a match
                if (c1, c2) in sequences:
                    sequences.remove((c1, c2))
                    swaps += 1

                else: sequences.add((c1, c2))

        # if we have anything left in sequences,
        # we either have proof that we cannot make
        # the strings equal, or we have an even
        # sequence that needs to get resolved.

        visited = set()

        for seq in sequences:
            if (seq[1], seq[0]) not in sequences:
                return -1

            if (seq[1], seq[0]) not in visited:
                swaps += 2
                visited.add(seq)


        return swaps



    def minimumSwap_1(self, s1, s2): # Answer that I never figured out

        s1 = list(s1)
        s2 = list(s2)

        swaps = 0
        i = 0
        haveSwapped = False

        while i < len(s1):
            if s1[i] == s2[i]:
                # do nothing
                i += 1

            elif s1[i] != s2[i]:
                case1 = None
                case2 = None

                for k in range(i+1, len(s2)):
                    if s2[k] == s2[i] and s1[k] != s2[k]:
                        # case one
                        case1 = k
                        break

                    elif s2[k] == s2[i] and s1[k] == s2[k] and case2 == None:
                        # case two
                        case2 = k

                if case1 == None and case2 == None and haveSwapped == False:
                    tmp = s1[i]
                    s1[i] = s2[i]
                    s2[i] = tmp
                    print(s1)
                    print(s2)
                    haveSwapped = True

                elif case1 == None and case2 == None and haveSwapped == True:
                    return -1

                elif case1 != None:
                    # do case 1
                    tmp = s1[i]
                    s1[i] = s2[case1]
                    s2[case1] = tmp

                    haveSwapped = False
                    swaps += 1

                elif case2 != None:
                    # do case 2
                    tmp = s1[i]
                    s1[i] = s2[case2]
                    s2[case2] = tmp

                    haveSwapped = False
                    swaps += 1

                i += 1

        return swaps


if __name__ == '__main__':
    s = Solution()

    # print(s.minimumSwap("xx", "yy"))
    print(s.minimumSwap("xy", "yx"))
