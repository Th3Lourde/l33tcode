
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def inorderTraversal_recursive(self, root):

        if root == None:
            return []

        return self.recursiveHelper(root, [])


    def recursiveHelper(self, root, ans):

        if root.left != None and root.right != None:
            ans = self.recursiveHelper(root.left, ans)
            ans.append(root.val)
            return self.recursiveHelper(root.right, ans)

        elif root.left == None and root.right != None:
            ans.append(root.val)
            return self.recursiveHelper(root.right, ans)

        elif root.left != None and root.right == None:
            ans = self.recursiveHelper(root.left, ans)
            ans.append(root.val)
            return ans

        elif root.left == None and root.right == None:
            ans.append(root.val)
            return ans

    # This is the iterative way of doing it
    def inorderTraversal(self, root):
        if root == None:
            return []

        stack = [root]
        ans = []
        current_node = root

        if current_node.left != None:
            current_node = current_node.left

        while len(stack) != 0:
            # print("At Node: {}".format(current_node.val))

            if current_node.left != None and stack[-1] != current_node:
                # Add node to stack, to ans
                stack.append(current_node)
                # ans.append(current_node.val)

                # Go left
                current_node = current_node.left

            elif current_node.right != None:
                # if stack[-1] != current_node:
                #     # Add node to stack
                #     # Remove 1
                #     stack.append(current_node)
                #     ans.append(current_node.val)

                ans.append(current_node.val)

                # Won't be coming back to this node
                # Remove 2
                stack.pop()

                # Or don't
                current_node = current_node.right


            elif current_node.left == None and current_node.right == None:
                # print("hi")

                # if stack[-1] != current_node:
                #     ans.append(current_node.val)

                ans.append(current_node.val)


                if stack != []:
                    current_node = stack[-1]

                elif stack == []:
                    return ans

            print("At Node: {}".format(current_node.val))

        return ans

    def inorderTraversal_1(self, root):
        if root == None:
            return []

        stack = [root]
        ans = []
        current_node = root

        if current_node.left != None:
            current_node = current_node.left

        while len(stack) != 0:
            # print("At Node: {}".format(current_node.val))

            if current_node.left != None and stack[-1] != current_node:
                # Add node to stack, to ans
                stack.append(current_node)
                # ans.append(current_node.val)

                # Go left
                current_node = current_node.left

            elif current_node.right != None:
                # if stack[-1] != current_node:
                #     # Add node to stack
                #     # Remove 1
                #     stack.append(current_node)
                #     ans.append(current_node.val)

                ans.append(current_node.val)

                # Won't be coming back to this node
                # Remove 2
                stack.pop()

                # Or don't
                current_node = current_node.right


            elif current_node.left == None and current_node.right == None:
                # print("hi")

                # if stack[-1] != current_node:
                #     ans.append(current_node.val)

                ans.append(current_node.val)


                if stack != []:
                    current_node = stack[-1]

                elif stack == []:
                    return ans

            print("At Node: {}".format(current_node.val))

        return ans




            # if stack[-1] != current_node:
            #     stack.append(current_node)
            #     ans.append(current_node.val)
            #
            #     if current_node.left != None:
            #         current_node = current_node.left
            #
            #     elif current_node.left == None and current_node.right != None:
            #         stack.pop()
            #         current_node = current_node.right
            #
            #     elif current_node.left == None and current_node.right == None:
            #         stack.pop()
            #
            #         if stack != []:
            #             current_node = stack[-1]
            #
            #         elif stack == []:
            #             return ans
            #
            # elif stack[-1] == current_node:
            #     stack.pop()
            #
            #     if current_node.right != None:
            #         current_node = current_node.right
            #
            #     elif current_node.right == None:
            #
            #         if stack != []:
            #             current_node = stack[-1]
            #
            #         elif stack == []:
            #             return ans













if __name__ == '__main__':
    root = TreeNode(4)
    a = TreeNode(2)
    b = TreeNode(3)
    c = TreeNode(1)

    d = TreeNode(5)
    e = TreeNode(6)
    f = TreeNode(7)

    b.left = c
    b.right = a
    root.left = b

    e.left = d
    e.right = f
    root.right = e

    '''
            4
        3       6
      1   2   5   7
    '''



    # nodes = [root,a,b,c,d,e,f]
    #
    # for node in nodes:
    #     print(node.val)



    s = Solution()
    print(s.inorderTraversal_recursive(root))
    print(s.inorderTraversal(root))
