'''
We are given that the two vectors are the same size.

 0 1 2 3 4
[1,0,0,2,3] --> [1,-2,2,3]

{
 0:1,
 3:2,
}

'''

class SparseVector:
    def __init__(self, nums):
        self.dict = {}

        for idx in range(len(nums)):
            if nums[idx] != 0:
                self.dict[idx] = nums[idx]

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec):
        dot = 0

        for key in vec.dict:
            if vec.dict[key] != 0 and key in self.dict:
                dot += vec.dict[key]*self.dict[key]

        return dot

v1 = SparseVector([0,1,0,0,2,0,0])
v2 = SparseVector([1,0,0,0,3,0,4])

v1.dotProduct(v2)

v1 = SparseVector([0,1,0,0,0])
v2 = SparseVector([0,0,0,0,2])

v1.dotProduct(v2)


v1 = SparseVector([1,0,0,2,3])
v2 = SparseVector([0,3,0,4,0])

v1.dotProduct(v2)
