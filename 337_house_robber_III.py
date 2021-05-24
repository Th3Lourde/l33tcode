'''
(now, later)


Redefine the problem in terms of this.

So we have this root.
Scenario 1, don't rob root
Scenario 2, rob root

if not node:
    return (0,0)




'''



class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # too slow
    def rob_1(self, root):
        def itr(dp, node):
            if not node:
                return 0

            if node in dp:
                return dp[node]

            hitRoot = node.val

            if node.left:
                hitRoot += itr(dp, node.left.left)
                hitRoot += itr(dp, node.left.right)

            if node.right:
                hitRoot += itr(dp, node.right.left)
                hitRoot += itr(dp, node.right.right)

            noRoot = itr(dp, node.left) + itr(dp, node.right)

            dp[node] = max(hitRoot, noRoot)

            return dp[node]

        return itr({}, root)

    def rob(self, root):

        # (robRoot, dontRobRoot)
        def itr(node):
            if not node:
                return (0,0)

            l = itr(node.left)
            r = itr(node.right)

            rob = node.val + l[1] + r[1]

            skip = max(l) + max(r)

            return (rob, skip)

        return max(itr(root))




if __name__ == '__main__':
    s = Solution()
    ...
