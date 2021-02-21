'''
A full binary tree is when each node
either has 0 or two children.

Let's say that we are at a node, and we
have n nodes to distribute. N must be even.

i = [0,n]

left(n-i)*right(i)

left(n-2)*right(2) + left(n-4)*right(4) + left(n-6)*right(6) + ...

Answer is deterministic. So maintain a cache. Only we don't care
about the count, we actually want the trees.

So how could we get them?

We could still maintain a cache, only it would instead be a cache
that maps to a tree.

There can be multiple trees for every cache value, so list of trees.
And we don't need a deep copy because we can just use it as a subtree.

Have a function called iter, stores n, the current tree.

Doing this top-down wouldn't be very practical, as it would be tedious
to compare all of the trees in the cache in order to figure out if there
are any left.

So iterative is probably the best solution. This way, we know that each
cache is complete before moving on to the next one.

We could move by odd numbers, since every solution will have an odd number
of nodes



'''

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def allPossibleFBT(self, n):
        dp = [[] for _ in range(n+1)]

        dp[1].append(TreeNode(0))

        for i in range(3, n+1, 2):

            # Vary number of nodes on left and on right
            # For every combination, append to dp.

            for k in range(1, i-1, 2):
                # print("For n: {}, left: {}, right: {}".format(i, k, i-1-k))
                # Nodes on left = k
                # Nodes on right = i-k

                for left in dp[k]:
                    for right in dp[i-1-k]:
                        root = TreeNode(0)
                        root.left = left
                        root.right = right
                        dp[i].append(root)

        return dp[n]


if __name__ == '__main__':
    s = Solution()

    print(s.allPossibleFBT(5))
