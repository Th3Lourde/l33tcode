'''
Given string num
insert binary operators (+,-,*) such that the evaluation
of the expression yields the target.

Return all such expressions

"1", "2", "3"

idx

So our options are to:
    - Insert an operator
    |--> +
    |--> -
    |--> *
    - Don't insert an operator

We can calculate the current number as we go.

Brute force: generate all possible expressions, evaluate them,
if any match return those.

Problem, inefficient, many possibilities

Could we be more intelligent?
Well only subtract if current num is too big?
Maybe, leave it out for now

Current idea:
Generate all possible expressions
evaluate them
save the ones that equal the target.

Notes:
Ok so this works, we should code it up to practice

Yea so we can calculate this on the fly, just subtract the element from whatever we have

(expression, valueOfExpression, idx, prevNum)

'''

class Solution:
    def addOperators(self, num, target):
        ans = []

        def backtrack(expression, valueOfExpression, idx, prevNum):
            if idx >= len(num):
                if valueOfExpression == target:
                    ans.append(expression)
                return

            for j in range(idx, len(num)):
                if j > idx and num[idx] == "0":
                    continue

                str_exp, int_eval = num[idx:j+1], int(num[idx:j+1])

                if idx == 0:
                    backtrack(expression+str_exp, valueOfExpression+int_eval, j+1, int_eval)

                else:
                    backtrack(expression+"+"+str_exp, valueOfExpression+int_eval, j+1, int_eval)
                    backtrack(expression+"-"+str_exp, valueOfExpression-int_eval, j+1, -int_eval)
                    backtrack(expression+"*"+str_exp, valueOfExpression-prevNum + prevNum*int_eval, j+1, prevNum*int_eval)

        backtrack("", 0, 0, 0)
        return ans
