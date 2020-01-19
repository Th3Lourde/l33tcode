
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# This works :)
class Solution:
    def update(self, node, my_dict):
        if node:
            node.val = my_dict[node.val]

            if node.left:
                self.update(node.left, my_dict)

            if node.right:
                self.update(node.right, my_dict)

        else:
            return None

    def isomorphism(self, start, total, my_dict):
        import copy
        map = {}

        for i in range(0, total):
            map[i+1] = start+i

        ans = []

        copy_dict = copy.deepcopy(my_dict)

        for j in range(len(copy_dict)):
            copy = copy_dict[j]

            self.update(copy, map)

            ans.append(copy)

        return ans

    def generateTrees(self, n):
        import copy
        resp = {}

        resp[0] = [None]

        if n == 0:
            return []

        for i in range(1, n+1):
            tmp = []

            for j in range(1, i+1):
                root = TreeNode(j)

                for h in range(len(resp[j-1])):
                    root.left = resp[j-1][h]

                    if i-j != 0:
                        rhs = self.isomorphism(j+1, i-j, resp[i-j])

                        for k in range(len(rhs)):
                            new_root = copy.deepcopy(root)
                            new_root.right = rhs[k]
                            tmp.append(new_root)

                    elif i-j == 0:
                        new_root = copy.deepcopy(root)
                        new_root.right = None
                        tmp.append(new_root)

            resp[i] = tmp

        return resp[n]


# This does not work
class Solution_1:
    def generateTrees_i(self, n):

        # want n+1 b/c you start at zero and end at n
        resp = [0] * (n+1)

        # there's one way to create
        # a tree containing zero nodes
        resp[0] = 1

        for i in range(1, n+1):
            for j in range(i):
                resp[i] += resp[j]*resp[i-1-j]


    def generateTrees_II(self, n):

        # want n+1 b/c you start at zero and end at n
        resp = {}

        # there's one way to create
        # a tree containing zero nodes
        resp[0] = [TreeNode(None)]

        if n == 0:
            return []

        for i in range(1, n+1):
            # i = number of nodes in tree
            # also value of greatest node
            # in tree

            # j represents the node
            #that is at the root position
            print("hi")

            tmp = []

            for j in range(1, i+1):
                root = TreeNode(j)


                # loop through the possibilities
                # for the left side of the tree
                for h in range(len(resp[j-1])):
                    root.left = resp[j-1][h]
                    # print(h)

                    # loop through the possibilities
                    # for the right side of the tree
                    for k in range(len([i-j])):
                        # print(k)
                        root.right = resp[i-j]
                        tmp.append(root)

            resp[i] = tmp

                # root.left = resp[j-1]
                # root.right = resp[n-j]
        print(resp)

        return resp[n]

    def update(self, node, dict):
        if node:
            node.val = dict[node.val]

            if node.left:
                self.update(node.left, dict)

            if node.right:
                self.update(node.right, dict)

        else:
            return None


    def isomorphism(self, start, total, dict):
        map = {}

        for i in range(0, total):
            map[i+1] = start+i

        ans = []

        for j in range(len(dict)):
            copy = dict[j]

            self.update(copy, map)

            ans.append(copy)

        return ans





    def generateTrees_III(self, n):
        resp = {}

        resp[0] = [None]

        if n == 0:
            return []

        for i in range(1, n+1):
            tmp = []

            for j in range(1, i+1):
                root = TreeNode(j)

                for h in range(len(resp[j-1])):
                    root.left = resp[j-1][h]

                    rhs = self.isomorphism(j+1, i-j, resp[i-j])

                    for k in range(len(rhs)):
                        root.right = rhs[k]
                        tmp.append(root)

                    # for k in range(len(resp[i-j])):
                    #     root.right = resp[i-j][k]
                    #     tmp.append(root)

            resp[i] = tmp

        return resp[n]


    '''
    The issue that I am dealing with is the question of what happens when the form of a binary search tree is similar, however the values of the tree are different. How might I go about solving this? Well we could try to map the values that I have with the values that will be contained in the tree
    the function would take three inputs:
    starting_value:int, number of nodes in the tree, dictionary that I have so far.
    So I would then create a dictionary that would contain the mapping from values that I would encounter in the dictionary to values that I want to be in the dictionary

    def isomorphism(start, total, dict):

        map = {}

        for i in range(0, total):
            map[1+i] = start+i


        # Iterate through the BST
        # updating the values properly
        #
        #



    One issue that I am dealing with is the fact that I am currently corrupting the dictionary that I plan to use for my dynamic programming. So how do I make a copy of a tree? Let's try copying the list instead of the elements in the list and see if that makes a difference.

    Something is happening to the nodes from when they are printed to when they are appended. I'm not really sure why or how this is, just that it happens.

    So it looks like the 'root' that I am changing is mutable in such a way that when I change .right, I am overwriting previous assignments of .right. Fun. Time to make another deep copy :)

    This time it worked! I got it! Yay! I'm happy I put in the time to debug the program. The most problematic assumptions that I made had to do with the lack of connection between different nodes that I was working with. This caused me to overwrite previous binary search trees, which caused my answer to have repeats. Anyways I fixed that. The algo is really slow, but that's ok :)
    '''




    '''
    So I am going to have a dictionary
    the keys represent the number of nodes
    the values are a list of binary search trees
    '''

if __name__ == '__main__':
    s = Solution()

    print(s.generateTrees_II(2))
