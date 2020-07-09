'''
[h,d,i,b,j,e,k,a,l,f,m,c,n,g,o]
               ^
f(a) --> (b,c)
f(7) --> (3,11)

given n:
    left child is n // 2
    right child is n + n // 2

I guess that I have really solved the
array problem and not the linked list problem.
Let's solve the array problem first.

given arr[in], n, min, max
    if n < min or n > max: return None

    node = TreeNode(ar[n])
    node.left = func(arr, n//2)
    node.right = func(arr, n + n//2)
    return node

get lo, hi, midddle

Ok so lo, hi changes as we go left, right

----------------------------------------------------------------------------------

[h,d,i,b,j,e,k,a,l,f,m,c,n,g,o]

n = 7
lo = 0
hi = 14

f(7, 0, 14)
n = 7
lo = 3
hi = 10

call f(3, 0, 7)
call f(10, 7, 14)

f(3, 0, 7)
call f(1, 0, 3)
call f(4, 3, 7)

f(1, 0, 3)

So there's a sticking point, the function never hits 2.
What if we do 1 index instead of 0?

[None, h,d,i,b,j,e,k,a,l,f,m,c,n,g,o]

n = 7
lo = 1
hi = 16 - 1 15

call f(7, 1, 15)

f(7, 1, 15)
call f(3, 1, 7)   [finished]
call f(10, 7, 15) [finished]

f(3, 1, 7)
call f(1, 1, 3) [stops]
call f(4, 3, 7) [finished]

f(4, 3, 7)
call f(2, 3, 4) [stops]
call f(6, 4, 7) [finished]

f(6, 4, 7)
call f(3...) [stops]
call f(9...) [stops]

Ok so I went through the left subtree. Let's now
go through the right subtree.

f(10, 7, 15)
call f(5)    [stops]
call f(15)   [stops]

So it isn't moving through the rhs of the tree correctly.
What could I do to try and solve this?

Let's try using lo + n//2 instead of just n//2
Run your recursive code (only printing n), to see
if it spans everything

Ok so it was just the mid of everything. The answer is just
to pass subarray after subarray to the function, always finding
the mid.

Let's see if we can't find an iterative solution instead of the
recursive one.

'''

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:

    def sortedArrayToBST_i(self, nums): # iterative solution was complicated
        ...


    def sortedArrayToBST(self, nums): # Works
        if not nums:
            return None

        mid = len(nums)//2

        node = TreeNode(nums[mid])

        node.left = self.sortedArrayToBST(nums[:mid])
        node.right = self.sortedArrayToBST(nums[mid+1:])

        return node



    def sortedArrayToBST_1(self, nums): # My attempt, doesn't work.
        if not nums: return None

        def createBST(arr, n, lo, hi):
            if n <= lo or n >= hi:
                print(n)
                return
                # return TreeNode(arr[n])
            print(arr[n])
            # node = TreeNode(arr[n])
            # node.left = createBST(arr, n//2, lo, n)
            # node.right = createBST(arr, n + n//2, n, hi)

            createBST(arr, n - n//2, lo, n)
            createBST(arr, n + (hi-n)//2, n, hi)
            # createBST(arr, n + n//2, n, hi)
            # return node

        lo = 0
        hi = len(nums)-1

        # nums =  [None] + nums

        n = hi // 2

        return createBST(nums, n, lo, hi)

if __name__ == '__main__':
    arr = [i for i in range(10)]
    arr

    s = Solution()
    s.sortedArrayToBST(arr)
