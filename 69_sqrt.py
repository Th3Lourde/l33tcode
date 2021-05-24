class Solution:
    def mySqrt(self,x):
        r = x
        while r*r > x:
            r = (r+x//r)//2
        return r

if __name__ == '__main__':
    s = Solution()
    print(s.mySqrt(2))
