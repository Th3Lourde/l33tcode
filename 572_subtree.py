
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None








def getHead(s, val):
    # print("{} {}".format(s.val, val))
    if s.val == val:
        return s

    if s.left != None:
        s = getHead(s.left, val)
        return s

    if s.right != None:
        s = getHead(s.right, val)
        return s


def check_similarity2(s,t):
    if s.val != t.val:
        return False

    # Check Left-Side
    if (s.left != None) and (t.left != None):
        l_r = check_similarity(s.left, r.left)

    elif (s.left == None) and (t.left == None):
        return True

    elif (s.left != None) and (t.left == None) or (s.left == None) and (t.left != None):
        return False

    # Check Right-Side
    if (s.right != None) and (t.right != None):
        r_r = check_similarity(s.right, r.right)

    elif (s.right == None) and (t.right == None):
        return True

    elif (s.right != None) and (t.right == None) or (s.right == None) and (t.right != None):
        return False


    if l_r and r_r:
        return True
    else:
        return False


class Solution:

    '''
    So the issue is that there can be multiple
    values or 'matches' in the tree. How to deal
    with this? One thing we can do is, once we've
    found a match, check to see if there are other
    matches .left or .right. Also return a list
    of nodes instead of just a node.
    '''


    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        tmp_head = self.getHead(s, t.val, [])


        print(tmp_head)


        # if tmp_head == None:
        #     return False
        #
        # # print("Got matching value: {}".format(tmp_head.left.val))
        #
        # ans = self.check_similarity(tmp_head,t)
        # return ans
        return False


    def getHead(self, s, target, hits):
        if s.val == target:
            # hunt is on
            foo bar foo

        elif s.val > target:

            if s.left != None:
                r = self.getHead(s.left, target, hits):
                return r

            elif s.left == None:
                return hits



        elif s.val < target:

            if

            r = self.getHead(s.right, target, hits):
            return r




    def check_similarity(self, s, t):
        if s.val != t.val:
            return False

        # Check Left-Side
        if ((s.left != None) and (t.left != None)) and ((s.right != None) and (t.right != None)):
            l_r = self.check_similarity(s.left, t.left)
            r_r = self.check_similarity(s.right, t.right)

            if l_r and r_r:
                return True

            else:
                return False


        # If LHS but RHS is null
        elif ((s.left != None) and (t.left != None)) and not((s.right != None) and (t.right != None)):
            l_r = self.check_similarity(s.left, r.left)

            if l_r:
                return True
            else:
                return False

        # If RHS but LHS is null
        elif ((s.right != None) and (t.right != None)) and not((s.left != None) and (t.left != None)):
            r_r = self.check_similarity(s.right, t.right)

            if r_r:
                return True
            else:
                return False

        elif ((s.left == None) and (s.right == None)) and ((t.left == None) and (t.right == None)):
            return True



    # if l_r and r_r:
    #     return True
    # else:
    #     return False




def check_similarity1(s, t):
    if s.val != t.val:
        return False
    elif s.val == t.val:
        # Make sure that the None's
        # match up :D

        # Cases where Nones do not match up
        # return false
        if s.left == None and t.left != None or s.right == None and t.right != None or t.left == None and s.left != None or t.right == None and s.right != None:
            return False

        # Cases where Nones do match up
        # Handle cases on how to proceed

        # left == None, right == None
        # -> Stop
        elif s.left == None and t.left == None and s.right == None and t.right == None:
            return True

        # left != None, right != None
        # -> check l & r
        elif s.left != None and t.left != None and s.right != None and t.right != None:
            resp_a = check_similarity(s.left, t.left)
            resp_b = check_similarity(s.right, t.right)

            if resp_a == True and resp_b == True:
                return True
            else:
                return False

        # left == None, right != None
        # -> proceed right
        elif s.left == None and t.left == None and s.right != None and t.right != None:
            resp = check_similarity(s.right, t.right)
            return resp

        # left != None, right == None
        # -> proceed left
        elif (s.left != None and t.left != None and s.right == None and t.right == None):
            resp = check_similarity(s.left, t.left)
            return resp


def isSubtree(s: TreeNode, t: TreeNode) -> bool:

    # Assuming t.val in s
    s_head = getHead(s, t.val)

    # Ok, so now we got the node :D,
    # now let's step through it to see
    # if everything is correct

    # print(s_head)

    resp = check_similarity(s_head, t)

    return resp



if __name__ == "__main__":
    # Construct Tree s from example one
    head = TreeNode(3)
    head.right = TreeNode(5)
    head.left = TreeNode(4)
    head.left.left = TreeNode(1)
    head.left.right = TreeNode(2)
    head.left.right.right = TreeNode(0)

    # print("   S:")
    # print("   {}".format(head.val))
    # print("  {}  {}".format(head.left.val, head.right.val))
    # print(" {} {}".format(head.left.left.val, head.left.right.val))

    copy = TreeNode(4)
    copy.left = TreeNode(1)
    copy.right = TreeNode(2)

    # print("\n   T:")

    # print("   {}".format(copy.val))
    # print("  {} {}".format(copy.left.val, copy.right.val))

    # resp = isSubtree(head, copy)

    # print(resp)

    head = TreeNode(1)
    head.left = TreeNode(1)

    copy = TreeNode(1)

    s = Solution()
    r = s.isSubtree(head,copy)

    print(r)
