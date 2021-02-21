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


    def numTrees_1(self, n):
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


    # Brute-force recursive solution
    # Works, too slow.
    def numTreesBruteForce(self, n):

        if n == 0:
            return 1

        if n == 1 or n == 2:
            return n

        ans = 0

        # (n,0), (n-1, 1), (n-2, 2) ... (n-1-k,k) until k = n, or n-k = 0
        for k in range(n):
            ans += self.iter(n-1-k, k)

        return ans

    def iterBruteForce(self, left, right):
        if left == 2 and right == 2:
            return 4
        elif left == 2 and right == 1:
            return 2
        elif left == 1 and right == 2:
            return 2
        elif left <= 1 and right <= 1:
            return 1

        if left == 0:
            return self.numTrees(right)

        elif right == 0:
            return self.numTrees(left)

            # Hoping left > 1 and right > 1
            # We tax the node in numTrees, so no need
            # to - 1 here.
        else:
            return self.numTrees(left) * self.numTrees(right)

    #DP
    def numTreesDpRec(self, n):
        if n == 0:
            return 1

        if n == 1 or n == 2:
            return n

        self.dp = [-1 for i in range(n+1)]
        self.dp[0] = 0
        self.dp[1] = 1
        self.dp[2] = 2

        return self.oneNode(n)

    def oneNode(self, n):
        if self.dp[n] != -1:
            return self.dp[n]

        ans = 0

        for k in range(n):
            # ans += self.twoNodes(n-1-k, k)
            l = n-1-k
            r = k

            if l == 0:
                ans += self.oneNode(r)
            elif r == 0:
                ans += self.oneNode(l)

            else:
                ans += self.oneNode(l) * self.oneNode(r)

        self.dp[n] = ans

        return ans

    def numTrees(self, n):
        if n == 1 or n == 2:
            return n

        dp = [0 for i in range(n+1)]
        dp[0] = 1

        for nodes in range(1, n+1):
            for k in range(nodes):
                l = nodes-1-k
                r = k

                dp[nodes] += dp[l] * dp[r]

        return dp[n]





if __name__ == '__main__':
    s = Solution()

    print(s.numTrees(1))
    print(s.numTrees(2))
    print(s.numTrees(3))
    print(s.numTrees(7))
    print(s.numTrees(10))

    # for i in range(1, 5):
    #     print(s.numTrees(i))
        # print(s.numTrees_catalan(i))
