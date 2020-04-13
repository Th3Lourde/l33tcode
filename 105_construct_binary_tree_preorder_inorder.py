
'''
Test cases:
[3,9,20,15,7] <--- preorder
[9,3,15,20,7] <--- inorder

[1,2,4,5,3,6,7]
[4,2,5,1,6,3,7]

[1,2,4,5]
[4,2,5,1]

[1,3,6,7]
[1,6,3,7]





'''

class Solution:

    class TreeNode:
        def __init__(self, x):
            self.val = x
            self.left = None
            self.right = None

    def buildTree(self, preorder, inorder):
        # We stop when yellow backtracks to the root
        # node for a second time.

        if len(preorder) == 0: # If no tree return None
            return None

        # In the case that we only have one node:
        if len(preorder) == 1: # If one node, return that one node
            return TreeNode(preorder[0])

        # 1) Get the root/initialize variables

        nodes = {}
        for val in preorder:
            nodes[val] = False

        root = TreeNode(preorder[0])
        current = root
        nodes[root.val] = root
        yellow = 0
        red = 0

        hits = 0

        while hits <= 1:

            while inorder[yellow] != root.val:

                while preorder[red] != inorder[yellow]:
                    red += 1
                    current.left = TreeNode(preorder[red])
                    nodes[preorder[red]] = current.left
                    current = current.left

                # Have finished building out the initial left subtree
                # find element of inorder that does not already exist

                # Backtracking
                yellow += 1

                if not nodes[inorder[yellow]]: # If this works, we have found our new node
                    current = nodes[inorder[yellow-1]]
                    red += 1
                    current.right = TreeNode(preorder[red])
                    nodes[preorder[red]] = current.right
                    current = current.right
                    # yellow += 1 # Set new outer bound

            yellow += 1
            red += 1
            current = root
            hits += 1

            if hits > 1:
                return root

            # Building right:
            while preorder[red] == inorder[yellow]: # Building right
                current.right = TreeNode(preorder[red])
                nodes[preorder[red]] = current.right
                current = current.right
                yellow += 1
                red += 1

        return root


    def buildTree1(self, preorder, inorder):

        if len(preorder) == 0: # If no tree return None
            return None

        # In the case that we only have one node:
        if len(preorder) == 1: # If one node, return that one node
            return TreeNode(preorder[0])

        # 1) Get the root/initialize variables

        nodes = {}
        for val in preorder:
            nodes[val] = False

        root = TreeNode(preorder[0])
        current = root
        nodes[root.val] = root
        yellow = 0
        red = 0

        '''
        What if red, yellow run out of bounds?
        Write function to add to red/yellow.
            * Which one will run out of room first?
            * If we run out of room, return root?
        '''

        # 2) Build the left subtree
        while inorder[yellow] != root.val:

            while preorder[red] != inorder[yellow]:
                red += 1
                current.left = TreeNode(preorder[red])
                nodes[preorder[red]] = current.left
                current = current.left

            # Have finished building out the initial left subtree
            # find element of inorder that does not already exist

            # Backtracking
            yellow += 1

            if not nodes[inorder[yellow]]: # If this works, we have found our new node
                current = nodes[inorder[yellow-1]]
                red += 1
                current.right = TreeNode(preorder[red])
                nodes[preorder[red]] = current.right
                current = current.right
                # yellow += 1 # Set new outer bound

        # 3) Build the right subtree
        # Either we build right for a bit or immediately go left
        yellow += 1
        red += 1
        current = root

        # Building right:
        while preorder[red] == inorder[yellow]: # Building right
            current.right = TreeNode(preorder[red])
            nodes[preorder[red]] = current.right
            current = current.right
            yellow += 1
            red += 1

        # Building left again:
        current.right = TreeNode(preorder[red])
        nodes[preorder[red]] = current.right
        current = current.right

        # While we still have nodes?

        while preorder[red] != inorder[yellow]:
            red += 1
            current.left = TreeNode(preorder[red])
            nodes[preorder[red]] = current.left
            current = current.left

        # Have finished building out the initial left subtree
        # find element of inorder that does not already exist

        # Backtracking
        yellow += 1

        if not nodes[inorder[yellow]]: # If this works, we have found our new node
            current = nodes[inorder[yellow-1]]
            red += 1
            current.right = TreeNode(preorder[red])
            nodes[preorder[red]] = current.right
            current = current.right

        return root # ?

