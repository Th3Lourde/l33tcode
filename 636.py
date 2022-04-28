class Solution:
    def exclusiveTime(self, n, logs):
        pidToEXtime = [0 for _ in range(n)]
        stack = []
        prev_time = 0

        for log in logs:
            pid, event, time = log.split(":")
            pid, time = int(pid), int(time)

            if event == "start":
                if stack:
                    pidToEXtime[stack[-1]] += time-prev_time
                stack.append(pid)
                prev_time = time

            else:
                pidToEXtime[stack.pop()] += time-prev_time+1
                prev_time = time + 1

        return pidToEXtime
