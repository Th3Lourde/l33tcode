
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        tmp_head = self.findMatches(s, t.val, [])

        if tmp_head == None or tmp_head == []:
            return False


        for i in range(len(tmp_head)):
            r = self.check_similarity(tmp_head[i], t)
            print(r)

            if r:
                return r

        return False


    def findMatches(self, s, t, matches):
        # Check if the value exists
        # in the Binary Tree

        if s.val == t:
            matches.append(s)

        if (s.left != None) and (s.right != None):
            r1 = self.findMatches(s.left, t, matches)
            r2 = self.findMatches(s.right, t, [])

            return r1 + r2

        elif (s.left != None) and (s.right == None):
            r1 = self.findMatches(s.left, t, matches)
            return r1

        elif (s.right != None) and (s.left == None):
            r2 = self.findMatches(s.right, t, matches)
            return r2

        elif (s.right == None) and (s.left == None):
            return matches



    def check_similarity(self, s, t):
        if (s != None) and (t != None):
            if s.val == t.val:
                r1 = self.check_similarity(s.left, t.left)
                r2 = self.check_similarity(s.right, t.right)

                if r1 and r2:
                    return True

                else:
                    return False


            elif s.val != t.val:
                return False

        elif (s == None) and (t == None):
            return True

        else:
            return False



if __name__ == '__main__':
    # head = TreeNode(1)
    # head.left = TreeNode(1)
    #
    # copy = TreeNode(1)


    head = TreeNode(3)
    head.right = TreeNode(5)
    head.left = TreeNode(4)
    head.left.left = TreeNode(1)
    head.left.right = TreeNode(2)
    # head.left.right.right = TreeNode(0)


    copy = TreeNode(4)
    copy.left = TreeNode(1)
    copy.right = TreeNode(2)

    # [1,2,3]
    # [1,2]

    # head = TreeNode(1)
    # head.left = TreeNode(2)
    # head.right = TreeNode(3)

    # copy = TreeNode(1)
    # copy.left = TreeNode(2)







    s = Solution()
    r = s.isSubtree(head,copy)

    print(r)