if __name__ == '__main__':
    s = Solution()


    testCases = [
        [[3,9,20,15,7], [9,3,15,20,7], True]
    ]

    passed = True
    z = 1

    for testCase in testCases:
        resp = s.buildTree(testCase[0], testCase[1])

        if resp != testCase[2]:
            passed = False
            print("[failed test case {}] wanted {} got {}".format(z, testCase[1], resp))
            break

        z += 1

    if passed:
        print("[passed all test cases] :)")



'''
Tmp code in case I screw up the other implementation:
'''

# # Definition for a binary tree node.
# # class TreeNode:
# #     def __init__(self, x):
# #         self.val = x
# #         self.left = None
# #         self.right = None
#
# class Solution:
#     def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
#         # We stop when yellow backtracks to the root
#         # node for a second time.
#
#         if len(preorder) == 0: # If no tree return None
#             return None
#
#         # In the case that we only have one node:
#         if len(preorder) == 1: # If one node, return that one node
#             return TreeNode(preorder[0])
#
#         # 1) Get the root/initialize variables
#
#         nodes = {}
#         for val in preorder:
#             nodes[val] = False
#
#         root = TreeNode(preorder[0])
#         current = root
#         nodes[root.val] = root
#         yellow = 0
#         red = 0
#
#         hits = 0
#
#         while hits <= 1:
#
#             while inorder[yellow] != root.val:
#
#                 # print("Before while red: {}".format(red))
#
#                 print("red: {} yellow: {} root: \n{}".format(red, yellow, root))
#
#                 while preorder[red] != inorder[yellow]:
#                     red += 1
#                     current.left = TreeNode(preorder[red])
#                     nodes[preorder[red]] = current.left
#                     current = current.left
#
#                 # Have finished building out the initial left subtree
#                 # find element of inorder that does not already exist
#
#                 print("[pre-backtracking] yellow : {}".format(yellow))
#
#
#
#                 # Backtracking
#                 yellow += 1
#
#                 print("[post-backtracking] yellow : {}".format(yellow))
#
#                 if not nodes[inorder[yellow]]: # If this works, we have found our new node
#                     current = nodes[inorder[yellow-1]]
#                     red += 1
#                     current.right = TreeNode(preorder[red])
#                     nodes[preorder[red]] = current.right
#                     current = current.right
#                     # yellow += 1 # Set new outer bound
#
#             yellow += 1
#             red += 1
#             current = root
#             hits += 1
#
#
#             if hits > 1:
#                 return root
#
#             if preorder[red] == inorder[yellow]:
#                 # Building right:
#                 while preorder[red] == inorder[yellow]: # Building right
#                     current.right = TreeNode(preorder[red])
#                     nodes[preorder[red]] = current.right
#                     current = current.right
#                     yellow += 1
#                     red += 1
#
#                 print("yellow: {}".format(yellow))
#                 red -= 1
#
#             elif preorder[red] != inorder[yellow]:
#                 current.right = TreeNode(preorder[red])
#
#                 nodes[preorder[red]] = current.right
#                 current = current.right
#
#
#             print("[to top] red: {} yellow: {} tree: {}".format(red, yellow, root))
#
#
#         return root


'''
tmp2 in case I mess up II
'''

