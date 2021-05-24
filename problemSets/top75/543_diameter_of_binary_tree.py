'''
Length of the longest path between any
two nodes in a tree.

Length of path is represented by the
number of edges between them.

So let's do a dfs on the nodes

Get the longest path going left, longest
path going right, longest diameter seen


            1
        2       3
     4    5

    dfs(1)
        dfs(3) | 0, 0
        dfs(2)
         dfs(4) | 0,0
         dfs(5) | 0,0




node.children
'''

class Solution:
    def diameterOfNaryTree(self, root):

        def dfs(node):
            maxDiam = 0
            maxChildren = 0
            currentDiam = 0

            childrenList = []

            for child in node.children:
                maxDiamChild, childrenOfChild = dfs(child)
                maxDiam = max(maxDiam, maxDiamChild)
                maxChildren = max(maxChildren, childrenOfChild+1)
                childrenList.append(childrenOfChild+1)

            childrenList.sort()

            if len(childrenList) >= 2:
                maxDiam = max(maxDiam, childrenList[-1]+childrenList[-2])

            return maxDiam, maxChildren

        maxDiam, _ = dfs(root)

        return maxDiam

    def diameterOfBinaryTree(self, root):

        def dfs(node):
            maxDiamL,  maxDiamR  = 0,0
            maxChildren = 0

            currentDiam = 0

            if node.left:
                maxDiamL, childrenL = dfs(node.left)
                maxChildren = childrenL+1
                currentDiam += childrenL+1

            if node.right:
                maxDiamR, childrenR = dfs(node.right)
                maxChildren = max(maxChildren, childrenR+1)
                currentDiam += childrenR+1

            return max(maxDiamL, maxDiamR, currentDiam), maxChildren

        maxDiam, _ = dfs(root)

        return maxDiam
