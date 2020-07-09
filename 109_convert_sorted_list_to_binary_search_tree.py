

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next next

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

'''
Given a singly linked list, convert it to
a height balanced BST.

1) convert the linked list into a list
2) start from the center and add nodes, left/right

Or, implement an avl tree.

convert to list:
[-10, -3, 0, 5, 9]

Create a function that adds a binary tree to a root node.

[-10, -3, 0, 5, 9]
          ^
       l     r

Create root

add left
add right

How do we deal with duplicates?
Add on a function parameter that varies
how we deal with the equality.

If left and right are equal, call two
different versions of the function to solve.

Even 5,5 is false, maybe we won't get repeat vals?

ok so we don't want to start at the center and branch out.

start from middle, start from end.

[0,1,2,3,4,5]

            3
        1       4
      0   2   3   5

Ok, so middle,

I don't see the pattern, read write-up.

----------------------------------------------------------------------------------
Ok so how can we do this in one pass?

Something to note is that the sorted linked list spells out the inOrder
traversal of our tree.

The root will be the center of the tree

See node value, make tree node, store it.
Based upon the next node value, store it as the .left or
the .right.

If we are at the root node, which is the center of the ll,
We just assign the previous node as left or right and start
fresh.

When we finish the rest of the elements, assign to .right of root
node.

1) Until we find root node
algo

2) find root node, store it

3) Until we hit null
algo

root.right = algo, return root.

            a
        b       c
      d   e   f   g

[d,b,e,a,f,c,g]
 ^
root = None
child = None
t_node = None


t_node = d
child = None ⟹ child = d

[d,b,e,a,f,c,g]
   ^

root = None
child = d
t_node = b

child != None
t_node > child
t_node.left = child
child = b

                        b.left = d

root = None
child = b
t_node = b

[d,b,e,a,f,c,g]
     ^
t_node = e

check if a right exists. If it doesn't, assign
right? But that only works when we have full trees.

If we know the length of the list and the index of
a node, can we find the parents?

Answer is yes (I think).

[-10, -3, 0, 5, 9]

n = 5
mid = n // 2 = 2 (0 index)

What is the address of the left child?

n = 2
left child = 2-1
right child = 2+1

I wonder if this ±1 varies depending on the
length of the linked list.

            a
        b       c
      d   e   f   g

[d,b,e,a,f,c,g]

n = 3
l = 3-2
l = 3+2

Initially, n ± (n-1)

Then, based upon how far away we are
from the root, the number goes down.
To avoid overlapping, we can have a min/max
if we go out of bounds, .left/.right = None

We want to decrease the effect that the bounds has,
add one to 'n'?

So min, max, the left child is the mid distance on the left
the right child is the mid distanc on the right.

Test on bigger tree


              a
         b           c
      d     e     f     g
     h i   j k   l m   n o


[h,d,i,b,j,e,k,a,l,f,m,c,n,g,o]

idxNode = len([]) // 2 ⟹ 15//2 ⩵ 7

left/right = 7 ± (6)

min = 0
max = 14
n = 7

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



----------------------------------------------------------------------------------
So turns out the fastest way to do this is just to convert the
linked list to an array and go from there


'''

class Solution:

    def sortedListToBST(self, head):
        # 1) Convert to array
        arr = []

        node = head

        while node:
            arr.append(node.val)
            node = node.next

        # 2) Create BST
        def helper(arr):
            if not arr: return None

            m = len(arr)//2

            node = TreeNode(arr[m])
            node.left = helper(arr[:m])
            node.right = helper(arr[m+1:])

            return node

        return helper(arr)



    def sortedListToBST_1(self, head, swap=False): # Doesn't work

        if not head: return None

        arr = []

        node = head

        while node:
            arr.append(node.val)
            node = node.next

        n = len(arr)

        def insert(node, val, swap):
            # Find node to assign val to.
            while True:
                # not sure if vals are unique
                # or how to handle when they are not

                if node.val == val:
                    if swap:
                        # go left
                        if not node.left:
                            node.left = TreeNode(val)
                            return
                        node = node.left

                    elif not swap:
                        # go right
                        if not node.right:
                            node.right = TreeNode(val)
                            return

                        node = node.right

                elif node.val > val:
                    # go left
                    if not node.left:
                        node.left = TreeNode(val)
                        return
                    node = node.left

                elif node.val < val:
                    # go right
                    if not node.right:
                        node.right = TreeNode(val)
                        return

                    node = node.right

        root = TreeNode(arr[n//2])

        l = n//2 - 1
        r = n-1
        swap = True

        while l > 0 or r > n//2:

            if l > -1 and r < len(arr) and arr[l] == arr[r]:
                insert(root, arr[l], swap)
                insert(root, arr[r], not swap)
                l -= 1
                r -= 1
                swap = not swap
                continue

            if l > 0:
                insert(root, arr[l], swap)

                l -= 1

            if r < len(arr):
                insert(root, arr[r], swap)
                r -= 1

        return root
