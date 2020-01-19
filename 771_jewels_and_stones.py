


# Solution if we care about runtime:

def numJewelsInStones(J:str, S:str):
    dict_v = {}

    for i in range(len(J)):
        dict_v[J[i]] = True


    ans = 0
    
    for j in range(len(S)):
        try:
            # Should only throw error if key
            # does not exist in the dictionary
            if dict_v[S[j]]:
                ans += 1

        except:
            None

    print(ans)

if __name__ == "__main__":

    # J = "aA"
    # S = "aAAbbbb"

    J = "z"
    S = "ZZ"


    numJewelsInStones(J,S)