# # Definition for a binary tree node.
# # class TreeNode:
# #     def __init__(self, x):
# #         self.val = x
# #         self.left = None
# #         self.right = None
#
# class Solution:
#     def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
#         # We stop when yellow backtracks to the root
#         # node for a second time.
#
#         if len(preorder) == 0: # If no tree return None
#             return None
#
#         # In the case that we only have one node:
#         if len(preorder) == 1: # If one node, return that one node
#             return TreeNode(preorder[0])
#
#         # 1) Get the root/initialize variables
#
#         nodes = {}
#         for val in preorder:
#             nodes[val] = False
#
#         root = TreeNode(preorder[0])
#         current = root
#         nodes[root.val] = root
#         size = 1
#         yellow = 0
#         red = 0
#
#         hits = 0
#
#         while hits <= 1:
#
#             while inorder[yellow] != root.val:
#
#                 # print("Before while red: {}".format(red))
#
#                 # print("red: {} yellow: {} root: \n{}".format(red, yellow, root))
#
#                 if hits == 1:
#                     print("\n{}\n".format(list(nodes.keys())))
#
#                 while preorder[red] != inorder[yellow]:
#                     red += 1
#                     current.left = TreeNode(preorder[red])
#                     nodes[preorder[red]] = current.left
#
#
#                     current = current.left
#
#                     size += 1
#                     print("[A] red: {}  yellow: {} size: {} root: {}".format(red, yellow, size, root))
#
#                     if size >= len(preorder):
#                         print("[A] root: {}".format(root))
#                         return root
#
#
#                 # print("root {}\n".format(root))
#
#                 # Have finished building out the initial left subtree
#                 # find element of inorder that does not already exist
#
#                 # print("[pre-backtracking] nodes: {}\n".format(nodes))
#
#                 # print("[pre-backtracking] yellow : {}".format(yellow))
#
#
#                 yellow += 1
#
#                 while nodes[inorder[yellow]] != False and inorder[yellow] != root.val and size < len(preorder)-1:
#                     # Backtracking
#                     yellow += 1
#
#                 # print("[post-backtracking] yellow : {}".format(yellow))
#
#                 if nodes[inorder[yellow]] == False: # If this works, we have found our new node
#                     current = nodes[inorder[yellow-1]]
#                     red += 1
#                     current.right = TreeNode(preorder[red])
#                     nodes[preorder[red]] = current.right
#
#                     current = current.right
#
#                     size += 1
#                     print("[B] root: {}".format(root))
#
#                     if size >= len(preorder):
#                         print("B")
#                         return root
#                     # yellow += 1 # Set new outer bound
#
#             yellow += 1
#             red += 1
#             current = root
#             hits += 1
#
#             if hits > 1 or size >= len(preorder):
#                 return root
#
#             if preorder[red] == inorder[yellow]:
#                 # print("[A]")
#                 # Building right:
#                 while preorder[red] == inorder[yellow]: # Building right
#                     current.right = TreeNode(preorder[red])
#                     nodes[preorder[red]] = current.right
#
#                     current = current.right
#                     yellow += 1
#                     red += 1
#
#                     size += 1
#                     print("[C] root: {}".format(root))
#
#                     if size >= len(preorder):
#                         print("C")
#                         return root
#
#                 # print("yellow: {}".format(yellow))
#                 red -= 1
#
#             elif preorder[red] != inorder[yellow]:
#                 # print("[B] preorder[red] {}".format(preorder[red]))
#                 current.right = TreeNode(preorder[red])
#
#                 nodes[preorder[red]] = current.right
#
#
#                 current = current.right
#
#                 size += 1
#
#                 print("[D] root: {}".format(root))
#
#                 if size >= len(preorder):
#                     print("D")
#                     return root
#
#
#             # print("[to top] red: {} yellow: {} current: {} tree: {}\n".format(red, yellow, current, root))
#
#             # print("[to top II] nodes: {}".format(nodes))
#
#
#         return root

'''
tmp3 This code actually passes the initial test case, however it hasn't been tested
Tomorrow: implement preorder, inorder traversal to help you test the code
Also, maybe come up with a more efficient implementation :)
Cheers, L,E.
'''

