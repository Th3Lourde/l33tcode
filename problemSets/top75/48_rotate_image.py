'''
Ok so the goal here is to rotate an image,
specifically a matrix.
  0 1 2
0|a b c
1|d e f
2|g h i

[0][0] --> [0][2]
[0][1] --> [1][2]
[0][2] --> [2][2]

[1][2] --> [2][1]
[2][2] --> [2][0]

[2][1] --> [1][0]
[2][0] --> [0][0]
[1][0] --> [0][1]

  0 1 2
0|a b c
1|d e f
2|g h i

  0 1 2
0|g h i
1|d e f
2|a b c

[0][0] --> [0][0]
[0][1] --> [1][0]
[0][2] --> [2][0]

[1][0] --> [0][1]
[1][1] --> [1][1]
[1][2] --> [2][1]

[2][0] --> [0][2]
[2][0] --> [0][2]

  0 1 2
0|g d a
1|h e
2|i b

Want:

 g d a
 h e b
 i f c

What does matrix.reverse do?

'''

# m = [
#     [1,2,3],
#     [4,5,6],
#     [7,8,9],
# ]

m = [
    ["a","b","c"],
    ["d","e","f"],
    ["g","h","i"],
]


class Solution:
    def rotate(self, matrix):
        matrix.reverse()

        for r in range(len(matrix)):
            for c in range(r):
                matrix[r][c], matrix[c][r]  = matrix[c][r], matrix[r][c]



print(Solution().rotate(m))
