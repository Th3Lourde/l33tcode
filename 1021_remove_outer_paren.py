


class Solution:

    def removeOuterParentheses(self, S):
        balance = 0
        i = 0
        ans = ""

        for j in range(len(S)):
            if S[j] == "(":
                balance += 1

            elif S[j] == ")":
                balance -= 1

            if balance == 0:
                ans += S[i+1:j]
                i = j + 1

        return ans

    def removeOuterParentheses_1(self, S): # Works
        ans = ""
        stack = []
        sub = ""

        for e in S:
            if e == "(":
                if stack != []:
                    sub += e

                stack.append(e)

            elif e == ")":
                stack.pop()

                sub += e

                if stack == []:
                    ans += sub[:-1]
                    sub = ""


        return ans


if __name__ == '__main__':
    s = Solution()

    testCases = [
        # None
        ["", ""],
        # Something --> None
        ["()()", ""],
        # One
        ["(()())", "()()"],
        # Bigger one
        ["(()())(())", "()()()"],
        # Multiple I
        ["(()()()((())))", "()()()((()))"],
        # Multiple II
        ["(()())(())(()(()))", "()()()()(())"],
    ]

    for tc in testCases:
        r = s.removeOuterParentheses(tc[0])
        assert r == tc[1], "[For {}] {} != {}".format(tc[0], r, tc[1])

    print("[passed all test cases]")
