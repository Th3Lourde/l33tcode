'''
Good job. This was a more difficult problem.
The top down was a bit confusing, but we got it :D
'''

class Solution:

    # Logically this should be quicker? Idk
    def minHeightShelves(self, books, shelf_width):
        dp = [float('inf') for _ in books]

        # populate first shelf

        width = 0
        height = books[0][1]
        z = 0

        for i in range(len(books)):
            width += books[i][0]

            if width > shelf_width:
                break

            if books[i][1] > height:
                height = books[i][1]

            dp[i] = height

            z += 1

        for i in range(z, len(books)):
            width = shelf_width
            height = 0

            minHeight = float('inf')

            for k in range(i, -1, -1):
                if books[k][1] > height:
                    height = books[k][1]

                width -= books[k][0]

                if width < 0:
                    break

                if dp[k-1]+height < minHeight:
                    minHeight = dp[k-1]+height

            dp[i] = minHeight

        return dp[-1]


    # Top Down, got 95% for this, wow
    def minHeightShelves_1(self, books, shelf_width):

        dp = [float('inf') for _ in books]

        def itr(i):
            if i >= len(books):
                return 0

            if dp[i] != float('inf'):
                return dp[i]

            width = 0
            height = 0
            rowHeight = float('inf')

            for z in range(i, len(books)):

                if width + books[z][0] > shelf_width:
                    possibleH = height + itr(z)

                    if possibleH < rowHeight:
                        rowHeight = possibleH

                    break

                if books[z][1] > height:
                    if z != i:
                        possibleH = height + itr(z)

                        if possibleH < rowHeight :
                            rowHeight = possibleH

                    height = books[z][1]

                width += books[z][0]

                if z == len(books)-1 and height < rowHeight:
                    rowHeight = height


            if rowHeight == float('inf'):
                rowHeight = height

            dp[i] = rowHeight

            return dp[i]

        itr(0)

        return dp[0]

s = Solution()

print(s.minHeightShelves([[1,1],[2,3],[2,3],[1,1],[1,1],[1,1],[1,2]], 4))
