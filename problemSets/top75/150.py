'''
Evaluate the value of the arithmetic expression
in reverse polish notation

Operators:
+,-,*,/

Each operand may be an integer or another expression

Division between two integers should truncate towards zero.

I smell a stack.


["4","13","5","/","+"]
                   ^

[4,2]

Idea:
- If int, append to stack.
- If operator, pop last two elements from stack and apply operator
|--> append the output of operation when done

Ok so it looks like this holds.
Let's implement

'''


class Solution:
    def evalRPN(self, tokens):
        stack = []
        ops = set({"+", "-", "/", "*"})

        for token in tokens:
            if token in ops:
                e2 = int(stack.pop())
                e1 = int(stack.pop())

                term = 0

                if token == "+":
                    term = e1+e2

                elif token == "-":
                    term = e1-e2

                elif token == "*":
                    term = e1*e2

                else:
                    term = int(e1/e2)

                stack.append(term)

            else:
                stack.append(token)

        return stack.pop()


print(Solution().evalRPN(["4","13","5","/","+"]))
print(Solution().evalRPN(["2","1","+","3","*"]))
