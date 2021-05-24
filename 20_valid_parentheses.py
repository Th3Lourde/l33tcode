

class Solution:
    def isValid_1(self, s):
        stack = []

        swap = {")":"(", "]":"[", "}":"{"}

        for e in s:
            if e == "(" or e == "[" or e == "{":
                stack.append(e)

            elif e == ")" or e == "]" or e == "}":
                if len(stack) == 0:
                    return False

                if stack.pop() != swap[e]:
                    return False

        if len(stack) != 0:
            return False

        return True

    def isValid(self, s):
        stack = []
        closeMapping = {
            ")": "(",
            "}": "{",
            "]": "[",
        }

        for chr in s:
            if chr == "(" or chr == "{" or chr == "[":
                stack.append(chr)

            else:
                if len(stack) == 0 or stack[-1] != closeMapping[chr]:
                    return False
                stack.pop()

        return len(stack) == 0



if __name__ == '__main__':
    s = Solution()

    testCases = [

        # Empty string works
        ["", True],

        ["()", True],
        ["(", False],
        [")", False],

        ["()", True],
        ["())", False],
        ["(())", True],
        ["(()", False],

        ["[]", True],
        ["[", False],
        ["]", False],

        ["[]", True],
        ["[]]", False],
        ["[[]]", True],
        ["[[]", False],

        ["{}", True],
        ["{", False],
        ["}", False],

        ["{}", True],
        ["{}}", False],
        ["{{}}", True],
        ["{{}", False],


        ["{(]", False],
        ["{()]", False],
        ["{()}]", False],
        ["[{()}]", True],

        # ["(*)", True],
        # ["{(*)}", True],
        # ["[{(*)}]", True],
        # ["[{(*))}]", False],

    ]

    for tc in testCases:
        assert s.isValid(tc[0]) == tc[1], "[For {}]: {} != {}".format(tc[0], s.isValid(tc[0]), tc[1])

    print("[passed all test cases]")


def isValid(s:str) -> bool:
    # Assuming can't contain spaces
    if s == "":
        return True

    brackets = [""]

    for i in range(len(s)):
        # If at end of list and the last character
        # isn't the correct closing bracket

        if len(s)-1 == i and brackets[0] != s[i]:
            return False

        # If next char isn't an opening bracket and
        # also isn't the correct closing bracket
        elif s[i] != "(" and s[i] != "{" and s[i] != "[" and s[i] != brackets[0]:
            return False

        # If the next char is an opening bracket
        elif s[i] == "(" or s[i] == "{" or s[i] == "[":
            if s[i] == "(":
                brackets.insert(0, ")")
            elif s[i] == "{":
                brackets.insert(0, "}")
            elif s[i] == "[":
                brackets.insert(0, "]")

        # If the next char is the correct
        # closing bracket
        elif s[i] == brackets[0]:
            brackets.remove(brackets[0])

    if len(brackets) == 1:
        return True
    else:
        return False



# if __name__ == "__main__":
#     resp = isValid("[")
#     print(resp)
