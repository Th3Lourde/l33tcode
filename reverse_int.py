

def reverse_int(x):
    num = x
    x = list(str(x))

    # Step 1): Setting the Stage
    # - Figure if len(x) == 1
    # - Figure out if x is valid size
    # - Figure out if x is pos or neg
    # - set x = list of strs that represents pos ints
    if (len(x) == 1):
        return num
    elif (num > 0):
        if (num > 2**31 - 1):
            return 0
        elif(num <= 2**31 - 1):
            neg = False
    elif (num < 0):
        if (len(x) > 2**31):
            return 0
        elif (len(x) <= 2**31):
            neg = True
            x.remove(x[0])

    # Step 2): Swapping
    # - Based upon if x is even or odd
    #   stop swapping at the appropriate location
    # - When swapping, place '' when you encounter '0'
    #   if we haven't put a non-zero at the front of the list

    kill_zero = True
    if (len(x) % 2 == 0):
        for i in range(int(len(x)/2)):
            tmp = x[i]

            # If we haven't put a non-zero at the front
            # of the list yet...
            if (x[len(x)-1-i] == '0' and kill_zero == True):
                x[i] = ''
            elif (x[len(x)-1-i] != '0'):
                if (kill_zero):
                    kill_zero = False

                x[i] = x[len(x)-1-i]

            x[len(x)-1-i] = tmp
    elif (len(x) % 2 == 1):
        for i in range((len(x)//2)):
            tmp = x[i]

            if (x[len(x)-1-i] == '0' and kill_zero == True):
                x[i] = ''
            elif (x[len(x)-1-i] == '0' and kill_zero == False):
                x[i] = x[len(x)-1-i]
            elif (x[len(x)-1-i] != '0'):
                if (kill_zero):
                    kill_zero = False
                x[i] = x[len(x)-1-i]

            x[len(x)-1-i] = tmp

    # Step 3): Presentation
    # - return int
    # - based upon if input was pos or neg
    #   conditionally multiply input by -1

    ans = "".join(x)
    ans = int(ans)


    if (neg and ans < 2**31):
        return ans*(-1)
    elif (neg and ans > 2**31):
        return 0
    elif (not(neg) and ans < (2**31 - 1)):
        return ans
    elif (not(neg) and ans > (2**31 - 1)):
        return 0


if __name__ == '__main__':
    # resp = reverse_int(-123)
    # print(resp)

    # resp = reverse_int(1534236469)
    # print(resp)

    resp = reverse_int(42804)
    print(resp)
