
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isValidBST(self, root):
        if root == None:
            return True

        def iterate(node, lessThan, greaterThan):
            if not node:
                return True

            if node.val < lessThan and node.val > greaterThan:
                return iterate(node.left, node.val, greaterThan) and iterate(node.right, lessThan, node.val)

            return False


        return iterate(root, float('inf'), float('-inf'))
        # return self.myValidBST(root, root.val, "n", {})
        # return self.myValidBST(root, None, None, {})


    def myValidBST_3(self, local_root, less, greater, unique):
        if local_root.left != None and local_root.right != None:
            if local_root.left.val < local_root.val and local_root.right.val > local_root.val:
                try:
                    unique[local_root.left]
                    return False

                except:
                    try:
                        unique[local_root.right]
                        return False

                    except:
                        unique[local_root.right] = 1
                        unique[local_root.left] = 1

                        if less != None and greater != None:
                            if (local_root.left.val > greater and local_root.left.val < less) and (local_root.right.val > greater and local_root.right.val < less):
                                # We are good to go and can continue our calls

                                l = self.myValidBST(local_root.left, local_root.val, greater, unique)
                                r = self.myValidBST(local_root.right, less, local_root.val, unique)

                                if l and r:
                                    return True

                                else:
                                    return False

                            else:
                                return False



                        elif less != None and greater == None:
                            if (local_root.left.val < less and local_root.right.val < less):
                                # We are good to go to make our next call

                                l = self.myValidBST(local_root.left, local_root.val, None, unique)
                                r = self.myValidBST(local_root.right, less, local_root.val, unique)

                                if l and r:
                                    return True

                                else:
                                    return False

                            else:
                                return False



                        elif less == None and greater != None:
                            if (local_root.left.val > greater and local_root.right.val > greater):
                                l = self.myValidBST(local_root.left, local_root.val, greater, unique)
                                r = self.myValidBST(local_root.right, None, local_root.val, unique)

                                if l and r:
                                    return True

                                else:
                                    return False

                            else:
                                return False

                        elif less == None and greater == None:
                            l = self.myValidBST(local_root.left, local_root.val, None, unique)
                            r = self.myValidBST(local_root.right, None, local_root.val, unique)

                            if l and r:
                                return True

                            else:
                                return False

            else:
                return False









        elif local_root.left != None and local_root.right == None:
            if local_root.left.val < local_root.val:
                try:
                    unique[local_root.left]
                    return False

                except:
                    unique[local_root.left] = 1

                    # We know that it is unique

                    if less != None and greater != None:
                        if (local_root.left.val > greater and local_root.left.val < less):
                            # We are good to go and can continue our calls

                            l = self.myValidBST(local_root.left, local_root.val, greater, unique)

                            if l:
                                return True

                            else:
                                return False

                        else:
                            return False

                    elif less != None and greater == None:
                        if (local_root.left.val < less):
                            l = self.myValidBST(local_root.left, local_root.val, None, unique)

                            if l:
                                return True

                            else:
                                return False

                        else:
                            return False

                    elif less == None and greater != None:
                        if (local_root.left.val > greater):
                            l = self.myValidBST(local_root.left, local_root.val, greater, unique)

                            if l:
                                return True

                            else:
                                return False

                        else:
                            return False

                    elif less == None and greater == None:
                        l = self.myValidBST(local_root.left, local_root.val, None, unique)

                        if l:
                            return True

                        else:
                            return False

            else:
                return False




        elif local_root.left == None and local_root.right != None:
            if local_root.right.val > local_root.val:
                try:
                    unique[local_root.right]
                    return False

                except:
                    unique[local_root.right] = 1

                    if less != None and greater != None:
                        if local_root.right.val > greater and local_root.right.val < less:
                            # We are good to go and can continue

                            r = self.myValidBST(local_root.right, less, local_root.val, unique)

                            if r:
                                return True

                            else:
                                return False


                        else:
                            return False


                    elif less != None and greater == None:
                        if local_root.right.val < less:
                            # We are good to go and can continue

                            r = self.myValidBST(local_root.right, less, local_root.val, unique)

                            if r:
                                return True

                            else:
                                return False

                        else:
                            return False


                    elif less == None and greater != None:
                        if local_root.right.val > greater:
                            # We are good to go and can continue

                            r = self.myValidBST(local_root.right, None, local_root.val, unique)

                            if r:
                                return True
                            else:
                                return False

                        else:
                            return False



                    elif less == None and greater == None:
                        r = self.myValidBST(local_root.right, None, local_root.val, unique)

                        if r:
                            return True
                        else:
                            return False

            else:
                return False

        elif local_root.left == None and local_root.right == None:
            return True


    def myValidBST_2(self, local_root, root_val, side, unique):
        # local_root != None

        if local_root.left != None and local_root.right != None:
            if local_root.left.val < local_root.val and local_root.right.val > local_root.val:
                try:
                    unique[local_root.left]
                    return False
                except:
                    try:
                        unique[local_root.right]
                        return False
                    except:
                        '''
                        So we know that both children are greater/less than their parents
                        Both children are unique

                        Record them in the dictionary, then make sure they are less than
                        or greater than the root
                        '''
                        unique[local_root.right] = 1
                        unique[local_root.left] = 1

                        if side == "n":
                            # parent check is sufficient
                            l = self.myValidBST(local_root.left, root_val, "l", unique)
                            r = self.myValidBST(local_root.right, root_val, "r", unique)

                            if l and r:
                                return True
                            else:
                                return False


                        elif side == "l":
                            if local_root.left.val < root_val and local_root.right.val < root_val:
                                l = self.myValidBST(local_root.left, root_val, side, unique)
                                r = self.myValidBST(local_root.right, root_val, side, unique)

                                if l and r:
                                    return True
                                else:
                                    return False

                            else:
                                return False




                        elif side == "r":
                            if local_root.left.val > root_val and local_root.right.val > root_val:
                                l = self.myValidBST(local_root.left, root_val, side, unique)
                                r = self.myValidBST(local_root.right, root_val, side, unique)

                                if l and r:
                                    return True
                                else:
                                    return False

                            else:
                                return False





            else:
                return False

        elif local_root.left != None and local_root.right == None:
            if local_root.left.val < local_root.val:
                try:
                    unique[local_root.left]
                    return False
                except:
                    unique[local_root.left] = 1

                    if side == "n":
                        l = self.myValidBST(local_root.left, root_val, "l", unique)

                        if l:
                            return True
                        else:
                            return False

                    elif side == "l":

                        if local_root.left.val < root_val:

                            l = self.myValidBST(local_root.left, root_val, side, unique)

                            if l:
                                return True
                            else:
                                return False

                        else:
                            return False

                    elif side == "r":

                        if local_root.left.val > root_val:

                            r = self.myValidBST(local_root.left, root_val, side, unique)

                            if r:
                                return True
                            else:
                                return False

                        else:
                            return False

        elif local_root.left == None and local_root.right != None:
            if local_root.right.val > local_root.val:
                try:
                    unique[local_root.right]
                    return False
                except:
                    unique[local_root.right] = 1

                    if side == "n":
                        r = self.myValidBST(local_root.right, root_val, "r", unique)

                        if r:
                            return True
                        else:
                            return False

                    elif side == "l":

                        if local_root.right.val < root_val:

                            r = self.myValidBST(local_root.right, root_val, side, unique)

                            if r:
                                return True
                            else:
                                return False

                        else:
                            return False

                    elif side == "r":

                        if local_root.right.val > root_val:
                            r = self.myValidBST(local_root.right, root_val, side, unique)

                            if r:
                                return True
                            else:
                                return False

                        else:
                            return False

        elif local_root.left == None and local_root.right == None:
            return True


    def myValidBST_1(self, root, val, side, seen):

        if root == None:
            return True

        elif (root.left != None) and (root.right != None):

            if side == "n":

                if (root.val > root.left.val) and (root.val < root.right.val):
                    # We are good to go :)
                    l = self.myValidBST(root.left, root.val, "l")
                    r = self.myValidBST(root.right, root.val, "r")

                    if l and r:
                        return True

                    else:
                        return False

                else:
                    return False

            elif side == "l":
                if (root.val > root.left.val and root.val < val) and (root.val < root.right.val and root.right.val < val):
                    l = self.myValidBST(root.left, root.val, "l")
                    r = self.myValidBST(root.right, root.val, "r")

                    if l and r:
                        return True

                    else:
                        return False

                else:
                    return False

            elif side == "r":
                if (root.val > root.left.val and root.val > val) and (root.val < root.right.val and root.left.val > val):
                    l = self.myValidBST(root.left, root.val, "l")
                    r = self.myValidBST(root.right, root.val, "r")

                    if l and r:
                        return True

                    else:
                        return False

                else:
                    return False

        elif (root.left != None) and (root.right == None):

            if side == "n":

                if (root.left.val < root.val):
                    resp = self.myValidBST(root.left, root.val, "l")

                    if resp:
                        return True

                else:
                    return False



            elif side == "l":

                if (root.left.val < root.val) and root.val < val:
                    resp = self.myValidBST(root.left, root.val, "l")

                    if resp:
                        return True

            elif side == "r":

                if root.left.val < root.val and root.val > val:
                    resp = self.myValidBST(root.left, root.val, "l")

                    if resp:
                        return True

        elif (root.left == None) and (root.right != None):

            if side == "n":
                if root.right.val > root.val:
                    resp = self.myValidBST(root.right, root.val, "r")

                    if resp:
                        return True

            elif side == "l":

                if root.right.val > root.val and root.val < val:
                    resp = self.myValidBST(root.right, root.val, "r")

                    if resp:
                        return True

            elif side == "r":

                if root.right.val > root.val and root.val > val:
                    resp = self.myValidBST(root.right, root.val, "r")

                    if resp:
                        return True

        elif (root.left == None) and (root.right == None):
            return True




'''

[10,5,15,null,null,6,20]

            10
        5       15
   null  null  6  20


[3,null,30,10,null,null,15,null,45]

               3
        null        30
      10   null  null 15
  null  45

'''
