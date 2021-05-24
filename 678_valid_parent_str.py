
'''
"(())((())()()(*)(*()(())())())()()((()())((()))(*"

"((*"

"(((((*(()((((*((**(((()()*)()()()*((((**)())*)*)))))))(())(()))())((*()()(((()((()*(())*(()**)()(())"
         ^


p    = 6
star = 1

close stars can only be used for )
open stars can be used for (

class Solution:
    def checkValidString(self, s):
        star = 0
        p = 0

        for e in s:
            if e == "(":
                p += 1
            elif e == ")":
                p -= 1
            if e == "*":
                star += 1

            if p < 0:
                star  -= 1
                p += 1

        for e in range(p):
            star -= 1

        return star >= 0



*******(((((((

maintain list of indices that represent *'s
also maintain a list of indices that represent '('

After we finish our run-through, loop
through '(' list. If there exists an '*' that can close
the open '(' use it. Else return false.

0123456789
*((*()((*)
 ^

stars = [0]
open = [1]

'''

# Prevent counting the lhs stars that won't
# be able to be used b/c they can't close anything
# have two sets of stars? One for closed, one for both?
class Solution:
    def checkValidString(self, s):
        star = []
        open = []

        # Forward traversal
        for idx, e in enumerate(s):
            if e == "(":
                open.append(idx)
            elif e == ")":
                if len(open) > 0:
                    open.pop()
                elif len(star) > 0:
                    star.pop()
                else:
                    return False
            else:
                star.append(idx)

        # Backwards traversal
        for idx in reversed(open):
            if len(star) <= 0:
                return False

            if star[-1] > idx:
                star.pop()
            else:
                return False

        return True






s = Solution()
print(s.checkValidString("((((*))")) # False
print(s.checkValidString("()")) # True
print(s.checkValidString("(*)")) # True
print(s.checkValidString("(*))")) # True
print(s.checkValidString("((*))")) # True
