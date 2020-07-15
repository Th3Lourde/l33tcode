'''
Given a string that contains only open/closed parentheses:
The parentheses are balanced.

() has score 1
AB has score A + B, where A and B are balanced parentheses strings.
(A) has score 2 * A, where A is a balanced parentheses string.
-------------------------------------------------------------------
(AB) has a score of 2*(A+B)?
((AB)) has a score of 4*(A+B)?

So:
(( ()() )) <-- won't actually be spaces

Set tmp to global when we have an empty stack.

We could have a local and global score.

When see ")", add one to score <-- conditionally

(( ()() ))
^
level = 1
lvlM = 0

(( ()() ))
 ^
level = 2
lvlM = 0

(( ()() ))
   ^
level = 3
lvlM = 0

(( ()() ))
    ^
level = 2
local = 1
lvlM = 0

(( ()() ))
     ^
level = 3
local = 1
lvlM = 0

(( ()() ))
      ^
level = 2
local = 2
lvlM = 0

(( ()() ))
        ^
level = 1
local = 2
lvlM = 1

(( ()() ))
         ^
level = 0
local = 2
lvlM = 2

if level == 0, global = max(local, local*lvlM)
reset variabls.

But what about (( (()) (())  ))

It looks like "(" cause action to happen.

count the level of open, the number of closed

l == "("
r == ")"

once we start hitting r, hitting l triggers something
Let's start with counting, l


(( ()() ))
^
l = 1

(( ()() ))
 ^
l = 2

(( ()() ))
   ^
l = 3

(( ()() ))
    ^
l = 3
r = 1

(( ()() ))
     ^
/* Trigger some run condition */
l = 4 <-- including current l
r = 1
have found score of 1
add score.
score = 1

l = 3
r = 0

(( ()() ))
      ^
l = 3
r = 1
have found another score of 1
score = 2

l = 2
r = 0

Probably better if we have the run condition
con on r than l.

(( ()() ))
^
l = 1

(( ()() ))
 ^
l = 2

(( ()() ))
   ^
l = 3
r = 0

(( ()() ))
    ^
l = 3
r = 1

When we see a right, if previous term is left, add one to tmp

tmp = 1

l = 2
r = 0

(( ()() ))
     ^
l = 3
r = 0

(( ()() ))
      ^
l = 3
r = 1

tmp += 1 --> 2

tmp = 2
l = 2
r = 0

(( ()() ))
        ^
tmp = 4

we are at ), previous element is not (, multiply by two.
Do we even need to keep track of left, right? maybe we only
care about closing paren. Since the string is closed, we should
be good to go.

if ")":
    if -1 == "(":
        score += 1

    elif -1 != "(":
        score *= 2


(( ()() ))
         ^
score = 8

Ok sick this works. Let's code it up.

"(()(()))"
      ^

The problem is that the mult 2 can increase
the previous sums

If we see "(", check if prev was ")". If so,
start a new local sum?

sums = [0]

If we see a "(" and previous was ")", add a new sum?
If we see a ")" and previous was ")" sum the previous two elements and mult by 2?

"(()(()))"

sums = [0]
sidx = 0

"(()(()))"
   ^
')' --> sums[0] += 1

sums = [1]
sidx = 0

"(()(()))"
    ^
")(" <-- create new sum
sums = [1, 0]
sidx = 1

"(()(()))"
      ^
')', prev '(' --> sums[0] += 1
sums = [1, 1]
sidx = 1

"(()(()))"
       ^

So I should keep track of the number of opens we have?

All of the solutions that we have feel very convoluted, let's
go ahead and look at the solution.

Proper solution:
itr:
        stack = [0] #The score of the current frame

        for x in S:
            if x == '(':
                stack.append(0)
            else:
                v = stack.pop()
                stack[-1] += max(2 * v, 1)

        return stack.pop()

So what if we append when we seen an open? Append a zero.
If we see a close, two things might be true:
 - Either we will have a zero, or we will have a non zero.
If we have zero, append one
If we have non-zero, mult prev value by 2 and add to new value

Ok so this one got me. Is there anything that I could have done
better? I could have written more, I could have dove deeper into
the subproblems. Honestly I think it just got me, I guessed wrong.

Let's save this one and move on. Come back to it when I'm a bit
better.


'''

class Solution:

    def scoreOfParentheses(self, S):
        stack = [0]

        for c in S:
            if c == '(':
                stack.append(0)

            else:
                e = stack.pop()
                stack[-1] += max(2*e, 1)

        return stack.pop()

    def scoreOfParentheses_1(self, S): # Wrong
        score = 0

        for i in range(len(S)):
            if S[i] == ")":
                if S[i-1] == "(":
                    score += 1

                elif S[i-1] == ")":
                    score *= 2

        return score

if __name__ == '__main__':
    s = Solution()

    print(s.scoreOfParentheses("()"))
    print(s.scoreOfParentheses("(())"))
    print(s.scoreOfParentheses("()()"))
    print(s.scoreOfParentheses("(()(()))")) # <-- ok this is wrong, should be 6
