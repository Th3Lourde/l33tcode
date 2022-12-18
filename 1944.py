'''
10,6,8,5,11,9
         ^

[4]

[3,1,2,1,1, 0]
10,6,8,5,11,9


2,1,0,0,0,0

Go to element
- have a local height, to track what elements can see the element that we are at, add to the list accordingly
|--> Upon seeing a new element, record which elements can see the new element

- While element >= top element, pop from stack
- Add element to stack


Ok so we know it is a stack problem.
How could we use a stack to our advantage?

If we keep the stack strictly decreasing we could
filter out some of the results


[3,1,2,1,1,0]
'''

class Solution:
    def canSeePersonsCount(self, heights):
        stack = []
        resp = [0] * len(heights)

        for idx in range(len(heights)):
            # print("idx: {} | stack: {}".format(idx, stack))
            # print(resp)
            if not stack:
                stack.append(idx)
            else:
                # Figure out what elements can see this element
                for i in reversed(stack):
                    # print("{} > {} ?".format(heights[i], heights[idx]))
                    resp[i] += 1

                    if heights[i] >= heights[idx]:
                        break

                # print(resp)

            while stack and heights[stack[-1]] <= heights[idx]:
                stack.pop()

            stack.append(idx)

        return resp

print(Solution().canSeePersonsCount([10,6,8,5,11,9]))
print(Solution().canSeePersonsCount([5,1,2,3,10]))