# # Definition for a binary tree node.
# # class TreeNode:
# #     def __init__(self, x):
# #         self.val = x
# #         self.left = None
# #         self.right = None
#
# class Solution:
#     def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
#         # We stop when yellow backtracks to the root
#         # node for a second time.
#
#         if len(preorder) == 0: # If no tree return None
#             return None
#
#         # In the case that we only have one node:
#         if len(preorder) == 1: # If one node, return that one node
#             return TreeNode(preorder[0])
#
#         # 1) Get the root/initialize variables
#
#         nodes = {}
#         for val in preorder:
#             nodes[val] = False
#
#         root = TreeNode(preorder[0])
#         current = root
#         nodes[root.val] = root
#         size = 1
#         yellow = 0
#         red = 0
#
#         hits = 0
#
#         while hits <= 1:
#
#             while inorder[yellow] != root.val:
#
#                 # print("Before while red: {}".format(red))
#
#                 # print("red: {} yellow: {} root: \n{}".format(red, yellow, root))
#
#                 if hits == 1:
#                     print("\n{}\n".format(list(nodes.keys())))
#
#                 while preorder[red] != inorder[yellow]:
#                     red += 1
#                     current.left = TreeNode(preorder[red])
#                     nodes[preorder[red]] = current.left
#
#
#                     current = current.left
#
#                     size += 1
#                     print("[A] red: {}  yellow: {} size: {} root: {}".format(red, yellow, size, root))
#
#                     if size >= len(preorder):
#                         print("[A] root: {}".format(root))
#                         return root
#
#
#                 # print("root {}\n".format(root))
#
#                 # Have finished building out the initial left subtree
#                 # find element of inorder that does not already exist
#
#                 # print("[pre-backtracking] nodes: {}\n".format(nodes))
#
#                 print("[pre-backtracking] yellow : {}".format(yellow))
#
#
#                 yellow += 1
#
#                 while nodes[inorder[yellow]] != False and inorder[yellow] != root.val:
#                     # Backtracking
#                     yellow += 1
#
#                 print("[post-backtracking] yellow : {}".format(yellow))
#
#                 if nodes[inorder[yellow]] == False: # If this works, we have found our new node
#                     current = nodes[inorder[yellow-1]]
#                     red += 1
#                     current.right = TreeNode(preorder[red])
#                     nodes[preorder[red]] = current.right
#
#                     current = current.right
#
#                     size += 1
#                     print("[B] root: {}".format(root))
#
#                     if size >= len(preorder):
#                         print("B")
#                         return root
#                     # yellow += 1 # Set new outer bound
#
#             yellow += 1
#             red += 1
#             current = root
#             hits += 1
#
#             if hits > 1 or size >= len(preorder):
#                 return root
#
#             if preorder[red] == inorder[yellow]:
#                 # print("[A]")
#                 # Building right:
#                 while preorder[red] == inorder[yellow]: # Building right
#                     current.right = TreeNode(preorder[red])
#                     nodes[preorder[red]] = current.right
#
#                     current = current.right
#                     yellow += 1
#                     red += 1
#
#                     size += 1
#                     print("[C] root: {}".format(root))
#
#                     if size >= len(preorder):
#                         print("C")
#                         return root
#
#                 # print("yellow: {}".format(yellow))
#                 red -= 1
#
#             elif preorder[red] != inorder[yellow]:
#                 # print("[B] preorder[red] {}".format(preorder[red]))
#                 current.right = TreeNode(preorder[red])
#
#                 nodes[preorder[red]] = current.right
#
#
#                 current = current.right
#
#                 size += 1
#
#                 print("[D] yellow: {} root: {}".format(yellow, root))
#
#                 if size >= len(preorder):
#                     print("D")
#                     return root
#
#
#             # print("[to top] red: {} yellow: {} current: {} tree: {}\n".format(red, yellow, current, root))
#
#             # print("[to top II] nodes: {}".format(nodes))
#
#
#         return root



'''
Closest that I got. Fuck this question. Fuck this question in particular.
Turns out we need to use dfs, something that we did not do. I'm ok with looking
at the answer. This was a bit tricky.
'''

