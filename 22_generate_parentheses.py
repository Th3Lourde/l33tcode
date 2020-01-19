



class Solution:
    def generateParenthesis(self, n):
        ans = []

        self.recurSolution(n, n, ans, "")

    def recurSolution(self, L, R, ans, current):

        if L == 0 and R == 0:
            ans.append(current)

        elif L == R and L != 0:
            self.recurSolution(L-1, R, ans, current + "(")

        elif L < R:

            if L >= 1:
                self.recurSolution(L-1, R, ans, current + "(")
            if R >= 1:
                self.recurSolution(L, R-1, ans, current + ")")



if __name__ == '__main__':
    s = Solution()

    s.generateParenthesis(3)
