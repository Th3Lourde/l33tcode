'''
There are n soldiers standing in a line. Each soldier is assigned a unique rating value.

You have to form a team of 3 soldiers amongst them under the following rules:

Choose 3 soldiers with index (i, j, k) with rating (rating[i], rating[j], rating[k]).
A team is valid if:  (rating[i] < rating[j] < rating[k]) or (rating[i] > rating[j] > rating[k])
where (0 <= i < j < k < n).

Given a list of integers. Each integer is unique.
Form grouping of elements:
    (i, j, k) ∋ (rating[i] < rating[j] < rating[k]) || (rating[i] > rating[j] > rating[k])
    where (0 ≤ i < j < k < n)

Ok so every element is unique.

We can find all possible groupings that satisfy the first condition, and then check to see
if the indices satisfy the second. If pass both, add to set, return len(set) when done.

Sort Rating.
[2,5,3,4,1] → [1,2,3,4,5]

I am assuming that gaps can exist, [1,2,4,5] is a valid input.
Ok so we have [1,2,3,4,5]

Valid pairings are:
 (1,2,3), (3,2,1), ....

This is giving us a permutation problem, most of the
permutations will fail due to indice values.

Alternate Solution:

Have two pointers, initialized at the edges of the list.
have a third pointer which cycles through all elements
in between the l, r pointer.



[2,5,3,4,1]
^    ^   ^
l    m   r

Once we have exausted all m values, l += 1,
Once we have exausted all m values, r -= 1,
continue until we don't have three elements.

For every pairing, check that
(rating[i] < rating[j] < rating[k]) || (rating[i] > rating[j] > rating[k])

So pairing == (l,m,r)
We will be indexing the tuple for the comparisons.

I don't think that we have a risk of adding repeats, since we only see each
permutation once.

Also each element is unique.

Ok so I am high confidence that we will only see each pairing once.
If a pairing is valid, += 1 to ans.
return ans.

tc: 0(n)
mc: 0(c)

if flip, l += 1
if not flip, r -= 1

adjust l, r
if we adjust l, m = l+1
if we adjust r, m = r-1

then m += || -= 1 until
m == l || r

Ok, so I have not tested all possible values.

pick a left, pick a right, pick an m.
vary r,m
l += 1

I still think that we cannot have/hit duplicates.


            if flip:
                l += 1
                m = l+1

            elif not flip:
                r -= 1
                m = l+1

            flip = not flip

            while m != r:
                pairing = (l, m, r)

                # if (rating[pairing[i]] < rating[j] < rating[k]) || (rating[i] > rating[j] > rating[k])
                if (rating[pairing[0]] < rating[pairing[1]] < rating[pairing[2]]) or (rating[pairing[0]] > rating[pairing[1]] > rating[pairing[2]]):
                    ans += 1

                m += 1

        return ans

ans = number of (i,j,k) s.t. i<j<k

for every i-value, we are picking 2 values from the remaining list.

Ok so I got it right. Didn't get the best time-complexity. Let's look
at the discussion.


'''

class Solution:
    def numTeams(self, rating):
        ans = 0
        l = 0
        r = len(rating)-1

        while l + 2 < len(rating):
            r = len(rating)-1

            while l + 1 != r:
                for m in range(l+1, r):
                    pairing = (l,m,r)

                    if (rating[pairing[0]] < rating[pairing[1]] < rating[pairing[2]]) or (rating[pairing[0]] > rating[pairing[1]] > rating[pairing[2]]):
                        ans += 1

                r -= 1

            l += 1

        return ans












if __name__ == '__main__':
    s = Solution()

    # 3
    print(s.numTeams([2,5,3,4,1]))

    # 0
    print(s.numTeams([2,1,3]))

    # 4
    print(s.numTeams([1,2,3,4]))
