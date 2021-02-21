class Solution:
    def maxDepth(self, s):
        ans = 0
        counter = 0

        for chr in s:
            if chr == "(":
                counter += 1

                if counter > ans:
                    ans = counter

            elif chr == ")":
                counter -= 1

        return ans

if __name__ == '__main__':
    s = Solution()
    print(s.maxDepth("(1+(2*3)+((8)/4))+1"))
    print(s.maxDepth("(1)+((2))+(((3)))"))
    print(s.maxDepth("1+(2*3)/(2-1)"))
