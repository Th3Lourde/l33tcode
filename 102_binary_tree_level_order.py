
class TreeNode():
    def __init__(self, x, l=None, r=None):
        self.val = x
        self.left = l
        self.right = r



class Solution:

    def levelOrder(self, root):
        if root:
            ans = []

        else:
            return []

        stack = [['h','h']]
        ans = []
        lvl = 0
        node = root

        while True:
            if node:
                if node != stack[-1][0]:
                    if len(ans) == lvl:
                        ans.append([])
                    ans[lvl].append(node.val)
                    stack.append([node,lvl])
                    lvl += 1
                    node = node.left

                elif node == stack[-1][0]:
                    lvl = stack[-1][1]
                    stack.pop()
                    lvl += 1
                    node = node.right

            elif not node:
                if stack == [['h','h']]:
                    return ans

                else:
                    node = stack[-1][0]







    # recursive, works
    def levelOrder_1(self, root):
        def itr(node, lvl, ans):
            if node:
                if len(ans) == lvl:
                    ans.append([])
                ans[lvl].append(node.val)
                itr(node.left, lvl+1, ans)
                itr(node.right, lvl+1, ans)

        if root:
            ans = [[root.val]]

        else:
            return []

        itr(root.left, 1, ans)
        itr(root.right, 1, ans)

        return ans


if __name__ == '__main__':
    s = Solution()

    root = TreeNode(3)
    a = TreeNode(9)
    b = TreeNode(20)
    c = TreeNode(15)
    d = TreeNode(7)

    root.left = a
    root.right = b
    b.left = c
    b.right = d

    print(s.levelOrder(root))
