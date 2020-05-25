

class Solution:
    def calPoints(self, ops):
        stack = []
        ans = 0

        for op in ops:
            if op == "C":
                ans -= stack.pop()

            elif op == "D":
                stack.append(stack[-1]*2)
                ans += stack[-1]

            elif op == "+":
                stack.append(stack[-1]+stack[-2])
                ans += stack[-1]

            else:
                stack.append(int(op))
                ans += stack[-1]


        return ans
