'''
Given a binary matrix A, we want to flip the
image horizontally, then invert it, and then
return it.

Reverse the order of the elements in each row
Then, for every element, if 1 put 0, if 0 put
1.

The niave solution is the one with quadratic time.

Is there a better way to do this?

I do not think so.

So loop through the image, for every
row: reverse it, invert it.

reverse, don't use the python shortcut
invert, 0(n)

Ok we did it, and it is way faster than
the other solutions

'''

class Solution:
    def flipAndInvertImage(self, A):

        def reverseBit(val):
            if val == 1:
                return 0

            elif val == 0:
                return 1

        def updateRow(row):
            l = 0
            r = len(row)-1

            while l <= r:

                if l != r:
                    tmp = row[l]
                    row[l] = reverseBit(row[r])
                    row[r] = reverseBit(tmp)

                elif l == r:
                    row[l] = reverseBit(row[l])

                l += 1
                r -= 1

            return row

        for i in range(len(A)):
            A[i] = updateRow(A[i])

        return A


if __name__ == '__main__':
    s = Solution()

    print(s.flipAndInvertImage([[1,1,0],[1,0,1],[0,0,0]]))
    print(s.flipAndInvertImage([[1,1,0,0],[1,0,0,1],[0,1,1,1],[1,0,1,0]]))
