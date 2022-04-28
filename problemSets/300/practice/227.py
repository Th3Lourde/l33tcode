import math

'''
12-3*4

'''

class Solution:
    def calculate(self, s):
        s = s.replace(" ", "")
        ops = set({"*", "/", "+", "-"})

        ans = []
        tmp = ""
        i = 0

        while i < len(s):
            symbol = s[i]

            if symbol in ops:
                ans.append(tmp)
                ans.append(symbol)
                tmp = ""
            else:
                tmp += symbol

            i += 1

        if len(tmp) > 0:
            ans.append(tmp)

        # return ans



        def operate(a,b,op):
            if op == "*":
                return str(int(a)*int(b))
            elif op == "/":
                return str(math.floor(int(a)/int(b)))
            elif op == "+":
                return str(int(a)+int(b))
            elif op == "-":
                return str(int(a)-int(b))

        op_to_ops = {0: set({"*", "/"}), 1: set({"+", "-"})}

        for op in range(2):
            new_ans = []

            idx = 0
            while idx < len(ans):
                symbol = ans[idx]
                if symbol in op_to_ops[op]:
                    outcome = operate(new_ans[-1], ans[idx+1], symbol)
                    new_ans[-1] = outcome
                    idx += 2
                else:
                    new_ans.append(symbol)
                    idx += 1

            ans = list(new_ans)

        return int("".join(ans))

print(Solution().calculate("12-3*4"))

print(Solution().calculate("10*2+1/5-5"))
print(Solution().calculate("1+1+1"))
print(Solution().calculate("42"))
print(Solution().calculate("3+2*2"))
print(Solution().calculate(" 3/2 "))
print(Solution().calculate(" 3+5 / 2 "))
