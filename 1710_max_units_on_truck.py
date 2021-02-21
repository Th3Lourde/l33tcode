
# Damn this is faster than 100% of submitted solutions
# and takes up 100% less space
class Solution:
    def maximumUnits(self, boxTypes, truckSize):
        d = {}

        # 1) Data transformation
        for i in range(len(boxTypes)):
            if boxTypes[i][1] not in d:
                d[boxTypes[i][1]] = boxTypes[i][0]
            else:
                d[boxTypes[i][1]] += boxTypes[i][0]

        keys = list(d.keys())
        keys.sort(reverse=True)
        n = truckSize
        i = 0
        ans = 0

        while n > 0 and i < len(keys):
            # Min between space and box available for use
            boxesUsed = min(n, d[keys[i]])
            ans += keys[i]*boxesUsed
            n -= boxesUsed
            d[keys[i]] -= boxesUsed

            if d[keys[i]] < 1: i+= 1

        return ans

if __name__ == '__main__':
    s = Solution()
    print(s.maximumUnits([[1,3],[2,2],[3,1]], 4))
    print(s.maximumUnits([[5,10],[2,5],[4,7],[3,9]], 10))
