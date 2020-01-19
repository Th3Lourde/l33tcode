
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    # def __str__(self):
    #     return str(self.val) + "\n" + str(self.left) + " " + str(self.right)


# So it isn't adding the values to the list correctly
# Troubleshoot later :)

def add_nodes(root:TreeNode, target:int, vals:list, g_o_l: bool) -> list:

    valz = vals

    if root.val == target:
        valz.append(target)
        return valz
    elif root.val > target:


        if not(root.val in valz):

            if g_o_l == True:
                if root.val > target:
                    valz.append(root.val)

            elif g_o_l == False:
                if root.val < target:
                    valz.append(root.val)

        # Check to make sure we can continue down the list
        if root.left != None:

            r = add_nodes(root.left, target, valz, g_o_l)
            return r

    elif root.val < target:
        if not(root.val in valz):

            if g_o_l == True:
                if root.val > target:
                    valz.append(root.val)

            elif g_o_l == False:
                if root.val < target:
                    valz.append(root.val)
            # vals = vals.append(root.val)

        if root.right != None:
            r = add_nodes(root.right, target, valz, g_o_l)
            return r



def rangeSumBST(root:TreeNode, L:int, R:int) -> int:

    n = add_nodes(root, L, [], True)

    print("Loop 1: {}".format(n))


    a = add_nodes(root, R, n, False)

    print("Loop 2: {}".format(n))


    ans = 0

    for i in range(len(n)):
        ans += n[i]

    return ans




if __name__ == "__main__":
    head = TreeNode(10)
    head.left = TreeNode(5)
    head.right = TreeNode(15)
    head.left.left = TreeNode(3)
    head.left.right = TreeNode(7)
    head.right.right = TreeNode(18)

    # print(head.right.left)

    r = rangeSumBST(head, 7, 15)
    print(r)

    '''
                 10
               /    \
              5      15
             / \    /  \
            3   7  N    18



    '''


