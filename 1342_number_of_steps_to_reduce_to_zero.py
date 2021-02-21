

class Solution:
    def numberOfSteps(self, num):
        ans = 0

        while num:
            if num % 2 == 0:
                ans += 1
            else:
                ans += 2

            num >>= 1

        return ans-1

if __name__ == '__main__':
    s = Solution()
    print(s.numberOfSteps(3))
