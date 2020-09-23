

'''
Given array of positive ints,
find a pattern of length m, that is
repeated k or more times.

Return true if ∃ a pattern of len m
that is repeated k or more times.

A pattern is a subset of adjacent elements

Sliding window of length m.
For each pattern, throw it in dict,
when updating the freq of pattern, if >= k,
return true

return false after loop

Ok so I was wrong on two fronts here:

1) The frequency of the pattern is determined by
how many times the pattern repeats consecutively

e.g. : a b a b a c, for m =2, a b occurs twice.

One loop through, get all of the patterns
Second loop through, count all of the frequencies
of a pattern.

Or, O(n^2) loop, sliding window to see if things match
the current pattern.

tail = m
if m == 1:
    tail = 0

# Every element can start
for i in range(len(arr)-tail):

    cache = [arr[i:i+m], 1]

    for j in range(i+m, len(arr)-tail):
        pattern = arr[j:j+m]

        if pattern == cache[0]:
            cache[1] += 1

            if cache[1] >= k:
                return True

        elif pattern != cache[0]:
            break

return False






'''

class Solution:
    def containsPattern(self, arr, m, k):
        tail = m
        if m == 1:
            tail = 0

        # Every element can start
        for i in range(len(arr)-tail+1):

            cache = [arr[i:i+m], 1]
            # print(cache)

            for j in range(i+m, len(arr)-tail+1):
                pattern = arr[j:j+m]

                if pattern == cache[0]:
                    cache[1] += 1

                    if cache[1] >= k:
                        return True

                elif pattern != cache[0]:
                    break

        return False

if __name__ == '__main__':
    s = Solution()

    print(s.containsPattern([1,2,4,4,4,4], 1, 3))
    print(s.containsPattern([1,2,1,2,1,1,1,3], 2, 2))
    print(s.containsPattern([2,2], 1, 2))

    print(s.containsPattern([2,2,1,2,2,1,1,1,2,1], 2, 2))


    print(s.containsPattern([1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1], 50, 2))

    print(s.containsPattern([1,1,1,1,1,1], 3, 2))
