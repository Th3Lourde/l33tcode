class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def str2tree(self, s):
        if len(s) == 0:
            return
        elif len(s) < 4:
            return TreeNode(int(s))

        levels = []
        level = 0
        neg = False
        prevEnd = False
        nonChrSet = set({"(", ")"})
        numStr = ""

        for chr in s:
            if chr not in nonChrSet:
                numStr += chr
                prevEnd = False

            elif chr in nonChrSet and len(numStr) > 0:
                    # Add on the number
                    val = int(numStr)

                    if level > len(levels)-1:
                        # levels.append([val])
                        levels.append([TreeNode(val)])
                    else:
                        # levels[level].append(val)
                        levels[level].append(TreeNode(val))

                    numStr = ""

            if chr == "(":
                level += 1
                prevEnd = False

            elif chr == ")":
                if prevEnd == True:
                    # print("Special Check")
                    if level != 0 and len(levels[level+1]) % 2 == 1:
                        levels[level+1].append(None)
                        # print("Add None")
                    prevEnd = False
                else:
                    prevEnd = True

                level -= 1

        # print(levels)
        # return

        for parent in range(len(levels)-1):
            child = parent + 1

            parent_idx = 0
            child_idx = 0

            left = True

            while child < len(levels) and child_idx < len(levels[child]):
                if left:
                    levels[parent][parent_idx].left = levels[child][child_idx]
                else:
                    levels[parent][parent_idx].right = levels[child][child_idx]
                    parent_idx += 1

                child_idx += 1
                left = not left

        return levels[0][0]

print(Solution().str2tree("51(232)(434)"))


"51(232)(434)"
