'''
Return the diameter of the tree.

the diameter of the binary tree is the length of the longest
path between any two nodes in the tree. This path may or may
not pass through the root node

longestPathIfNodeIsRoot, longestChildPath = dfs(node)

            1
         2     3
       4  5

4, 3 = dfs(1)
    3,2 = dfs(2)
        1,1 = dfs(4)
        1,1 = dfs(5)
    1,1 = dfs(3)

'''

class Solution:
    def diameterOfBinaryTree(self, root):
        def dfs(node):
            if not node:
                return 0, 0

            maxHeightLeft, childLeft = dfs(node.left)
            maxHeightRight, childRight = dfs(node.right)

            return max(maxHeightLeft, maxHeightRight, childLeft+childRight+1), max(childLeft, childRight)+1


        ans, _ =  dfs(root)
        return ans-1
