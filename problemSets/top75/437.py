'''
Given the root of a binary tree and an integer targetSum,
return the number of paths where the sum of the values
along the path equals target sum

10 | {10:1}
5  | {10:1, 15:1}
3  | {10:1, 15:1, 18:1}

'''

class Solution:
    def pathSum(self, root, targetSum):
        if not root:
            return 0

        self.ans = 0

        def dfs(node, sumSet, s):
            s += node.val

            if s-targetSum in sumSet:
                self.ans += sumSet[s-targetSum]

            if s in sumSet:
                sumSet[s] += 1
            else:
                sumSet[s] = 1

            if node.left:
                dfs(node.left, dict(sumSet), s)

            if node.right:
                dfs(node.right, dict(sumSet), s)


        dfs(root, {0:1}, 0)
        return self.ans



a = {1:1, 2:2}
type(a)
