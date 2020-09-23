

class Solution:
    def readBinaryWatch(self, num):
        ans = []

        def parse(arr):
            # print(arr)
            hr = 0
            for i in range(3, -1, -1):
                if arr[i] == 1:
                    hr += 2**(3-i)

            if not 0 <= hr <= 11:
                return

            min = 0
            for i in range(9, 3, -1):
                if arr[i] == 1:
                    min += 2**(9-i)

            if not 0 <= min <= 59:
                return

            # Else we have a valid answer

            if min < 10:
                time = "{}:0{}".format(hr, min)

            else:
                time = "{}:{}".format(hr, min)

            ans.append(time)

            return

        def itr(arr, n, idx):
            if n == 0:
                parse(arr)
                # Parse/evaluate
                return

            for i in range(idx, len(arr)):
                arr[i] = 1
                itr(arr, n-1, i+1)
                arr[i] = 0

        itr([0 for i in range(10)], num, 0)

        return ans



if __name__ == '__main__':
    s = Solution()

    print(s.readBinaryWatch(1))
