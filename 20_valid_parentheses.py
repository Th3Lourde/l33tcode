
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



if __name__ == "__main__":
    resp = isValid("[")
    print(resp)
