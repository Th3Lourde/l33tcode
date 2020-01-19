


def toLowerCase(input: str) -> str:
    itr = list(input) 

    for i in range(len(itr)):
        if ord(itr[i]) <= 90 and ord(itr[i]) >= 65:
            # It's upper-case
            itr[i] = chr(ord(itr[i]) + 32)


    ans = "".join(itr)

    return ans 


if __name__ == "__main__":
    v = "LoVELY"

    r = toLowerCase(v)

    print(r)
