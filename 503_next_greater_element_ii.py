'''
Given a circular array nums

So same problem, only now the array is circular

So perform the search on the rhs.
If that doesn't work, perform the search on the lhs

So for each element, perform rhs search

Then for each element that has -1, perform lhs search

'''

class Solution:
    def nextGreaterElements(self, A):
        stack, res = [], [-1] * len(A)
        for i in range(len(A)):
            while stack and (A[stack[-1]] < A[i]):
                res[stack.pop()] = A[i]
            stack.append(i)

        for i in range(len(A)):
            while stack and (A[stack[-1]] < A[i]):
                res[stack.pop()] = A[i]
            stack.append(i)
        return res

print(Solution().nextGreaterElements([1,2,1] ))
print(Solution().nextGreaterElements([1,2,3,4,3]))
