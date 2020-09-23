'''
Given two integers n and k,
return all possible combinations
of k numbers where the combinations
are created by numbers from [1, n]

Ok I think I get this pattern now,
sick.

So create an array of size k, fill
it with zeros.

Then use loops as well as other things
in order to step through all of the
different solutions that you could
possibly use.

ans = []

def itr(arr, idx, opts):
    if idx == len(arr):
        # append
        ans.append(arr)
        return

    else:
        for i in range(len(opts)):
            arr[idx] = opts[i]

            itr(arr, idx+1, opts[:i]+opts[i+1:])

            arr[idx] = 0


Ok so no set. How can we just logic this out?

The first element is used n-1 times, then n-2,
then n-3, ...

So we use the first element n-1 times,
the second element n-2 times, the third
element, n-3 times, ...

What we could try to do is have some kind of moving
min value as well and a constant max value.

--------------------------------------------------

i is the number of times we want to use that term

# k is how much space that we have left
# k is also how many times we will use said term (again)
# i is the term that we are currently at

Damn, this is just so smart on so many levels.

If we use +[j] instead of .append(), we can avoid having
to worry about using the same block of memory multiple times.

(arr, k, i)

if k == 0:
    resp

for j in range(i, n+2-k):



    arr+[j], k-1, j+1





'''


class Solution:
    def combine(self, n, k):
        ans = []

        def itr(arr, k, i):
            if k == 0:
                ans.append(arr)
                return

            for j in range(i, n-k+2):
                itr(arr+[j], k-1, j+1)

        itr([], k, 1)

        return ans

if __name__ == '__main__':
    s = Solution()

    print(s.combine(4, 2))
