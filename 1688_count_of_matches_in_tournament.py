class Solution:
    # Initial Solution
    # Can also just return n-1
    def numberOfMatches(self, n):
        matches = 0

        while n > 1:
            if n % 2 == 0:
                # if even
                matches += n//2
                n = n //2
            else:
                # if odd
                matches += (n-1)//2
                n = 1 + (n-1)//2

        return matches

if __name__ == '__main__':
    s = Solution()
    print(s.numberOfMatches(7))
    print(s.numberOfMatches(14))
