'''
Ok so we should get the level
order of the tree.

loop through the nodes
check .left, .right, as soon
as .left or .right is false, toggle bool
continue to traverse, if node has child, return false
else return true
'''

from collections import deque

class Solution:
    def isCompleteTree(self, root):
        levelOrder = []
        q = deque([(root, 1)])

        while q:
            node, level = q.pop()

            if level > len(levelOrder):
                levelOrder.append([node])
            else:
                levelOrder[level-1].append(node)

            if node.left:
                q.appendleft((node.left, level+1))

            if node.right:
                q.appendleft((node.right, level+1))


        # Check that nodes are all to the far left
        for level in levelOrder:
            mustBeEmpty = False

            for node in level:
                if mustBeEmpty and node.left:
                    return False

                if node.left == None:
                    mustBeEmpty = True

                if mustBeEmpty and node.right:
                    return False

                if node.right == None:
                    mustBeEmpty = True


        # Find a level that isn't completely filled
        # if if exists
        # this level should be the last
        # level in the tree
        # if it isn't return False
        for idx,level in enumerate(levelOrder):
            if idx == 0:
                continue

            if len(levelOrder[idx]) < len(levelOrder[idx-1])*2 and idx+1 < len(levelOrder):
                return False

        return True
