class Solution:
  def findLeaves(self, root):

    leavesOfBinaryTree = []

    def dfs(node):
      if not node:
        return -1

      level = max(dfs(node.left), dfs(node.right)) + 1

      while level >= len(leavesOfBinaryTree:
        leavesOfBinaryTree.append([])

      leavesOfBinaryTree[level].append(node.val)

      return level

    dfs(root)

    return leavesOfBinaryTree
