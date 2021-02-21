'''
Given an array of positive integers, consider all binary
trees ∋:
    - Each node has zero or two children
    - Moving through the array l → r mirrors the in-order traversal of the leafs of the tree
    - The value of each non-leaf node is equal to the product of the largest leaf value in
    its left and right subtree respectively.

Among all possible trees, return the smallest possible sum of the values of each non-leaf node.

So bruteforce is the way to go.

So the order is pre-determined. The only thing you determine is the height of the different trees

So for each node you decide either to pair the two nodes together or to not pair them together.
'''

class Solution:
    def mctFromLeafValues(self, arr):
        ans = 0

        while len(arr) > 1:
            i = arr.index(min(arr))
            ans += min(arr[i-1:i]+arr[i+1:i+2])*arr.pop(i)

        return ans
