'''
Given list of integers: Create a heap.




while len(heap) > 1:
    ...

1) poll twice from the heap
2) calculate the new stone value (DONE)
3) add that new stone value to the heap

when done, return the remaining value.


'''
import sys
sys.path[0] = "/home/th3lourde/Documents/InterviewPrep/tools/python"
from priorityQueue.priorityQueueF import priorityQueue


class Solution:
    def lastStoneWeight_1(self, stones): # Used library implementation
        import heapq
        # from heapq import heappush, heappop

        for i in range(len(stones)):
            stones[i] = (-1)*stones[i]

        heapq.heapify(stones)
        # Step 0: Create heap
        # heap = priorityQueue('max', stones)

        while len(stones) > 1:
            # Step 1: Poll twice from the heap
            # heapq.heappush(heap, item)
            # heapq.heappop(heap)¶

            a = heapq.heappop(stones)
            b = heapq.heappop(stones)
            r = (-1)*abs(abs(a)-abs(b))

            # print("a: {} b: {}, newVal: {}".format(a, b, r))

            # Step 2: Calculate new weight
            # Step 3: Add that new weight to heap
            heapq.heappush(stones, r)

        # Step 4: Return the last value
        return abs(stones[0])



    def lastStoneWeight(self, stones): # My heap doesn't work correctly :/

        # Step 0: Create heap
        heap = priorityQueue('max', stones)
        print(heap)

        while heap.getSize() > 1:
            # Step 1: Poll twice from the heap
            a = heap.poll()
            b = heap.poll()

            print("a: {} b: {} newNode: {}".format(a, b, abs(a-b)))

            # Step 2: Calculate new weight
            # Step 3: Add that new weight to heap
            heap.add(abs(a-b))
            print(heap)

        # Step 4: Return the last value
        return heap.poll()


if __name__ == '__main__':
    s = Solution()

    # inp = [2,7,4,1,8,1]
    # inp = [1,1,1,1,2]
    inp = [6,8,10,1,10,2,7,4]

    print(s.lastStoneWeight(inp))
