'''
Given a string containing '(', ')', and lowercase english letters,

So we wish to identify all paren that are not valid and
remove them.

We could just record the indices that don't have a match.
Then return the string without those elements.

If "(", push. If ")", pop (if can).
Have a list of indices that we want to remove.
Do we split?

2+5+2+3+10+10+6+7+8


"lee(t(c)o)de)"
 ^
s = []

"lee(t(c)o)de)"
    ^
s = ["("]

"lee(t(c)o)de)"
      ^
s = ["(", "("]

"lee(t(c)o)de)"
        ^
s = ["("] <-- Pop

"lee(t(c)o)de)"
          ^
s = [] <-- Pop

"lee(t(c)o)de)"
             ^
s = [] stack is empty, record the index

Do this for now, come up with a better solution later.

What if we have extra open paren? This supports the idea
that we should keep a list of indices that we want to remove.

We want these indices to be ordered.

When we have too many open paren, append index to list.
If we have left-over open, start at the left.
Since all paren in open are getting larger, we don't have
to start from the beginning every time.

So either start from front or binary search/backtrack.

Depends how many left-over () we have. Either we have left over
left or left over right? I don't think that we will have both?
Yea I agree with that.

)))((( <-- counter

Ok so we care about both.
Wait, bot rm, stack will be sorted.
Use mergesort to create a sorted list?
Sounds good.

rm = []
stack = []

for i in range(len(s)):
    if s[i] == "(":
        stack.append(i)

    elif s[i] == ")":
        if stack:
            stack.pop()

        elif not stack:
            rm.append(s[i])

ans = []

i = 0
j = 0

while i < len(rm) or j < len(stack):
    if i == len(rm):
        ans.append(j)
        j += 1

    elif j === len(stack):
        ans.append(i)
        i += 1


    elif rm[i] < stack[j]:
        ans.append(i)
        i += 1

    else:
        ans.append(j)
        j += 1

return ans


Ok got it right.
I could have done a better job
walking through different examples, I
probably would have figured out that I
didn't need a list earlier.

'''

class Solution:
    def minRemoveToMakeValid(self, s):
        rm = set()
        stack = []

        for i in range(len(s)):
            if s[i] == "(":
                stack.append(i)

            elif s[i] == ")":
                if stack:
                    stack.pop()

                elif not stack:
                    rm.add(i)

        for i in range(len(stack)):
            rm.add(stack[i])

        ans_s = ""

        for i in range(len(s)):
            if i not in rm:
                ans_s = ans_s + s[i]

        return ans_s



if __name__ == '__main__':
    s = Solution()
    # print(s.minRemoveToMakeValid("lee(t(c)o)de)"))
    # print(s.minRemoveToMakeValid("lee(t(c)o)de)"))
    # print(s.minRemoveToMakeValid("))(("))
    print(s.minRemoveToMakeValid("(a(b(c)d)"))
