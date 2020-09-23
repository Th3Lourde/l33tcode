'''
Given an n-ary tree, return the level order traversal


Ok, so this isn't too bad.

It's level order, each node is a list [level, node]

Ans is a list of lists. Every time we hit a node that we haven't
seen yet, we add its level to the list (if the level is 'new'), and
then append the children to our list.

So the children are just a list of nodes.

ans = []

[[0, 1]]

[0, 1]

(len(ans) == 0) <= (node[0] == 0):
    ans.append([node[1].val]) → ans = [[1]]

q = [

    [1, (3)],
    [1, (2)],
    [1, (4)],

]

'''


class Solution:
    def levelOrder(self, root):

        if not root: return []

        ans = []

        q = [[0, root]]

        while q:
            node = q.pop()

            # Can we have empty nodes? Let's say no.
            if len(ans) <= node[0]:
                ans.append([node[1].val])

            elif len(ans) > node[0]:
                ans[node[0]].append(node[1].val)

                # Assuming that this only executes when ∃ children
            for child in node[1].children:
                q.insert(0, [node[0]+1, child])

        return ans

if __name__ == '__main__':
    s = Solution()
