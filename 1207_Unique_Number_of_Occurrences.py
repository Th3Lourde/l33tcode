

def uniqueOccurrences(arr: list) -> bool:
    d = {}

    for i in range(len(arr)):
        try:
            d[arr[i]] += 1

        except:
            d[arr[i]] = 1


    occ = []

    keys = list(d.keys())

    for j in range(len(keys)):
        occ.append(d[keys[j]])

    occ.sort()

    for z in range(len(occ)-1):
        if occ[z] == occ[z+1]:
            return False

    return True


if __name__ == "__main__":
    # i = [1,2,2,1,1,3]
    # i = [1,2]
    i = [-3,0,1,-3,1,1,1,-3,10,0]

    r = uniqueOccurrences(i)

    print(r)