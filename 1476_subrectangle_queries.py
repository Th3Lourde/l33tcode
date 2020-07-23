'''
Ok so we are given a matrix.

We should be able to return the value of
the matrix given some specific coordinates

Also, given a top left, bottom right, and
a new value, set all elements within the
selection to the new value.

update:
 Niave: just loop through everything.
    Is there a better way? I cannot
    think of one. Let us continue.



'''

class SubrectangleQueries:

    def __init__(self, rectangle):
        self.matrix = rectangle

    def updateSubrectangle(self, row1, col1, row2, col2, newValue):
        for row in range(row1, row2+1):
            for col in range(col1, col2+1):
                self.matrix[row][col] = newValue


    def getValue(self, row, col):
        return self.matrix[row][col]
