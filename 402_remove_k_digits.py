import heapq

class Solution:
    def removeKdigits(self, num, k): # ToDo
        # 1) Find and expose all zeros
        # Find the 'deepest' zero, figure
        # out how long the run is.
        # update num, k accordingly, continue
        num = list(num)

        i = 0
        z = 0 # We know that we will not be given a leading zero. 0 chance false positive.
        while i < k:
            if num[i] == "0":
                z = i
            i += 1

        if z != 0:
            # z is the index of the zero
            k -= z + 1 # number of terms needed to pop to expose the zero

            while num[z] == "0": # finding the length of the 'run'
                z += 1

            # z is now the index of the first element that is not a zero
            num = num[z:]

        # print(num)
        # Find the k-largest elements and remove them
        # from the list. Totally a heap problem.
        heap = list(num)
        heapq._heapify_max(heap) # maybe have a dictionary reference so you have the indices stored.

        # print(heap)
        # print(num)

        for i in range(k):
            num.remove(heap[i])
            # del num.index(heap[i])

        print(num)

        # for i in range(k):
        #     r = heapq._heappop_max(maxheap)
        #     print(r)

        # Have exposed any possible zeros.
        # Did this first because this is the most important.
        # while k > 0:
        #     ...


        # return "".join(num)

if __name__ == '__main__':
    s = Solution()


    testCases = [
        ["1432219", 3, "1219"],
        "1221"
    ]

    for tc in testCases:
        r = s.removeKdigits(tc[0], tc[1])

        # assert r == tc[1], "[For {}] {} != {}".format(tc[0], r, tc[2])

    print("[passed all test cases]")
