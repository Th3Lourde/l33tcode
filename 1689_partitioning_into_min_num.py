

class Solution:
    def minPartitions(self, n):
        ans = -1
        for i in range(len(n)):
            e = int(n[i])
            if e > ans:
                ans = e
        return ans

if __name__ == '__main__':
    s = Solution()
    print(s.minPartitions("32"))
    print(s.minPartitions("82734"))
    print(s.minPartitions("27346209830709182346"))
