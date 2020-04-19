



'''
So we are given a string containing characters and numbers

Can we re-write the string s.t. no two characters happen twice?

if we have n of one type
and n+2
'''


def reformat(s):
    # num = [str(i) for i in range(10)]

    num = {"0": True, "1": True, "2": True, "3": True, "4": True, "5": True, "6": True, "7": True, "8":True, "9": True}

    ans = ""
    prev = 0
    type = "" # 0: num | 1: char
    hist = [[],[]]
    n = 0
    c = 0

    for char in s:
        # Get type
        try:
            if num[char]:
                n += 1
                type = 0

        except:
            c += 1
            type = 1

        # Add char to string or save it

        if ans == "":
            ans += char
            prev = type

        elif ans != "":
            if prev == type:
                hist[type].append(char)

                if type == 0 and hist[1] != []:
                    ans += hist[1].pop()
                    ans += hist[type].pop()

                elif type == 1 and hist[0] != []:
                    ans += hist[0].pop()
                    ans += hist[type].pop()


            elif prev != type:
                ans += char
                prev = type

                if type == 0:
                    type = 1

                elif type == 1:
                    type = 0

    if max(n,c)-min(n,c) > 1:
        return ""

    nums = hist[0]
    chars = hist[1]

    try:
        if num[ans[-1]]:
            type = True


    except:
        type = False

    while nums != [] and chars != []:
        if type:
            ans += chars.pop()
            type = not type

        elif not type:
            ans += nums.pop()
            type = not type


    if nums != []:
        if not type:
            ans += nums.pop()

        else:
            ans = nums.pop() + ans

    if chars != []:
        if type:
            ans += chars.pop()
        else:
            ans = chars.pop() + ans

    return ans





# print(reformat("a0b1c2"))
print(reformat("covid2019"))
