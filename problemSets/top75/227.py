'''
Ok so basic calculator, the issue we ran into
was that the different numbers can be multiple
digits
'''

import math

class Solution:
    def calculate(self, s):
        s = s.replace(" ", "")
        n = len(s)

        terms = []
        l, r = 0, 0
        ops = set({"+","-","/","*"})

        while l <= r < n:
            while r < n and s[r] not in ops:
                r += 1

            if r >= n:
                break

            terms.append(int(s[l:r]))
            terms.append(s[r])
            l, r = r+1, r+1

        terms.append(int(s[l:]))

        def mathEvaluate(n1,n2,op):
            if op == "+":
                return n1+n2
            elif op == "-":
                return n1-n2
            elif op == "*":
                return n1*n2
            else:
                return int(n1/n2)

        stack = []
        i = 0

        while i < len(terms):
            if terms[i] == "*" or terms[i] == "/":
                result = mathEvaluate(stack.pop(), terms[i+1], terms[i])
                stack.append(result)
                i += 1
            else:
                stack.append(terms[i])

            i += 1

        resp = []
        i = 0
        while i < len(stack):
            if stack[i] == "+" or stack[i] == "-":
                result = mathEvaluate(resp.pop(), stack[i+1], stack[i])
                resp.append(result)
                i += 1
            else:
                resp.append(stack[i])

            i += 1

        return resp[-1]






print(Solution().calculate("3-2*2+6"))
print(Solution().calculate("42"))
print(Solution().calculate("23 / 2"))
print(Solution().calculate("32+5/2"))
print(Solution().calculate("3/2*2"))
print(Solution().calculate("3+2*2"))
