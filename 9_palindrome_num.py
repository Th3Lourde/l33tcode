
class Solution:
    def isPalindrome(self, x: int) -> bool:

        if x == None:
            return False

        a = list(str(x))

        if len(a) == 1:
            return True

        if len(a) % 2 == 0:
            i = 0

            while i < len(a)/2:
                if a[i] != a[len(a)-i-1]:
                    return False

                elif a[i] == a[len(a)-i-1]:
                    i += 1

        elif len(a)%2 == 1:
            i = 0

            while i < (len(a)-1) / 2:
                if a[i] != a[len(a)-i-1]:
                    return False

                elif a[i] == a[len(a)-i-1]:
                    i += 1

        return True


if __name__ == '__main__':
    s = Solution()

    num = 12211
    print(s.isPalindrome(num))
