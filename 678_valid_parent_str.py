
'''
"(())((())()()(*)(*()(())())())()()((()())((()))(*"

"((*"
'''



class Solution:

    def checkValidString(self, s):
        open = 0
        close = 0
        astrix = 0
        gone = 0
        stack = []

        # Uses stack to test that the order is valid
        for e in s:

            if e == "*":
                astrix += 1

            elif e == "(":
                open += 1

            elif e == ")":
                close += 1

            if e == "(" or e == "*":
                stack.append(e)

            elif e == ")":
                if len(stack) == 0:
                    return False

                r = stack.pop()

                if r == "*":
                    ...

        return True




    def checkValidString_5(self, s):
        open = 0
        close = 0
        astrix = 0
        gone = 0
        stack = []

        # Uses stack to test that the order is valid
        for e in s:

            if e == "*":
                astrix += 1

            elif e == "(":
                open += 1

            elif e == ")":
                close += 1

            if e == "(" or e == "*":
                stack.append(e)

            elif e == ")":
                if len(stack) == 0:
                    return False

                r = stack.pop()

                if r == "*":
                    gone += 1

        # Check there are not too many '('
        if len(stack)-(astrix - gone) > astrix:
            return False

        # Check there are enough *
        if max(open, close) - min(open, close) > astrix:
            return False

        return True



    def checkValidString_4(self, s):
        open = 0
        astrix = 0
        close = 0

        for e in s:
            if e == "(": open += 1
            elif e == "*": astrix += 1
            elif e == ")": close += 1

        if max(open, close) - min(open, close) > astrix:
            return False

        return True


    def checkValidString_3(self, s): # Let's actually solve the problem this time :)
        astrix = 0                 # Better, doesn't work
        gone = 0
        stack = []

        for e in s:
            if e == "(" or e == "*":
                stack.append(e)

                if e == "*":
                    astrix += 1

            elif e == ")":
                if len(stack) == 0:
                    return False

                r = stack.pop()

                if r == "*":
                    gone += 1

        if len(stack)-(astrix - gone) > astrix:
            return False

        return True


    def checkValidString_2(self, s): # we meant to solve the wrong problem this time :)
        pCounter = [0,0,0]

        for p in s:
            if p == "(":
                pCounter[0] += 1

            elif p == "[":
                pCounter[1] += 1

            elif p == "{":
                pCounter[2] += 1

            elif p == "}":
                pCounter[2] -= 1

            elif p == "]":
                pCounter[1] -= 1

            elif p == ")":
                pCounter[0] -= 1

        if sum(pCounter) == 0:
            return True

        return False








    def checkValidString_1(self, s): # solved the wrong problem :^D
        s1 = [] # (
        s2 = [] # [
        s3 = [] # {

        for p in s:
            if p == "(":
                s1.append('(')

            elif p == "[":
                s2.append('[')

            elif p == "{":
                s3.append("{")

            elif p == "}":
                try:
                    s3.pop()

                except:
                    return False

            elif p == ")":
                try:
                    s1.pop()

                except:
                    return False

            elif p == "]":
                try:
                    s2.pop()

                except:
                    return False

        return True
