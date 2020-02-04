


class Solution:
    # Alex's Solution:
    def sumSubarrayMins(self, A):
        MOD = 10**9 + 7
        N = len(A)

        stack = []
        prev = [None] * N
        for i in range(N):
            # print("i: {}".format(i))
            while stack and A[i] <= A[stack[-1]]:
                # print("popped: {}".format(stack.pop()))
                stack.pop()
            prev[i] = stack[-1] if stack else -1
            # print("prev[{}] = {}".format(i, prev[i]))
            stack.append(i)
            # print("stack: {}".format(stack))

        stack = []
        next_ = [None] * N

        for k in range(N-1, -1, -1):
            while stack and A[k] < A[stack[-1]]:
                stack.pop()
            next_[k] = stack[-1] if stack else N
            stack.append(k)

        print("prev: {}".format(prev))
        print("next: {}".format(next_))

        ans = 0
        for i in range(N):
            print("increment: {}*{} = {}".format((i - prev[i]) * (next_[i] - i), A[i], (i - prev[i]) * (next_[i] - i) * A[i]))
            ans += (i - prev[i]) * (next_[i] - i) * A[i]

        return ans%MOD



    def sumSubarrayMins_2(self, A):
        ans = 0
        for i in range(len(A)):
            ans += A[i]
            min_e = A[i]
            j = i+1

            while j < len(A):
                if min_e != 1:
                    min_e = min(min_e, A[j])
                ans += min_e
                j += 1

        return ans%(10**9 + 7)


    def sumSubarrayMins_1(self, A):
        d = {}
        ans = 0
        for i in range(len(A)):
            for j in range(i, len(A)+1):
                sub = A[i:j+1]
                key = str(A[i:j+1])
                # print("sub: {}".format(sub))
                try:
                    d[key+str(i)]
                    # break?
                except:
                    # print("sub: {}".format(sub))
                    d[key+str(i)] = True
                    ans += min(sub)

        return ans%(10**9 + 7)



if __name__ == '__main__':
    s = Solution()
    print(s.sumSubarrayMins([3,1,2,4]))
