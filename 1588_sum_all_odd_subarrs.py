
class Solution:
    def sumOddLengthSubarrays(self, arr):
        ans = 0
        idx = 0
        max_idx = len(arr)

        while idx < max_idx:
            sub_idx = idx
            tmp = arr[sub_idx]
            ans += tmp

            while sub_idx < max_idx:
                if sub_idx + 2 < max_idx:
                    for i in range(2):
                        sub_idx += 1
                        tmp += arr[sub_idx]
                    ans += tmp
                else:
                    break

            idx += 1

        return ans

if __name__ == '__main__':
    s = Solution()
    print(s.sumOddLengthSubarrays([]))
