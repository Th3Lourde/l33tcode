# https://www.youtube.com/watch?v=7pJo_rM0z_s

'''
So when we create a prefix sum of an array nums,
we create another array prefix.

let i be an index in array nums.

prefix[i] = sum(nums[0], nums[1], ..., nums[i])

And when we do this we can simplify the equation
to be:

prefix[i] = nums[i] + prefix[i-1], for all i > 0
'''
