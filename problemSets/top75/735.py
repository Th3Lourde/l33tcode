'''
We are given an array asteroids of integers representing astroids in a row


For each asteroid:
the abs value represents its size
the sign represetnts its direction (left or right)

All asteroids move at the same speed

If two asteroids colide, an asteroid explodes if it has a size <= than
the asteroid that it collided with.

So I'm thinking a stack solution.
Move left to right

if positive, add to stack
if negative, check if stack exists, replace element in stack if it doesn't

return stack when we are done

[5,10,-5]
       ^

stack = [5,10]


[5,10,-5] --> [5,10]
    ^             ^

[5,10,-50] --> [5,-50] --> [-50]
    ^           ^

--------------------------------------------------

[-50]
   ^

s = [5,10,15]

--------------------------------------------------
[5,-10,2,3,4,-5,7,-6]
                   ^

s = [-10,-5,7]

addAsteroid = False
rock = 7
outcome= 7



'''

class Solution:
    def asteroidCollision(self, asteroids):
        stack = []

        def collision(a,b):
            if abs(a) > abs(b):
                return a
            elif abs(a) < abs(b):
                return b
            else:
                return None

        for asteroid in asteroids:

            if asteroid < 0:
                # Handle case where the top most element
                # is negative

                if not stack or stack[-1] < 0:
                    stack.append(asteroid)

                else:
                    # Keep popping and colliding until
                    # a positive asteroid wins or we are out of asteroids
                    addAsteroid = True

                    while stack and stack[-1] > 0:
                        rock = stack.pop()
                        outcome = collision(rock, asteroid)

                        if outcome == rock:
                            addAsteroid = False
                            stack.append(rock)
                            break

                        elif outcome == None:
                            addAsteroid = False
                            break

                    if addAsteroid:
                        stack.append(asteroid)

            else:
                stack.append(asteroid)

        return stack

print(Solution().asteroidCollision([5,4]))
print(Solution().asteroidCollision([5,-10,2,3,4,-5,7,-6]))
print(Solution().asteroidCollision([-10,2,-5]))
print(Solution().asteroidCollision([-10,-2,-5]))
print(Solution().asteroidCollision([5,10,-5]))
print(Solution().asteroidCollision([8,-8]))
print(Solution().asteroidCollision([10,2,-5]))