# # Definition for a binary tree node.
# # class TreeNode:
# #     def __init__(self, x):
# #         self.val = x
# #         self.left = None
# #         self.right = None
#
# class Solution:
#     def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
#         # We stop when yellow backtracks to the root
#         # node for a second time.
#
#         if len(preorder) == 0: # If no tree return None
#             return None
#
#         # In the case that we only have one node:
#         if len(preorder) == 1: # If one node, return that one node
#             return TreeNode(preorder[0])
#
#         # 1) Get the root/initialize variables
#
#         nodes = {}
#         for val in preorder:
#             nodes[val] = False
#
#         root = TreeNode(preorder[0])
#         current = root
#         nodes[root.val] = root
#         size = 1
#         yellow = 0
#         red = 0
#
#         hits = 0
#
#         while hits <= 1:
#
#             while inorder[yellow] != root.val:
#
#                 # print("Before while red: {}".format(red))
#
#                 # print("red: {} yellow: {} root: \n{}".format(red, yellow, root))
#
# #                 if hits == 1:
# #                     print("\n{}\n".format(list(nodes.keys())))
#
#                 while preorder[red] != inorder[yellow]:
#                     red += 1
#                     current.left = TreeNode(preorder[red])
#                     nodes[preorder[red]] = current.left
#
#
#                     current = current.left
#
#                     size += 1
#                     print("[A] red: {}  yellow: {} size: {} root: {}".format(red, yellow, size, root))
#
#                     if size >= len(preorder):
#                         print("[A] root: {}".format(root))
#                         return root
#
#
#                 # print("root {}\n".format(root))
#
#                 # Have finished building out the initial left subtree
#                 # find element of inorder that does not already exist
#
#                 # print("[pre-backtracking] nodes: {}\n".format(nodes))
#
#                 print("[pre-backtracking] yellow : {}".format(yellow))
#
#
#                 yellow += 1
#
#                 while nodes[inorder[yellow]] != False and inorder[yellow] != root.val:
#                     # Backtracking
#                     yellow += 1
#
#                 print("[post-backtracking] yellow : {}".format(yellow))
#
#                 if nodes[inorder[yellow]] == False: # If this works, we have found our new node
#                     current = nodes[inorder[yellow-1]]
#                     red += 1
#                     current.right = TreeNode(preorder[red])
#                     nodes[preorder[red]] = current.right
#
#                     current = current.right
#
#                     size += 1
#                     print("[B] root: {}".format(root))
#
#                     if size >= len(preorder):
#                         print("B")
#                         return root
#                     # yellow += 1 # Set new outer bound
#
#             yellow += 1
#             red += 1
#             current = root
#             hits += 1
#
#             if hits > 1 or size >= len(preorder):
#                 return root
#
#             if preorder[red] == inorder[yellow]:
#                 # print("[A]")
#                 # Building right:
#                 while preorder[red] == inorder[yellow]: # Building right
#                     current.right = TreeNode(preorder[red])
#                     nodes[preorder[red]] = current.right
#
#                     current = current.right
#                     yellow += 1
#                     red += 1
#
#                     size += 1
#                     print("[C] root: {}".format(root))
#
#                     if size >= len(preorder):
#                         print("C")
#                         return root
#
#                 # print("yellow: {}".format(yellow))
#                 red -= 1
#
#             elif preorder[red] != inorder[yellow]:
#                 # print("[B] preorder[red] {}".format(preorder[red]))
#                 current.right = TreeNode(preorder[red])
#
#                 nodes[preorder[red]] = current.right
#
#
#                 current = current.right
#
#                 size += 1
#
#                 print("[D] yellow: {} root: {}".format(yellow, root))
#
#                 if size >= len(preorder):
#                     print("D")
#                     return root
#
#
#             while preorder[red+1] != inorder[yellow]:
#                 red += 1
#                 # Case D, might fuck up everything else, idk...
#                 current.right = TreeNode(preorder[red])
#                 nodes[preorder[red]] = current.right
#                 current = current.right
#
#                 size += 1
#
#
#
#         return root
