



class Solution:

    def fact(self, x):
        ans = 1
        while x > 1:
            ans *= x
            x -= 1

        return ans

    def uniquePaths(self, m, n): # Solution that I used
        top = self.fact(m-1+n-1)
        bottom = (self.fact(m-1)*self.fact(n-1))

        return int(top/bottom)


    def uniquePaths1(self, m, n): # Works, can do better not using the api
        import math

        top = math.factorial(m-1+n-1)
        # bottom = (math.factorial(m-1))*(math.factorial(m-1+n-1 - (m-1) ))
        bottom = (math.factorial(m-1))*(math.factorial(n-1))

        return int(top/bottom)



if __name__ == '__main__':
    s = Solution()

    testCases = [
        [3,2,3],
        [7,3,28],
    ]

    z = 0

    for case in testCases:
        resp = s.uniquePaths(case[0], case[1])

        if resp == case[2]:
            print("[passed case {}]".format(z))

        elif resp != case[2]:
            print("[failed case {}] wanted {} got {}".format(z, case[2], resp))

        z += 1
