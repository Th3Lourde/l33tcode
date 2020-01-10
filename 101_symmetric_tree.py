
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left =  None
        self.right = None

    def __str__(self):
        return "val:{} ".format(self.val)
        # return "val:{} left:{} right:{}".format(self.val, self.left, self.right)

class Solution:


    def isSymmetric(self, root):
        def itr(l,r):
            s1 = ['h']
            s2 = ['h']
            n1 = l
            n2 = r

            while True:
                if (not n1 and n2) or (n1 and not n2):
                    # Trees have different structure
                    return False

                elif n1 and n2:
                    if n1.val == n2.val:

                        if n1 != s1[-1] and n2 != s2[-1]:
                            s1.append(n1)
                            s2.append(n2)

                            n1 = n1.left
                            n2 = n2.right

                        elif n1 == s1[-1] and n2 == s2[-1]:
                            s1.pop()
                            s2.pop()

                            n1 = n1.right
                            n2 = n2.left

                    elif n1.val != n2.val:
                        return False

                elif not n1 and not n2:
                    if s1 == ['h'] and s2 == ['h']:
                        return True

                    elif len(s1) > 1 and len(s2) > 1:
                        n1 = s1[-1]
                        n2 = s2[-1]



        if root:
            return itr(root.left, root.right)

        return True







    def isSymmetric_f(self, root):
        def itr_itr(l,r):
            s1 = ['h']
            s2 = ['h']
            n1 = l
            n2 = r

            while len(s1) != 0 and len(s2) != 0:
                if (not n1 and n2) or (n1 and not n2):
                    # Trees have different structure
                    return False

                elif n1 and n2:
                    if n1.val == n2.val:
                        print("n1: {} n2: {} s1: {} s2: {}".format(n1.val, n2.val, s1, s2))
                        # iterate
                        if (s1 == ['h']) and (s2 == ['h']):
                            s1 = [n1]
                            s2 = [n2]

                            n1 = n1.left
                            n2 = n2.right

                        elif s1[-1] == 'h' and s2[-1] == 'h':
                            # We switched iterative directions
                            s1[-1] = n1
                            s2[-1] = n2

                            n1 = n1.left
                            n2 = n2.right

                        elif s1[-1] != n1 and s2[-1] != n2:
                            s1.append(n1)
                            s2.append(n2)

                            n1 = n1.left
                            n2 = n2.right

                        elif n1 == s1[-1] and n2 == s2[-1]:
                            s1.pop()
                            s2.pop()

                            n1 = n1.right
                            n2 = n2.left

                            if len(s1) == 0 and len(s2) == 0:
                                s1.append('H')
                                s2.append('H')

                    elif n1.val != n2.val:
                        # Same structure, different values
                        return False


                elif not n1 and not n2:

                    if s1[-1] == "H" and s2[-1] == "H":
                        if len(s1) == 1 and len(s2) == 1:
                            s1.pop()
                            s2.pop()

                        elif len(s1) > 1 and len(s2) > 1:
                            s1.pop()
                            s2.pop()
                            n1 = s1[-1]
                            n2 = s2[-1]

                    else:
                        n1 = s1[-1]
                        n2 = s2[-1]

                    # n1.pop()
                    # n2.pop()

                else:
                    print("[Error] Other")
                    return False


            if len(s1) != len(s2): # Might not need this, fingers crossed :)
                return False

            else:
                return True



        if root:
            return itr_itr(root.left, root.right)

        return True


    # recursive solution
    def isSymmetric_1(self, root):
        def itr_rec(l,r):
            print("left: {} right: {}".format(l, r))
            if (not l and r) or (l and not r):
                return False

            elif l and r:
                if l.val == r.val:
                    return itr_rec(l.left, r.right) and itr_rec(l.right, r.left)

                elif l.val != r.val:
                    return False

            elif not l and not r:
                return True


        if root:
            return itr_rec(root.left, root.right)

        return True


if __name__ == '__main__':
    s = Solution()

    '''
        1
       / \
      2   2
     / \ / \
    3  4 4  3
    '''
    root = TreeNode(1)
    two_1 = TreeNode(2)
    two_2 = TreeNode(2)
    three_1 = TreeNode(3)
    three_2 = TreeNode(3)
    four_1 = TreeNode(4)
    four_2 = TreeNode(4)

    root.left = two_1
    root.right = two_2

    two_1.left = three_1
    two_1.right = four_1

    # two_2.left = four_2
    # two_2.right = three_2

    two_2.left = three_2
    two_2.right = four_2

    # print(root.left)

    # print(s.isSymmetric(root))




    '''
    [2,-75,-75,95,-61,-61,95,75,9,-73,-11,-11,-73,8,75]

                        2
              -75               -75
          95       -61      -61      95
        75  9   -73  -11  -11  -73   8   75
    '''

    root1 = TreeNode(2)
    a = TreeNode(-75)
    b = TreeNode(-75)

    root1.left = a
    root1.right = b

    c = TreeNode(95)
    d = TreeNode(-61)
    a.left = c
    a.right = d

    e = TreeNode(-61)
    f = TreeNode(95)
    b.left = e
    b.right = f

    g = TreeNode(75)
    h = TreeNode(9)
    c.left = g
    c.right = h

    i = TreeNode(-73)
    j = TreeNode(-11)
    d.left = i
    d.right = j

    m = TreeNode(-73)
    n = TreeNode(-11)
    e.left = n
    e.right = m

    k = TreeNode(75)
    l = TreeNode(8)
    f.left = l
    f.right = k

    print(s.isSymmetric(root1))
