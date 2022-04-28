class Solution:
    def maximumSwap(self, num):
        num_to_idx = {}
        num = str(num)

        for idx in range(len(num)):
            if num[idx] in num_to_idx:
                num_to_idx[num[idx]].append(idx)
            else:
                num_to_idx[num[idx]] = [idx]

        for idx in range(len(num)-1):
            for target in range(9, int(num[idx]), -1):
                if str(target) in num_to_idx and num_to_idx[str(target)][-1] > idx:
                    # Swap num_to_idx[-1] idx
                    target = str(target)
                    # print("target: {}".format(target))
                    # print("switch: {}".format(num[idx]))
                    target_idx = num_to_idx[target][-1]
                    front = num[:idx]
                    mid = num[idx+1:target_idx]
                    back = num[target_idx+1:]
                    # print("{} + {} + {} + {} + {}".format(front, target, mid, num[idx], back))
                    num = front + target + mid + num[idx] + back
                    return int(num)

                    # ----idx----t---
                    # ----t----idx---

        return int(num)

print(Solution().maximumSwap(2367))
