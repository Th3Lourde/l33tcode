class Solution:
    def exclusiveTime(self, n, logs):
        resp = [0]*n
        stack = []
        prev_time = 0

        for log in logs:
            pid, action, time = log.split(":")
            pid, time = int(pid), int(time)

            if action == "start":
                if stack:
                    resp[stack[-1]] += time-prev_time

                prev_time = time
                stack.append(pid)

            else:
                resp[stack.pop()] += time-prev_time+1
                prev_time = time + 1

        return resp

print(Solution().exclusiveTime(2, ["0:start:0","0:start:2","0:end:5","1:start:6","1:end:6","0:end:7"]))


print(Solution().exclusiveTime(2, ["0:start:0","0:start:2","0:end:5","1:start:6","1:end:6","0:end:7"]))
print(Solution().exclusiveTime(1, ["0:start:0","0:start:2","0:end:5","0:start:6","0:end:6","0:end:7"]))
print(Solution().exclusiveTime(2, ["0:start:0","1:start:2","1:end:5","0:end:6"]))
