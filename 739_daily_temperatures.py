
'''
You are given a list of integers. For every element in the list, find the
distance to another element of larger size. If no such element exists, record
zero.

Run time for this is: O(n^2)
Memory Complexity: O(n)

How can we improve the run time?

'''

class TreeNode:
    def __init__(self, x, i):
        self.val = x
        self.index = i
        self.left = None
        self.right = None

    def __str__(self):
        return "val: {} i: {}".format(self.val, self.index)

class BST:
    def __init__(self, y):
        self.root = y
        # self.size = 1

    def update(self, target, i):
        # Find where to put the newly found node
        print("updating: {} {}".format(target, i))

        if self.found:
            return

        node = self.root

        while True: # since not found, there will not exist a node
                    # with the target value
            if node.val > target:
                if node.left:
                    node = node.left

                elif not node.left:
                    node.left = TreeNode(target, i)
                    print("creating node left of: {}".format(node.val, node.left))
                    break


            elif node.val < target:
                if node.right:
                    node = node.right

                elif not node.right:
                    node.right = TreeNode(target, i)
                    print("creating node right of {}: {}".format(node.val, node.right))
                    break


    def find(self, target, i): # if node in in tree, find will find it run find, then update
        # Find all of the nodes > target,
        # return the index of the node that is closest
        print("finding: {} {}".format(target, i))
        node = self.root
        self.found = False

        # if self.size == 0:
        #     print("[error] BST is empty")

        stack = ['h']
        max_i = None

        while True:
            if node:
                if node.val > target: # if we have found a valid node
                    if max_i:         # check the .right and the .left
                        if node.index < max_i:
                            max_i = node.index

                    elif not max_i:
                        # print("initializing max_i: ".format({node}))
                        max_i = node.index

                    # Check both .right and .left
                    if node != stack[-1]: # go left
                        stack.append(node)
                        node = node.left

                    elif node == stack[-1]: # go right
                        stack.pop()
                        node = node.right

                elif node.val <= target: # Check only the .right
                    if node.val == target:
                        node.index = i
                        self.found = True

                    if node == stack[-1]:
                        stack.pop()

                    node = node.right

            elif not node:
                # go to stack/rhs
                if stack == ['h']:
                    break

                elif stack != ['h']:
                    # print("node [before]: {}".format(node))
                    node = stack[-1]
                    # print("node [after]: {}".format(node))

        if max_i:
            return max_i-i

        elif not max_i:
            return 0

class Solution:

    def dailyTemperatures(self, T): # understand it, however had to look it up.
        ans = [0]*len(T)
        stack = []

        for i in range(len(T)-1, -1, -1):
            while stack and T[i] > T[stack[-1]]:
                stack.pop()

            if stack:
                ans[i] = stack[-1]-i

            stack.append(i)

        return ans


    def dailyTemperatures_5(self, T): # works, is slow
        temps = [101]*101
        ans = [0]*len(T)

        for i in range(len(T)-1, -1, -1):
            replacement = len(T)
            temps[T[i]] = i

            for largerTemp in range(T[i]+1, 101):
                replacement = min(replacement, temps[largerTemp])

            if replacement < len(T):
                ans[i] = replacement - i

        return ans

    def dailyTemperatures_4(self, T): #TLE
        d = {key: [] for key in range(30,101)}


        for i in range(len(T)):
            d[T[i]].append(i)

        ans = []

        for t in range(len(T)):
            ans.append(0)

            higherTemp = len(T)

            for i in range(T[t]+1, 101):
                if d[i] != []:
                    for index in d[i]:
                        if index > t:
                            higherTemp = min(higherTemp, index)

            if higherTemp != len(T):
                ans[-1] = higherTemp-t

        return ans


    # supplied solution
    def dailyTemperatures_3(self, T):
        '''
        create list of size 71 (include 30-100)
        initialize the list to have values of 29
        '''
        print("input: {}".format(T))

        history = [-1]*71
        ans = []

        for i in range(len(T)-1, -1, -1):
            element = T[i]
            minVal = None

            for j in range(element-29, len(history)): # search for elements > target
                if history[j] != -1:
                    if not minVal:
                        minVal = history[j]

                    elif history[j] < minVal:
                        minVal = history[j]

            if not minVal:
                ans.insert(0, 0)

            if minVal:
                ans.insert(0, minVal-i)

            history[element-30] = i

        return ans

    # bst solution, 34/37 passed
    def dailyTemperatures_2(self, T):
        ans = []
        print("temps: {}".format(T))

        for i in range(len(T)-1, -1, -1):
            # look for T[i] in tree, get closest value greater than it
            if i == len(T)-1:
                node = TreeNode(T[i],i)
                bst = BST(node)
                ans.insert(0, 0)
                print("creating BST")

            elif i < len(T)-1:
                ans.insert(0, bst.find(T[i], i))
                bst.update(T[i], i)

        return ans



    # brute-force 27/37 passed
    def dailyTemperatures_1(self, T):
        ans = []
        for i in range(len(T)):
            element = T[i]

            for j in range(i+1, len(T)):
                if T[j] > element:
                    ans.append(j-i)
                    break

                elif j == len(T)-1:
                    ans.append(0) # We know that T[j] not > element
                    break

        ans.append(0)

        return ans

if __name__ == '__main__':
    s = Solution()
    # print(s.dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73]))
    print("have: {}".format(s.dailyTemperatures([89,62,70,58,47,47,46,76,100,70])))
    correct = [8,1,5,4,3,2,1,1,0,0]
    print("want: {}".format(correct))

    assert s.dailyTemperatures([89,62,70,58,47,47,46,76,100,70]) == correct, ":)"
