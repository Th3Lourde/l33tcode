'''
inp: List[int]
Construct a maximum binary tree

1. the root is the maximum number in the array

2. left subtree is the max tree constructed using
   the elements left of the max term

3. right subtree is the max tree constructed using
   the elements right of the max term

Use a recursive function.

search nums for the largest element
create a node w/that element
.left = funct(leftArray)
.right = funct(rightArray)

return node


'''

class Solution:
    def constructMaximumBinaryTree(self, nums):
        if nums == []: return None

        # 1) find max
        m = [nums[0], 0]

        for i in range(1, len(nums)):
            if nums[i] > m[0]:
                m = [nums[i], i]

        # 2) create node
        node = TreeNode(val=m[0])

        node.left = self.constructMaximumBinaryTree(nums[:m[1]])
        node.right = self.constructMaximumBinaryTree(nums[m[1]+1:])

        return node
