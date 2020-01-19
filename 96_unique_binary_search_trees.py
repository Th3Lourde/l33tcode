import math


class Solution:

    def myTrees_my_dp(self, n):

        # want n+1 b/c you start at zero and end at n
        resp = [0] * (n+1)

        # there's one way to create
        # a tree containing zero nodes
        resp[0] = 1

        for i in range(1, n+1):
            for j in range(i):
                resp[i] += resp[j]*resp[i-1-j]

        return resp[n]


    def numTrees(self, n):
        # figure out the number of nodes you can fix
        tw0_ch1ldr3n = (n-1)//2

        ans = 0

        no_children = 2**(n-1)

        if tw0_ch1ldr3n == 0:
            return no_children

        elif tw0_ch1ldr3n != 0:
            for i in range(1, tw0_ch1ldr3n+1):
                '''
                Generate configurations if we only
                have 1 node with two children
                '''

                # Only have one special node, what do we do?
                if i == 1:

                    for j in range(1, n-1):

                        if j == 1:
                            # ans += (number of nodes available to give parents to)*(number of free nodes)
                            ans += (2)*(2**(n-3))

                        elif j > 1:
                            # ans += (number of ways to get to said parent)*(number of ways to move on from parent)
                            ans += ((2)**(j-1))*((2)*(2**(n-3-j+1)))


                    # Have
                elif i > 1:
                    '''
                    Generate configurations where we have multiple
                    nodes that have two children
                    '''


        ans += no_children


        return ans


    # Dynamic Programming Solution
    def numTrees_dp(self, n):
        res = [0] * (n+1)
        res[0] = 1
        for i in range(1, n+1):
            for j in range(i):
                res[i] += res[j] * res[i-1-j]
        return res[n]


    # Combinatorial Solution
    def numTrees_catalan(self, n):
        return int(math.factorial(2*n)/(math.factorial(n)*math.factorial(n+1)))



if __name__ == '__main__':
    s = Solution()

    for i in range(1, 5):
        # print(s.numTrees(i))
        print(s.numTrees_catalan(i))
