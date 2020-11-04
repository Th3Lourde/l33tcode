'''
Packages must be shipped from one port to another
within D days.

The i-th package on the belt has a weight of weights[i]
Each day, we load the ship with packages on the conveyer
belt (in the order established in weights).

What must the max capacity of the ship be in order
for us to hit our deadline?

A prefix tree sounds like a good solution for this.

What if we add up all of the weights of the packages?

We can get the min capacity by recording the local max
of the given list.

Then we can create as many groupings with sum 10 as possible

We can then try to keeping increasing the sum until we hit our
goal.

Or we can start at the sum of the elements divided by the limitation
that we have been given.

[1,2,3,4,5,6,7,8,9,10] = 55

Min sum = 1

So I was on the right track.
I noticed that max(weights) and sum(weights)
were important to solving the problem.

So max(weights) is too low (or could be too low) [This is the min val]
sum(weights) is too high (or could be too high) [This is the max val]

Both left and right are potential answers.

The answer is somewhere in the middle. Instead of increasing bit by
bit, we can instead jump to the midpoint of our interval each time.

mid is our proposed ship capacity.

Need is the number of days that we need to deliver the packages.

So what we do is test our proposed capacity.

What we do, is determine how many days it will take to deliver
everything.

If the capacity is too low, look on the right of the midpoint,
as we just tried out using the midpoint.

If the capacity is too high, look on the left of the midpoint,
as we just tried out using the midpoint

We could also return right?


'''

class Solution:
    def shipWithinDays(self, weights, D):
        left, right = max(weights), sum(weights)

        while left < right:
            proposed, days_needed, current_cap = (right+left) // 2 , 1, 0

            for w in weights:
                if current_cap + w > proposed:
                    days_needed += 1
                    current_cap = 0

                current_cap += w

            if days_needed > D:
                left = proposed + 1

            else:
                right = proposed

        return left


if __name__ == '__main__':
    s = Solution()

    print(s.shipWithinDays([1,2,3,4,5,6,7,8,9,10], 5))
