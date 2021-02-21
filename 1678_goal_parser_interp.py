

class Solution:
    def interpret(self, command):
        ans = ""
        for i in range(len(command)):
            if command[i] == "(":
                if command[i+1] == ")":
                    ans += "o"
            elif command[i] == ")":
                continue
            else:
                ans += command[i]
        return ans


if __name__ == '__main__':
    s = Solution()
    print(s.interpret("G()(al)"))
    print(s.interpret("G()()()()(al)"))
    print(s.interpret("(al)G(al)()()G"))
