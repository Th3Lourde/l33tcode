'''
An image is represented by the int grid
image[i][j] is the pixel value of the image

change image[sr][sc], as well as all pixels adjancent
to it that have the same value as image[sr][sc] to newColor
'''

from collections import deque

class Solution:
    def floodFill(self, image, sr, sc, newColor):
        initialColor = image[sr][sc]
        rows = len(image)
        cols = len(image[0])

        q = deque([(sr,sc)])
        seen = set()

        if image[sr][sc] == newColor:
            return image

        while q:
            row, column = q.pop()

            if (row, column) in seen:
                continue

            image[row][column] = newColor

            seen.add((row, column))


            for nr, nc in [(row+1, column), (row-1, column), (row, column+1), (row, column-1)]:
                if 0 <= nr < rows and 0 <= nc < cols:
                    if image[nr][nc] == initialColor:
                        q.appendleft((nr, nc))

        return image
