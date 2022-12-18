import heapq

class Solution:
    def leastInterval(self, tasks, n):
        exec = []
        taskToFreq = {}
        heap = []

        for task in tasks:
            if task in taskToFreq:
                taskToFreq[task] += 1

            else:
                taskToFreq[task] = 1


        for task in taskToFreq:
            heapq.heappush(heap, (-1*taskToFreq[task], task))

        def insert(task, freq, exec):
            i = 0
            l = len(exec)
            # handle case where exec is empty
            if not exec:
                for _ in range(freq):
                    exec = exec + [task] + [""]*n

                # print(exec)
                return exec

            # insert task into exec

            while i < l and freq > 0:
                if exec[i] == "":
                    exec[i] = task
                    freq -= 1
                    i += n+1

                else:
                    i += 1

            if freq > 0:
                if exec[-1] == task:
                    exec = exec + [""]*n

                for _ in range(freq):
                    exec = exec + [""]*n + [task]

            return exec


        while heap:
            freq, task = heapq.heappop(heap)

            exec = insert(task, -1*freq, exec)

        # shave off ""
        while len(exec) > 0 and exec[-1] == "":
            exec.pop()

        print(exec)

        return len(exec)

print(Solution().leastInterval(["A","A","A","B","B","B", "C","C","C", "D", "D", "E"], 2))

print(Solution().leastInterval(["A","A","A","A","A","A","B","C","D","E","F","G"], 2))
