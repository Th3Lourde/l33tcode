class TreeNode:
    def __init__(self, x, l=None, r=None):
        self.val = x
        self.left = l
        self.right = r


class Solution:
    def diameterOfBinaryTree(self, root):
        self.ans = 1
        def depth(node):
            if not node: return 0
            L = depth(node.left)
            R = depth(node.right)
            self.ans = max(self.ans, L+R+1)
            return max(L, R) + 1

        depth(root)
        return self.ans-1





# Refactor Code
class Solution_2:

    def diameterOfBinaryTree(self, root):

        def get_h(node, h):
            if node:
                return max(get_h(node.left, h+1), get_h(node.right, h+1))

            else:
                if h == 0:
                    return 0

                else:
                    return h-1


        def itr(node, d):

            if node:
                current = get_h(node.left, 1) + get_h(node.right, 1)
                d = max(d, current)
                return max(d, itr(node.left, d), itr(node.right, d))

            else:
                return 0

        if not root:
            return 0

        return itr(root, 0)

class Solution_1:
    def get_h(self, node, h):
        if node:
            return max(self.get_h(node.left, h+1), self.get_h(node.right, h+1))

        else:
            if h == 0:
                return 0

            else:
                return h-1

    def itr(self, node, d):

        if node:
            current = self.get_h(node.left, 1) + self.get_h(node.right, 1)
            d = max(d, current)

            return max(d, self.itr(node.left, d), self.itr(node.right, d))

        else:
            return 0


    def diameterOfBinaryTree(self, root):
        if not root:
            return 0

        return self.itr(root, 0)






if __name__ == '__main__':
    s = Solution()

    root =  TreeNode(1)
    a =  TreeNode(2)
    b =  TreeNode(3)
    root.left = a
    root.right = b

    c =  TreeNode(4)
    d =  TreeNode(5)
    a.left = c
    a.right = d

    # print(s.get_h(root, 0))

    print(s.diameterOfBinaryTree(root))
