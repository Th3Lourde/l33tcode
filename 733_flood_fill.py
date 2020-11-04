'''
An image is represented via a 2D array of ints

Given an image, coordinate in said image.

The coordinate has a color. That pixel is connected
to other pixels. Imagine all pixels in a 4-pathway
connection to the given coord, filter ∋ the only pixels
we keep have the same value of the initial point.

Set all of those pixels to have the value newColor.

'''

class Solution:
    def floodFill(self, image, sr, sc, newColor):

        initial = image[sr][sc]

        if initial == newColor:
            return image

        def isValid(r,c):
            if 0 <= r < len(image) and 0 <= c < len(image[0]):
                return True
            return False

        stack = [ (sr, sc) ]

        opts = [ (0, 1), (0, -1), (1, 0), (-1, 0) ]

        while stack:
            r,c  = stack.pop()

            image[r][c] = newColor

            for opt in opts:
                nR, nC = r+opt[0], c+opt[1]

                if isValid(nR, nC) and image[nR][nC] == initial and (r,c) != (nR, nC):
                    stack.append( (nR, nC) )

        return image
