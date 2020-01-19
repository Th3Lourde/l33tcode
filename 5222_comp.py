


class Solution:

    def balancedStringSplit(self, s:str) -> int:
        ans = 0

        i = 0
        while i <= len(s)-2:
            if s[i] == "L":
                if s[i+1] == "R":
                    ans += 1
                    i += 2
                else:
                    i += 1

            elif s[i] == "R":
                if s[i+1] == "L":
                    ans += 1
                    i += 2
                else:
                    i += 1

        return ans

    def balancedStringSplit1(self, s:str) -> int:
        ans = 0

        i = 0
        while i <= len(s)-2:
            if s[i] == "L":
                if s[i+1] == "R":
                    # Found 1
                    ans += 1

                    l = i
                    r = i+1
                    i += 1

                    while (l-1 >= 0) and (r + 1 <= len(s)-1):
                        l -= 1
                        r += 1

                        if s[l] == "L" and s[r] == "R":
                            continue
                            # ans += 1
                        else:
                            # print(s[r])
                            r -= 1
                            break
                    i = r

                else:
                    i += 1


            elif s[i] == "R":
                if s[i+1] == "L":
                    ans += 1

                    l = i
                    r = i+1
                    i += 1


                    while (l-1 >= 0) and (r + 1 <= len(s)-1):
                        l -= 1
                        r += 1

                        if s[l] == "R" and s[r] == "L":
                            # ans += 1
                            continue
                        else:
                            # i = r-1
                            # print(s[r])
                            r -= 1
                            break
                    i = r

                else:
                    i += 1

        return ans

if __name__ == '__main__':
    s = Solution()

    # t1 = "RLRRLLRLRL"
    # t1 = "RLLLLRRRLR"
    # t1 = "LLLLRRRR"
    # t1 = "RLRRLLRLRL"
    # Want 4
    # t1 = "RLLRRRLLLR"

    t1 = "R[RL]R[RL][RL]L[LR]L"
    # Want 2

    r = s.balancedStringSplit(t1)
    print(r)
