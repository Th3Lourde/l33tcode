

class Solution:

    def fib_1(self, N):
        if N == 0:
            return 0

        if N == 1 or N == 2:
            return 1
        elif N >= 2:
            return self.fib(N-1) + self.fib(N-2)


    def fib(self, N, mem):
        if mem[N] != None:
            result = mem[N]

        elif N == 1 or N == 2:
            result = 1

        elif N >= 2:
            result = self.fib(N-1, mem) + self.fib(N-2, mem)

        mem[N] = result
        return result


if __name__ == '__main__':
    s = Solution()

    n = 4

    mem = [None] * (n+1)

    # print(mem)

    # print(s.fib(4, mem))

    # print(mem)
