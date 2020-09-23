'''
Brute force solution would be to
iterate through all of the possible
placements of one image on top of the
other image and then simply compute the
overlap.

This would be O(n²).

Something better, might be just to perform
this with all of the 1's.

Or maybe all of the patterns of the ones.

If we have a one, and the patter continues if
we go right, follow the pattern.

I'm pretty sure that this is the right answer.

The trickier part is how to encode movements that
go up/down? Which is to focus on representing scenarios
where we have two options (and we should probably explore both).

Ok so here is the idea.

1) Create two lists that represent the coordinates of all of the
    different 1's in both the A and the B matrix.

If we were going to perform a translation on either matrix, we
would require a distinguishable translation vector in order to
do so.

If we iterate through all of the 1's in A and all of the 1's in B,
We can match a one from A and a one from B via a given translation vector.

For every 1 in A and 1 in B, we calculate the translation vector needed in order
for these two values to overlap.

It will likely be the case that the same translation vector will pop up multiple
times while we are doing this.

It would be nice if we could answer the questions of: For a given translation vector,
how many instances of overlap exist? If we were to create a dict with which we could
keep track how many overlaps exist for a given translation vector, we would be able to
answer the question.



'''



class Solution:
    def largestOverlap(self, A, B):
        A = [(row, col) for row in range(len(A)) for col in range(len(A[0])) if A[row][col] == 1]
        B = [(row, col) for row in range(len(B)) for col in range(len(B[0])) if B[row][col] == 1]

        d = {}

        for a_row, a_col in A:
            for b_row, b_col in B:
                translation_vect = (a_row-b_row, a_col-b_col)

                if translation_vect not in d:
                    d[translation_vect] = 1

                else:
                    d[translation_vect] += 1

        return max(list(d.values()))
