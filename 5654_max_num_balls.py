class Solution:
    def countBalls(self, lowLimit, highLimit):
        boxes = {}
        ans = 0

        for i in range(lowLimit, highLimit+1):
            tmp = i
            t = 0

            while tmp > 0:
                t += tmp % 10
                tmp //= 10

            if t in boxes:
                boxes[t] += 1
            else:
                boxes[t] = 1

            if ans < boxes[t]:
                ans = boxes[t]

        print(boxes)

        return ans

if __name__ == '__main__':
    s = Solution()

    print(s.countBalls(5, 15))
