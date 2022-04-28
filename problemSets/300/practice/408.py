class Solution:
    def validWordAbbreviation(self, word, abbr):
        nums = set({'0','1','2','3','4','5','6','7','8','9'})

        p1 = 0
        p2 = 0
        can_abbr = True

        while p1 < len(word) and p2 < len(abbr):
            if word[p1] == abbr[p2]:
                can_abbr = True
                p1 += 1
                p2 += 1

            elif word[p1] != abbr[p2] and abbr[p2] not in nums:
                # print("A")
                return False

            else:
                if not can_abbr:
                    return False
                can_abbr = False

                # word[p1] != abbr[p2] and abbr[p2] in nums
                if abbr[p2] == '0':
                    # print("B")
                    return False

                # find length of abbr
                p2r = p2

                while p2r < len(abbr) and abbr[p2r] in nums:
                    p2r += 1

                # the rest of the string is an abb
                p1 += int(abbr[p2:p2r])

                if p1 > len(word):
                    return False

                p2 = p2r

        if not (p1 >= len(word) and p2 >= len(abbr)):
            # print("C")
            return False

        return True

print(Solution().validWordAbbreviation("a","2"))
print(Solution().validWordAbbreviation("internationalization","i12iz4n"))




# Fail if a1
