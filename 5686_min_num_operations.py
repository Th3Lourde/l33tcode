'''
n boxes

given string boxes, composed of either "0" || "1"

if boxes[i] == "0", the ith box is empty
if boxes[i] == "1", the ith box contains one ball

operation: move a ball into an adjacent box

return array ans.

ans[i] == min number of operations required to move
all the balls into the ith box.

Two passes?

"001011"
      ^

left = [[],[],[2],[2],[2,4],[2,4,5]]



'''

class Solution:
    def minOperations(self, boxes):
        l = [[] for _ in range(len(boxes))]
        r = [[] for _ in range(len(boxes))]

        # left
        e = [0, 0]
        for i in range(len(boxes)):
            e[0] += e[1]
            if boxes[i] == "1":
                e[1] += 1
            l[i] = [e[0], e[1]]

        # right
        e = [0, 0]
        for i in range(len(boxes)-1, -1, -1):
            e[0] += e[1]
            if boxes[i] == "1":
                e[1] += 1
            r[i] = [e[0], e[1]]

        ans = []

        for i in range(len(boxes)):
            ans.append(l[i][0]+r[i][0])

        return ans


if __name__ == '__main__':
    s = Solution()
    print(s.minOperations("001011"))
